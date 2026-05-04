from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path

try:
    from batch_inputs.paper_only_variants import MODEL_TAGS as OPENAI_MODEL_TAGS
except ModuleNotFoundError:
    import sys

    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    if str(PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(PROJECT_ROOT))
    from batch_inputs.paper_only_variants import MODEL_TAGS as OPENAI_MODEL_TAGS


DEFAULT_SOURCE_JSONL = Path("openAI_batch_input/prediction_literature_joint_suite_reps1to5_gpt51.jsonl")

OPENAI_MODELS = [
    "gpt-4.1",
    "gpt-4.1-mini",
    "gpt-4.1-nano",
    "gpt-5.1",
    "gpt-5-mini",
    "gpt-5-nano",
]
GEMINI_MODELS = ["gemini-2.5-flash", "gemini-2.5-pro"]
CLAUDE_MODELS = ["claude-opus-4-6", "claude-sonnet-4-6", "claude-haiku-4-5"]

GEMINI_MODEL_TAGS = {
    "gemini-2.5-flash": "gemini25flash",
    "gemini-2.5-pro": "gemini25pro",
}
CLAUDE_MODEL_TAGS = {
    "claude-opus-4-6": "opus46",
    "claude-sonnet-4-6": "sonnet46",
    "claude-haiku-4-5": "haiku45",
}

SCIENCE_REPORTS = [
    (
        "PGG_Science_gpt41",
        Path("literature/output/paper_analysis_reports/pgg_science_card41/paper_set_single/PGG_Science.md"),
    ),
    (
        "PGG_Science_gpt51",
        Path("literature/output/paper_analysis_reports/pgg_science_cardgpt51/paper_set_single/PGG_Science.md"),
    ),
]

DEFAULT_OPENAI_OUTPUT_DIR = Path("openAI_batch_input")
DEFAULT_GEMINI_OUTPUT_DIR = Path("gemini_batch_input")
DEFAULT_CLAUDE_OUTPUT_DIR = Path("claude_batch_input")
DEFAULT_MANIFEST_DIR = Path("literature/output/batch_input_manifests")

DEFAULT_OPENAI_PREFIX = "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint"
DEFAULT_GEMINI_PREFIX = "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint"
DEFAULT_CLAUDE_PREFIX = (
    "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_reasoning_anthropic_merged"
)
DEFAULT_CLAUDE_COMBINED_SUFFIX = "allmodels"

DEFAULT_SEED_BASE = 20260329
DEFAULT_BASELINE_START_REP = 6
DEFAULT_TOTAL_REPS = 30
DEFAULT_GEMINI_TEMPERATURE = 1.0
DEFAULT_CLAUDE_TEMPERATURE = 1.0
DEFAULT_CLAUDE_MAX_TOKENS = 32768

BASELINE_SOURCE_ID = "baseline_joint_reasoning_rep1"
BENCHMARK_SOURCE_ID = "paper_analysis_report_joint_rep1/PGG_MS_202502"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build incremental literature prediction batch inputs for OpenAI, Gemini, "
            "and Claude: baseline reps 6-30 plus 30 repeats each for the two new "
            "PGG_Science report variants."
        )
    )
    parser.add_argument("--source-jsonl", type=Path, default=DEFAULT_SOURCE_JSONL)
    parser.add_argument("--openai-output-dir", type=Path, default=DEFAULT_OPENAI_OUTPUT_DIR)
    parser.add_argument("--gemini-output-dir", type=Path, default=DEFAULT_GEMINI_OUTPUT_DIR)
    parser.add_argument("--claude-output-dir", type=Path, default=DEFAULT_CLAUDE_OUTPUT_DIR)
    parser.add_argument("--manifest-dir", type=Path, default=DEFAULT_MANIFEST_DIR)
    parser.add_argument("--openai-prefix", default=DEFAULT_OPENAI_PREFIX)
    parser.add_argument("--gemini-prefix", default=DEFAULT_GEMINI_PREFIX)
    parser.add_argument("--claude-prefix", default=DEFAULT_CLAUDE_PREFIX)
    parser.add_argument("--seed-base", type=int, default=DEFAULT_SEED_BASE)
    parser.add_argument("--baseline-start-rep", type=int, default=DEFAULT_BASELINE_START_REP)
    parser.add_argument("--total-reps", type=int, default=DEFAULT_TOTAL_REPS)
    parser.add_argument("--gemini-temperature", type=float, default=DEFAULT_GEMINI_TEMPERATURE)
    parser.add_argument("--claude-temperature", type=float, default=DEFAULT_CLAUDE_TEMPERATURE)
    parser.add_argument("--claude-max-tokens", type=int, default=DEFAULT_CLAUDE_MAX_TOKENS)
    return parser.parse_args()


