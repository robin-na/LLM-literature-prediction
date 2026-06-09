import unittest

from scripts.mismatch_report import render_mismatch_report_markdown


class TestMismatchReport(unittest.TestCase):
    def test_rendered_markdown_includes_all_major_sections(self) -> None:
        report = {
            "review_session_id": "default",
            "reviewer_id": "alice",
            "summary": {
                "eval_scope": "lab-only",
                "ground_truth_path": "/tmp/ground_truth.csv",
                "llm_path": "/tmp/llm.xlsx",
                "total_papers": 2,
                "feature_scoring_papers_count": 2,
                "overall": {
                    "mismatched_papers": ["paper_a"],
                    "matched_papers": ["paper_b"],
                },
                "rows": [
                    {
                        "field": "Empirical",
                        "denominator_count": 2,
                        "mismatch_count": 1,
                        "match_count": 1,
                        "mismatched_papers": ["paper_a"],
                    }
                ],
            },
            "analysis": {
                "top_fields": [("Empirical", 1)],
                "pattern_summaries": [
                    {
                        "pattern": "value_interpretation_error",
                        "count": 1,
                        "top_fields": [("Empirical", 1)],
                        "top_papers": [("paper_a", 1)],
                        "description": "desc",
                        "reasoning_assessment": "assessment",
                        "prompt_implication": "implication",
                        "examples": [
                            {
                                "field": "Empirical",
                                "paper_id": "paper_a",
                                "human_value": "1",
                                "llm_value": "0",
                                "llm_reason": "reason",
                                "human_grounded_explanation": "correction",
                            }
                        ],
                    }
                ],
            },
            "reasons": {
                "granularity_mismatch_papers": [],
                "rows": [
                    {
                        "field": "Empirical",
                    }
                ],
                "rows_by_field": {
                    "Empirical": [
                        {
                            "paper_id": "paper_a",
                            "row_index": "0",
                            "human_label": "Condition A",
                            "llm_label": "Condition A",
                            "human_value": "1",
                            "llm_value": "0",
                            "mismatch_kind": "mismatch",
                            "llm_reason": "reason",
                            "llm_confidence": "0.3",
                        }
                    ]
                },
            },
        }

        markdown = render_mismatch_report_markdown(report)

        self.assertIn("# Mismatch Report", markdown)
        self.assertIn("## Summary", markdown)
        self.assertIn("## Error Taxonomy", markdown)
        self.assertIn("## Field Examples", markdown)
        self.assertIn("## Overall Paper Lists", markdown)
        self.assertIn("### value interpretation error", markdown)
        self.assertIn("### Empirical", markdown)
