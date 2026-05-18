import unittest

from scripts.llm_error_analysis_report import (
    build_error_analysis_report_from_mismatch_report,
    render_error_analysis_markdown,
)


class TestLlmErrorAnalysisReport(unittest.TestCase):
    def test_groups_rows_into_prompt_relevant_error_patterns(self) -> None:
        mismatch_report = {
            "review_session_id": "default",
            "reviewer_id": "alice",
            "eval_scope": "lab-only",
            "ground_truth_path": "/tmp/ground_truth.csv",
            "llm_path": "/tmp/llm.xlsx",
            "target_papers": ["paper_a", "paper_b", "paper_c"],
            "feature_scoring_papers": ["paper_a", "paper_b", "paper_c"],
            "rows": [
                {
                    "paper_id": "paper_a",
                    "field": "CONFIG_playerCount",
                    "human_value": "4",
                    "llm_value": "12",
                    "llm_reason": "N=4 teams of size 3, so 12 human participants are involved.",
                },
                {
                    "paper_id": "paper_b",
                    "field": "DV_contributionRate",
                    "human_value": "0.3095",
                    "llm_value": "6.19",
                    "llm_reason": "Average contribution is 6.19 tokens out of 20.",
                },
                {
                    "paper_id": "paper_c",
                    "field": "CONFIG_defaultContribProp",
                    "human_value": "0",
                    "llm_value": "N/A",
                    "llm_reason": "No contribution game is described.",
                },
            ],
        }

        report = build_error_analysis_report_from_mismatch_report(mismatch_report, max_examples_per_pattern=2)

        self.assertEqual(report["rows"][0]["error_pattern"], "unit_of_analysis_confusion")
        self.assertEqual(report["rows"][1]["error_pattern"], "normalization_or_scale_error")
        self.assertEqual(report["rows"][2]["error_pattern"], "schema_zero_vs_missingness")
        self.assertEqual(len(report["pattern_summaries"]), 3)

    def test_rendered_markdown_includes_pattern_sections_and_corrections(self) -> None:
        mismatch_report = {
            "review_session_id": "default",
            "reviewer_id": "alice",
            "eval_scope": "lab-only",
            "ground_truth_path": "/tmp/ground_truth.csv",
            "llm_path": "/tmp/llm.xlsx",
            "target_papers": ["paper_a"],
            "feature_scoring_papers": ["paper_a"],
            "rows": [
                {
                    "paper_id": "paper_a",
                    "field": "DV_contributionRate",
                    "human_value": "0.3095",
                    "llm_value": "6.19",
                    "llm_reason": "Average contribution is 6.19 tokens out of 20.",
                }
            ],
        }

        report = build_error_analysis_report_from_mismatch_report(mismatch_report, max_examples_per_pattern=1)
        markdown = render_error_analysis_markdown(report)

        self.assertIn("# LLM Error Analysis Report", markdown)
        self.assertIn("## normalization or scale error", markdown)
        self.assertIn("Human-Grounded Correction", markdown)
        self.assertIn("the gold value is `0.3095`", markdown)
