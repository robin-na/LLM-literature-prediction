from __future__ import annotations

import json
from typing import Any

try:
    from batch_processing.agentic_tools import (
        SUPPORTED_AGENTIC_FIELDS,
        build_tool_specs,
        execute_tool,
        parse_json_object,
        validate_field_output,
    )
    from batch_processing.build_field_extractors import FIELD_CONFIGS, build_user_prompt
except ImportError:  # pragma: no cover - allows direct script execution
    from agentic_tools import (  # type: ignore
        SUPPORTED_AGENTIC_FIELDS,
        build_tool_specs,
        execute_tool,
        parse_json_object,
        validate_field_output,
    )
    from build_field_extractors import FIELD_CONFIGS, build_user_prompt  # type: ignore


EXTRACTOR_APPENDIX = """
You are the primary extraction agent.

Use tools when they can reduce extraction error:
- use quote_finder to confirm exact text support,
- use calculator for arithmetic,
- use field_rulebook for deterministic reminders,
- use validate_candidate_output before finalizing.

Return only the final extraction JSON object for the selected field.
""".strip()

CRITIC_SYSTEM_PROMPT = """
You are a skeptical auditor reviewing a field extraction from a PGG paper.

Your job is to attack weak claims without inventing errors. Only raise an issue when
you can point to a concrete textual gap, quote mismatch, arithmetic mistake,
normalization mistake, or condition-mixing risk. If the extraction is well supported,
say so explicitly.

Do not rewrite the extraction. Return only a structured attack report as JSON.
""".strip()

REVISION_APPENDIX = """
You are revising an existing field extraction after critique.

Only change a value when the critic provides a grounded objection backed by text or
arithmetic. If the attack report is ungrounded or weak, preserve the original answer.
Use tools if needed, and validate your candidate JSON before finalizing.

Return only the revised extraction JSON object.
""".strip()

VALIDATION_REPAIR_APPENDIX = """
Your previous extraction failed deterministic validation.

Repair only the schema or value issues listed below. Keep supported values intact.
Use tools if needed and validate your candidate JSON before finalizing.

Return only the repaired extraction JSON object.
""".strip()


def make_openai_client(api_key: str | None = None, organization: str | None = None):
    try:
        from openai import OpenAI
    except ImportError as exc:  # pragma: no cover - import guard
        raise ImportError(
            "The 'openai' package is required. Install it with `pip install openai`."
        ) from exc

    kwargs: dict[str, Any] = {}
    if api_key:
        kwargs["api_key"] = api_key
    if organization:
        kwargs["organization"] = organization
    return OpenAI(**kwargs)


def supported_fields() -> tuple[str, ...]:
    return tuple(SUPPORTED_AGENTIC_FIELDS)


def run_agentic_field_extraction(
    *,
    client: Any,
    field: str,
    paper_text: str,
    model: str,
    max_critic_rounds: int = 1,
    temperature: float = 0.0,
    max_tool_rounds: int = 8,
) -> dict[str, Any]:
    if field not in SUPPORTED_AGENTIC_FIELDS:
        raise ValueError(
            f"Unsupported field '{field}'. Supported fields: {', '.join(SUPPORTED_AGENTIC_FIELDS)}"
        )

    cfg = FIELD_CONFIGS[field]
    extractor_prompt = build_user_prompt(cfg, paper_text)
    current_draft = _run_json_agent(
        client=client,
        model=model,
        system_prompt=f"{cfg['system_prompt']}\n\n{EXTRACTOR_APPENDIX}",
        user_prompt=extractor_prompt,
        paper_text=paper_text,
        temperature=temperature,
        max_tool_rounds=max_tool_rounds,
    )

    critique_rounds: list[dict[str, Any]] = []
    for critic_index in range(max_critic_rounds):
        critic_report = _run_json_agent(
            client=client,
            model=model,
            system_prompt=CRITIC_SYSTEM_PROMPT,
            user_prompt=_build_critic_prompt(
                field=field,
                field_config=cfg,
                paper_text=paper_text,
                draft_text=current_draft["text"],
            ),
            paper_text=paper_text,
            temperature=temperature,
            max_tool_rounds=max_tool_rounds,
        )
        critique_entry = {
            "round": critic_index + 1,
            "report_text": critic_report["text"],
            "report_json": critic_report["parsed"],
            "trace": critic_report["trace"],
            "response_id": critic_report["response_id"],
        }
        critique_rounds.append(critique_entry)

        if not _critique_requires_revision(critic_report["parsed"]):
            break

        revised_draft = _run_json_agent(
            client=client,
            model=model,
            system_prompt=f"{cfg['system_prompt']}\n\n{REVISION_APPENDIX}",
            user_prompt=_build_revision_prompt(
                extractor_prompt=extractor_prompt,
                draft_text=current_draft["text"],
                critique_text=critic_report["text"],
            ),
            paper_text=paper_text,
            temperature=temperature,
            max_tool_rounds=max_tool_rounds,
        )
        critique_entry["revision_text"] = revised_draft["text"]
        critique_entry["revision_json"] = revised_draft["parsed"]
        critique_entry["revision_trace"] = revised_draft["trace"]
        critique_entry["revision_response_id"] = revised_draft["response_id"]
        current_draft = revised_draft

    validation = validate_field_output(field, current_draft["parsed"]).to_dict()
    repaired_validation: dict[str, Any] | None = None
    if not validation["ok"]:
        repaired = _run_json_agent(
            client=client,
            model=model,
            system_prompt=f"{cfg['system_prompt']}\n\n{VALIDATION_REPAIR_APPENDIX}",
            user_prompt=_build_validation_repair_prompt(
                extractor_prompt=extractor_prompt,
                draft_text=current_draft["text"],
                validation=validation,
            ),
            paper_text=paper_text,
            temperature=temperature,
            max_tool_rounds=max_tool_rounds,
        )
        repaired_validation = validate_field_output(field, repaired["parsed"]).to_dict()
        current_draft = repaired

    final_validation = validate_field_output(field, current_draft["parsed"]).to_dict()
    return {
        "field": field,
        "model": model,
        "draft_output": current_draft["parsed"],
        "draft_text": current_draft["text"],
        "draft_trace": current_draft["trace"],
        "draft_response_id": current_draft["response_id"],
        "critic_rounds": critique_rounds,
        "validation": final_validation,
        "pre_repair_validation": validation,
        "post_repair_validation": repaired_validation,
        "final_output": current_draft["parsed"],
    }


