"""Structural checks only: local plans do not establish ownership or grants."""
import hashlib
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / ".opensiro/roadmap/s3-d1a-autonomy-20261126"

class LocalRoadmapTests(unittest.TestCase):
    def test_local_route_and_receipt(self):
        skill = (ROOT / "skills/vsm-oss-local/SKILL.md").read_text()
        self.assertIn("opensiro-local roadmap", skill)
        self.assertIn("no fork", skill)
        receipt = (CASE / "roadmap.md").read_text()
        human = (CASE / "issue.md").read_text()
        ai = (CASE / "constructor-sufficiency.md").read_text()
        self.assertIn("- Mode: LOCAL_UNREVIEWED", receipt)
        self.assertIn("- Receipt contract: organization-local-roadmap", receipt)
        self.assertIn("- External publication: NONE", receipt)
        self.assertNotIn("- Accepted Index assessment:", receipt)
        for field in ("Target family", "Target transition", "Current selected function state",
                      "Mode preservation", "Prospective authority",
                      "Cross-function authority compatibility", "Proposal-stage decision", "Research disposition"):
            expected = re.search(r"^- " + re.escape(field) + r": (.+)$", receipt, re.M)[1]
            for doc in (human, ai):
                self.assertIn(f"**{field}:** {expected}", doc)
        for fn in ("S1", "S2", "S3", "S3*", "S4", "S5"):
            self.assertEqual(len(re.findall(r"^\| \*\*" + re.escape(fn) + r" ·", human, re.M)), 1)
            self.assertIn(f"- {fn} disposition:", receipt)
        self.assertIn("[roadmap.md](roadmap.md)", human)
        self.assertIn("[roadmap.md](roadmap.md)", ai)
        digest = re.search(r"^- Local assessment SHA-256: ([0-9a-f]{64})$", receipt, re.M)[1]
        baseline = ROOT / ".opensiro/assessments/2026-11-26-organization-346-preliminary.md"
        self.assertEqual(hashlib.sha256(baseline.read_bytes()).hexdigest(), digest)
        self.assertIn("- Validation state: NOT_RUN", receipt)
        self.assertIn("- Implementation: NOT_STARTED", receipt)

if __name__ == "__main__":
    unittest.main()
