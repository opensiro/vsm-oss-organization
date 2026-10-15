"""M3 D1-A authority separation/fail-closed tests (no live S3 cases)."""
from __future__ import annotations
import copy
from datetime import datetime, timedelta, timezone
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "scripts" / "check_s3_d1a_gate.py"
SPEC = importlib.util.spec_from_file_location("s3_d1a_gate", SRC)
assert SPEC and SPEC.loader
gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gate)
GRANT = json.loads((ROOT / "contracts" / "s3" / "autonomous-d1a.json").read_text(encoding="utf-8"))
ACTOR = "s3-agent-execution-20261015-001"
NOW = datetime(2026, 10, 15, 14, 0, tzinfo=timezone.utc)


def activated():
    g = copy.deepcopy(GRANT)
    g.update({
        "status": "ACTIVE",
        "recipient_execution_identity": ACTOR,
        "owner_attestation_url": "https://github.com/opensiro/vsm-oss-organization/issues/5#issuecomment-777",
        "grant_publication_commit": "a" * 40,
        "effective_from_utc": "2026-10-15T13:00:00Z",
        "expires_at_utc": "2026-11-13T12:00:00Z"
    })
    return g


class D1AGate(unittest.TestCase):
    def test_shipped_grant_is_inactive(self):
        self.assertEqual("PENDING_S5_PUBLIC_ATTESTATION", GRANT["status"])
        with self.assertRaisesRegex(gate.GateError, "NO_AUTHORITY"):
            gate.check(GRANT, agent_id=ACTOR, now=NOW)

    def test_structural_only_never_claims_verified_authority(self):
        self.assertEqual("STRUCTURAL_READY_LIVE_AUTHORITY_STILL_REQUIRED",
                         gate.check(activated(), agent_id=ACTOR, now=NOW))

    def test_cannot_borrow_human_g1_identity(self):
        with self.assertRaisesRegex(gate.GateError, "identity"):
            gate.check(activated(), agent_id="xLagerFeuer", now=NOW)

    def test_no_s3_grant_derived_from_generic_issue_link(self):
        g = activated()
        g["owner_attestation_url"] = "https://github.com/opensiro/vsm-oss-organization/issues/5"
        with self.assertRaisesRegex(gate.GateError, "canonical S5"):
            gate.check(g, agent_id=ACTOR, now=NOW)

    def test_invalid_decision_class_fails(self):
        g = activated()
        g["allowed_classes"].append("SET_CONSTRAINT")
        with self.assertRaisesRegex(gate.GateError, "decision class"):
            gate.check(g, agent_id=ACTOR, now=NOW)

    def test_out_of_scope_and_unbounded_grants_fail(self):
        g = activated()
        g["s1_domains"].append("Research")
        with self.assertRaisesRegex(gate.GateError, "scope"):
            gate.check(g, agent_id=ACTOR, now=NOW)
        g = activated()
        g["expires_at_utc"] = "2026-12-15T00:00:00Z"
        with self.assertRaisesRegex(gate.GateError, "30 days"):
            gate.check(g, agent_id=ACTOR, now=NOW)

    def test_expiry_is_exclusive_and_revocation_cannot_be_inferred_offline(self):
        g = activated()
        with self.assertRaisesRegex(gate.GateError, "expired"):
            gate.check(g, agent_id=ACTOR, now=datetime(2026, 11, 13, 12, tzinfo=timezone.utc))
        self.assertTrue(g["requires_live_authority_checks"])

    def test_local_s3_mode_is_separate_from_human_g1(self):
        mode = (ROOT / "modes" / "s3-autonomous" / "RUN.md").read_text(encoding="utf-8")
        self.assertIn("decision.owner_class = agent", mode)
        self.assertIn("not invoke `--g1`", mode)
        self.assertIn("separately owner-authored", mode)

if __name__ == "__main__":
    unittest.main()
