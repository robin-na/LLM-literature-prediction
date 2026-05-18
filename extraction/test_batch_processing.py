from __future__ import annotations

import json
import tempfile
import unittest
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from batch_processing.agentic_tools import (
    evaluate_expression,
    execute_tool,
    needs_review_gate,
    validate_field_output,
)
from batch_processing.agentic_workflow import run_agentic_field_extraction
from batch_processing.extraction_cli_common import is_derived_markdown_dir, resolve_paper_dir
from batch_processing.extraction_pipeline import (
    DEFAULT_HYBRID_AGENTIC_FIELDS,
    merge_agentic_fields_into_rows,
    run_agentic_overrides,
    simple_fields,
)


@dataclass
class FakeFunction:
    name: str
    arguments: str


@dataclass
class FakeToolCall:
    id: str
    function: FakeFunction
    type: str = "function"


@dataclass
class FakeMessage:
    content: str
    tool_calls: list[FakeToolCall] | None = None


@dataclass
class FakeChoice:
    message: FakeMessage


@dataclass
class FakeResponse:
    id: str
    choices: list[FakeChoice]


class FakeChatCompletions:
    def __init__(self, scripted_messages: list[FakeMessage]):
        self._scripted_messages = scripted_messages
        self.calls: list[dict] = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        if not self._scripted_messages:
            raise AssertionError("No scripted fake responses remaining.")
        message = self._scripted_messages.pop(0)
        return FakeResponse(
            id=f"resp_{len(self.calls)}",
            choices=[FakeChoice(message=message)],
        )


class FakeClient:
    def __init__(self, scripted_messages: list[FakeMessage]):
        self.chat = SimpleNamespace(completions=FakeChatCompletions(scripted_messages))