def _build_critic_prompt(
    *,
    field: str,
    field_config: dict[str, Any],
    paper_text: str,
    draft_text: str,
) -> str:
    return "\n\n".join(
        [
            "Selected field: " + field,
            "Field-specific extraction rules:",
            field_config["system_prompt"],
            "Expected extraction schema and task framing:",
            build_user_prompt(field_config, paper_text),
            "Current extraction draft JSON:",
            draft_text,
            (
                "Return JSON with keys: verdict, summary, issues. "
                "verdict must be 'pass' or 'needs_revision'. "
                "Each issue must include severity, kind, target, evidence, and proposed_fix."
            ),
        ]
    )


def _build_revision_prompt(
    *,
    extractor_prompt: str,
    draft_text: str,
    critique_text: str,
) -> str:
    return "\n\n".join(
        [
            extractor_prompt,
            "Current extraction draft JSON:",
            draft_text,
            "Critic attack report JSON:",
            critique_text,
        ]
    )


def _build_validation_repair_prompt(
    *,
    extractor_prompt: str,
    draft_text: str,
    validation: dict[str, Any],
) -> str:
    return "\n\n".join(
        [
            extractor_prompt,
            "Current extraction draft JSON:",
            draft_text,
            "Deterministic validation result:",
            json.dumps(validation, ensure_ascii=True, indent=2),
        ]
    )


def _critique_requires_revision(report: dict[str, Any]) -> bool:
    verdict = str(report.get("verdict", "")).strip().lower()
    if verdict == "needs_revision":
        return True
    issues = report.get("issues", [])
    return isinstance(issues, list) and bool(issues)


def _run_json_agent(
    *,
    client: Any,
    model: str,
    system_prompt: str,
    user_prompt: str,
    paper_text: str,
    temperature: float,
    max_tool_rounds: int,
) -> dict[str, Any]:
    messages: list[dict[str, Any]] = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    trace: list[dict[str, Any]] = []
    tools = build_tool_specs()

    for _ in range(max_tool_rounds + 1):
        response = client.chat.completions.create(
            model=model,
            temperature=temperature,
            response_format={"type": "json_object"},
            tools=tools,
            tool_choice="auto",
            messages=messages,
        )
        choice = response.choices[0]
        message = choice.message
        content = _message_text(message)
        tool_calls = _message_tool_calls(message)
        trace.append(
            {
                "role": "assistant",
                "content": content,
                "tool_calls": tool_calls,
            }
        )

        if tool_calls:
            messages.append(_assistant_history_message(content, tool_calls))
            for tool_call in tool_calls:
                arguments = _load_tool_arguments(tool_call["function"]["arguments"])
                result = execute_tool(tool_call["function"]["name"], arguments, paper_text)
                tool_message = {
                    "role": "tool",
                    "tool_call_id": tool_call["id"],
                    "content": json.dumps(result, ensure_ascii=True),
                }
                messages.append(tool_message)
                trace.append(
                    {
                        "role": "tool",
                        "name": tool_call["function"]["name"],
                        "arguments": arguments,
                        "result": result,
                    }
                )
            continue

        if not content or not content.strip():
            raise ValueError("Model returned an empty response.")

        parsed, parse_error = parse_json_object(content)
        if parse_error:
            raise ValueError(parse_error)
        return {
            "text": content,
            "parsed": parsed,
            "trace": trace,
            "response_id": getattr(response, "id", None),
        }

    raise RuntimeError("Model exceeded the maximum number of tool rounds.")


def _assistant_history_message(content: str, tool_calls: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "role": "assistant",
        "content": content or "",
        "tool_calls": tool_calls,
    }


def _message_text(message: Any) -> str:
    content = getattr(message, "content", "")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, dict):
                text = item.get("text")
                if text:
                    parts.append(str(text))
        return "\n".join(parts).strip()
    return str(content or "")


def _message_tool_calls(message: Any) -> list[dict[str, Any]]:
    raw_tool_calls = getattr(message, "tool_calls", None) or []
    tool_calls: list[dict[str, Any]] = []
    for tool_call in raw_tool_calls:
        if isinstance(tool_call, dict):
            tool_calls.append(tool_call)
            continue
        function = getattr(tool_call, "function", None)
        tool_calls.append(
            {
                "id": getattr(tool_call, "id", ""),
                "type": getattr(tool_call, "type", "function"),
                "function": {
                    "name": getattr(function, "name", ""),
                    "arguments": getattr(function, "arguments", "{}"),
                },
            }
        )
    return tool_calls


def _load_tool_arguments(raw_arguments: str) -> dict[str, Any]:
    try:
        parsed = json.loads(raw_arguments)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Tool arguments were not valid JSON: {exc}") from exc
    if not isinstance(parsed, dict):
        raise ValueError("Tool arguments must decode to a JSON object.")
    return parsed
