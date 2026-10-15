# Live GitHub S5-source verification and S1 transport — D1-A

**Scope:** M3 #5, D1-A; **not active**. [`autonomous-d1a.json`](../../contracts/s3/autonomous-d1a.json) remains `PENDING_S5_PUBLIC_ATTESTATION`. Neither a GH login, a CI check nor a newly created GitHub issue comment can alone establish S5 authority. The *genuine parent-holder decision* is a separate source from an assistant-created GitHub artifact, even when tools use the parent's connected account.

## Source-based D1-A grant

[`github_s5_authority.py`](github_s5_authority.py) checks live Organization `main`, the activation source commit's ancestry, current grant bytes and a separately published grant snapshot, the exact public S5 authorization message, issuer login, finite term and **all M3 #5 comment pages for revocation**. It requires a **separate trusted `parent_authorship(comment)` check**: authenticated GitHub account attribution *by itself* is insufficient to prove the owner personally made the governing S5 decision, given delegated credentials and agent tools. This check must be provided by a genuinely separate trusted parent-channel mechanism; `lambda _:True` is a **test fixture**, never a production authenticator.

Explicit public machine-readable parent source, as an example of the record format **not a valid pre-issued grant**:

```text
OPENSIRO_S5_D1A_AUTHORIZATION_V1
{"decision":"AUTHORIZE_D1A","recipient_execution_identity":"<real separate agent runtime>","allowed_classes":["CONTINUE","REQUIRE_REPAIR"],"allowed_standing_commitments":["selected-methodology-continuity","canonical-publication-continuity"],"effective_from_utc":"<future UTC>","expires_at_utc":"<at most 30 days>","grant_publication_commit":"<40-char SHA of earlier published ACTIVE grant snapshot>"}
```

An owner-governed revocation comment uses prefix `OPENSIRO_S5_D1A_REVOCATION_V1` and JSON `{"owner_attestation_url":"<the original owner comment URL>"}`. The checker exhaustively reads a bounded total of up to 3000 comments, failing closed if pagination is inaccessible or truncated. A separately trusted parent authentication mechanism must cover S5 issuance; revocation posted from the owner's verified account is conservatively binding.

**Non-circular two-phase publication:** the first grant commit cannot cite its own SHA, and the owner's S5 decision comment cannot cite that SHA until the commit exists. After separately confirmed S5 permission to prepare an inert snapshot, publish a **non-operative first-phase `ACTIVE` snapshot** with both `owner_attestation_url=null` and `grant_publication_commit=null`, with the concrete recipient and finite dates already fixed. Its `ACTIVE` status alone grants nothing: the existing structural gate still fails. Once this first commit is merged into `main` and its SHA is known, the legitimate S5 holder **personally** publishes an attributable authorization comment containing that SHA and a start date no earlier than the comment creation time. Then a second commit fills **both** `owner_attestation_url` (the owner's comment URL) and `grant_publication_commit` (the first SHA) while every other grant field remains identical. Live checks verify first-phase source ancestry, both snapshots, the personal owner source and revocations. These steps are not authorized or performed by this engineering fix; assistant-authored GitHub text cannot replace personal S5 consent.

## S1 delivery

[`github_s1_delivery.py`](github_s1_delivery.py) transports **only** a bounded, authenticated, admitted agent-owned `CONTINUE` or `REQUIRE_REPAIR` to the named currently open owning-S1 issue; it checks live GitHub token identity (must not be the human parent), owning-repository write permission, exact target and issue status. It writes one machine-readable, SHA-256 identified issue comment, pre-scans current issue comments to avoid duplicate sending on retries and refuses to post if it cannot exhaust the source history. Receipt means `S1_RETURN_SENT_EFFECT_UNVERIFIED` and must never mark S1 acknowledgement or effect.

Required external verifiers `verify_authority` and `verify_admission` must be supplied by a trusted, separately checked host. Calling the transport helper with an attacker-created callback does **not** satisfy the real S5/agent or whole-system semantic threshold. The helper cannot independently authenticate owner intention or decide whether a S1 conflict requires S3; it is explicitly a **transport primitive**, not a standalone public autonomous decision endpoint. An actual standard mode must connect this to trusted live parent assurance and a source-backed semantic S3 assessment before accepting write permission.

[`github_rest.py`](github_rest.py) supplies a concrete token-backed HTTP adapter with only whitelisted source GET and bounded S1-comment POST; it never calls an arbitrary URL, changes grade/code, merges, or grants authority. Use it for GitHub evidence read calls and the delivery adapter. Secret tokens never appear in source artifacts or test records.

## Status and assessment

Tests simulate GitHub REST responses and transport only; they do not contact GitHub for a S3 transaction and do not prove parent authorship. With the current D1-A grant pending, `decision_loop.py` remains blocked **before** any model or S1 transport. The user-selected source-first VSM evidence method is sufficient for a *positive* `S3=A` assessment only once the decisive autonomous owner and feedback path genuinely operate in the supported first-party mode; a fake run is not required.
