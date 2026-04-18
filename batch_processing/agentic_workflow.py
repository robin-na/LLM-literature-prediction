from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

try:
    from batch_processing.agentic_tools import (
        SUPPORTED_AGENTIC_FIELDS,
        build_tool_specs,
        execute_tool,
        needs_review_gate,
        parse_json_object,
        validate_field_output,
    )
    from batch_processing.build_field_extractors import FIELD_CONFIGS, build_user_prompt
except ImportError:  # pragma: no cover - allows direct script execution
    from agentic_tools import (  # type: ignore
        SUPPORTED_AGENTIC_FIELDS,
        build_tool_specs,
        execute_tool,
        needs_review_gate,
        parse_json_object,
        validate_field_output,
    )
    from build_field_extractors import FIELD_CONFIGS, build_user_prompt  # type: ignore


EXTRACTOR_APPENDIX = """
You are the primary extraction agent.

Use tools when they can reduce extraction error:
- start with evidence_pack_builder to gather field-specific support,
- use condition_aligner if there may be multiple arms or conditions,
- use quote_finder to confirm exact text support,
- use calculator for arithmetic,
- use normalization_checker for DV normalization or efficiency formulas,
- use payoff_formula_parser for MPCR or efficiency ingredients,
- use field_rulebook for deterministic reminders,
- use validate_candidate_output before finalizing,
- use needs_review_gate if the candidate still looks uncertain.

Return only the final extraction JSON object for the selected field.
""".strip()

CRITIC_SYSTEM_PROMPT = """
You are a skeptical auditor reviewing a field extraction from a PGG paper.

Your job is to attack weak claims without inventing errors. Only raise an issue when
you can point to a concrete textual gap, quote mismatch, arithmetic mistake,
normalization mistake, or condition-mixing risk. If the extraction is well supported,
say so explicitly.

Use tools when needed, especially evidence_pack_builder, condition_aligner,
quote_finder, normalization_checker, and payoff_formula_parser.

Do not rewrite the extraction. Return only a structured attack report as JSON.
""".strip()

REVISION_APPENDIX = """
You are revising an existing field extraction after critique.

Only change a value when the critic provides a grounded objection backed by text or
arithmetic. If the attack report is ungrounded or weak, preserve the original answer.
Use tools if needed, especially evidence_pack_builder, condition_aligner,
normalization_checker, payoff_formula_parser, validate_candidate_output, and
needs_review_gate.

Return only the revised extraction JSON object.
""".strip()

VALIDATION_REPAIR_APPENDIX = """
Your previous extraction failed deterministic validation.

Repair only the schema or value issues listed below. Keep supported values intact.
Use tools if needed and validate your candidate JSON before finalizing. If the
candidate still looks dubious after repair, consult needs_review_gate.

Return only the repaired extraction JSON object.
""".strip()

V2_GLOBAL_MISMATCH_APPENDIX = """
V2 failure-aware extraction policy based on prior mismatch analysis:
- enumerate conditions before assigning row-level values; do not collapse, merge, or invent conditions,
- prefer the strategic interaction unit over the most salient human headcount in prose,
- use 0 only when the paper clearly supports that coding; reserve N/R for genuinely unsupported numeric values,
- for CONFIG_rewardExists and CONFIG_showRewardId: if the paper does not clearly state the fact, use N/A—do not treat silence or a vague "public goods game" as 0,
- do not guess unsupported values,
- do derive values when the paper provides enough grounded numeric ingredients,
- avoid partial-period or cherry-picked summaries unless the paper clearly defines them as the target outcome.
""".strip()

