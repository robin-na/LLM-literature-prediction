import tempfile
import unittest
from pathlib import Path

from scripts.mismatch_reason_report import (
    build_mismatch_reason_report_from_rows,
    render_mismatch_reason_markdown,
    write_mismatch_reason_outputs,
)
from utils.finalize import build_final_rows
from utils.csvio import read_csv


def _human_row(
    paper_id: str,
    *,
    empirical: str = "1",
    player_count: str = "4",
) -> dict[str, str]:
    return {
        "Filename": paper_id,
        "Alignment_Label": paper_id,
        "Granularity": "",
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
    empirical_reason: str = "",
    empirical_confidence: str = "",
    player_count: str = "4",
) -> dict[str, str]:
    return {
        "custom_id": f"{paper_id}.md",
        "v": paper_id,
        "METHOD_empirical": empirical,
        "METHOD_empirical_reason": empirical_reason,
        "METHOD_empirical_confidence": empirical_confidence,
        "METHOD_lab": "FALSE",
        "METHOD_experiment": "TRUE",
        "CONFIG_playerCount": player_count,
        "CONFIG_playerCount_reason": "",
        "CONFIG_playerCount_confidence": "",
        "CONFIG_numRounds": "10",
        "CONFIG_numRounds_reason": "",
        "CONFIG_numRounds_confidence": "",
        "CONFIG_allOrNothing": "1",
        "CONFIG_allOrNothing_reason": "",
        "CONFIG_allOrNothing_confidence": "",
        "CONFIG_defaultContribProp": "0",
        "CONFIG_defaultContribProp_reason": "",
        "CONFIG_defaultContribProp_confidence": "",
        "CONFIG_MPCR": "0.5",
        "CONFIG_MPCR_reason": "",
        "CONFIG_MPCR_confidence": "",
        "CONFIG_chat": "0",
        "CONFIG_chat_reason": "",
        "CONFIG_chat_confidence": "",
        "CONFIG_showOtherSummaries": "0",
        "CONFIG_showOtherSummaries_reason": "",
        "CONFIG_showOtherSummaries_confidence": "",
        "CONFIG_showPunishmentId": "0",
        "CONFIG_showPunishmentId_reason": "",
        "CONFIG_showPunishmentId_confidence": "",
        "CONFIG_showRewardId": "0",
        "CONFIG_showRewardId_reason": "",
        "CONFIG_showRewardId_confidence": "",
        "DV_contributionRate": "",
        "DV_contributionRate_reason": "",
        "DV_contributionRate_confidence": "",
        "DV_efficiency": "",
        "DV_efficiency_reason": "",
        "DV_efficiency_confidence": "",
    }


