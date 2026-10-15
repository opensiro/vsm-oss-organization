#!/usr/bin/env python3
"""Read first-party GitHub S1 evidence without promoting URLs to S3 authority.

This module is a *factual* source verifier: it cannot grant D1-A, determine
whether a real question requires S3 rather than S1/S2, or replace the S1
actor's independent judgment. Never accepts permissions claimed by the model.
"""
from __future__ import annotations

from datetime import datetime, timezone
import json
import os
import re
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

S1_REPOS = frozenset({"vsm-harness-index", "vsm-harness-skills", "awesome-vsm-harness"})
ISSUE = re.compile(r"https://github\.com/opensiro/(vsm-harness-index|vsm-harness-skills|awesome-vsm-harness)/issues/([1-9][0-9]*)$")
COMMENT = re.compile(r"https://github\.com/opensiro/(vsm-harness-index|vsm-harness-skills|awesome-vsm-harness)/issues/([1-9][0-9]*)#issuecomment-([1-9][0-9]*)$")
PR = re.compile(r"https://github\.com/opensiro/(vsm-harness-index|vsm-harness-skills|awesome-vsm-harness)/pull/([1-9][0-9]*)$")
USER = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]{0,38}$")
HEADER = "OPENSIRO_S1_ADMISSION_V1\n"
WRITE_ROLES = frozenset({"write", "maintain", "admin"})


class GitHubEvidenceError(ValueError):
    pass


def check(condition: bool, message: str) -> None:
    if not condition:
        raise GitHubEvidenceError(message)


def issue_parts(url: str) -> tuple[str, str]:
    m = ISSUE.fullmatch(url) if isinstance(url, str) else None
    check(m is not None, "S1 issue URL must be in owning bounded repository")
    return m.group(1), m.group(2)


def comment_parts(url: str, target: str) -> tuple[str, str, str]:
    m = COMMENT.fullmatch(url) if isinstance(url, str) else None
    check(m is not None and url.startswith(target + "#issuecomment-"),
          "comment must be attached to exact owning S1 issue")
    return m.group(1), m.group(2), m.group(3)


def instant(value: object) -> datetime:
    check(isinstance(value, str) and value.endswith("Z"), "missing UTC source timestamp")
    try:
        d = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as e:
        raise GitHubEvidenceError("invalid UTC timestamp") from e
    check(d.tzinfo is not None, "timestamp must be aware")
    return d.astimezone(timezone.utc)


