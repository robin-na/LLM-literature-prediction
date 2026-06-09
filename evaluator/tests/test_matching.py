import unittest

from utils.matching import classify_match, to_html_class


class TestMatching(unittest.TestCase):
    def test_lab_or_field_exception(self) -> None:
        cls = classify_match("Lab / Experiment", "0", "TRUE", True, True)
        self.assertEqual(cls, "match")

    def test_boolean_equivalence(self) -> None:
        cls = classify_match("Any", "Yes", "true", True, True)
        self.assertEqual(cls, "match")

    def test_missing_row(self) -> None:
        cls = classify_match("Any", "x", "y", True, False)
        self.assertEqual(cls, "missing_row")

    def test_html_class_mapping(self) -> None:
        self.assertEqual(to_html_class("missing_row"), "missing-row")
        self.assertEqual(to_html_class("both_empty"), "both-empty")

    def test_na_human_vs_llm_zero_is_match_for_reward_config(self) -> None:
        cls = classify_match("CONFIG_showRewardId", "N/A", "0", True, True)
        self.assertEqual(cls, "match")
        cls = classify_match("CONFIG_rewardExists", "N/R", "FALSE", True, True)
        self.assertEqual(cls, "match")

    def test_na_vs_zero_still_mismatch_for_other_fields(self) -> None:
        cls = classify_match("CONFIG_playerCount", "N/A", "0", True, True)
        self.assertEqual(cls, "mismatch")

    def test_na_vs_zero_human_vs_human_does_not_match(self) -> None:
        cls = classify_match(
            "CONFIG_showRewardId",
            "N/A",
            "0",
            True,
            True,
            compare_human_to_llm=False,
        )
        self.assertEqual(cls, "mismatch")