V2_FIELD_MISMATCH_NOTES = {
    "CONFIG_playerCount": """
High-risk failure mode: counting members per team or focal actors instead of strategic players.
- If teams act as the strategic units, count teams.
- If one representative acts for a team, count the interacting teams, not members per team.
- In third-party punishment or trust-game style interactions, count the players in the strategic interaction, not just the actor described in one sentence.
""".strip(),
    "CONFIG_allOrNothing": """
Check whether the contribution choice is continuous, binary, or absent. Do not confuse binary actions with a continuous contribution scale.
""".strip(),
    "CONFIG_MPCR": """
High-risk failure mode: dividing MPCR by group size again.
- MPCR is already the coefficient on the public-good term in the individual payoff function.
- If the paper says each player gets 0.4 times the sum of contributions, MPCR is 0.4, not 0.4 / group size.
- For heterogeneous MPCRs, preserve which players receive which coefficients.
""".strip(),
    "DV_contributionRate": """
High-risk failure mode: using the wrong period window.
- Do not use first-5-period or other subperiod summaries unless the paper treats that exact summary as the target condition outcome.
- Match the condition and aggregation window before normalizing.
""".strip(),
    "DV_efficiency": """
High-risk failure modes: overconservative abstention and unsupported derivation.
- If the paper gives grounded payoff or earnings ingredients, derive efficiency instead of defaulting to N/R.
- If grounded payoff ingredients are incomplete, abstain rather than estimating.
- Do not use partial-period earnings unless the target outcome is explicitly defined that way.
""".strip(),
    "DVs": """
High-risk failure modes:
- Listing identical DVs for all conditions when punishment only exists in some conditions.
- Omitting group_contribution when the paper reports group averages alongside individual contributions.
- Including independent variables (endowment, group_size, MPCR) in the DVs list.
- Using punishment_expenditure instead of punishment_assigned/received when the paper reports the latter.
""".strip(),
    "DVs_Definitions": """
High-risk failure modes:
- Using generic textbook definitions instead of paper-specific ones.
- Having keys that do not match the DVs list for this row.
- Omitting measurement units or normalization details that the paper specifies.
""".strip(),
    "DV_efficiencyReported": """
High-risk failure mode: coding 0 for a condition row just because efficiency is not that condition's
primary DV. This is a paper-level field — search all tables, figures, appendices, and sections.
If efficiency appears anywhere in the paper, code 1 for all rows.
""".strip(),
    "CONFIG_showNRounds": """
High-risk failure mode: coding 0 from silence or from rounds being fixed/known.
The ONLY valid values are 1 (explicit display statement) and N/A.
Fixed rounds ≠ displayed. Common knowledge ≠ display. Silence → N/A, never 0.
""".strip(),
    "CONFIG_showOtherSummaries": """
High-risk failure mode: coding 0 from silence when the paper does not mention whether
post-round feedback was shown. Use N/A for silence; 0 only when the paper explicitly
states that information about others was withheld.
""".strip(),
    "CONFIG_punishmentCost": "Risk: confusing punisher cost with target reduction. Report what the SENDER pays per unit, not what the target loses.",
    "CONFIG_punishmentTech": "Risk: confusing target reduction with punisher cost. Report how much the TARGET's payoff falls per unit of punishment received.",
    "CONFIG_showPunishmentId": "Risk: coding N/A instead of 0 when punishment exists but is anonymous. If punishment exists and is anonymous, code 0, not N/A.",
    "CONFIG_defaultContribProp": "Risk: coding N/A when the paper describes a standard VCM (default = 0). Absence of a special default means 0.",
    "CONFIG_chat": "Risk: coding 1 for structured/numeric messages. Only unrestricted free-form text qualifies as chat.",
}


@dataclass(frozen=True)
class V2FieldProfile:
    """Per-field compute budget and early-exit policy for agentic extraction v2."""

    extractor_use_tools: bool
    extractor_max_tool_rounds: int
    recovery_max_tool_rounds: int
    critic_max_tool_rounds: int
    repair_max_tool_rounds: int


