#!/usr/bin/env python3
"""Bounded GitHub REST HTTP client for first-party S3 facts and S1 delivery.

Only enumerated GET and narrowly scoped S1 issue-comment POST are possible.
GitHub token permissions, actor trust and D1-A mandate still apply separately.
"""
from __future__ import annotations
import json
import os
import re
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

S1="(?:vsm-harness-index|vsm-harness-skills|awesome-vsm-harness)"
SHA="[0-9a-f]{40}"
USER="[A-Za-z0-9][A-Za-z0-9-]{0,38}"
ORG="/repos/opensiro/vsm-oss-organization"
GET_PATTERNS=[
 r"/user",
 ORG+r"/branches/main",
 ORG+r"/compare/"+SHA+r"\.\.\."+SHA,
 ORG+r"/contents/contracts/s3/autonomous-d1a\.json\?ref="+SHA,
 ORG+r"/issues/comments/[1-9][0-9]*",
 ORG+r"/issues/5",
 ORG+r"/issues/5/comments\?per_page=100&page=(?:[1-9]|[12][0-9]|30)",
 rf"/repos/opensiro/{S1}/issues/[1-9][0-9]*",
 rf"/repos/opensiro/{S1}/issues/comments/[1-9][0-9]*",
 rf"/repos/opensiro/{S1}/pulls/[1-9][0-9]*",
 rf"/repos/opensiro/{S1}/collaborators/{USER}/permission",
 rf"/repos/opensiro/{S1}/issues/[1-9][0-9]*/comments\?per_page=100&page=(?:[1-9]|[12][0-9]|30)"
]
POST_PATTERNS=[rf"/repos/opensiro/{S1}/issues/[1-9][0-9]*/comments"]

class GitHubTransportError(ValueError):
    pass

class GitHubREST:
    def __init__(self, token=None, *, transport=None):
        self.token=token if token is not None else os.environ.get("GITHUB_TOKEN",os.environ.get("GH_TOKEN"))
        self.transport=transport
        if transport is None and (not isinstance(self.token,str) or not self.token):
            raise GitHubTransportError("GITHUB_TOKEN/ GH_TOKEN required")

    def __call__(self, method, path, payload=None):
        if method not in ("GET","POST") or not isinstance(path,str):
            raise GitHubTransportError("Unsupported GitHub request")
        allowed=GET_PATTERNS if method=="GET" else POST_PATTERNS
        if not any(re.fullmatch(p,path) for p in allowed):
            raise GitHubTransportError("GitHub API route not allowlisted for this S3 mode")
        if method=="GET" and payload is not None:
            raise GitHubTransportError("GET must be read only")
        if method=="POST" and (type(payload) is not dict or
                               set(payload)!={"body"} or
                               not isinstance(payload["body"],str) or
                               len(payload["body"].encode())>6400):
            raise GitHubTransportError("S1 mutation must be one bounded issue comment")
        if self.transport is not None:
            response=self.transport(method,path,payload)
        else:
            body=json.dumps(payload).encode() if method=="POST" else None
            req=Request("https://api.github.com"+path,data=body,method=method,headers={
                "Authorization":"Bearer "+self.token,
                "Accept":"application/vnd.github+json",
                "X-GitHub-Api-Version":"2022-11-28",
                "Content-Type":"application/json",
                "User-Agent":"opensiro-s3-d1a"
            })
            try:
                with urlopen(req,timeout=20) as resp:
                    result=resp.read(400001)
            except (HTTPError,URLError,TimeoutError) as exc:
                raise GitHubTransportError("GitHub source/transport unavailable; fail closed") from exc
            if len(result)>400000:
                raise GitHubTransportError("GitHub response too large")
            try:response=json.loads(result)
            except ValueError as exc:
                raise GitHubTransportError("Malformed GitHub API response") from exc
        if type(response) not in (dict,list):
            raise GitHubTransportError("Unexpected GitHub response type")
        return response

    def get(self,path):
        return self("GET",path,None)
