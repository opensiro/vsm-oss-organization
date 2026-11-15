"""Source-routed operator policy: an older standing publication grant is not consent to third-party outreach."""
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
class ExternalPublicConsentRoutingTests(unittest.TestCase):
    def test_bootstrap_escalates_external_public_communication(self):
        s=(ROOT/'START_HERE.md').read_text()
        self.assertIn('External-public communication consent',s)
        self.assertIn('EXTERNAL_PUBLIC_COMMUNICATION_GATE.md',s)
        self.assertIn('exact destination, action and public text/diff',s)
        self.assertIn('continue',s)

    def test_osm_control_plane_no_longer_infers_public_pr_permission(self):
        s=(ROOT/'docs/AGENT_CONTROL_PLANE.md').read_text()
        self.assertIn('2026-11-15',s)
        self.assertIn('EXTERNAL_PUBLIC_COMMUNICATION_GATE.md',s)
        self.assertIn('exact current-conversation owner approval',s)
        self.assertNotIn('a qualifying publication needs no further per-PR owner conversation',s)
        for action in ('comment','design question','review','third-party PR'):
            self.assertIn(action.lower(),s.lower())

if __name__=='__main__':unittest.main()