V2_FIELD_PROFILES: dict[str, V2FieldProfile] = {
    "CONFIG_playerCount": V2FieldProfile(
        extractor_use_tools=False,
        extractor_max_tool_rounds=0,
        recovery_max_tool_rounds=10,
        critic_max_tool_rounds=8,
        repair_max_tool_rounds=6,
    ),
    "CONFIG_allOrNothing": V2FieldProfile(
        extractor_use_tools=False,
        extractor_max_tool_rounds=0,
        recovery_max_tool_rounds=10,
        critic_max_tool_rounds=8,
        repair_max_tool_rounds=6,
    ),
    "CONFIG_MPCR": V2FieldProfile(
        extractor_use_tools=True,
        extractor_max_tool_rounds=10,
        recovery_max_tool_rounds=12,
        critic_max_tool_rounds=10,
        repair_max_tool_rounds=8,
    ),
    "DV_contributionRate": V2FieldProfile(
        extractor_use_tools=True,
        extractor_max_tool_rounds=12,
        recovery_max_tool_rounds=12,
        critic_max_tool_rounds=10,
        repair_max_tool_rounds=8,
    ),
    "DV_efficiency": V2FieldProfile(
        extractor_use_tools=True,
        extractor_max_tool_rounds=12,
        recovery_max_tool_rounds=12,
        critic_max_tool_rounds=10,
        repair_max_tool_rounds=8,
    ),
    "DVs": V2FieldProfile(
        extractor_use_tools=False,
        extractor_max_tool_rounds=0,
        recovery_max_tool_rounds=4,
        critic_max_tool_rounds=4,
        repair_max_tool_rounds=4,
    ),
    "DVs_Definitions": V2FieldProfile(
        extractor_use_tools=False,
        extractor_max_tool_rounds=0,
        recovery_max_tool_rounds=4,
        critic_max_tool_rounds=4,
        repair_max_tool_rounds=4,
    ),
    "DV_efficiencyReported": V2FieldProfile(
        extractor_use_tools=False,
        extractor_max_tool_rounds=0,
        recovery_max_tool_rounds=4,
        critic_max_tool_rounds=4,
        repair_max_tool_rounds=4,
    ),
    "CONFIG_showNRounds": V2FieldProfile(
        extractor_use_tools=False,
        extractor_max_tool_rounds=0,
        recovery_max_tool_rounds=4,
        critic_max_tool_rounds=4,
        repair_max_tool_rounds=4,
    ),
    "CONFIG_showOtherSummaries": V2FieldProfile(
        extractor_use_tools=False,
        extractor_max_tool_rounds=0,
        recovery_max_tool_rounds=4,
        critic_max_tool_rounds=4,
        repair_max_tool_rounds=4,
    ),
    "CONFIG_punishmentCost": V2FieldProfile(
        extractor_use_tools=False,
        extractor_max_tool_rounds=0,
        recovery_max_tool_rounds=4,
        critic_max_tool_rounds=4,
        repair_max_tool_rounds=4,
    ),
    "CONFIG_punishmentTech": V2FieldProfile(
        extractor_use_tools=False,
        extractor_max_tool_rounds=0,
        recovery_max_tool_rounds=4,
        critic_max_tool_rounds=4,
        repair_max_tool_rounds=4,
    ),
    "CONFIG_showPunishmentId": V2FieldProfile(
        extractor_use_tools=False,
        extractor_max_tool_rounds=0,
        recovery_max_tool_rounds=4,
        critic_max_tool_rounds=4,
        repair_max_tool_rounds=4,
    ),
    "CONFIG_defaultContribProp": V2FieldProfile(
        extractor_use_tools=False,
        extractor_max_tool_rounds=0,
        recovery_max_tool_rounds=4,
        critic_max_tool_rounds=4,
        repair_max_tool_rounds=4,
    ),
    "CONFIG_chat": V2FieldProfile(
        extractor_use_tools=False,
        extractor_max_tool_rounds=0,
        recovery_max_tool_rounds=4,
        critic_max_tool_rounds=4,
        repair_max_tool_rounds=4,
    ),
}


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


def _v2_field_prompt(base_system_prompt: str, field: str, role_appendix: str) -> str:
    parts = [base_system_prompt, V2_GLOBAL_MISMATCH_APPENDIX]
    field_notes = V2_FIELD_MISMATCH_NOTES.get(field)
    if field_notes:
        parts.append(field_notes)
    parts.append(role_appendix)
    return "\n\n".join(parts)


