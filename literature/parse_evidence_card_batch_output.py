from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


DEFAULT_OUTPUT_ROOT = Path("literature/output/evidence_cards")
TARGET_DIMENSIONS = [
    "player_count",
    "num_rounds",
    "chat",
    "all_or_nothing",
    "default_contrib",
    "mpcr",
    "punishment_cost",
    "punishment_tech",
    "reward_exists",
    "reward_cost",
    "reward_tech",
    "show_n_rounds",
    "show_other_summaries",
    "show_punishment_id",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Parse OpenAI batch-output JSONL for literature evidence-card extraction "
            "into flat CSV tables."
        )
    )
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Path to the OpenAI batch output JSONL.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help=(
            "Directory for parsed CSV outputs. Defaults to "
            "literature/output/evidence_cards/<input-stem>/"
        ),
    )
    return parser.parse_args()


def normalize_paper_id(custom_id: str) -> str:
    return custom_id.removesuffix(".md")


def join_str_list(values: Any) -> str:
    if not isinstance(values, list):
        return ""
    parts: list[str] = []
    for value in values:
        if value is None:
            continue
        text = str(value).strip()
        if text:
            parts.append(text)
    return " | ".join(parts)


def serialize_key_claims(values: Any) -> str:
    if not isinstance(values, list):
        return ""
    parts: list[str] = []
    for item in values:
        if not isinstance(item, dict):
            continue
        claim = str(item.get("claim", "")).strip()
        support_level = str(item.get("support_level", "")).strip()
        support_refs = join_str_list(item.get("support_refs"))
        segment = claim
        if support_level:
            segment = f"{segment} [support={support_level}]"
        if support_refs:
            segment = f"{segment} [refs={support_refs}]"
        if segment.strip():
            parts.append(segment.strip())
    return " || ".join(parts)


def extract_response_text(record: dict[str, Any]) -> tuple[str | None, dict[str, str]]:
    response = record.get("response") or {}
    body = response.get("body") or {}
    meta = {
        "status_code": str(response.get("status_code", "")),
        "request_id": str(response.get("request_id", "")),
        "model": str(body.get("model", "")),
        "api_error_message": "",
    }

    if response.get("status_code") != 200:
        error = body.get("error") or record.get("error") or {}
        if isinstance(error, dict):
            meta["api_error_message"] = str(error.get("message", "")).strip()
        else:
            meta["api_error_message"] = str(error).strip()
        return None, meta

    if body.get("object") == "chat.completion":
        choices = body.get("choices") or []
        if choices:
            message = choices[0].get("message") or {}
            content = message.get("content")
            if isinstance(content, str):
                return content, meta
        return None, meta

    if body.get("object") == "response":
        outputs = body.get("output") or []
        text_parts: list[str] = []
        for output in outputs:
            if output.get("type") != "message":
                continue
            for item in output.get("content") or []:
                if item.get("type") == "output_text":
                    text = item.get("text")
                    if isinstance(text, str) and text.strip():
                        text_parts.append(text)
        return ("\n".join(text_parts) if text_parts else None), meta

    return None, meta


def parse_json_content(text: str) -> dict[str, Any]:
    candidate = text.strip()
    if not candidate:
        raise ValueError("empty assistant content")

    try:
        parsed = json.loads(candidate)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        pass

    if candidate.startswith("```"):
        first_newline = candidate.find("\n")
        last_fence = candidate.rfind("```")
        if first_newline != -1 and last_fence != -1 and last_fence > first_newline:
            inner = candidate[first_newline + 1 : last_fence].strip()
            parsed = json.loads(inner)
            if isinstance(parsed, dict):
                return parsed

    start = candidate.find("{")
    end = candidate.rfind("}")
    if start != -1 and end != -1 and end > start:
        parsed = json.loads(candidate[start : end + 1])
        if isinstance(parsed, dict):
            return parsed

    raise ValueError("assistant content is not a JSON object")


