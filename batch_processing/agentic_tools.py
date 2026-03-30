from __future__ import annotations

import ast
import json
import math
import re
from dataclasses import dataclass
from typing import Any


SUPPORTED_AGENTIC_FIELDS = (
    "CONFIG_playerCount",
    "CONFIG_allOrNothing",
    "DV_contributionRate",
    "DV_efficiency",
    "CONFIG_MPCR",
)

FIELD_DEFAULT_TERMS = {
    "CONFIG_playerCount": [
        "group of",
        "groups of",
        "players",
        "participants",
        "teams",
        "members",
    ],
    "CONFIG_allOrNothing": [
        "contribute",
        "contribution",
        "all or nothing",
        "0 to",
        "full endowment",
        "binary",
    ],
    "DV_contributionRate": [
        "contribution",
        "endowment",
        "average contribution",
        "group contribution",
        "control",
        "treatment",
    ],
    "DV_efficiency": [
        "efficiency",
        "payoff",
        "earnings",
        "endowment",
        "MPCR",
        "multiplier",
        "control",
        "treatment",
    ],
    "CONFIG_MPCR": [
        "MPCR",
        "marginal per capita return",
        "multiplier",
        "payoff",
        "sum of contributions",
        "group size",
    ],
}

FIELD_TOOL_HINTS = {
    "CONFIG_playerCount": [
        "Count strategic players in the payoff-relevant group, not total session headcount.",
        "If teams act as players, count teams rather than people.",
        "Use N/R only when group structure is truly absent.",
    ],
    "CONFIG_allOrNothing": [
        "Return 1 when players can choose any contribution from 0 to endowment.",
        "Return 0 for binary or no continuous contribution scale.",
        "Do not confuse binary actions with flexible contribution choice.",
    ],
    "DV_contributionRate": [
        "Normalize raw contributions to a 0-1 fraction.",
        "If a group total is reported, divide by players times endowment.",
        "Use N/R when the value cannot be derived from text, not from graphs.",
    ],
    "DV_efficiency": [
        "Efficiency must be a 0-1 fraction or N/R.",
        "Do not report a raw payoff as efficiency.",
        "If the denominator cannot be derived, prefer N/R.",
    ],
    "CONFIG_MPCR": [
        "MPCR is the coefficient on the public-good term in the individual payoff function.",
        "Do not divide a per-capita coefficient again.",
        "Heterogeneous MPCR values may be represented as a list or compact string.",
    ],
}

FIELD_EXTRA_KEYS = {
    "CONFIG_playerCount": [],
    "CONFIG_allOrNothing": [],
    "DV_contributionRate": ["step1_raw_quotes", "step2_endowment", "step3_computation"],
    "DV_efficiency": ["step2_max_payoff", "step3_computation"],
    "CONFIG_MPCR": [],
}

_ALLOWED_CALCULATOR_FUNCTIONS = {
    "abs": abs,
    "max": max,
    "min": min,
    "round": round,
}

_ALLOWED_AST_NODES = (
    ast.Expression,
    ast.BinOp,
    ast.UnaryOp,
    ast.Add,
    ast.Sub,
    ast.Mult,
    ast.Div,
    ast.Pow,
    ast.Mod,
    ast.USub,
    ast.UAdd,
    ast.Call,
    ast.Name,
    ast.Load,
    ast.Constant,
)


@dataclass
class ValidationResult:
    ok: bool
    errors: list[str]
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "errors": self.errors,
            "warnings": self.warnings,
        }


