import unittest

from utils.finalize import build_final_rows
from utils.row_alignment import align_rows


def _human_row(
    paper_id: str,
    *,
    alignment_label: str = "",
    player_count: str = "4",
    mpcr: str = "0.5",
) -> dict[str, str]:
    return {
        "Filename": paper_id,
        "Alignment_Label": alignment_label,
        "Granularity": "",
        "Empirical": "1",
        "Controled_Or_Observational": "0",
        "Lab_Or_Field": "0",
        "CONFIG_playerCount": player_count,
        "CONFIG_numRounds": "10",
        "CONFIG_allOrNothing": "1",
        "CONFIG_defaultContribProp": "0",
        "CONFIG_MPCR": mpcr,
        "CONFIG_chat": "0",
        "CONFIG_showOtherSummaries": "0",
        "CONFIG_showPunishmentId": "0",
        "CONFIG_showRewardId": "0",
        "DV_contributionRate": "",
        "DV_efficiency": "",
    }


def _llm_row(
    paper_id: str,
    *,
    data_id: str = "",
    v: str = "",
    player_count: str = "4",
    mpcr: str = "0.5",
) -> dict[str, str]:
    return {
        "custom_id": f"{paper_id}.md",
        "data_id": data_id,
        "v": v,
        "METHOD_empirical": "TRUE",
        "METHOD_lab": "FALSE",
        "METHOD_experiment": "TRUE",
        "CONFIG_playerCount": player_count,
        "CONFIG_numRounds": "10",
        "CONFIG_allOrNothing": "1",
        "CONFIG_defaultContribProp": "0",
        "CONFIG_MPCR": mpcr,
        "CONFIG_chat": "0",
        "CONFIG_showOtherSummaries": "0",
        "CONFIG_showPunishmentId": "0",
        "CONFIG_showRewardId": "0",
        "DV_contributionRate": "",
        "DV_efficiency": "",
    }


class TestRowAlignment(unittest.TestCase):
    def test_aligns_swapped_rows_by_feature_similarity(self) -> None:
        human_rows = [
            _human_row("paper1", player_count="4", mpcr="0.5"),
            _human_row("paper1", player_count="8", mpcr="0.2"),
        ]
        llm_rows = [
            _llm_row("paper1", data_id="second", player_count="8", mpcr="0.2"),
            _llm_row("paper1", data_id="first", player_count="4", mpcr="0.5"),
        ]

        rows = build_final_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            overrides_ui={},
            notes={},
            review_session_id="default",
            reviewer_id="alice",
        )
        by_key = {row["key"]: row for row in rows}

        self.assertEqual(by_key["paper1|0|CONFIG_playerCount"]["llm_value"], "4")
        self.assertEqual(by_key["paper1|1|CONFIG_playerCount"]["llm_value"], "8")

    def test_aligns_identical_rows_by_alignment_label_when_available(self) -> None:
        human_rows = [
            _human_row("paper1", alignment_label="Piece Rate Pay"),
            _human_row("paper1", alignment_label="Relative Incentive Scheme"),
        ]
        llm_rows = [
            _llm_row("paper1", v="Relative Incentive Scheme"),
            _llm_row("paper1", v="Piece Rate Pay"),
        ]

        pairs = align_rows(
            human_rows,
            llm_rows,
            column_map={
                "Empirical": ("Empirical", "METHOD_empirical"),
                "CONFIG_playerCount": ("CONFIG_playerCount", "CONFIG_playerCount"),
            },
        )

        self.assertEqual(pairs[0][1]["v"], "Piece Rate Pay")
        self.assertEqual(pairs[1][1]["v"], "Relative Incentive Scheme")

    def test_equal_row_counts_do_not_leave_all_rows_unmatched(self) -> None:
        human_rows = [
            _human_row("paper1", alignment_label="Control: Relative Performance Pay"),
            _human_row("paper1", alignment_label="Condition: Piece Rate Pay"),
        ]
        llm_rows = [
            _llm_row("paper1", v="Relative incentive scheme"),
            _llm_row("paper1", v="Piece-rate scheme"),
        ]

        pairs = align_rows(
            human_rows,
            llm_rows,
            column_map={
                "Empirical": ("Empirical", "METHOD_empirical"),
                "CONFIG_playerCount": ("CONFIG_playerCount", "CONFIG_playerCount"),
                "CONFIG_chat": ("CONFIG_chat", "CONFIG_chat"),
            },
        )

        self.assertEqual(len(pairs), 2)
        self.assertTrue(all(h is not None and l is not None for h, l in pairs))
