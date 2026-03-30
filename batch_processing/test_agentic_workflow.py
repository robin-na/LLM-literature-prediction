from __future__ import annotations

import json
import unittest
from dataclasses import dataclass
from types import SimpleNamespace

from batch_processing.agentic_tools import (
    evaluate_expression,
    execute_tool,
    needs_review_gate,
    validate_field_output,
)
from batch_processing.agentic_workflow import run_agentic_field_extraction


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


if __name__ == "__main__":
    unittest.main()