def build_tool_specs() -> list[dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": "calculator",
                "description": (
                    "Evaluate a short arithmetic expression for normalization or payoff "
                    "checks. Use only for math, not for semantic reasoning."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                            "description": "Arithmetic expression such as '(29.64)/(4*20)'.",
                        }
                    },
                    "required": ["expression"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "quote_finder",
                "description": (
                    "Find matching text spans in the paper for field-relevant terms such as "
                    "endowment, payoff, MPCR, multiplier, contribution, or condition names."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "terms": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "One or more search terms.",
                        },
                        "max_results": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 10,
                            "default": 5,
                        },
                        "context_chars": {
                            "type": "integer",
                            "minimum": 40,
                            "maximum": 500,
                            "default": 180,
                        },
                    },
                    "required": ["terms"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "evidence_pack_builder",
                "description": (
                    "Build a compact field-specific evidence pack by collecting the most "
                    "relevant snippets from the paper before extraction or critique."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "field": {
                            "type": "string",
                            "enum": list(SUPPORTED_AGENTIC_FIELDS),
                        },
                        "terms": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional extra search terms to prioritize.",
                        },
                        "max_results": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 12,
                            "default": 6,
                        },
                    },
                    "required": ["field"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "condition_aligner",
                "description": (
                    "Extract candidate condition labels and supporting snippets to reduce "
                    "condition-mixing mistakes."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "known_labels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional known condition labels to search for.",
                        },
                        "max_results": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 12,
                            "default": 6,
                        },
                    },
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "normalization_checker",
                "description": (
                    "Check normalization arithmetic for contribution-rate or efficiency "
                    "derivations and return the computed value plus formula."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "field": {
                            "type": "string",
                            "enum": ["DV_contributionRate", "DV_efficiency"],
                        },
                        "raw_value": {"type": "number"},
                        "endowment": {"type": "number"},
                        "player_count": {"type": "number"},
                        "percentage": {"type": "number"},
                        "already_normalized": {"type": "number"},
                        "actual_payoff": {"type": "number"},
                        "max_payoff": {"type": "number"},
                    },
                    "required": ["field"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "payoff_formula_parser",
                "description": (
                    "Extract candidate payoff-formula ingredients relevant for MPCR or "
                    "efficiency, including multipliers, player counts, endowments, and "
                    "payoff-equation snippets."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "field": {
                            "type": "string",
                            "enum": ["DV_efficiency", "CONFIG_MPCR"],
                        },
                        "max_results": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 10,
                            "default": 5,
                        },
                    },
                    "required": ["field"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "needs_review_gate",
                "description": (
                    "Decide whether a candidate extraction should be auto-accepted or "
                    "flagged for human review based on validation and confidence."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "field": {
                            "type": "string",
                            "enum": list(SUPPORTED_AGENTIC_FIELDS),
                        },
                        "candidate_json": {
                            "type": "string",
                            "description": "Candidate JSON text to assess.",
                        },
                        "min_confidence": {
                            "type": "number",
                            "minimum": 0,
                            "maximum": 1,
                            "default": 0.85,
                        },
                    },
                    "required": ["field", "candidate_json"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "field_rulebook",
                "description": "Return deterministic validation hints for the selected field.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "field": {
                            "type": "string",
                            "enum": list(SUPPORTED_AGENTIC_FIELDS),
                        }
                    },
                    "required": ["field"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "validate_candidate_output",
                "description": (
                    "Validate a candidate JSON string against deterministic field-specific "
                    "rules before finalizing an answer."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "field": {
                            "type": "string",
                            "enum": list(SUPPORTED_AGENTIC_FIELDS),
                        },
                        "candidate_json": {
                            "type": "string",
                            "description": "Candidate JSON text to validate.",
                        },
                    },
                    "required": ["field", "candidate_json"],
                    "additionalProperties": False,
                },
            },
        },
    ]


def execute_tool(name: str, arguments: dict[str, Any], paper_text: str) -> dict[str, Any]:
    if name == "calculator":
        expression = str(arguments.get("expression", ""))
        return evaluate_expression(expression)
    if name == "quote_finder":
        terms = arguments.get("terms", [])
        max_results = int(arguments.get("max_results", 5))
        context_chars = int(arguments.get("context_chars", 180))
        return find_quotes(
            paper_text=paper_text,
            terms=[str(term) for term in terms],
            max_results=max_results,
            context_chars=context_chars,
        )
    if name == "evidence_pack_builder":
        field = str(arguments.get("field", ""))
        terms = [str(term) for term in arguments.get("terms", [])]
        max_results = int(arguments.get("max_results", 6))
        return build_evidence_pack(
            field=field,
            paper_text=paper_text,
            extra_terms=terms,
            max_results=max_results,
        )
    if name == "condition_aligner":
        known_labels = [str(label) for label in arguments.get("known_labels", [])]
        max_results = int(arguments.get("max_results", 6))
        return condition_aligner(
            paper_text=paper_text,
            known_labels=known_labels,
            max_results=max_results,
        )
    if name == "normalization_checker":
        return normalization_checker(arguments)
    if name == "payoff_formula_parser":
        field = str(arguments.get("field", ""))
        max_results = int(arguments.get("max_results", 5))
        return payoff_formula_parser(
            field=field,
            paper_text=paper_text,
            max_results=max_results,
        )
    if name == "needs_review_gate":
        field = str(arguments.get("field", ""))
        candidate_json = str(arguments.get("candidate_json", ""))
        min_confidence = float(arguments.get("min_confidence", 0.85))
        return needs_review_gate(
            field=field,
            candidate_json=candidate_json,
            min_confidence=min_confidence,
        )
    if name == "field_rulebook":
        field = str(arguments.get("field", ""))
        return {
            "field": field,
            "supported": field in SUPPORTED_AGENTIC_FIELDS,
            "required_keys": required_experiment_keys(field),
            "hints": FIELD_TOOL_HINTS.get(field, []),
        }
    if name == "validate_candidate_output":
        field = str(arguments.get("field", ""))
        candidate_json = str(arguments.get("candidate_json", ""))
        parsed, parse_error = parse_json_object(candidate_json)
        if parse_error:
            return {"ok": False, "errors": [parse_error], "warnings": []}
        return validate_field_output(field, parsed).to_dict()
    raise ValueError(f"Unknown tool: {name}")