def count_dimensions_with_tier(dimensions: dict[str, Any], tiers: set[str]) -> int:
    count = 0
    for payload in dimensions.values():
        if not isinstance(payload, dict):
            continue
        if str(payload.get("evidence_tier", "")).strip() in tiers:
            count += 1
    return count


def build_paper_row(
    *,
    custom_id: str,
    meta: dict[str, str],
    payload: dict[str, Any] | None,
    parse_status: str,
    parse_error: str,
) -> dict[str, Any]:
    paper_id = normalize_paper_id(custom_id)
    target_relevance = payload.get("target_relevance") if isinstance(payload, dict) else {}
    outcomes_reported = payload.get("outcomes_reported") if isinstance(payload, dict) else {}
    dimensions = payload.get("dimensions") if isinstance(payload, dict) else {}
    key_claims = payload.get("key_claims") if isinstance(payload, dict) else []
    limitations = payload.get("important_limitations") if isinstance(payload, dict) else []

    return {
        "custom_id": custom_id,
        "paper_id": paper_id,
        "status_code": meta["status_code"],
        "request_id": meta["request_id"],
        "model": meta["model"],
        "parse_status": parse_status,
        "api_error_message": meta["api_error_message"],
        "parse_error": parse_error,
        "paper_type_primary": payload.get("paper_type_primary", "") if isinstance(payload, dict) else "",
        "paper_type_empirical": payload.get("paper_type_empirical", "") if isinstance(payload, dict) else "",
        "paper_type_experimental": payload.get("paper_type_experimental", "") if isinstance(payload, dict) else "",
        "relevance_pgg_or_variant": target_relevance.get("pgg_or_variant", "") if isinstance(target_relevance, dict) else "",
        "relevance_punishment_or_sanctions": target_relevance.get("punishment_or_sanctions", "") if isinstance(target_relevance, dict) else "",
        "relevance_efficiency_or_related_payoff_outcome": target_relevance.get("efficiency_or_related_payoff_outcome", "") if isinstance(target_relevance, dict) else "",
        "outcomes_primary_outcome_type": outcomes_reported.get("primary_outcome_type", "") if isinstance(outcomes_reported, dict) else "",
        "outcomes_payoff_related_outcomes": join_str_list(outcomes_reported.get("payoff_related_outcomes")) if isinstance(outcomes_reported, dict) else "",
        "outcomes_non_payoff_outcomes": join_str_list(outcomes_reported.get("non_payoff_outcomes")) if isinstance(outcomes_reported, dict) else "",
        "outcomes_notes": outcomes_reported.get("notes", "") if isinstance(outcomes_reported, dict) else "",
        "overall_effect_direction_on_efficiency_or_related_payoff": (
            payload.get("overall_effect_direction_on_efficiency_or_related_payoff", "")
            if isinstance(payload, dict)
            else ""
        ),
        "overall_summary": payload.get("overall_summary", "") if isinstance(payload, dict) else "",
        "paper_findings": payload.get("paper_findings", "") if isinstance(payload, dict) else "",
        "decision_support": payload.get("decision_support", "") if isinstance(payload, dict) else "",
        "dimension_count": len(dimensions) if isinstance(dimensions, dict) else 0,
        "dimension_contextual_or_better_count": (
            count_dimensions_with_tier(dimensions, {"contextual", "informative_indirect", "informative_direct"})
            if isinstance(dimensions, dict)
            else 0
        ),
        "dimension_informative_direct_count": (
            count_dimensions_with_tier(dimensions, {"informative_direct"})
            if isinstance(dimensions, dict)
            else 0
        ),
        "key_claim_count": len(key_claims) if isinstance(key_claims, list) else 0,
        "important_limitation_count": len(limitations) if isinstance(limitations, list) else 0,
    }


