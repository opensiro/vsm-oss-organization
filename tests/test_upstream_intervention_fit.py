"""Structural provenance checks for the optional external PR attribution ledger."""

import copy
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "experiments" / "upstream-intervention-fit" / "compute.py"
SPEC = importlib.util.spec_from_file_location("upstream_fit_compute", SOURCE)
compute = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(compute)


class UpstreamAttributionTests(unittest.TestCase):
    def setUp(self):
        self.data = compute.load_observations()
        self.entry = next(x for x in self.data["interventions"] if x["id"] == "henterprise-1")

    def assert_rejected(self, transform, pattern):
        value = copy.deepcopy(self.data)
        row = next(x for x in value["interventions"] if x["id"] == "henterprise-1")
        transform(row)
        with self.assertRaisesRegex(ValueError, pattern):
            compute.validate_observations(value)

    def test_one_intervention_not_two_for_original_and_replacement(self):
        result = compute.compute(self.data)
        self.assertEqual(len(result["interventions"]), len(self.data["interventions"]))
        rows = [x for x in result["interventions"] if x["id"] == "henterprise-1"]
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["lifecycle"], "merged")
        self.assertEqual(rows[0]["fit"], "pending")
        self.assertEqual(rows[0]["pull_request"], "https://github.com/humbertobellor/henterprise/pull/1")
        self.assertEqual(rows[0]["landing_pull_request"], "https://github.com/humbertobellor/henterprise/pull/3")
        self.assertEqual([p["lifecycle"] for p in rows[0]["related_pull_requests"]], ["closed_unmerged", "merged"])
        self.assertEqual([x["github_login"] for x in rows[0]["participants"]], ["xLagerFeuer", "humbertobellor"])

    def test_original_fit_and_other_interventions_are_preserved(self):
        self.assertEqual(sum(1 for x in self.data["interventions"] if x["id"] == "henterprise-1"), 1)
        self.assertEqual(len(self.data["interventions"]), 8)
        self.assertEqual(compute.compute(self.data)["fit_counts"], {"pass": 3, "fail": 2, "pending": 3})

    def test_duplicate_intervention_identity_rejected(self):
        value = copy.deepcopy(self.data)
        value["interventions"].append(copy.deepcopy(self.entry))
        with self.assertRaisesRegex(ValueError, "duplicate intervention id"):
            compute.validate_observations(value)

    def test_duplicate_link_rejected(self):
        self.assert_rejected(lambda row: row["related_pull_requests"].append(copy.deepcopy(row["related_pull_requests"][0])), "duplicate linked PR")

    def test_original_pr_cannot_be_reassigned(self):
        self.assert_rejected(lambda row: row["related_pull_requests"][0].update(url="https://github.com/humbertobellor/henterprise/pull/8"), "original PR must equal")

    def test_landing_must_be_linked_and_merged(self):
        self.assert_rejected(lambda row: row["related_pull_requests"][1].update(lifecycle="open"), "landing PR must be merged")
        self.assert_rejected(lambda row: row.update(landing_pull_request="https://github.com/humbertobellor/henterprise/pull/5"), "landing PR must be merged")
        self.assert_rejected(lambda row: row.update(lifecycle="closed_unmerged"), "merged landing requires intervention lifecycle merged")

    def test_other_repo_cannot_be_linked_as_landing(self):
        self.assert_rejected(lambda row: row["related_pull_requests"][1].update(url="https://github.com/opensiro/vsm-harness-index/pull/1442"), "first-party GitHub upstream PR")

    def test_duplicate_actor_rejected(self):
        self.assert_rejected(lambda row: row["participants"].append(copy.deepcopy(row["participants"][0])), "duplicate participant")

    def test_actor_needs_real_evidence(self):
        self.assert_rejected(lambda row: row["participants"][0].update(evidence_urls=[]), "evidence URLs")
        self.assert_rejected(lambda row: row["participants"][0].update(evidence_urls=["https://github.com/opensiro/vsm-oss-organization/issues/209"]), "must reference original upstream GitHub")

    def test_commit_attribution_requires_commit_url(self):
        self.assert_rejected(lambda row: row["participants"][0].update(evidence_urls=["https://github.com/humbertobellor/henterprise/pull/1"]), "requires commit evidence")

    def test_review_role_requires_submitted_review(self):
        self.assert_rejected(lambda row: row["participants"][1].update(roles=["reviewer"]), "submitted GitHub review evidence")

    def test_unknown_actor_type_is_not_assumed_to_be_human(self):
        value = copy.deepcopy(self.data)
        value["interventions"][4]["participants"][0]["account_type"] = "unknown"
        compute.validate_observations(value)
        self.assert_rejected(lambda row: row["participants"][0].update(account_type="human"), "invalid account type")


    def test_refreshed_eight_intervention_cohort(self):
        rows = {x["id"]: x for x in self.data["interventions"]}
        self.assertEqual(rows["marveen-1516"]["lifecycle"], "merged")
        self.assertEqual(rows["scion-2047"]["lifecycle"], "closed_unmerged")
        self.assertEqual(rows["scion-2047"]["gates"]["scope_compatibility"], "fail")
        self.assertEqual(rows["scion-2047"]["gates"]["upstream_need"], "unknown")
        self.assertEqual(rows["shep-933"]["lifecycle"], "open")
        self.assertEqual(rows["shep-934"]["lifecycle"], "open")
        self.assertNotEqual(rows["shep-933"]["pull_request"], rows["shep-934"]["pull_request"])
        summary = compute.compute(self.data)
        self.assertEqual(summary["lifecycle_counts"], {"closed_unmerged": 2, "merged": 2, "open": 4})
        self.assertEqual(summary["primary_metric"]["numerator_pass"], 3)
        self.assertEqual(summary["primary_metric"]["denominator_completed_reviews"], 5)
        self.assertEqual(summary["primary_metric"]["value"], 0.6)

    def test_shep_contributor_roles_have_first_party_evidence(self):
        rows = {x["id"]: x for x in self.data["interventions"]}
        s2, hotfix = rows["shep-933"], rows["shep-934"]
        self.assertEqual([p["github_login"] for p in s2["participants"]],
                         ["xLagerFeuer", "arielshad", "claude"])
        reviewer = s2["participants"][1]
        self.assertEqual(reviewer["roles"], ["reviewer"])
        self.assertTrue(any("#pullrequestreview-" in u for u in reviewer["evidence_urls"]))
        self.assertEqual([p["github_login"] for p in hotfix["participants"]],
                         ["xLagerFeuer", "claude"])
        self.assertEqual(compute.derived_fit(s2["gates"]), "pending")
        self.assertEqual(compute.derived_fit(hotfix["gates"]), "pass")
        compute.validate_observations(copy.deepcopy(self.data))

    def test_snapshot_is_pinned_to_validated_observations(self):
        actual = (SOURCE.parent / "snapshot.json").read_text(encoding="utf-8")
        self.assertEqual(actual, compute.rendered_snapshot(self.data))


if __name__ == "__main__":
    unittest.main()