def evaluate_expression(expression: str) -> dict[str, Any]:
    try:
        tree = ast.parse(expression, mode="eval")
        _assert_safe_ast(tree)
        value = _eval_node(tree.body)
    except Exception as exc:
        return {"ok": False, "expression": expression, "error": str(exc)}

    if isinstance(value, float) and math.isfinite(value):
        rounded = round(value, 10)
    else:
        rounded = value
    return {"ok": True, "expression": expression, "value": rounded}


def _assert_safe_ast(node: ast.AST) -> None:
    for child in ast.walk(node):
        if not isinstance(child, _ALLOWED_AST_NODES):
            raise ValueError(f"Unsupported syntax: {type(child).__name__}")
        if isinstance(child, ast.Call):
            if not isinstance(child.func, ast.Name) or child.func.id not in _ALLOWED_CALCULATOR_FUNCTIONS:
                raise ValueError("Unsupported function call")


def _eval_node(node: ast.AST) -> Any:
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only numeric constants are allowed")
    if isinstance(node, ast.BinOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right
        if isinstance(node.op, ast.Pow):
            return left ** right
        if isinstance(node.op, ast.Mod):
            return left % right
    if isinstance(node, ast.UnaryOp):
        operand = _eval_node(node.operand)
        if isinstance(node.op, ast.UAdd):
            return +operand
        if isinstance(node.op, ast.USub):
            return -operand
    if isinstance(node, ast.Call):
        func_name = node.func.id
        func = _ALLOWED_CALCULATOR_FUNCTIONS[func_name]
        args = [_eval_node(arg) for arg in node.args]
        return func(*args)
    if isinstance(node, ast.Name) and node.id in {"pi", "e"}:
        return getattr(math, node.id)
    raise ValueError(f"Unsupported expression node: {type(node).__name__}")


def find_quotes(
    *,
    paper_text: str,
    terms: list[str],
    max_results: int = 5,
    context_chars: int = 180,
) -> dict[str, Any]:
    normalized_terms = [term.strip() for term in terms if term and term.strip()]
    if not normalized_terms:
        return {"matches": []}

    matches: list[dict[str, Any]] = []
    seen_spans: set[tuple[int, int]] = set()
    for term in normalized_terms:
        pattern = re.compile(re.escape(term), flags=re.IGNORECASE)
        for match in pattern.finditer(paper_text):
            start = max(0, match.start() - context_chars)
            end = min(len(paper_text), match.end() + context_chars)
            span = (start, end)
            if span in seen_spans:
                continue
            seen_spans.add(span)
            snippet = paper_text[start:end].replace("\n", " ").strip()
            matches.append(
                {
                    "term": term,
                    "start": match.start(),
                    "end": match.end(),
                    "snippet": snippet,
                }
            )
            if len(matches) >= max_results:
                return {"matches": matches}
    return {"matches": matches}


def build_evidence_pack(
    *,
    field: str,
    paper_text: str,
    extra_terms: list[str] | None = None,
    max_results: int = 6,
) -> dict[str, Any]:
    base_terms = FIELD_DEFAULT_TERMS.get(field, [])
    all_terms = list(dict.fromkeys([*base_terms, *(extra_terms or [])]))
    quote_result = find_quotes(
        paper_text=paper_text,
        terms=all_terms,
        max_results=max_results,
        context_chars=220,
    )
    return {
        "field": field,
        "terms_used": all_terms,
        "evidence_count": len(quote_result["matches"]),
        "evidence": quote_result["matches"],
    }


def condition_aligner(
    *,
    paper_text: str,
    known_labels: list[str] | None = None,
    max_results: int = 6,
) -> dict[str, Any]:
    sentences = _split_text_units(paper_text)
    label_patterns = [label.strip() for label in (known_labels or []) if label and label.strip()]
    generic_pattern = re.compile(
        r"\b(control|treatment|condition|arm|baseline|experiment\s*\d+|study\s*\d+)\b",
        flags=re.IGNORECASE,
    )
    matches: list[dict[str, Any]] = []
    seen: set[str] = set()
    for sentence in sentences:
        sentence_lower = sentence.lower()
        labels: list[str] = []
        for label in label_patterns:
            if label.lower() in sentence_lower:
                labels.append(label)
        for found in generic_pattern.findall(sentence):
            labels.append(str(found))
        unique_labels = [label for label in dict.fromkeys(labels) if label]
        if not unique_labels:
            continue
        snippet = sentence.strip()
        if snippet in seen:
            continue
        seen.add(snippet)
        matches.append({"labels": unique_labels, "snippet": snippet})
        if len(matches) >= max_results:
            break
    return {"conditions": matches}


def normalization_checker(arguments: dict[str, Any]) -> dict[str, Any]:
    field = str(arguments.get("field", ""))
    if field == "DV_contributionRate":
        already_normalized = arguments.get("already_normalized")
        if isinstance(already_normalized, (int, float)):
            return {
                "ok": 0 <= float(already_normalized) <= 1,
                "field": field,
                "computed_value": float(already_normalized),
                "formula": "already_normalized",
            }
        percentage = arguments.get("percentage")
        if isinstance(percentage, (int, float)):
            value = float(percentage) / 100.0
            return {
                "ok": True,
                "field": field,
                "computed_value": round(value, 10),
                "formula": f"{percentage} / 100",
            }
        raw_value = arguments.get("raw_value")
        endowment = arguments.get("endowment")
        player_count = arguments.get("player_count")
        if isinstance(raw_value, (int, float)) and isinstance(endowment, (int, float)):
            if isinstance(player_count, (int, float)):
                value = float(raw_value) / (float(player_count) * float(endowment))
                return {
                    "ok": True,
                    "field": field,
                    "computed_value": round(value, 10),
                    "formula": f"{raw_value} / ({player_count} * {endowment})",
                }
            value = float(raw_value) / float(endowment)
            return {
                "ok": True,
                "field": field,
                "computed_value": round(value, 10),
                "formula": f"{raw_value} / {endowment}",
            }
        return {
            "ok": False,
            "field": field,
            "error": "Need already_normalized, percentage, or raw_value plus endowment.",
        }
    if field == "DV_efficiency":
        actual_payoff = arguments.get("actual_payoff")
        max_payoff = arguments.get("max_payoff")
        if isinstance(actual_payoff, (int, float)) and isinstance(max_payoff, (int, float)):
            if float(max_payoff) == 0:
                return {"ok": False, "field": field, "error": "max_payoff must be non-zero."}
            value = float(actual_payoff) / float(max_payoff)
            return {
                "ok": True,
                "field": field,
                "computed_value": round(value, 10),
                "formula": f"{actual_payoff} / {max_payoff}",
            }
        return {
            "ok": False,
            "field": field,
            "error": "Need actual_payoff and max_payoff for efficiency.",
        }
    return {"ok": False, "field": field, "error": f"Unsupported field for normalization: {field}"}


def payoff_formula_parser(
    *,
    field: str,
    paper_text: str,
    max_results: int = 5,
) -> dict[str, Any]:
    evidence = build_evidence_pack(field=field, paper_text=paper_text, max_results=max_results)
    snippets = [item["snippet"] for item in evidence["evidence"]]
    number_pattern = re.compile(r"(?<!\w)(\d+(?:\.\d+)?)")
    extracted_numbers: list[float] = []
    for snippet in snippets:
        for match in number_pattern.findall(snippet):
            try:
                extracted_numbers.append(float(match))
            except ValueError:
                continue

    player_count = _extract_first_number(
        paper_text,
        patterns=[
            r"group(?:s)? of (\d+(?:\.\d+)?)",
            r"(\d+(?:\.\d+)?) players",
            r"(\d+(?:\.\d+)?) members",
        ],
    )
    endowment = _extract_first_number(
        paper_text,
        patterns=[
            r"endowment of (\d+(?:\.\d+)?)",
            r"each player.*?(\d+(?:\.\d+)?) tokens",
        ],
    )
    multiplier = _extract_first_number(
        paper_text,
        patterns=[
            r"multiplier(?: of)? (\d+(?:\.\d+)?)",
            r"multiplied by (\d+(?:\.\d+)?)",
            r"(\d+(?:\.\d+)?) times the sum of contributions",
        ],
    )
    mpcr = _extract_first_number(
        paper_text,
        patterns=[
            r"MPCR(?: of)? (\d+(?:\.\d+)?)",
            r"marginal per capita return(?: of)? (\d+(?:\.\d+)?)",
            r"each player(?: receives| gets)? (\d+(?:\.\d+)?) per",
            r"(\d+(?:\.\d+)?) times the sum of contributions",
        ],
    )
    return {
        "field": field,
        "candidate_player_count": player_count,
        "candidate_endowment": endowment,
        "candidate_multiplier": multiplier,
        "candidate_mpcr": mpcr,
        "snippets": snippets,
        "numbers_seen": extracted_numbers[:20],
    }


def needs_review_gate(
    *,
    field: str,
    candidate_json: str,
    min_confidence: float = 0.85,
) -> dict[str, Any]:
    parsed, parse_error = parse_json_object(candidate_json)
    if parse_error:
        return {
            "decision": "needs_review",
            "reasons": [parse_error],
            "validation": {"ok": False, "errors": [parse_error], "warnings": []},
        }
    validation = validate_field_output(field, parsed).to_dict()
    reasons = list(validation["errors"]) + list(validation["warnings"])
    if not validation["ok"]:
        return {
            "decision": "needs_review",
            "reasons": reasons,
            "validation": validation,
        }
    experiments = parsed.get("experiments", [])
    confidences: list[float] = []
    confidence_key = f"{field}_confidence"
    for experiment in experiments:
        confidence = experiment.get(confidence_key)
        if isinstance(confidence, (int, float)):
            confidences.append(float(confidence))
    low_confidence = [value for value in confidences if value < min_confidence]
    if low_confidence:
        reasons.append(
            f"One or more confidences fell below the review threshold of {min_confidence:.2f}."
        )
    decision = "needs_review" if reasons else "auto_accept"
    return {
        "decision": decision,
        "reasons": reasons,
        "validation": validation,
        "min_confidence": min_confidence,
        "confidences": confidences,
    }


def required_experiment_keys(field: str) -> list[str]:
    if field not in SUPPORTED_AGENTIC_FIELDS:
        return []
    return ["data_id", field, f"{field}_reason", f"{field}_confidence", *FIELD_EXTRA_KEYS[field]]


def parse_json_object(text: str) -> tuple[dict[str, Any] | None, str | None]:
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as exc:
        return None, f"Invalid JSON: {exc}"
    if not isinstance(parsed, dict):
        return None, "Top-level JSON value must be an object."
    return parsed, None


def validate_field_output(field: str, payload: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []
    warnings: list[str] = []

    if field not in SUPPORTED_AGENTIC_FIELDS:
        return ValidationResult(ok=False, errors=[f"Unsupported field: {field}"], warnings=[])

    experiments = payload.get("experiments")
    if not isinstance(experiments, list) or not experiments:
        return ValidationResult(
            ok=False,
            errors=["Top-level 'experiments' must be a non-empty list."],
            warnings=[],
        )

    required_keys = required_experiment_keys(field)
    for index, experiment in enumerate(experiments):
        prefix = f"experiments[{index}]"
        if not isinstance(experiment, dict):
            errors.append(f"{prefix} must be an object.")
            continue
        for key in required_keys:
            if key not in experiment:
                errors.append(f"{prefix} is missing required key '{key}'.")

        data_id = experiment.get("data_id")
        if not isinstance(data_id, str) or not data_id.strip():
            errors.append(f"{prefix}.data_id must be a non-empty string.")

        confidence = experiment.get(f"{field}_confidence")
        if not isinstance(confidence, (int, float)) or not (0 <= float(confidence) <= 1):
            errors.append(f"{prefix}.{field}_confidence must be a number in [0, 1].")

        reason = experiment.get(f"{field}_reason")
        if not isinstance(reason, str):
            errors.append(f"{prefix}.{field}_reason must be a string.")

        value = experiment.get(field)
        if field == "DV_contributionRate":
            _validate_fraction_value(prefix, field, value, errors)
            quotes = experiment.get("step1_raw_quotes")
            if not isinstance(quotes, list) or not all(isinstance(item, str) for item in quotes):
                errors.append(f"{prefix}.step1_raw_quotes must be a list of strings.")
            _validate_number_or_token(
                prefix=f"{prefix}.step2_endowment",
                value=experiment.get("step2_endowment"),
                errors=errors,
                allowed_tokens={"N/R"},
            )
            if not isinstance(experiment.get("step3_computation"), str):
                errors.append(f"{prefix}.step3_computation must be a string.")
            if isinstance(value, (int, float)) and value > 1:
                errors.append(f"{prefix}.{field} must be a normalized fraction, not a raw amount.")
        elif field == "DV_efficiency":
            _validate_fraction_value(prefix, field, value, errors)
            max_payoff = experiment.get("step2_max_payoff")
            _validate_number_or_token(
                prefix=f"{prefix}.step2_max_payoff",
                value=max_payoff,
                errors=errors,
                allowed_tokens={"N/R"},
            )
            if not isinstance(experiment.get("step3_computation"), str):
                errors.append(f"{prefix}.step3_computation must be a string.")
            if isinstance(value, (int, float)) and max_payoff == "N/R":
                errors.append(f"{prefix}.{field} cannot be numeric when step2_max_payoff is 'N/R'.")
        elif field == "CONFIG_MPCR":
            _validate_mpcr_value(prefix, value, errors, warnings)
        elif field == "CONFIG_playerCount":
            if value != "N/R" and not (
                isinstance(value, int) and not isinstance(value, bool) and value > 0
            ):
                errors.append(f"{prefix}.CONFIG_playerCount must be a positive integer or 'N/R'.")
        elif field == "CONFIG_allOrNothing":
            if value not in {0, 1}:
                errors.append(f"{prefix}.CONFIG_allOrNothing must be 0 or 1.")

    return ValidationResult(ok=not errors, errors=errors, warnings=warnings)


def _validate_fraction_value(prefix: str, field: str, value: Any, errors: list[str]) -> None:
    if value == "N/R":
        return
    if not isinstance(value, (int, float)):
        errors.append(f"{prefix}.{field} must be a number or 'N/R'.")
        return
    if not (0 <= float(value) <= 1):
        errors.append(f"{prefix}.{field} must be in [0, 1].")


def _validate_number_or_token(
    *,
    prefix: str,
    value: Any,
    errors: list[str],
    allowed_tokens: set[str],
) -> None:
    if value in allowed_tokens:
        return
    if not isinstance(value, (int, float)):
        allowed_display = ", ".join(sorted(allowed_tokens))
        errors.append(f"{prefix} must be a number or one of: {allowed_display}.")


def _validate_mpcr_value(
    prefix: str,
    value: Any,
    errors: list[str],
    warnings: list[str],
) -> None:
    if value == "N/R":
        return
    if isinstance(value, (int, float)):
        if float(value) < 0:
            errors.append(f"{prefix}.CONFIG_MPCR must be non-negative.")
        return
    if isinstance(value, list):
        if not value:
            errors.append(f"{prefix}.CONFIG_MPCR list cannot be empty.")
            return
        for item in value:
            if not isinstance(item, (int, float)):
                errors.append(f"{prefix}.CONFIG_MPCR list entries must be numeric.")
                return
            if float(item) < 0:
                errors.append(f"{prefix}.CONFIG_MPCR list entries must be non-negative.")
                return
        return
    if isinstance(value, str) and value.strip():
        if value == "N/A":
            errors.append(f"{prefix}.CONFIG_MPCR does not allow 'N/A'.")
            return
        if not re.search(r"\d", value):
            warnings.append(f"{prefix}.CONFIG_MPCR string does not contain a numeric cue.")
        return
    errors.append(
        f"{prefix}.CONFIG_MPCR must be a number, list of numbers, descriptive string, or 'N/R'."
    )


def _split_text_units(text: str) -> list[str]:
    units = re.split(r"[\n\r]+|(?<=[.!?])\s+", text)
    return [unit.strip() for unit in units if unit and unit.strip()]


def _extract_first_number(text: str, patterns: list[str]) -> float | None:
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
        if not match:
            continue
        try:
            return float(match.group(1))
        except ValueError:
            continue
    return None
