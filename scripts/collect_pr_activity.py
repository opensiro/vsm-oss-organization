#!/usr/bin/env python3
"""Bounded, provenance-rich GitHub PR lifecycle telemetry for public OpenSiro OSS.

This is secondary non-KPI operational telemetry, not a VSM outcome metric.
One PR is counted once in the repository where it lives, regardless of actors.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import statistics
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Callable, Any

REPOSITORIES = (
    "opensiro/vsm-harness-profile",
    "opensiro/vsm-harness-skills",
    "opensiro/vsm-harness-index",
    "opensiro/awesome-vsm-harness",
    "opensiro/vsm-oss-organization",
)
WINDOWS = {"24h": timedelta(hours=24), "7d": timedelta(days=7), "30d": timedelta(days=30)}
BASE = "https://api.github.com"
LINK = re.compile(r'<([^>]+)>; rel="([^"]+)"')
NULL_STATS = {"median_hours": None, "p90_hours": None, "sample_size": None}


class PRActivityError(RuntimeError):
    pass


def parse_time(value: str) -> datetime:
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise PRActivityError(f"timestamp must include UTC offset: {value!r}")
    return dt.astimezone(timezone.utc)


def timestamp(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def in_window(value: str | None, cutoff: datetime, now: datetime) -> bool:
    return value is not None and cutoff < parse_time(value) <= now


def quantile(values: list[float]) -> dict:
    if not values:
        return {"median_hours": None, "p90_hours": None, "sample_size": 0}
    sorted_values = sorted(values)
    index = max(0, (9 * len(sorted_values) + 9) // 10 - 1)  # nearest-rank 90th percentile
    return {
        "median_hours": round(statistics.median(sorted_values), 2),
        "p90_hours": round(sorted_values[index], 2),
        "sample_size": len(sorted_values),
    }


def first_qualifying_review(pr: dict, reviews: list[dict]) -> tuple[datetime | None, bool]:
    """Return earliest submitted non-author GitHub User review; false means incomplete provenance."""
    author = (pr.get("user") or {}).get("login")
    if not author:
        return None, False
    times: list[datetime] = []
    for review in reviews:
        if review.get("state") == "PENDING":
            continue
        actor = review.get("user") or {}
        login = actor.get("login")
        kind = actor.get("type")
        if not login or not kind:
            return None, False
        if login.lower() == author.lower() or kind == "Bot" or login.lower().endswith("[bot]"):
            continue
        if kind != "User":
            return None, False
        submitted = review.get("submitted_at")
        if not submitted:
            return None, False
        times.append(parse_time(submitted))
    return min(times) if times else None, True


class GitHubAPI:
    def __init__(self, token: str | None = None, requester: Callable | None = None, max_pages: int = 100):
        self.token = token
        self.requester = requester or self._request
        self.max_pages = max_pages
        self.requests = 0

    def _request(self, url: str) -> tuple[list, str | None]:
        headers = {"Accept": "application/vnd.github+json",
                   "X-GitHub-Api-Version": "2022-11-28",
                   "User-Agent": "OpenSiro-Public-PR-Telemetry"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=25) as response:
                data = json.load(response)
                return data, response.headers.get("Link")
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ValueError) as exc:
            code = getattr(exc, "code", None)
            raise PRActivityError(f"GitHub API request failed ({code or type(exc).__name__}) for {url.split('?')[0]}") from exc

    def pages(self, path: str):
        url = BASE + path
        visited = set()
        for _ in range(self.max_pages):
            parsed = urllib.parse.urlparse(url)
            if parsed.scheme != "https" or parsed.hostname != "api.github.com" or not (parsed.path.startswith("/repos/opensiro/") or re.fullmatch(r"/repositories/[0-9]+/pulls(?:/[0-9]+/reviews)?", parsed.path)):
                raise PRActivityError("refusing unexpected API pagination destination")
            if url in visited:
                raise PRActivityError("API pagination loop")
            visited.add(url)
            items, link = self.requester(url)
            self.requests += 1
            if not isinstance(items, list):
                raise PRActivityError("expected a JSON list from GitHub API")
            yield items
            next_links = [match.group(1) for match in LINK.finditer(link or "") if match.group(2) == "next"]
            if not next_links:
                return
            url = next_links[0]
        raise PRActivityError(f"pagination limit exceeded ({self.max_pages} pages)")

    def list_prs(self, repo: str, *, state: str, cutoff: datetime | None = None) -> list[dict]:
        path = f"/repos/{repo}/pulls?state={state}&sort=updated&direction=desc&per_page=100"
        result = []
        for page in self.pages(path):
            for item in page:
                if cutoff is None or parse_time(item["updated_at"]) > cutoff:
                    result.append(item)
            if cutoff is not None and page and parse_time(page[-1]["updated_at"]) <= cutoff:
                return result
        return result

    def list_reviews(self, repo: str, number: int) -> list[dict]:
        return [review for page in self.pages(f"/repos/{repo}/pulls/{number}/reviews?per_page=100") for review in page]


def compute_repository(repo: str, recent: list[dict], open_prs: list[dict],
                       reviews: dict[int, list[dict]], as_of: datetime) -> dict:
    if repo not in REPOSITORIES:
        raise PRActivityError("repository outside bounded OSS scope")
    if len({pr["id"] for pr in recent}) != len(recent):
        raise PRActivityError("duplicate PR identity in recent dataset")
    if len({pr["id"] for pr in open_prs}) != len(open_prs):
        raise PRActivityError("duplicate open PR identity")
    if any(pr.get("state") != "open" for pr in open_prs):
        raise PRActivityError("open stock contains non-open PR")
    missing_reviews = {pr["number"] for pr in recent} - set(reviews)
    first_reviews = {
        pr["number"]: first_qualifying_review(pr, reviews[pr["number"]])
        if pr["number"] in reviews else (None, False)
        for pr in recent
    }
    rows = {}
    for label, delta in WINDOWS.items():
        cutoff = as_of - delta
        opened = sum(in_window(pr.get("created_at"), cutoff, as_of) for pr in recent)
        merged = [pr for pr in recent if in_window(pr.get("merged_at"), cutoff, as_of)]
        closed = [pr for pr in recent if pr.get("merged_at") is None
                  and pr.get("state") == "closed" and in_window(pr.get("closed_at"), cutoff, as_of)]
        merge_hours = [(parse_time(pr["merged_at"]) - parse_time(pr["created_at"])).total_seconds()/3600 for pr in merged]
        review_hours = []
        review_samples = []
        ambiguous = 0
        ambiguous_numbers = []
        for pr in recent:
            dt, complete = first_reviews[pr["number"]]
            if not complete:
                ambiguous += 1
                ambiguous_numbers.append(pr["number"])
            elif dt and cutoff < dt <= as_of:
                hours = (dt - parse_time(pr["created_at"])).total_seconds()/3600
                review_hours.append(hours)
                review_samples.append({"number": pr["number"], "hours": round(hours, 4), "first_review_at": timestamp(dt)})
        review_latency = quantile(review_hours) if not ambiguous else dict(NULL_STATS)
        known_unreviewed = sum(1 for (dt, complete) in first_reviews.values() if complete and dt is None)
        rows[label] = {
            "opened": opened,
            "merged": len(merged),
            "closed_without_merge": len(closed),
            "opened_pr_numbers": sorted(pr["number"] for pr in recent if in_window(pr.get("created_at"), cutoff, as_of)),
            "merged_pr_numbers": sorted(pr["number"] for pr in merged),
            "closed_unmerged_pr_numbers": sorted(pr["number"] for pr in closed),
            "merge_latency_samples": sorted(
                ({"number": pr["number"], "hours": round((parse_time(pr["merged_at"]) -
                    parse_time(pr["created_at"])).total_seconds()/3600, 4)} for pr in merged),
                key=lambda x: x["number"]),
            "time_to_merge": quantile(merge_hours),
            "first_review_latency_samples": sorted(review_samples, key=lambda x: x["number"]) if not ambiguous else None,
            "first_review_latency": {**review_latency, "status": "complete" if not ambiguous else "partial",
                                     "unresolved_review_histories": ambiguous,
                                     "complete_review_histories": len(recent) - ambiguous,
                                     "known_unreviewed_prs": known_unreviewed,
                                     "unresolved_pr_numbers": sorted(ambiguous_numbers)},
        }
    return {
        "status": "complete" if not any(row["first_review_latency"]["status"] == "partial" for row in rows.values()) else "partial",
        "source": f"https://api.github.com/repos/{repo}/pulls",
        "pr_identity": "GitHub immutable PR id; one PR counts once per owning repository",
        "open_prs": len(open_prs),
        "open_pr_numbers": sorted(pr["number"] for pr in open_prs),
        "recent_prs_examined": len(recent),
        "windows": rows,
    }


def collect_one(api: GitHubAPI, repo: str, as_of: datetime) -> dict:
    cutoff = as_of - WINDOWS["30d"]
    recent = api.list_prs(repo, state="all", cutoff=cutoff)
    open_prs = api.list_prs(repo, state="open")
    # Current open stock is an observation at fetch time, not an atomic historic state.
    # A review API error must not erase independently complete PR count data.
    reviews: dict[int, list[dict]] = {}
    review_errors = []
    for pr in recent:
        try:
            reviews[pr["number"]] = api.list_reviews(repo, pr["number"])
        except PRActivityError as exc:
            review_errors.append(str(exc))
            break  # avoid repeated requests during a rate-limit outage
    result = compute_repository(repo, recent, open_prs, reviews, as_of)
    if review_errors:
        result["review_collection_issue"] = review_errors[0]
    return result


def collect(api: GitHubAPI, as_of: datetime) -> dict:
    result = {
        "schema_version": 1,
        "classification": "secondary_non_kpi",
        "collected_at": timestamp(as_of),
        "source": "GitHub public REST API /pulls and /pulls/{number}/reviews",
        "scope": list(REPOSITORIES),
        "windows": list(WINDOWS),
        "window_semantics": "(collected_at - window, collected_at], UTC; event counts not stock delta",
        "review_definition": "first submitted non-author user review; excludes PENDING, author, bots and ordinary PR issue comments",
        "quantile_method": "median and nearest-rank p90; hours; no sample -> null with n=0",
        "source_completeness_rule": "PR event counts and open stock are complete only with exhaustive API pagination; missing review histories null review latency, not PR counts",
        "limitation": "GitHub PR timestamps show current PR state and latest close, not every historic reopen/close transition. API sampling is not an atomic snapshot.",
        "repositories": {},
        "collector_revision": os.environ.get("GITHUB_SHA"),
    }
    for repo in REPOSITORIES:
        try:
            result["repositories"][repo] = collect_one(api, repo, as_of)
        except (PRActivityError, KeyError, TypeError, ValueError) as exc:
            result["repositories"][repo] = {
                "status": "unavailable", "reason": str(exc),
                "source": f"https://api.github.com/repos/{repo}/pulls",
                "open_prs": None, "windows": None,
            }
    result["api_requests"] = api.requests
    result["complete_repositories"] = sum(x["status"] == "complete" for x in result["repositories"].values())
    return result


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--max-pages", type=int, default=100)
    p.add_argument("--token-env", default="GITHUB_TOKEN")
    args = p.parse_args()
    if args.max_pages < 1:
        raise SystemExit("max-pages must be positive")
    now = datetime.now(timezone.utc).replace(microsecond=0)
    result = collect(GitHubAPI(token=os.getenv(args.token_env), max_pages=args.max_pages), now)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(f"PR telemetry: {result['complete_repositories']}/5 complete; source snapshot {args.output}")
    return 0 if result["complete_repositories"] == len(REPOSITORIES) else 2


if __name__ == "__main__":
    sys.exit(main())