class TestMismatchReasonReport(unittest.TestCase):
    def test_joins_reason_columns_for_field_mismatch(self) -> None:
        human_rows = [_human_row("paper_a", empirical="1")]
        llm_rows = [
            _llm_row(
                "paper_a",
                empirical="FALSE",
                empirical_reason="Model confused observational with lab coding.",
                empirical_confidence="0.22",
            )
        ]
        final_rows = build_final_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            overrides_ui={},
            notes={},
            review_session_id="default",
            reviewer_id="alice",
        )

        report = build_mismatch_reason_report_from_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            final_rows=final_rows,
            review_session_id="default",
            reviewer_id="alice",
            paper_ids=["paper_a"],
        )

        empirical_rows = report["rows_by_field"]["Empirical"]
        self.assertEqual(len(empirical_rows), 1)
        self.assertEqual(empirical_rows[0]["llm_reason"], "Model confused observational with lab coding.")
        self.assertEqual(empirical_rows[0]["llm_confidence"], "0.22")

    def test_excludes_granularity_mismatch_papers_from_field_examples(self) -> None:
        human_rows = [
            _human_row("paper_a", empirical="1"),
            _human_row("paper_b"),
            _human_row("paper_b"),
        ]
        llm_rows = [
            _llm_row("paper_a", empirical="FALSE", empirical_reason="wrong", empirical_confidence="0.1"),
            _llm_row("paper_b"),
        ]
        final_rows = build_final_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            overrides_ui={},
            notes={},
            review_session_id="default",
            reviewer_id="alice",
        )

        report = build_mismatch_reason_report_from_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            final_rows=final_rows,
            review_session_id="default",
            reviewer_id="alice",
            paper_ids=["paper_a", "paper_b"],
        )

        self.assertEqual(report["granularity_mismatch_papers"], ["paper_b"])
        self.assertEqual(report["feature_scoring_papers"], ["paper_a"])
        self.assertEqual(report["rows_by_field"]["granularity"][0]["paper_id"], "paper_b")
        self.assertEqual(report["rows_by_field"]["Empirical"][0]["paper_id"], "paper_a")

    def test_lab_only_scope_filters_non_lab_papers(self) -> None:
        human_rows = [
            _human_row("paper_a", empirical="1"),
            {**_human_row("paper_b", empirical="1"), "Lab_Or_Field": "1"},
        ]
        llm_rows = [
            _llm_row("paper_a", empirical="FALSE", empirical_reason="wrong", empirical_confidence="0.1"),
            _llm_row("paper_b", empirical="FALSE", empirical_reason="also wrong", empirical_confidence="0.2"),
        ]
        final_rows = build_final_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            overrides_ui={},
            notes={},
            review_session_id="default",
            reviewer_id="alice",
        )

        report = build_mismatch_reason_report_from_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            final_rows=final_rows,
            review_session_id="default",
            reviewer_id="alice",
            paper_ids=["paper_a", "paper_b"],
            eval_scope="lab-only",
        )

        self.assertEqual(report["target_papers"], ["paper_a"])
        self.assertEqual(report["excluded_non_lab_papers"], ["paper_b"])
        self.assertEqual(report["rows_by_field"]["Empirical"][0]["paper_id"], "paper_a")

    def test_writes_markdown_and_csv_outputs(self) -> None:
        human_rows = [_human_row("paper_a", empirical="1")]
        llm_rows = [_llm_row("paper_a", empirical="FALSE", empirical_reason="wrong", empirical_confidence="0.1")]
        final_rows = build_final_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            overrides_ui={},
            notes={},
            review_session_id="default",
            reviewer_id="alice",
        )
        report = build_mismatch_reason_report_from_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            final_rows=final_rows,
            review_session_id="default",
            reviewer_id="alice",
            paper_ids=["paper_a"],
        )

        with tempfile.TemporaryDirectory() as tmp:
            markdown_path = Path(tmp) / "report.md"
            csv_path = Path(tmp) / "report.csv"
            written_markdown, written_csv = write_mismatch_reason_outputs(
                report,
                markdown_out=markdown_path,
                csv_out=csv_path,
            )

            self.assertEqual(written_markdown, markdown_path.resolve())
            self.assertEqual(written_csv, csv_path.resolve())
            self.assertIn("# Mismatch Reason Report", markdown_path.read_text(encoding="utf-8"))
            csv_rows = read_csv(csv_path)
            self.assertEqual(csv_rows[0]["field"], "Empirical")
            self.assertEqual(csv_rows[0]["llm_reason"], "wrong")

    def test_rendered_markdown_includes_field_sections(self) -> None:
        human_rows = [_human_row("paper_a", empirical="1")]
        llm_rows = [_llm_row("paper_a", empirical="FALSE", empirical_reason="wrong", empirical_confidence="0.1")]
        final_rows = build_final_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            overrides_ui={},
            notes={},
            review_session_id="default",
            reviewer_id="alice",
        )
        report = build_mismatch_reason_report_from_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            final_rows=final_rows,
            review_session_id="default",
            reviewer_id="alice",
            paper_ids=["paper_a"],
        )

        markdown = render_mismatch_reason_markdown(report)

        self.assertIn("- Evaluation scope: all", markdown)
        self.assertIn("## Empirical", markdown)
        self.assertIn("wrong", markdown)
