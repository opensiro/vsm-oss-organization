#!/usr/bin/env python3
"""Prospective first-winner S3* claim refs, Organization #194 (not Index approval)."""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

REPO = "opensiro/vsm-oss-organization"
API = "https://api.github.com/repos/" + REPO
WAVE = re.compile(r"S3STAR-INDEX-BATCH-\d{8}-W\d{3}\Z")
SHA = re.compile(r"[0-9a-f]{40}\Z")
IDENT = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:@/-]{7,120}\Z")
OUTCOMES = {"PASS", "FINDING", "INSUFFICIENT"}
TERMINAL = OUTCOMES | {"YIELDED", "BLOCKED"}


class AuditLockError(RuntimeError):
    pass


class GitHubError(AuditLockError):
    def __init__(self, code, message):
        super().__init__("GitHub HTTP %s: %s" % (code, message[:240]))
        self.code = code


class GitHub:
    def __init__(self, token):
        if not token:
            raise AuditLockError("GH_TOKEN/GITHUB_TOKEN is required")
        self.token = token

    def request(self, method, path, data=None):
        body = json.dumps(data).encode() if data is not None else None
        req = urllib.request.Request(API + path, method=method, data=body, headers={
            "Authorization": "Bearer " + self.token,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
        })
        try:
            with urllib.request.urlopen(req, timeout=20) as response:
                return json.loads(response.read())
        except urllib.error.HTTPError as exc:
            raise GitHubError(exc.code, exc.read().decode(errors="replace")) from exc


def validate(payload):
    if not WAVE.fullmatch(payload["wave"]) or not (1 <= payload["batch"] <= 999999):
        raise AuditLockError("invalid wave/batch")
    if payload["kind"] not in ("semantic", "lifecycle") or not (1 <= payload["row"] <= 999):
        raise AuditLockError("invalid scope: one specific row and semantic/lifecycle kind required")
    if not all(SHA.fullmatch(payload[k]) for k in ("source_sha", "index_sha")):
        raise AuditLockError("original source and index snapshot require pinned 40-character SHAs")
    if not all(IDENT.fullmatch(payload[k]) for k in ("actor", "claim_id")):
        raise AuditLockError("real actor/context and unique claim ID required")
    if not re.fullmatch(
        r"https://github\.com/opensiro/vsm-oss-organization/issues/\d+#issuecomment-\d+",
        payload["manifest"],
    ):
        raise AuditLockError("manifest must link to an actual Organization freeze comment")
    if type(payload["epoch"]) is not int or payload["epoch"] < 0:
        raise AuditLockError("invalid epoch")


def base(payload):
    return "s3star-locks/v1/{wave}/{batch}/{kind}-{row}".format(**payload)


def reference(payload, event):
    return "refs/tags/" + base(payload) + "/e%d-%s" % (payload["epoch"], event)


def record_path(payload, event):
    return "records/s3star/events/" + base(payload) + "/e%d-%s.json" % (payload["epoch"], event)


def read_ref(api, ref):
    try:
        return api.request("GET", "/git/ref/" + urllib.parse.quote(ref.removeprefix("refs/"), safe="/"))
    except GitHubError as exc:
        if exc.code == 404:
            return None
        raise


def file_at(api, commit, path):
    response = api.request(
        "GET", "/contents/" + urllib.parse.quote(path, safe="/") + "?ref=" + commit
    )
    if response.get("encoding") != "base64":
        raise AuditLockError("invalid GitHub event payload")
    return json.loads(base64.b64decode(response["content"]))


def event(api, payload, name):
    tag = read_ref(api, reference(payload, name))
    if tag is None:
        return None
    event_data = file_at(api, tag["object"]["sha"], record_path(payload, name))
    slot = {k: payload[k] for k in ("wave", "batch", "kind", "row", "epoch")}
    if event_data.get("schema") != "s3star-slot-v1" or event_data.get("slot") != slot or event_data.get("state") != name:
        raise AuditLockError("tag points at invalid or unrelated event")
    return event_data


def active_epoch(api, payload):
    path = "records/s3star/handoffs/" + base(payload) + ".json"
    main = api.request("GET", "/git/ref/heads/main")["object"]["sha"]
    try:
        handoff = file_at(api, main, path)
    except GitHubError as exc:
        if exc.code == 404:
            return 0, None
        raise
    epoch = handoff.get("active_epoch")
    if handoff.get("schema") != "s3star-handoff-v1" or type(epoch) is not int or epoch < 1:
        raise AuditLockError("invalid integrated handoff record")
    old = dict(payload, epoch=epoch - 1)
    previous = event(api, old, "claim")
    if not previous or previous["claim_id"] != handoff.get("previous_claim_id"):
        raise AuditLockError("handoff predecessor mismatch")
    finished = event(api, old, "terminal")
    if (not finished or finished.get("outcome") != "YIELDED") and not handoff.get("maintainer_override_issue"):
        raise AuditLockError("requires YIELDED or explicit maintainer override")
    if not re.fullmatch(r"https://github\.com/opensiro/vsm-oss-organization/pull/\d+", str(handoff.get("authorization_pr", ""))):
        raise AuditLockError("handoff must identify its integrated Organization PR")
    if not all(IDENT.fullmatch(str(handoff.get(k, ""))) for k in ("next_claim_id", "next_actor")):
        raise AuditLockError("handoff must name exact next actor and claim")
    return epoch, handoff