class AgenticWorkflowTests(unittest.TestCase):
    def test_calculator_tool(self):
        result = evaluate_expression("(29.64)/(4*20)")
        self.assertTrue(result["ok"])
        self.assertAlmostEqual(result["value"], 0.3705)

    def test_quote_finder_tool(self):
        paper_text = "Each player had an endowment of 20 tokens. Mean contribution was 6.19."
        result = execute_tool(
            "quote_finder",
            {"terms": ["endowment", "contribution"], "max_results": 2},
            paper_text,
        )
        self.assertEqual(len(result["matches"]), 1)
        self.assertIn("20 tokens", result["matches"][0]["snippet"])

    def test_evidence_pack_and_normalization_tools(self):
        paper_text = (
            "Control groups had four players with an endowment of 20 tokens each. "
            "Average group contribution was 29.64 tokens."
        )
        evidence = execute_tool(
            "evidence_pack_builder",
            {"field": "DV_contributionRate", "max_results": 4},
            paper_text,
        )
        self.assertGreaterEqual(evidence["evidence_count"], 1)

        normalized = execute_tool(
            "normalization_checker",
            {
                "field": "DV_contributionRate",
                "raw_value": 29.64,
                "endowment": 20,
                "player_count": 4,
            },
            paper_text,
        )
        self.assertTrue(normalized["ok"])
        self.assertAlmostEqual(normalized["computed_value"], 0.3705)

    def test_payoff_formula_parser_and_review_gate(self):
        paper_text = (
            "Each player's payoff was 20 - c_i + 0.4 times the sum of contributions. "
            "Groups had 4 players and each player had an endowment of 20 tokens."
        )
        parsed = execute_tool(
            "payoff_formula_parser",
            {"field": "CONFIG_MPCR", "max_results": 3},
            paper_text,
        )
        self.assertEqual(parsed["candidate_player_count"], 4.0)
        self.assertEqual(parsed["candidate_endowment"], 20.0)
        self.assertEqual(parsed["candidate_mpcr"], 0.4)

        gate = needs_review_gate(
            field="CONFIG_MPCR",
            candidate_json=json.dumps(
                {
                    "experiments": [
                        {
                            "data_id": "Baseline",
                            "CONFIG_MPCR": 0.4,
                            "CONFIG_MPCR_reason": "coefficient on the public-good term",
                            "CONFIG_MPCR_confidence": 0.7,
                        }
                    ]
                }
            ),
            min_confidence=0.85,
        )
        self.assertEqual(gate["decision"], "needs_review")

    def test_review_gate_flags_mpcr_divided_by_group_size(self):
        paper_text = (
            "Groups had 4 players. Each player's payoff was 20 - c_i + 0.4 times the sum of contributions."
        )
        gate = needs_review_gate(
            field="CONFIG_MPCR",
            candidate_json=json.dumps(
                {
                    "experiments": [
                        {
                            "data_id": "Baseline",
                            "CONFIG_MPCR": 0.1,
                            "CONFIG_MPCR_reason": "Marginal per team return is 0.4; MPCR = 0.4 / 4 = 0.1.",
                            "CONFIG_MPCR_confidence": 0.98,
                        }
                    ]
                }
            ),
            min_confidence=0.85,
            paper_text=paper_text,
        )
        self.assertEqual(gate["decision"], "needs_review")
        self.assertTrue(any("divided by player count" in reason for reason in gate["reasons"]))

    def test_review_gate_flags_derivable_efficiency_abstention(self):
        paper_text = (
            "Groups had 4 players with an endowment of 20 tokens each. "
            "Average group earnings were reported for each treatment. "
            "Each player's payoff was 20 - c_i + 0.4 times the sum of contributions."
        )
        gate = needs_review_gate(
            field="DV_efficiency",
            candidate_json=json.dumps(
                {
                    "experiments": [
                        {
                            "data_id": "Control",
                            "DV_efficiency": "N/R",
                            "DV_efficiency_reason": "Not directly reported.",
                            "DV_efficiency_confidence": 0.95,
                            "step2_max_payoff": "N/R",
                            "step3_computation": "N/R",
                        }
                    ]
                }
            ),
            min_confidence=0.85,
            paper_text=paper_text,
        )
        self.assertEqual(gate["decision"], "needs_review")
        self.assertTrue(any("derivation cues" in reason for reason in gate["reasons"]))

    def test_validator_rejects_raw_contribution_amount(self):
        payload = {
            "experiments": [
                {
                    "data_id": "Control",
                    "DV_contributionRate": 6.19,
                    "DV_contributionRate_reason": "raw mean",
                    "DV_contributionRate_confidence": 0.8,
                    "step1_raw_quotes": ["mean contribution 6.19"],
                    "step2_endowment": 20,
                    "step3_computation": "6.19",
                }
            ]
        }
        validation = validate_field_output("DV_contributionRate", payload)
        self.assertFalse(validation.ok)
        self.assertTrue(any("normalized fraction" in error for error in validation.errors))

    def test_workflow_revises_after_skeptical_critique(self):
        paper_text = (
            "Control groups had four players with an endowment of 20 tokens each. "
            "Average group contribution was 29.64 tokens."
        )
        scripted_messages = [
            FakeMessage(
                content="",
                tool_calls=[
                    FakeToolCall(
                        id="tool_1",
                        function=FakeFunction(
                            name="calculator",
                            arguments=json.dumps({"expression": "(29.64)/(4*20)"}),
                        ),
                    )
                ],
            ),
            FakeMessage(
                content=json.dumps(
                    {
                        "experiments": [
                            {
                                "data_id": "Control",
                                "DV_contributionRate": 1.482,
                                "DV_contributionRate_reason": "29.64 / 20",
                                "DV_contributionRate_confidence": 0.72,
                                "step1_raw_quotes": ["Average group contribution was 29.64 tokens."],
                                "step2_endowment": 20,
                                "step3_computation": "29.64 / 20 = 1.482",
                            }
                        ]
                    }
                )
            ),
            FakeMessage(
                content=json.dumps(
                    {
                        "verdict": "needs_revision",
                        "summary": "The draft divided a group total by the per-player endowment only.",
                        "issues": [
                            {
                                "severity": "high",
                                "kind": "wrong_normalization_risk",
                                "target": "experiments[0].DV_contributionRate",
                                "evidence": "The paper reports a group total for four players.",
                                "proposed_fix": "Divide by 4 * 20 instead of 20.",
                            }
                        ],
                    }
                )
            ),
            FakeMessage(
                content=json.dumps(
                    {
                        "experiments": [
                            {
                                "data_id": "Control",
                                "DV_contributionRate": 0.3705,
                                "DV_contributionRate_reason": "29.64 / (4 * 20)",
                                "DV_contributionRate_confidence": 0.93,
                                "step1_raw_quotes": ["Average group contribution was 29.64 tokens."],
                                "step2_endowment": 20,
                                "step3_computation": "29.64 / (4 * 20) = 0.3705",
                            }
                        ]
                    }
                )
            ),
        ]
        client = FakeClient(scripted_messages)

        result = run_agentic_field_extraction(
            client=client,
            field="DV_contributionRate",
            paper_text=paper_text,
            model="fake-model",
            max_critic_rounds=1,
        )

        self.assertTrue(result["validation"]["ok"])
        self.assertEqual(result["final_output"]["experiments"][0]["DV_contributionRate"], 0.3705)
        self.assertEqual(len(result["critic_rounds"]), 1)
        self.assertEqual(result["critic_rounds"][0]["report_json"]["verdict"], "needs_revision")

    def test_workflow_repairs_validation_failure(self):
        paper_text = "Each player's payoff included 0.4 times the sum of contributions."
        scripted_messages = [
            FakeMessage(
                content=json.dumps(
                    {
                        "experiments": [
                            {
                                "data_id": "Baseline",
                                "CONFIG_MPCR": 0.4,
                                "CONFIG_MPCR_reason": "coefficient on the sum",
                                "CONFIG_MPCR_confidence": "high",
                            }
                        ]
                    }
                )
            ),
            FakeMessage(
                content=json.dumps(
                    {
                        "verdict": "pass",
                        "summary": "No grounded objections.",
                        "issues": [],
                    }
                )
            ),
            FakeMessage(
                content=json.dumps(
                    {
                        "experiments": [
                            {
                                "data_id": "Baseline",
                                "CONFIG_MPCR": 0.4,
                                "CONFIG_MPCR_reason": "coefficient on the public-good term",
                                "CONFIG_MPCR_confidence": 0.91,
                            }
                        ]
                    }
                )
            ),
        ]
        client = FakeClient(scripted_messages)

        result = run_agentic_field_extraction(
            client=client,
            field="CONFIG_MPCR",
            paper_text=paper_text,
            model="fake-model",
            max_critic_rounds=1,
        )

        self.assertTrue(result["validation"]["ok"])
        self.assertIsNotNone(result["post_repair_validation"])
        self.assertEqual(result["final_output"]["experiments"][0]["CONFIG_MPCR"], 0.4)