def _openai_tag(model: str) -> str:
    return OPENAI_MODEL_TAGS.get(model, "".join(ch for ch in model.lower() if ch.isalnum()))


def _gemini_tag(model: str) -> str:
    return GEMINI_MODEL_TAGS[model]


def _claude_tag(model: str) -> str:
    return CLAUDE_MODEL_TAGS[model]


def _load_source_templates(path: Path) -> tuple[dict, dict]:
    baseline_item = None
    benchmark_item = None
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            custom_id = str(item.get("custom_id", "")).strip()
            if custom_id == BASELINE_SOURCE_ID:
                baseline_item = item
            elif custom_id == BENCHMARK_SOURCE_ID:
                benchmark_item = item
            if baseline_item and benchmark_item:
                break
    if baseline_item is None or benchmark_item is None:
        raise FileNotFoundError(
            f"Could not find {BASELINE_SOURCE_ID!r} and {BENCHMARK_SOURCE_ID!r} in {path}"
        )
    return baseline_item, benchmark_item


def _extract_text_pair(item: dict) -> tuple[str, str]:
    messages = item["body"]["messages"]
    system_text = next(msg["content"] for msg in messages if msg["role"] == "system")
    user_text = next(msg["content"] for msg in messages if msg["role"] == "user")
    return system_text, user_text


def _extract_benchmark_prompt_parts(benchmark_user_text: str) -> tuple[str, str]:
    match = re.search(
        r"^(.*?----------Analysis Report Starts----------\n\n)(.*?)(\n\n----------Analysis Report Ends----------\n.*)$",
        benchmark_user_text,
        re.S,
    )
    if not match:
        raise ValueError("Could not split benchmark prompt into report wrapper and suffix.")
    return match.group(1), match.group(3)


def _seed_for_rep(seed_base: int, rep_idx: int) -> int:
    return seed_base + rep_idx - 1


def _baseline_custom_id(rep_idx: int) -> str:
    return f"baseline_joint_reasoning_rep{rep_idx}"


def _science_custom_id(rep_idx: int, variant_id: str) -> str:
    return f"paper_analysis_report_joint_rep{rep_idx}/{variant_id}"


def _build_science_user_prompt(report_prefix: str, report_suffix: str, report_text: str) -> str:
    return f"{report_prefix}{report_text.strip()}{report_suffix}"


def _clone_openai_request(
    source_item: dict,
    *,
    custom_id: str,
    model: str,
    user_text: str,
    seed: int,
) -> dict:
    item = copy.deepcopy(source_item)
    item["custom_id"] = custom_id
    item["body"]["model"] = model
    item["body"]["messages"][1]["content"] = user_text
    item["body"]["seed"] = seed
    return item


def _sanitize_custom_id(custom_id: str) -> str:
    safe = re.sub(r"[^a-zA-Z0-9_-]", "_", custom_id)
    if len(safe) <= 64:
        return safe
    head, _, tail = safe.rpartition("_")
    if not tail:
        return safe[:64]
    max_head_len = max(1, 64 - len(tail) - 1)
    return f"{head[:max_head_len]}_{tail}"


def _merged_claude_custom_id(custom_id: str, model: str) -> str:
    return _sanitize_custom_id(f"{custom_id}__{_claude_tag(model)}")


def _build_gemini_record(
    *,
    custom_id: str,
    model: str,
    system_text: str,
    user_text: str,
    temperature: float,
    seed: int,
) -> dict:
    return {
        "key": custom_id,
        "request": {
            "system_instruction": {"parts": [{"text": system_text}]},
            "contents": [{"role": "user", "parts": [{"text": user_text}]}],
            "generation_config": {
                "response_mime_type": "application/json",
                "temperature": temperature,
                "seed": seed,
            },
            "model": model,
        },
    }


def _build_claude_record(
    *,
    custom_id: str,
    model: str,
    system_text: str,
    user_text: str,
    max_tokens: int,
    temperature: float,
) -> dict:
    return {
        "custom_id": _merged_claude_custom_id(custom_id, model),
        "params": {
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "system": [{"type": "text", "text": system_text}],
            "messages": [{"role": "user", "content": [{"type": "text", "text": user_text}]}],
        },
    }