def build_dimension_rows(custom_id: str, payload: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    dimensions = payload.get("dimensions") or {}
    if not isinstance(dimensions, dict):
        return rows

    paper_id = normalize_paper_id(custom_id)
    for dimension_name, dimension_payload in dimensions.items():
        if not isinstance(dimension_payload, dict):
            dimension_payload = {}
        rows.append(
            {
                "custom_id": custom_id,
                "paper_id": paper_id,
                "dimension": dimension_name,
                "present": dimension_payload.get("present", ""),
                "evidence_tier": dimension_payload.get("evidence_tier", ""),
                "effect_direction": dimension_payload.get("effect_direction", ""),
                "evidence_basis": dimension_payload.get("evidence_basis", ""),
                "notes": dimension_payload.get("notes", ""),
                "support_refs": join_str_list(dimension_payload.get("support_refs")),
            }
        )
    return rows


def build_key_claim_rows(custom_id: str, payload: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    key_claims = payload.get("key_claims") or []
    if not isinstance(key_claims, list):
        return rows

    paper_id = normalize_paper_id(custom_id)
    for idx, claim_payload in enumerate(key_claims, start=1):
        if not isinstance(claim_payload, dict):
            claim_payload = {}
        rows.append(
            {
                "custom_id": custom_id,
                "paper_id": paper_id,
                "claim_index": idx,
                "claim": claim_payload.get("claim", ""),
                "support_level": claim_payload.get("support_level", ""),
                "support_refs": join_str_list(claim_payload.get("support_refs")),
            }
        )
    return rows


def build_limitation_rows(custom_id: str, payload: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    limitations = payload.get("important_limitations") or []
    if not isinstance(limitations, list):
        return rows

    paper_id = normalize_paper_id(custom_id)
    for idx, limitation in enumerate(limitations, start=1):
        rows.append(
            {
                "custom_id": custom_id,
                "paper_id": paper_id,
                "limitation_index": idx,
                "limitation": str(limitation),
            }
        )
    return rows


def build_error_row(
    *,
    custom_id: str,
    meta: dict[str, str],
    parse_status: str,
    parse_error: str,
    raw_text: str | None,
) -> dict[str, Any]:
    return {
        "custom_id": custom_id,
        "paper_id": normalize_paper_id(custom_id),
        "status_code": meta["status_code"],
        "request_id": meta["request_id"],
        "model": meta["model"],
        "parse_status": parse_status,
        "api_error_message": meta["api_error_message"],
        "parse_error": parse_error,
        "raw_response_text": raw_text or "",
    }


def combined_fieldnames() -> list[str]:
    base_fields = [
        "custom_id",
        "paper_id",
        "status_code",
        "request_id",
        "model",
        "parse_status",
        "api_error_message",
        "parse_error",
        "paper_type_primary",
        "paper_type_empirical",
        "paper_type_experimental",
        "relevance_pgg_or_variant",
        "relevance_punishment_or_sanctions",
        "relevance_efficiency_or_related_payoff_outcome",
        "outcomes_primary_outcome_type",
        "outcomes_payoff_related_outcomes",
        "outcomes_non_payoff_outcomes",
        "outcomes_notes",
        "overall_effect_direction_on_efficiency_or_related_payoff",
        "overall_summary",
        "paper_findings",
        "decision_support",
        "dimension_count",
        "dimension_contextual_or_better_count",
        "dimension_informative_direct_count",
        "key_claim_count",
        "important_limitation_count",
        "key_claims_joined",
        "important_limitations_joined",
    ]
    dimension_fields: list[str] = []
    for dimension in TARGET_DIMENSIONS:
        prefix = f"dim_{dimension}"
        dimension_fields.extend(
            [
                f"{prefix}_present",
                f"{prefix}_evidence_tier",
                f"{prefix}_effect_direction",
                f"{prefix}_evidence_basis",
                f"{prefix}_notes",
                f"{prefix}_support_refs",
            ]
        )
    return base_fields + dimension_fields


def build_combined_row(
    *,
    custom_id: str,
    paper_row: dict[str, Any],
    payload: dict[str, Any] | None,
) -> dict[str, Any]:
    row = dict(paper_row)
    row["key_claims_joined"] = ""
    row["important_limitations_joined"] = ""
    for dimension in TARGET_DIMENSIONS:
        prefix = f"dim_{dimension}"
        row[f"{prefix}_present"] = ""
        row[f"{prefix}_evidence_tier"] = ""
        row[f"{prefix}_effect_direction"] = ""
        row[f"{prefix}_evidence_basis"] = ""
        row[f"{prefix}_notes"] = ""
        row[f"{prefix}_support_refs"] = ""

    if not isinstance(payload, dict):
        return row

    row["key_claims_joined"] = serialize_key_claims(payload.get("key_claims"))
    row["important_limitations_joined"] = join_str_list(payload.get("important_limitations"))

    dimensions = payload.get("dimensions") or {}
    if not isinstance(dimensions, dict):
        return row

    for dimension in TARGET_DIMENSIONS:
        payload_item = dimensions.get(dimension)
        if not isinstance(payload_item, dict):
            continue
        prefix = f"dim_{dimension}"
        row[f"{prefix}_present"] = payload_item.get("present", "")
        row[f"{prefix}_evidence_tier"] = payload_item.get("evidence_tier", "")
        row[f"{prefix}_effect_direction"] = payload_item.get("effect_direction", "")
        row[f"{prefix}_evidence_basis"] = payload_item.get("evidence_basis", "")
        row[f"{prefix}_notes"] = payload_item.get("notes", "")
        row[f"{prefix}_support_refs"] = join_str_list(payload_item.get("support_refs"))

    return row


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> None:
    args = parse_args()
    input_path = args.input
    if not input_path.exists():
        raise FileNotFoundError(f"Batch output not found: {input_path}")

    output_dir = args.output_dir or (DEFAULT_OUTPUT_ROOT / input_path.stem)
    output_dir.mkdir(parents=True, exist_ok=True)

    paper_rows: list[dict[str, Any]] = []
    combined_rows: list[dict[str, Any]] = []
    dimension_rows: list[dict[str, Any]] = []
    key_claim_rows: list[dict[str, Any]] = []
    limitation_rows: list[dict[str, Any]] = []
    error_rows: list[dict[str, Any]] = []

    n_records = 0
    n_ok = 0
    n_api_errors = 0
    n_json_parse_errors = 0

    with input_path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            n_records += 1
            record = json.loads(line)
            custom_id = str(record.get("custom_id", "")).strip()
            text, meta = extract_response_text(record)

            if text is None:
                n_api_errors += 1
                paper_row = build_paper_row(
                    custom_id=custom_id,
                    meta=meta,
                    payload=None,
                    parse_status="api_error",
                    parse_error="",
                )
                paper_rows.append(paper_row)
                combined_rows.append(
                    build_combined_row(
                        custom_id=custom_id,
                        paper_row=paper_row,
                        payload=None,
                    )
                )
                error_rows.append(
                    build_error_row(
                        custom_id=custom_id,
                        meta=meta,
                        parse_status="api_error",
                        parse_error="",
                        raw_text=None,
                    )
                )
                continue

            try:
                payload = parse_json_content(text)
            except Exception as exc:
                n_json_parse_errors += 1
                parse_error = repr(exc)
                paper_row = build_paper_row(
                    custom_id=custom_id,
                    meta=meta,
                    payload=None,
                    parse_status="json_parse_error",
                    parse_error=parse_error,
                )
                paper_rows.append(paper_row)
                combined_rows.append(
                    build_combined_row(
                        custom_id=custom_id,
                        paper_row=paper_row,
                        payload=None,
                    )
                )
                error_rows.append(
                    build_error_row(
                        custom_id=custom_id,
                        meta=meta,
                        parse_status="json_parse_error",
                        parse_error=parse_error,
                        raw_text=text,
                    )
                )
                continue

            n_ok += 1
            paper_row = build_paper_row(
                custom_id=custom_id,
                meta=meta,
                payload=payload,
                parse_status="ok",
                parse_error="",
            )
            paper_rows.append(paper_row)
            combined_rows.append(
                build_combined_row(
                    custom_id=custom_id,
                    paper_row=paper_row,
                    payload=payload,
                )
            )
            dimension_rows.extend(build_dimension_rows(custom_id, payload))
            key_claim_rows.extend(build_key_claim_rows(custom_id, payload))
            limitation_rows.extend(build_limitation_rows(custom_id, payload))

    write_csv(
        output_dir / "papers.csv",
        paper_rows,
        [
            "custom_id",
            "paper_id",
            "status_code",
            "request_id",
            "model",
            "parse_status",
            "api_error_message",
            "parse_error",
            "paper_type_primary",
            "paper_type_empirical",
            "paper_type_experimental",
            "relevance_pgg_or_variant",
            "relevance_punishment_or_sanctions",
            "relevance_efficiency_or_related_payoff_outcome",
            "outcomes_primary_outcome_type",
            "outcomes_payoff_related_outcomes",
            "outcomes_non_payoff_outcomes",
            "outcomes_notes",
            "overall_effect_direction_on_efficiency_or_related_payoff",
            "overall_summary",
            "paper_findings",
            "decision_support",
            "dimension_count",
            "dimension_contextual_or_better_count",
            "dimension_informative_direct_count",
            "key_claim_count",
            "important_limitation_count",
        ],
    )
    write_csv(
        output_dir / "combined.csv",
        combined_rows,
        combined_fieldnames(),
    )
    write_csv(
        output_dir / "dimensions.csv",
        dimension_rows,
        [
            "custom_id",
            "paper_id",
            "dimension",
            "present",
            "evidence_tier",
            "effect_direction",
            "evidence_basis",
            "notes",
            "support_refs",
        ],
    )
    write_csv(
        output_dir / "key_claims.csv",
        key_claim_rows,
        [
            "custom_id",
            "paper_id",
            "claim_index",
            "claim",
            "support_level",
            "support_refs",
        ],
    )
    write_csv(
        output_dir / "important_limitations.csv",
        limitation_rows,
        [
            "custom_id",
            "paper_id",
            "limitation_index",
            "limitation",
        ],
    )
    write_csv(
        output_dir / "errors.csv",
        error_rows,
        [
            "custom_id",
            "paper_id",
            "status_code",
            "request_id",
            "model",
            "parse_status",
            "api_error_message",
            "parse_error",
            "raw_response_text",
        ],
    )

    summary = {
        "input_path": str(input_path),
        "output_dir": str(output_dir),
        "n_records": n_records,
        "n_ok": n_ok,
        "n_api_errors": n_api_errors,
        "n_json_parse_errors": n_json_parse_errors,
        "papers_csv": str(output_dir / "papers.csv"),
        "combined_csv": str(output_dir / "combined.csv"),
        "dimensions_csv": str(output_dir / "dimensions.csv"),
        "key_claims_csv": str(output_dir / "key_claims.csv"),
        "important_limitations_csv": str(output_dir / "important_limitations.csv"),
        "errors_csv": str(output_dir / "errors.csv"),
    }
    (output_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Parsed {n_records} batch rows from {input_path}")
    print(f"Wrote paper table to {output_dir / 'papers.csv'}")
    print(f"Wrote combined table to {output_dir / 'combined.csv'}")
    print(f"Wrote dimension table to {output_dir / 'dimensions.csv'}")
    print(f"Wrote key-claim table to {output_dir / 'key_claims.csv'}")
    print(f"Wrote limitation table to {output_dir / 'important_limitations.csv'}")
    print(f"Wrote error table to {output_dir / 'errors.csv'}")
    print(f"Wrote summary to {output_dir / 'summary.json'}")


if __name__ == "__main__":
    main()
