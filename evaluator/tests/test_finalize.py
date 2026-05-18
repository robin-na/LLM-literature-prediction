import unittest

from utils.finalize import build_final_rows


class TestFinalize(unittest.TestCase):
    def test_build_final_rows_applies_override_and_note(self) -> None:
        human_rows = [
            {
                "Filename": "paper1",
                "Empirical": "1",
                "Controled_Or_Observational": "0",
                "Lab_Or_Field": "0",
                "CONFIG_playerCount": "4",
                "CONFIG_numRounds": "10",
                "CONFIG_allOrNothing": "1",
                "CONFIG_defaultContribProp": "0",
                "CONFIG_MPCR": "0.5",
                "CONFIG_chat": "0",
                "CONFIG_showOtherSummaries": "0",
                "CONFIG_showPunishmentId": "0",
                "CONFIG_showRewardId": "0",
                "DV_contributionRate": "",
                "DV_efficiency": "",
            }
        ]
        llm_rows = [
            {
                "custom_id": "paper1.md",
                "METHOD_empirical": "TRUE",
                "METHOD_lab": "FALSE",
                "METHOD_experiment": "TRUE",
                "CONFIG_playerCount": "4",
                "CONFIG_numRounds": "10",
                "CONFIG_allOrNothing": "1",
                "CONFIG_defaultContribProp": "0",
                "CONFIG_MPCR": "0.5",
                "CONFIG_chat": "0",
                "CONFIG_showOtherSummaries": "0",
                "CONFIG_showPunishmentId": "0",
                "CONFIG_showRewardId": "0",
                "DV_contributionRate": "0.4",
                "DV_efficiency": "",
            }
        ]
        overrides_ui = {"paper1|0|DV_contributionRate": "one-empty"}
        notes = {"paper1": "needs follow-up"}

        rows = build_final_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            overrides_ui=overrides_ui,
            notes=notes,
            review_session_id="default",
            reviewer_id="alice",
        )
        by_key = {r["key"]: r for r in rows}

        overridden = by_key["paper1|0|DV_contributionRate"]
        self.assertEqual(overridden["final_classification"], "mismatch")
        self.assertEqual(overridden["paper_note"], "")

        notes = [r.get("paper_note", "") for r in rows if (r.get("paper_id") == "paper1")]
        self.assertEqual([n for n in notes if n], ["needs follow-up"])

        lab = by_key["paper1|0|Lab_Or_Field"]
        self.assertEqual(lab["auto_classification"], "match")
        self.assertEqual(lab["final_classification"], "match")