def _write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _build_openai_files(
    *,
    baseline_source: dict,
    benchmark_source: dict,
    benchmark_prefix: str,
    benchmark_suffix: str,
    openai_output_dir: Path,
    output_prefix: str,
    baseline_user_text: str,
    science_reports: list[tuple[str, str]],
    seed_base: int,
    baseline_start_rep: int,
    total_reps: int,
) -> list[dict[str, object]]:
    outputs: list[dict[str, object]] = []
    for model in OPENAI_MODELS:
        records: list[dict] = []
        for rep_idx in range(baseline_start_rep, total_reps + 1):
            records.append(
                _clone_openai_request(
                    baseline_source,
                    custom_id=_baseline_custom_id(rep_idx),
                    model=model,
                    user_text=baseline_user_text,
                    seed=_seed_for_rep(seed_base, rep_idx),
                )
            )
        for variant_id, report_text in science_reports:
            user_text = _build_science_user_prompt(benchmark_prefix, benchmark_suffix, report_text)
            for rep_idx in range(1, total_reps + 1):
                records.append(
                    _clone_openai_request(
                        benchmark_source,
                        custom_id=_science_custom_id(rep_idx, variant_id),
                        model=model,
                        user_text=user_text,
                        seed=_seed_for_rep(seed_base, rep_idx),
                    )
                )
        output_path = openai_output_dir / f"{output_prefix}_{_openai_tag(model)}.jsonl"
        _write_jsonl(output_path, records)
        outputs.append({"provider": "openai", "model": model, "path": str(output_path), "request_count": len(records)})
    return outputs


def _build_gemini_files(
    *,
    system_text: str,
    baseline_user_text: str,
    benchmark_prefix: str,
    benchmark_suffix: str,
    science_reports: list[tuple[str, str]],
    gemini_output_dir: Path,
    output_prefix: str,
    seed_base: int,
    baseline_start_rep: int,
    total_reps: int,
    temperature: float,
) -> list[dict[str, object]]:
    outputs: list[dict[str, object]] = []
    for model in GEMINI_MODELS:
        records: list[dict] = []
        for rep_idx in range(baseline_start_rep, total_reps + 1):
            records.append(
                _build_gemini_record(
                    custom_id=_baseline_custom_id(rep_idx),
                    model=model,
                    system_text=system_text,
                    user_text=baseline_user_text,
                    temperature=temperature,
                    seed=_seed_for_rep(seed_base, rep_idx),
                )
            )
        for variant_id, report_text in science_reports:
            user_text = _build_science_user_prompt(benchmark_prefix, benchmark_suffix, report_text)
            for rep_idx in range(1, total_reps + 1):
                records.append(
                    _build_gemini_record(
                        custom_id=_science_custom_id(rep_idx, variant_id),
                        model=model,
                        system_text=system_text,
                        user_text=user_text,
                        temperature=temperature,
                        seed=_seed_for_rep(seed_base, rep_idx),
                    )
                )
        output_path = gemini_output_dir / f"{output_prefix}_{_gemini_tag(model)}.jsonl"
        _write_jsonl(output_path, records)
        outputs.append({"provider": "gemini", "model": model, "path": str(output_path), "request_count": len(records)})
    return outputs


def _build_claude_file(
    *,
    system_text: str,
    baseline_user_text: str,
    benchmark_prefix: str,
    benchmark_suffix: str,
    science_reports: list[tuple[str, str]],
    claude_output_dir: Path,
    output_prefix: str,
    baseline_start_rep: int,
    total_reps: int,
    max_tokens: int,
    temperature: float,
) -> dict[str, object]:
    requests: list[dict] = []
    for model in CLAUDE_MODELS:
        for rep_idx in range(baseline_start_rep, total_reps + 1):
            requests.append(
                _build_claude_record(
                    custom_id=_baseline_custom_id(rep_idx),
                    model=model,
                    system_text=system_text,
                    user_text=baseline_user_text,
                    max_tokens=max_tokens,
                    temperature=temperature,
                )
            )
        for variant_id, report_text in science_reports:
            user_text = _build_science_user_prompt(benchmark_prefix, benchmark_suffix, report_text)
            for rep_idx in range(1, total_reps + 1):
                requests.append(
                    _build_claude_record(
                        custom_id=_science_custom_id(rep_idx, variant_id),
                        model=model,
                        system_text=system_text,
                        user_text=user_text,
                        max_tokens=max_tokens,
                        temperature=temperature,
                    )
                )

    output_path = claude_output_dir / f"{output_prefix}_{DEFAULT_CLAUDE_COMBINED_SUFFIX}.json"
    _write_json(output_path, {"requests": requests})
    return {"provider": "claude", "model": "allmodels", "path": str(output_path), "request_count": len(requests)}


