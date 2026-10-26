"""Regression boundary for S5 #274; this is not an autonomy assessment."""
from pathlib import Path
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]
PARENT_COMMENT = "issues/274#issuecomment-6420871211"
UPSTREAM = "opensiro/upstream"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class UpstreamS1AdmissionTests(unittest.TestCase):
    def test_legitimate_s5_return_and_four_explicit_s1_contracts(self):
        decision = read("records/s5/2026-10-26-upstream-domain-admission.md")
        contracts = read("contracts/s1/domain-contracts.md")
        for marker in (PARENT_COMMENT, "ADMIT_WITH_ENVELOPE", "PARENT_DECIDED / BOUNDARY_APPLIED / S1_WITNESS_PENDING"):
            self.assertIn(marker, decision)
        self.assertIn("upstream/pull/134", decision)
        self.assertIn("vsm-oss-organization/pull/292", decision)
        self.assertIn("## Upstream Contributions domain", contracts)
        domain_heads = [line for line in contracts.splitlines() if line.startswith("## ") and line.endswith(" domain")]
        self.assertEqual(4, len(domain_heads))
        self.assertIn("GitHub writes to forks or external PRs require a **separate effective", contracts)

    def test_scope_is_six_and_upstream_is_operational_s1_not_metasytem(self):
        README = read("README.md")
        org = read("docs/ORGANIZATION.md")
        metrics = yaml.safe_load(read("metrics.yaml"))
        scope = metrics["scope"]["repositories"]
        self.assertEqual(6, len(scope))
        self.assertEqual(6, len(set(scope)))
        self.assertIn(UPSTREAM, scope)
        self.assertIn("- `opensiro/upstream`", README)
        self.assertIn("**Upstream Contributions** — `opensiro/upstream`", org)
        self.assertEqual("operational_s1", metrics["repositories"][UPSTREAM]["organizational_role"])
        self.assertEqual("verified_external_outcomes", metrics["repositories"][UPSTREAM]["primary_metric"])

    def test_no_automatic_grant_or_autonomy_grade(self):
        decision = read("records/s5/2026-10-26-upstream-domain-admission.md")
        control = read("docs/AGENT_CONTROL_PLANE.md")
        contract = read("contracts/s1/domain-contracts.md")
        self.assertIn("No new credential, external fork/branch/PR publication", decision)
        self.assertIn("not** a standing fork-creation port or autonomy grade", control)
        self.assertIn("finite Corrective cohort is not a standing permission", contract)
        self.assertIn("does **not** by itself establish `S1=A`", contract)

    def test_four_domain_read_only_s3_inventory_without_new_s3_grant(self):
        script = read("scripts/collect_s3_current_view.py")
        self.assertIn('"opensiro/upstream",', script)
        self.assertIn('"s3_admission": "NOT_ASSESSED"', script)
        self.assertIn('BOUNDARY = "CANDIDATES_ONLY_NOT_ACTIVE_S1_OR_S3_EVIDENCE"', script)


if __name__ == "__main__":
    unittest.main()