class ExtractionPipelineTests(unittest.TestCase):
    def test_simple_fields_excludes_agentic_fields(self):
        result = simple_fields()
        for field in DEFAULT_HYBRID_AGENTIC_FIELDS:
            self.assertNotIn(field, result)
        self.assertIn("CONFIG_chat", result)

    def test_merge_agentic_fields_overrides_target_field_only(self):
        rows = [
            {
                "custom_id": "paper-1",
                "data_id": "Control",
                "CONFIG_MPCR": "N/R",
                "CONFIG_MPCR_reason": "",
                "CONFIG_MPCR_confidence": 0,
                "CONFIG_chat": 0,
                "CONFIG_chat_reason": "simple extraction",
                "CONFIG_chat_confidence": 0.8,
            }
        ]
        agentic_results = {
            "CONFIG_MPCR": {
                "final_output": {
                    "experiments": [
                        {
                            "data_id": "Control",
                            "CONFIG_MPCR": 0.4,
                            "CONFIG_MPCR_reason": "coefficient on the public-good term",
                            "CONFIG_MPCR_confidence": 0.95,
                        }
                    ]
                },
                "validation": {"ok": True, "errors": [], "warnings": []},
                "critic_rounds": [],
            }
        }

        merged_rows, metadata_rows = merge_agentic_fields_into_rows(
            simple_rows=rows,
            agentic_results=agentic_results,
        )

        self.assertEqual(merged_rows[0]["CONFIG_MPCR"], 0.4)
        self.assertEqual(merged_rows[0]["CONFIG_MPCR_confidence"], 0.95)
        self.assertEqual(merged_rows[0]["CONFIG_chat"], 0)
        self.assertEqual(len(metadata_rows), 1)
        self.assertEqual(metadata_rows[0]["field"], "CONFIG_MPCR")
        self.assertEqual(metadata_rows[0]["agentic_error"], "")
        self.assertTrue(metadata_rows[0]["merge_applied"])

    def test_merge_skips_v2_when_pipeline_not_accept(self):
        rows = [
            {
                "custom_id": "paper-1",
                "data_id": "Control",
                "CONFIG_MPCR": 0.2,
                "CONFIG_MPCR_reason": "simple",
                "CONFIG_MPCR_confidence": 0.5,
                "CONFIG_chat": 0,
                "CONFIG_chat_reason": "simple extraction",
                "CONFIG_chat_confidence": 0.8,
            }
        ]
        agentic_results = {
            "CONFIG_MPCR": {
                "agentic_version": "v2",
                "pipeline_decision": "needs_review",
                "gate_result": {"decision": "needs_review", "reasons": ["low confidence"]},
                "final_output": {
                    "experiments": [
                        {
                            "data_id": "Control",
                            "CONFIG_MPCR": 0.9,
                            "CONFIG_MPCR_reason": "agentic",
                            "CONFIG_MPCR_confidence": 0.99,
                        }
                    ]
                },
                "validation": {"ok": True, "errors": [], "warnings": []},
                "critic_rounds": [],
            }
        }

        merged_rows, metadata_rows = merge_agentic_fields_into_rows(
            simple_rows=rows,
            agentic_results=agentic_results,
        )

        self.assertEqual(merged_rows[0]["CONFIG_MPCR"], 0.2)
        self.assertFalse(metadata_rows[0]["merge_applied"])
        self.assertEqual(metadata_rows[0]["pipeline_decision"], "needs_review")

    def test_run_agentic_overrides_falls_back_on_field_error(self):
        field = DEFAULT_HYBRID_AGENTIC_FIELDS[0]

        def fake_run_agentic_field_extraction(**kwargs):
            if kwargs["field"] == field:
                raise RuntimeError("Model exceeded the maximum number of tool rounds.")
            return {
                "final_output": {"experiments": []},
                "validation": {"ok": True, "errors": [], "warnings": []},
                "critic_rounds": [],
            }

        with patch(
            "batch_processing.extraction_pipeline.run_agentic_field_extraction",
            side_effect=fake_run_agentic_field_extraction,
        ):
            results = run_agentic_overrides(
                client=object(),
                model="gpt-4.1",
                paper_text="paper text",
                agentic_fields=(field,),
                continue_on_error=True,
                agentic_version="v1",
            )

        self.assertIn(field, results)
        self.assertFalse(results[field]["validation"]["ok"])
        self.assertIn("tool rounds", results[field]["error"])
        self.assertEqual(results[field]["final_output"]["experiments"], [])


class HybridExtractAppTests(unittest.TestCase):
    def test_is_derived_markdown_dir_flags_report_paths(self):
        path = Path("literature/output/paper_analysis_reports/broad_all")
        self.assertTrue(is_derived_markdown_dir(path))

    def test_resolve_paper_dir_rejects_derived_markdown(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            derived_dir = Path(temp_dir) / "paper_card_memos" / "strict_predictive_empirical_payoff"
            derived_dir.mkdir(parents=True)

            with self.assertRaisesRegex(ValueError, "derived markdown"):
                resolve_paper_dir(str(derived_dir))

    def test_resolve_paper_dir_accepts_regular_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_dir = Path(temp_dir) / "raw_markdown"
            raw_dir.mkdir()

            self.assertEqual(resolve_paper_dir(str(raw_dir)), raw_dir)


if __name__ == "__main__":
    unittest.main()