def _write_seed_manifest(
    *,
    manifest_dir: Path,
    outputs: list[dict[str, object]],
    seed_base: int,
    baseline_start_rep: int,
    total_reps: int,
) -> Path:
    manifest_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = manifest_dir / "prediction_literature_incremental_baseline_pgg_science_seed_manifest.json"
    payload = {
        "seed_formula_openai_gemini": f"seed = {seed_base} + repeat_index - 1",
        "baseline_incremental_repeats": {
            "repeat_start": baseline_start_rep,
            "repeat_end": total_reps,
            "seed_start": _seed_for_rep(seed_base, baseline_start_rep),
            "seed_end": _seed_for_rep(seed_base, total_reps),
        },
        "new_pgg_science_variants": {
            "repeat_start": 1,
            "repeat_end": total_reps,
            "seed_start": _seed_for_rep(seed_base, 1),
            "seed_end": _seed_for_rep(seed_base, total_reps),
            "variant_ids": [variant_id for variant_id, _ in SCIENCE_REPORTS],
        },
        "claude_seed_note": (
            "Anthropic batch payloads in this repo keep repeat indices in custom_id but do not include "
            "a provider-supported seed field. Claude requests therefore track repeat identity without "
            "a deterministic API seed."
        ),
        "files": outputs,
    }
    _write_json(manifest_path, payload)
    return manifest_path


def main() -> None:
    args = parse_args()
    baseline_source, benchmark_source = _load_source_templates(args.source_jsonl)
    system_text, baseline_user_text = _extract_text_pair(baseline_source)
    _, benchmark_user_text = _extract_text_pair(benchmark_source)
    benchmark_prefix, benchmark_suffix = _extract_benchmark_prompt_parts(benchmark_user_text)
    science_reports = [(variant_id, path.read_text(encoding="utf-8")) for variant_id, path in SCIENCE_REPORTS]

    outputs: list[dict[str, object]] = []
    outputs.extend(
        _build_openai_files(
            baseline_source=baseline_source,
            benchmark_source=benchmark_source,
            benchmark_prefix=benchmark_prefix,
            benchmark_suffix=benchmark_suffix,
            openai_output_dir=args.openai_output_dir,
            output_prefix=args.openai_prefix,
            baseline_user_text=baseline_user_text,
            science_reports=science_reports,
            seed_base=args.seed_base,
            baseline_start_rep=args.baseline_start_rep,
            total_reps=args.total_reps,
        )
    )
    outputs.extend(
        _build_gemini_files(
            system_text=system_text,
            baseline_user_text=baseline_user_text,
            benchmark_prefix=benchmark_prefix,
            benchmark_suffix=benchmark_suffix,
            science_reports=science_reports,
            gemini_output_dir=args.gemini_output_dir,
            output_prefix=args.gemini_prefix,
            seed_base=args.seed_base,
            baseline_start_rep=args.baseline_start_rep,
            total_reps=args.total_reps,
            temperature=args.gemini_temperature,
        )
    )
    outputs.append(
        _build_claude_file(
            system_text=system_text,
            baseline_user_text=baseline_user_text,
            benchmark_prefix=benchmark_prefix,
            benchmark_suffix=benchmark_suffix,
            science_reports=science_reports,
            claude_output_dir=args.claude_output_dir,
            output_prefix=args.claude_prefix,
            baseline_start_rep=args.baseline_start_rep,
            total_reps=args.total_reps,
            max_tokens=args.claude_max_tokens,
            temperature=args.claude_temperature,
        )
    )

    manifest_path = _write_seed_manifest(
        manifest_dir=args.manifest_dir,
        outputs=outputs,
        seed_base=args.seed_base,
        baseline_start_rep=args.baseline_start_rep,
        total_reps=args.total_reps,
    )

    for output in outputs:
        print(f"Wrote {output['request_count']} requests to {output['path']}")
    print(f"Wrote seed manifest to {manifest_path}")


if __name__ == "__main__":
    main()
