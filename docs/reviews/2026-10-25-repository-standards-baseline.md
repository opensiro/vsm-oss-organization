# Repository standards baseline — 2026-10-25

**Owner:** `opensiro/vsm-oss-organization`, [#288](https://github.com/opensiro/vsm-oss-organization/issues/288). **Type:** source-backed comparative probe of repository metadata and root handoff. **No external writes or settings changes.** `opensiro/upstream` was included only as an **adjacent comparator**.

## Sources and scope

- Canonical boundary: [Organization README](../../README.md) and [`START_HERE`](../../START_HERE.md) on current main, **five in-scope repos** (Profile, Skills, Index, Awesome, Organization); operational S1 domains remain Index/Skills/Awesome only.
- Mandatory routing oracle: [`ROUTING_CONFORMANCE`](../ROUTING_CONFORMANCE.md); its direct-root README requirements apply only inside the declared boundary.
- Metadata: GitHub `GET /repos/opensiro/{repo}`. Branch: `GET /repos/opensiro/{repo}/branches/main`. Active rulesets: `GET /repos/opensiro/{repo}/rulesets`. Files: root README and directory listings on default branch.
- Reproducible deterministic code: [`check_repository_standards.py`](../../scripts/check_repository_standards.py) and [`test_repository_standards.py`](../../tests/test_repository_standards.py). The live CLI uses the public REST API; separately, authenticated GitHub connector readback was used for fields omitted anonymously.

## Results

| Dimension | Five in-scope repos | Adjacent Upstream | Interpretation |
| --- | --- | --- | --- |
| Direct shared START_HERE / TODO and Organization route in root README | **5/5 PASS** | START_HERE + TODO missing; Organization route present | Required in-scope; advisory adjacent drift |
| `delete_branch_on_merge` | **5/5 `true`** (authenticated metadata) | **`false`** (authenticated metadata) | Advisory comparison; anonymous CLI returned `UNKNOWN` for all six because field was omitted |
| Default branch | **5/5 `main`** | `main` | Same current convention |
| `main` protected | **5/5 `true`** | `true` | Protected; full rule details not attested |
| Active ruleset `Protect main` | **5/5 present** | **No active ruleset returned** | Upstream has some other/legacy branch protection; do **not** claim unprotected |
| Root LICENSE file | **5/5 present** | **Absent** | Advisory, no inference about rights/compatibility of externally linked patches |
| `.github/workflows` | **5/5 present** | Present | CI artifacts exist; individual CI success not evaluated here |
| Root CONTRIBUTING | Mixed in-scope | Present | Informational; not treated as standard violation |

Reference head SHAs from successful public CLI readback:

| Repository | Default-branch head |
| --- | --- |
| Profile | `527fe01ccf1ee22e54bd9525285a89a93179c1e7` |
| Skills | `5d36fd2e40e4e8a1711b1f315f7a60a9a78a2a25` |
| Index | `87e70a25192f7ca254cce4fd02b9abe2b1f642ab` |
| Awesome | `5a7b8ada7c2a3739633b9c2b4f3c21425fc6a07c` |
| Organization | `089837e3bc119b0c8b0b7b8224916a6a3a92b0a9` |
| Upstream (adjacent) | `781407dcb2a53ec155c147bf3cb078b1af27952b` |

## Verification and limitations

- Native mock-based probe tests: **7/7 PASS** (scope isolation, routing, anonymous-field uncertainty, `403`, legacy protection distinction, source pin).
- First public-API run: **exit 0**, **15/15 required root routing checks PASS** across the five in-scope repos; all six `delete_branch_on_merge` fields were `UNKNOWN` through the anonymous runtime. This is **not** an all-checks PASS.
- GitHub's branch-protection detail endpoint reported integration access restrictions during authenticated connector inspection. The public branch summary still returned `protected=true` for Upstream, so the absence of a ruleset cannot be construed as no protection.
- No determination that all observed 5/5 conventions are compulsory. No independent S3* audit claim, no exercised S3 decision, no S1 correction, no Upstream admission, no settings mutation, no permanent monitoring deployment.

## Next authorized steps

1. Review [#288](https://github.com/opensiro/vsm-oss-organization/issues/288) against S3/S3* admission thresholds and determine which **existing** standards are binding and which practices merely warrant a policy/owner choice.
2. Stage a separate claim-relative S3* audit, if genuinely complementary evidence and an independent owner are available; do not conflate routine probe output with S3*.
3. For an actual present whole-system violation, route the finding to a legitimate S3 holder for a bounded decision, and then to an admitted S1 repair owner. Upstream may be offered a repo-local opt-in patch/settings proposal, but remains outside Organization S3 command scope pending [#274](https://github.com/opensiro/vsm-oss-organization/issues/274).
