from __future__ import annotations

import ast
import json
import math
import re
from dataclasses import dataclass
from typing import Any


SUPPORTED_AGENTIC_FIELDS = (
    "DV_contributionRate",
    "DV_efficiency",
    "CONFIG_MPCR",
)

FIELD_TOOL_HINTS = {
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
