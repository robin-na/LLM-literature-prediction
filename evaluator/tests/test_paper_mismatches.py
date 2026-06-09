import unittest

from utils.finalize import build_final_rows
from utils.paper_mismatches import (
    mismatch_summary_from_rows,
    mismatched_papers_from_rows,
    render_mismatch_summary_report,
)


def _human_row(
    paper_id: str,
    *,
    empirical: str = "1",
    player_count: str = "4",
) -> dict[str, str]:
    return {
        "Filename": paper_id,
        "Empirical": empirical,
        "Controled_Or_Observational": "0",
        "Lab_Or_Field": "0",
        "CONFIG_playerCount": player_count,
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


def _llm_row(
    paper_id: str,
    *,
    empirical: str = "TRUE",
    player_count: str = "4",
) -> dict[str, str]:
    return {
        "custom_id": f"{paper_id}.md",
        "METHOD_empirical": empirical,
        "METHOD_lab": "FALSE",
        "METHOD_experiment": "TRUE",
        "CONFIG_playerCount": player_count,
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


class TestPaperMismatches(unittest.TestCase):
    def test_returns_granularity_mismatch_papers(self) -> None:
        human_rows = [_human_row("paper_a"), _human_row("paper_a"), _human_row("paper_b")]
        llm_rows = [_llm_row("paper_a"), _llm_row("paper_b")]
        final_rows = build_final_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            overrides_ui={},
            notes={},
            review_session_id="default",
            reviewer_id="alice",
        )

        result = mismatched_papers_from_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            final_rows=final_rows,
            field_name="granularity",
            paper_ids=["paper_a", "paper_b"],
        )

        self.assertEqual(result, ["paper_a"])

    def test_returns_field_level_mismatch_papers(self) -> None:
        human_rows = [_human_row("paper_a", empirical="1"), _human_row("paper_b", empirical="1")]
        llm_rows = [_llm_row("paper_a", empirical="FALSE"), _llm_row("paper_b", empirical="TRUE")]
        final_rows = build_final_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            overrides_ui={},
            notes={},
            review_session_id="default",
            reviewer_id="alice",
        )

        result = mismatched_papers_from_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            final_rows=final_rows,
            field_name="Empirical",
            paper_ids=["paper_a", "paper_b"],
        )

        self.assertEqual(result, ["paper_a"])

    def test_returns_global_summary_without_field_name(self) -> None:
        human_rows = [
            _human_row("paper_a", empirical="1"),
            _human_row("paper_b"),
            _human_row("paper_b"),
            _human_row("paper_c"),
        ]
        llm_rows = [
            _llm_row("paper_a", empirical="FALSE"),
            _llm_row("paper_b"),
            _llm_row("paper_c"),
        ]
        final_rows = build_final_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            overrides_ui={},
            notes={},
            review_session_id="default",
            reviewer_id="alice",
        )

        result = mismatched_papers_from_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            final_rows=final_rows,
            paper_ids=["paper_a", "paper_b", "paper_c"],
        )

        self.assertEqual(
            result,
            {
                "mismatched_papers": ["paper_a", "paper_b"],
                "matched_papers": ["paper_c"],
            },
        )

    def test_lab_only_scope_excludes_non_lab_papers(self) -> None:
        human_rows = [
            _human_row("paper_a", empirical="1"),
            {**_human_row("paper_b", empirical="1"), "Lab_Or_Field": "1"},
        ]
        llm_rows = [_llm_row("paper_a", empirical="FALSE"), _llm_row("paper_b", empirical="FALSE")]
        final_rows = build_final_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            overrides_ui={},
            notes={},
            review_session_id="default",
            reviewer_id="alice",
        )

        result = mismatched_papers_from_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            final_rows=final_rows,
            paper_ids=["paper_a", "paper_b"],
            eval_scope="lab-only",
        )

        self.assertEqual(result, {"mismatched_papers": ["paper_a"], "matched_papers": []})

    def test_rejects_unknown_field(self) -> None:
        human_rows = [_human_row("paper_a")]
        llm_rows = [_llm_row("paper_a")]
        final_rows = build_final_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            overrides_ui={},
            notes={},
            review_session_id="default",
            reviewer_id="alice",
        )

        with self.assertRaisesRegex(ValueError, "Unknown field"):
            mismatched_papers_from_rows(
                human_rows=human_rows,
                llm_rows=llm_rows,
                final_rows=final_rows,
                field_name="NotARealField",
                paper_ids=["paper_a"],
            )

    def test_builds_markdown_summary_report(self) -> None:
        human_rows = [
            _human_row("paper_a", empirical="1"),
            _human_row("paper_b"),
            _human_row("paper_b"),
            _human_row("paper_c"),
        ]
        llm_rows = [
            _llm_row("paper_a", empirical="FALSE"),
            _llm_row("paper_b"),
            _llm_row("paper_c"),
        ]
        final_rows = build_final_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            overrides_ui={},
            notes={},
            review_session_id="default",
            reviewer_id="alice",
        )

        summary = mismatch_summary_from_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            final_rows=final_rows,
            review_session_id="default",
            reviewer_id="alice",
            paper_ids=["paper_a", "paper_b", "paper_c"],
        )
        report = render_mismatch_summary_report(summary)

        self.assertIn("# Mismatch Summary", report)
        self.assertIn("- Evaluation scope: all", report)
        self.assertIn("- Target papers for eval matrix: 3", report)
        self.assertIn("- Papers used for feature scoring: 2", report)
        self.assertIn("| granularity | 3 | 1 | 2 | paper_b |", report)
        self.assertIn("| Empirical | 2 | 1 | 1 | paper_a |", report)
        self.assertIn("Papers with any mismatch: paper_a, paper_b", report)