def run_agentic_field_extraction(
    *,
    client: Any,
    field: str,
    paper_text: str,
    model: str,
    max_critic_rounds: int = 1,
    temperature: float = 0.0,
    max_tool_rounds: int = 8,
    progress_callback: Any | None = None,
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
        request_label=f"{field}:extractor",
        progress_callback=progress_callback,
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
            request_label=f"{field}:critic_round_{critic_index + 1}",
            progress_callback=progress_callback,
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
            request_label=f"{field}:revision_round_{critic_index + 1}",
            progress_callback=progress_callback,
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
            request_label=f"{field}:validation_repair",
            progress_callback=progress_callback,
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


def run_agentic_field_extraction_v2(
    *,
    client: Any,
    field: str,
    paper_text: str,
    model: str,
    max_critic_rounds: int = 1,
    temperature: float = 0.0,
    max_tool_rounds: int = 8,
    min_confidence: float = 0.85,
    progress_callback: Any | None = None,
) -> dict[str, Any]:
    if field not in SUPPORTED_AGENTIC_FIELDS:
        raise ValueError(
            f"Unsupported field '{field}'. Supported fields: {', '.join(SUPPORTED_AGENTIC_FIELDS)}"
        )

    profile = V2_FIELD_PROFILES[field]
    cfg = FIELD_CONFIGS[field]
    extractor_prompt = build_user_prompt(cfg, paper_text)

    def _cap(rounds: int) -> int:
        return max(0, min(rounds, max_tool_rounds))

    def _extract(
        *,
        use_tools: bool,
        tool_rounds: int,
        label: str,
    ) -> dict[str, Any]:
        return _run_json_agent(
            client=client,
            model=model,
            system_prompt=_v2_field_prompt(cfg["system_prompt"], field, EXTRACTOR_APPENDIX),
            user_prompt=extractor_prompt,
            paper_text=paper_text,
            temperature=temperature,
            max_tool_rounds=_cap(tool_rounds),
            request_label=f"{field}:{label}",
            progress_callback=progress_callback,
            enable_tools=use_tools,
        )

    def _validate_and_repair(draft: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any] | None]:
        validation = validate_field_output(field, draft["parsed"]).to_dict()
        if validation["ok"]:
            return draft, validation, None
        repaired = _run_json_agent(
            client=client,
            model=model,
            system_prompt=_v2_field_prompt(
                cfg["system_prompt"],
                field,
                VALIDATION_REPAIR_APPENDIX,
            ),
            user_prompt=_build_validation_repair_prompt(
                extractor_prompt=extractor_prompt,
                draft_text=draft["text"],
                validation=validation,
            ),
            paper_text=paper_text,
            temperature=temperature,
            max_tool_rounds=_cap(profile.repair_max_tool_rounds),
            request_label=f"{field}:validation_repair",
            progress_callback=progress_callback,
            enable_tools=True,
        )
        repaired_validation = validate_field_output(field, repaired["parsed"]).to_dict()
        return repaired, validation, repaired_validation

    def _finalize(
        *,
        current_draft: dict[str, Any],
        critique_rounds: list[dict[str, Any]],
        pre_repair_validation: dict[str, Any],
        post_repair_validation: dict[str, Any] | None,
        skipped_critic: bool,
    ) -> dict[str, Any]:
        final_validation = validate_field_output(field, current_draft["parsed"]).to_dict()
        gate = needs_review_gate(
            field=field,
            candidate_json=current_draft["text"],
            min_confidence=min_confidence,
            paper_text=paper_text,
        )
        if final_validation["ok"] and gate["decision"] == "auto_accept":
            pipeline_decision = "accept"
        elif not final_validation["ok"]:
            pipeline_decision = "abstain"
        else:
            pipeline_decision = "needs_review"

        return {
            "field": field,
            "model": model,
            "agentic_version": "v2",
            "pipeline_decision": pipeline_decision,
            "gate_result": gate,
            "skipped_critic": skipped_critic,
            "draft_output": current_draft["parsed"],
            "draft_text": current_draft["text"],
            "draft_trace": current_draft["trace"],
            "draft_response_id": current_draft["response_id"],
            "critic_rounds": critique_rounds,
            "validation": final_validation,
            "pre_repair_validation": pre_repair_validation,
            "post_repair_validation": post_repair_validation,
            "final_output": current_draft["parsed"],
        }

    critique_rounds: list[dict[str, Any]] = []
    skipped_critic = False

    use_tools = profile.extractor_use_tools
    ext_rounds = profile.extractor_max_tool_rounds if use_tools else 0
    current_draft = _extract(use_tools=use_tools, tool_rounds=ext_rounds, label="extractor_v2")
    current_draft, pre_val, post_val = _validate_and_repair(current_draft)

    if not profile.extractor_use_tools and (
        not validate_field_output(field, current_draft["parsed"]).to_dict()["ok"]
        or needs_review_gate(
            field=field,
            candidate_json=current_draft["text"],
            min_confidence=min_confidence,
            paper_text=paper_text,
        )["decision"]
        != "auto_accept"
    ):
        current_draft = _extract(
            use_tools=True,
            tool_rounds=_cap(profile.recovery_max_tool_rounds),
            label="extractor_v2_recovery",
        )
        current_draft, pre_val, post_val = _validate_and_repair(current_draft)

    critic_tool_cap = _cap(profile.critic_max_tool_rounds)
    for critic_index in range(max_critic_rounds):
        critic_report = _run_json_agent(
            client=client,
            model=model,
            system_prompt=(
                f"{CRITIC_SYSTEM_PROMPT}\n\n{V2_FIELD_MISMATCH_NOTES.get(field, '')}".strip()
            ),
            user_prompt=_build_critic_prompt(
                field=field,
                field_config=cfg,
                paper_text=paper_text,
                draft_text=current_draft["text"],
            ),
            paper_text=paper_text,
            temperature=temperature,
            max_tool_rounds=critic_tool_cap,
            request_label=f"{field}:critic_round_{critic_index + 1}",
            progress_callback=progress_callback,
            enable_tools=True,
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
            system_prompt=_v2_field_prompt(cfg["system_prompt"], field, REVISION_APPENDIX),
            user_prompt=_build_revision_prompt(
                extractor_prompt=extractor_prompt,
                draft_text=current_draft["text"],
                critique_text=critic_report["text"],
            ),
            paper_text=paper_text,
            temperature=temperature,
            max_tool_rounds=critic_tool_cap,
            request_label=f"{field}:revision_round_{critic_index + 1}",
            progress_callback=progress_callback,
            enable_tools=True,
        )
        critique_entry["revision_text"] = revised_draft["text"]
        critique_entry["revision_json"] = revised_draft["parsed"]
        critique_entry["revision_trace"] = revised_draft["trace"]
        critique_entry["revision_response_id"] = revised_draft["response_id"]
        current_draft = revised_draft

    current_draft, pre_val, post_val = _validate_and_repair(current_draft)
    return _finalize(
        current_draft=current_draft,
        critique_rounds=critique_rounds,
        pre_repair_validation=pre_val,
        post_repair_validation=post_val,
        skipped_critic=False,
    )


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
    request_label: str,
    progress_callback: Any | None,
    enable_tools: bool = True,
) -> dict[str, Any]:
    messages: list[dict[str, Any]] = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    trace: list[dict[str, Any]] = []
    tools = build_tool_specs() if enable_tools else None

    for _ in range(max_tool_rounds + 1):
        if progress_callback is not None:
            progress_callback(
                {
                    "label": request_label,
                    "messages": messages,
                    "model": model,
                }
            )
        completion_kwargs: dict[str, Any] = {
            "model": model,
            "temperature": temperature,
            "response_format": {"type": "json_object"},
            "messages": messages,
        }
        if tools is not None:
            completion_kwargs["tools"] = tools
            completion_kwargs["tool_choice"] = "auto"
        response = client.chat.completions.create(**completion_kwargs)
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