def create_event(api, payload, state, outcome=None, evidence=None):
    """Only POST /git/refs admits a winner: on existing tag return LOCKED."""
    main = api.request("GET", "/git/ref/heads/main")["object"]["sha"]
    parent = api.request("GET", "/git/commits/" + main)
    data = {
        "schema": "s3star-slot-v1",
        "slot": {k: payload[k] for k in ("wave", "batch", "kind", "row", "epoch")},
        "state": state,
        "claim_id": payload["claim_id"],
        "actor": payload["actor"],
        "manifest": payload["manifest"],
        "source_sha": payload["source_sha"],
        "index_sha": payload["index_sha"],
    }
    if state == "terminal":
        data.update(outcome=outcome, evidence_url=evidence)
    tree = api.request("POST", "/git/trees", {
        "base_tree": parent["tree"]["sha"],
        "tree": [{"path": record_path(payload, state), "mode": "100644",
                  "type": "blob", "content": json.dumps(data, sort_keys=True) + "\n"}],
    })
    commit = api.request("POST", "/git/commits", {
        "message": "S3* %s: %s batch %s %s row %s" % (
            state, payload["wave"], payload["batch"], payload["kind"], payload["row"]),
        "tree": tree["sha"], "parents": [main],
    })
    ref = reference(payload, state)
    try:
        api.request("POST", "/git/refs", {"ref": ref, "sha": commit["sha"]})
    except GitHubError as exc:
        if exc.code == 422 and read_ref(api, ref) is not None:
            return {"status": "LOCKED", "ref": ref}
        raise
    return {"status": "RECORDED", "ref": ref, "commit": commit["sha"]}


def claim(api, payload):
    validate(payload)
    epoch, successor = active_epoch(api, dict(payload, epoch=0))
    if payload["epoch"] != epoch:
        raise AuditLockError("stale or unauthorized claim epoch")
    if successor and (payload["claim_id"], payload["actor"]) != (
        successor["next_claim_id"], successor["next_actor"]
    ):
        raise AuditLockError("handoff forbids an unassigned new claimant")
    if read_ref(api, reference(payload, "claim")) is not None:
        return {"status": "LOCKED", "ref": reference(payload, "claim")}
    return create_event(api, payload, "claim")


def finalize(api, payload, outcome, evidence_url):
    validate(payload)
    if outcome not in TERMINAL:
        raise AuditLockError("invalid terminal result")
    if not re.fullmatch(
        r"https://github\.com/opensiro/(?:vsm-oss-organization|vsm-harness-index)/(?:issues|pull)/\d+(?:#issuecomment-\d+)?",
        evidence_url,
    ):
        raise AuditLockError("terminal receipt requires an owning GitHub record")
    if active_epoch(api, dict(payload, epoch=0))[0] != payload["epoch"]:
        raise AuditLockError("old claimant was superseded")
    original = event(api, payload, "claim")
    if not original or any(original.get(k) != payload[k] for k in (
        "claim_id", "actor", "manifest", "source_sha", "index_sha"
    )):
        raise AuditLockError("nonowner or changed source/ref cannot finalize")
    if read_ref(api, reference(payload, "terminal")) is not None:
        return {"status": "LOCKED", "ref": reference(payload, "terminal")}
    return create_event(api, payload, "terminal", outcome, evidence_url)


def reduce_receipts(receipts):
    """Count verified slot outcomes at most once; duplicate/conﬂict -> fail closed."""
    slots = {}
    duplicates = 0
    for item in receipts:
        if item.get("verified_owner") is not True or item.get("outcome") not in OUTCOMES:
            continue
        key = tuple(item[k] for k in ("wave", "batch", "kind", "row"))
        fingerprint = (item["claim_id"], item["outcome"])
        if key in slots:
            if slots[key] != fingerprint:
                raise AuditLockError("conflicting same-slot terminal receipts")
            duplicates += 1
        else:
            slots[key] = fingerprint
    return {"unique": len(slots), "supplements": duplicates,
            "semantic": sum(key[2] == "semantic" for key in slots),
            "lifecycle": sum(key[2] == "lifecycle" for key in slots)}


def verify_slots(api, slots):
    """Verify accepted Git refs before reducing; never use producer issue text alone."""
    results = []
    for scope in slots:
        epoch, _ = active_epoch(api, dict(scope, epoch=0))
        unit = dict(scope, epoch=epoch)
        first = event(api, unit, "claim")
        last = event(api, unit, "terminal")
        if last is None:
            continue
        if not first or any(first.get(k) != last.get(k) for k in (
            "claim_id", "actor", "manifest", "source_sha", "index_sha"
        )):
            raise AuditLockError("terminal receipt does not match accepted claimant")
        results.append(dict(scope, verified_owner=True,
                            claim_id=first["claim_id"], outcome=last["outcome"]))
    return reduce_receipts(results)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("claim", "terminal"))
    for key in ("wave", "kind", "claim-id", "actor", "manifest", "source-sha", "index-sha"):
        parser.add_argument("--" + key, required=True)
    parser.add_argument("--batch", required=True, type=int)
    parser.add_argument("--row", required=True, type=int)
    parser.add_argument("--epoch", default=0, type=int)
    parser.add_argument("--outcome")
    parser.add_argument("--evidence-url")
    args = parser.parse_args()
    payload = vars(args)
    payload["claim_id"] = payload.pop("claim_id")
    try:
        api = GitHub(os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN"))
        if args.action == "claim":
            result = claim(api, payload)
        else:
            if not args.outcome or not args.evidence_url:
                raise AuditLockError("--outcome and --evidence-url required")
            result = finalize(api, payload, args.outcome, args.evidence_url)
        print(json.dumps(result, sort_keys=True))
        return 0 if result["status"] == "RECORDED" else 3
    except (AuditLockError, KeyError, ValueError) as exc:
        print(json.dumps({"status": "BLOCKED", "reason": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