class GitHubS1Reader:
    """Use a narrowly allowlisted GitHub REST source API; no writes or trust in URL shapes."""

    def __init__(self, *, token: str | None = None, fetch=None):
        self._token = token if token is not None else os.environ.get("GITHUB_TOKEN")
        self._fetch = fetch
        check(fetch is not None or isinstance(self._token, str) and bool(self._token),
              "authenticated GitHub REST read token required for collaborator permission checks")

    def _get(self, repo: str, route: str) -> dict:
        check(repo in S1_REPOS, "repository outside operational S1 boundary")
        path = "/repos/opensiro/" + repo + "/" + route
        if self._fetch is not None:
            obj = self._fetch(path)
        else:
            req = Request("https://api.github.com" + path, headers={
                "Authorization": "Bearer " + self._token,
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "opensiro-s3-s1-primary-evidence",
            })
            try:
                with urlopen(req, timeout=15) as res:
                    raw = res.read(300001)
            except (HTTPError, URLError, TimeoutError) as exc:
                raise GitHubEvidenceError("S1 GitHub source unavailable; fail closed") from exc
            check(len(raw) <= 300000, "GitHub source payload exceeds bound")
            try:
                obj = json.loads(raw)
            except (ValueError, UnicodeError) as exc:
                raise GitHubEvidenceError("GitHub source JSON invalid") from exc
        check(type(obj) is dict, "GitHub source object is unavailable")
        return obj

    def _authorized_user(self, repo: str, login: object) -> str:
        check(type(login) is str and USER.fullmatch(login) is not None,
              "unknown or invalid S1 actor login")
        result = self._get(repo, "collaborators/" + login + "/permission")
        check(result.get("permission") in WRITE_ROLES,
              "no independently inspected S1 write/maintain/admin capability")
        return login

    def issue(self, repo: str, number: str, *, require_open: bool) -> dict:
        obj = self._get(repo, "issues/" + number)
        check(obj.get("html_url") == f"https://github.com/opensiro/{repo}/issues/{number}"
              and not obj.get("pull_request"), "source issue missing or mismatched")
        if require_open:
            check(obj.get("state") == "open", "current S1 work item not open")
        return obj

    def comment(self, target: str, comment_url: str) -> dict:
        repo, issue_no, comment_id = comment_parts(comment_url, target)
        obj = self._get(repo, "issues/comments/" + comment_id)
        check(obj.get("html_url") == comment_url
              and isinstance(obj.get("user"), dict)
              and isinstance(obj.get("body"), str),
              "source comment missing, invalid or wrong owning issue")
        return obj

    def read_s1_admission(self, case: dict) -> dict:
        """Verify current authentic S1 ADMIT only, never claim S3-level semantic authority."""
        check(type(case) is dict, "S3 candidate case is not a source object")
        target = case.get("return_target")
        repo, issue_no = issue_parts(target)
        self.issue(repo, issue_no, require_open=True)
        ref = case.get("s1_admission_comment_url")
        approval = self.comment(target, ref)
        login = self._authorized_user(repo, approval["user"].get("login"))
        text = approval["body"]
        check(text.startswith(HEADER), "no explicit standardized S1 admission record")
        try:
            admitted = json.loads(text[len(HEADER):])
        except ValueError as exc:
            raise GitHubEvidenceError("invalid S1 admission record") from exc
        check(type(admitted) is dict
              and set(admitted) == {"verdict", "target", "commitment_id"}
              and admitted.get("verdict") == "ADMIT"
              and admitted.get("target") == target
              and admitted.get("commitment_id") == case.get("commitment_id"),
              "not an admitted current bounded S1 work item")
        refs = case.get("nonlocal_evidence_refs")
        check(type(refs) is list and len(refs) >= 2,
              "nonlocal primary facts not supplied")
        domains = set()
        for item in refs:
            source_repo, source_no = issue_parts(item)
            self.issue(source_repo, source_no, require_open=False)
            domains.add(source_repo)
        check(len(domains) >= 2, "nonlocal source inventory must span two real S1 domains")
        return {
            "admitted": True,
            "return_target": target,
            "commitment_id": case["commitment_id"],
            "s1_admission_ref": ref,
            "s1_admission_actor": login,
            "source_repositories_verified": sorted(domains),
            "nonlocal_right_verified": False,
            "s1_s2_s5_falsifiers_checked": False,
            "limitation": "S1 admission/source existence verified; nonlocal S3 discretion requires separate actual semantic examination."
        }

    def verify_s1_return(self, action: dict, *, acknowledgement_ref: str,
                         effect_pr_ref: str) -> dict:
        """Verify same-target actor + merged S1 PR, rejecting fake/agent-owned closure."""
        check(type(action) is dict and action.get("status") ==
              "S1_RETURN_SENT_EFFECT_UNVERIFIED" and action.get("closed") is False,
              "S3 return is not an unclosed delivered action")
        target = action.get("return_target")
        repo, issue_no = issue_parts(target)
        self.issue(repo, issue_no, require_open=False)
        transport_ref = action.get("transport_url")
        sent = self.comment(target, transport_ref)
        ack = self.comment(target, acknowledgement_ref)
        transport_actor = sent["user"].get("login")
        ack_actor = self._authorized_user(repo, ack["user"].get("login"))
        check(ack_actor != transport_actor,
              "S3 transport actor cannot self-attest S1 acknowledgement")
        check(instant(ack.get("created_at")) > instant(sent.get("created_at")),
              "S1 acknowledgement predates current S3 return")
        m = PR.fullmatch(effect_pr_ref) if isinstance(effect_pr_ref, str) else None
        check(m is not None and m.group(1) == repo,
              "effect PR must belong to exact owning S1 repository")
        p = self._get(repo, "pulls/" + m.group(2))
        check(p.get("html_url") == effect_pr_ref
              and p.get("merged_at") is not None
              and isinstance(p.get("merge_commit_sha"), str)
              and re.fullmatch(r"[0-9a-f]{40}", p["merge_commit_sha"]) is not None
              and type(p.get("changed_files")) is int and p["changed_files"] > 0,
              "effect PR not demonstrably merged and changed")
        check(instant(p.get("merged_at")) >= instant(ack.get("created_at")),
              "effect merge predates S1 acknowledgement")
        check(isinstance(p.get("body"), str)
              and target in p["body"]
              and transport_ref in p["body"],
              "merged S1 PR does not link exact work and S3 instruction")
        check(type(p.get("user")) is dict and p["user"].get("login") != transport_actor,
              "S3 actor authored alleged independent S1 repair")
        self._authorized_user(repo, p["user"]["login"])
        return {
            "acknowledgement_ref": acknowledgement_ref,
            "effect_refs": [effect_pr_ref],
            "s1_owner_verified": True,
            "effect_verified": True,
            "s1_independent_of_s3_actor": True,
            "limitation": "GitHub source/permission/chronology checked; semantic correctness still requires task-level assessment."
        }
