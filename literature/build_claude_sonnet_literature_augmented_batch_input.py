from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
import re
import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from batch_inputs.paper_only_variants import build_joint_prompt, build_joint_system_prompt


DEFAULT_DF_PGG = Path("input/pgg_CONFIGmerged_validation.csv")
DEFAULT_OUTPUT_DIR = Path("claude_batch_input")
DEFAULT_OUTPUT_PATH = Path(
    "claude_batch_input/prediction_literature_papers2011-collections717_joint_reps1to5_reasoning_anthropic_sonnet46_cached.json"
)
DEFAULT_MANIFEST_OUT = Path(
    "literature/output/batch_input_manifests/prediction_literature_claude_sonnet_augmented_repeat5_cached_manifest.json"
)

DEFAULT_MODEL = "claude-sonnet-4-6"
DEFAULT_MAX_TOKENS = 32768
DEFAULT_TEMPERATURE = 1.0
DEFAULT_N_REPEATS = 5

DEFAULT_PAPER_SET_CSV = Path(
    "literature/output/evidence_cards/literature_evidence_cards_cleaned/collection_switch_sets/sets/broad_all.csv"
)
DEFAULT_PAPER_REPORT_INDEX = Path("literature/output/paper_analysis_reports/broad_all/report_index.csv")
DEFAULT_COLLECTION_REPORT_INDEX = Path("literature/output/collection_analysis_reports/metadata_filters/report_index.csv")
DEFAULT_ALL_PAPERS_COLLECTION_ID = "broad_all_2011"
DEFAULT_ALL_PAPERS_COLLECTION_REPORT = Path(
    "literature/output/collection_analysis_reports/switch_sets_stage1/broad_all_2011.md"
)

PAPER_MEMO_WRAPPER = """Below is an analysis report distilled from one academic paper.
Use it as contextual evidence about how design features may change the efficiency impact of punishment.
Respect the report's stated limitations and do not infer beyond what the report supports."""

COLLECTION_REPORT_WRAPPER = """Below is an analysis report synthesized from multiple academic papers.
Use it as contextual evidence about how design features may change the efficiency impact of punishment.
Respect the report's stated limitations and do not infer beyond what the report supports."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build a Claude Sonnet 4.6 Message Batches payload for the large literature augmentation families "
            "(2011 single-paper reports + 717 collection reports including broad_all_2011), with prompt "
            "caching enabled."
        )
    )
    parser.add_argument("--df-pgg", type=Path, default=DEFAULT_DF_PGG)
    parser.add_argument("--paper-set-csv", type=Path, default=DEFAULT_PAPER_SET_CSV)
    parser.add_argument("--paper-report-index", type=Path, default=DEFAULT_PAPER_REPORT_INDEX)
    parser.add_argument("--collection-report-index", type=Path, default=DEFAULT_COLLECTION_REPORT_INDEX)
    parser.add_argument("--all-papers-collection-id", default=DEFAULT_ALL_PAPERS_COLLECTION_ID)
    parser.add_argument("--all-papers-collection-report", type=Path, default=DEFAULT_ALL_PAPERS_COLLECTION_REPORT)
    parser.add_argument("--model", default=DEFAULT_MODEL, choices=[DEFAULT_MODEL])
    parser.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    parser.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE)
    parser.add_argument("--n-repeats", type=int, default=DEFAULT_N_REPEATS)
    parser.add_argument(
        "--paper-sample-frac",
        type=float,
        help="Optional fraction of paper reports to sample deterministically from the full 2011-paper set.",
    )
    parser.add_argument(
        "--paper-sample-count",
        type=int,
        help="Optional absolute count of paper reports to sample deterministically.",
    )
    parser.add_argument(
        "--paper-sample-seed",
        type=int,
        default=20260409,
        help="Random seed for deterministic paper sampling.",
    )
    parser.add_argument(
        "--skip-collections",
        action="store_true",
        help="If set, build only the single-paper report requests.",
    )
    parser.add_argument(
        "--skip-papers",
        action="store_true",
        help="If set, build only the collection-report requests.",
    )
    parser.add_argument(
        "--cache-ttl",
        choices=["default", "1h", "none"],
        default="default",
        help="Prompt caching TTL. 'default' means Anthropic's default 5-minute ephemeral cache.",
    )
    parser.add_argument("--output-path", type=Path, default=DEFAULT_OUTPUT_PATH)
    parser.add_argument("--manifest-out", type=Path, default=DEFAULT_MANIFEST_OUT)
    return parser.parse_args()


def _load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _load_report_index_map(path: Path, *, id_field: str) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for row in _load_csv_rows(path):
        item_id = (row.get(id_field) or "").strip()
        report_path = (row.get("report_path") or "").strip()
        if item_id and report_path:
            mapping[item_id] = report_path
    if not mapping:
        raise ValueError(f"No usable {id_field}/report_path rows found in {path}")
    return mapping


def _load_paper_entries(paper_set_csv: Path, paper_report_index: Path) -> list[tuple[str, str]]:
    paper_order = [(row.get("custom_id") or "").strip() for row in _load_csv_rows(paper_set_csv)]
    paper_order = [paper_id for paper_id in paper_order if paper_id]
    if not paper_order:
        raise ValueError(f"No custom_id rows found in {paper_set_csv}")
    report_map = _load_report_index_map(paper_report_index, id_field="custom_id")
    missing = [paper_id for paper_id in paper_order if paper_id not in report_map]
    if missing:
        raise KeyError(f"Missing {len(missing)} paper reports; example ids: {missing[:5]}")
    return [(paper_id, report_map[paper_id]) for paper_id in paper_order]


def _load_collection_entries(
    collection_report_index: Path,
    *,
    all_papers_collection_id: str | None,
    all_papers_collection_report: Path | None,
) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    seen: set[str] = set()
    for row in _load_csv_rows(collection_report_index):
        variant_id = (row.get("variant_id") or "").strip()
        report_path = (row.get("report_path") or "").strip()
        if variant_id and report_path and variant_id not in seen:
            entries.append((variant_id, report_path))
            seen.add(variant_id)
    if all_papers_collection_id and all_papers_collection_report and all_papers_collection_id not in seen:
        entries.append((all_papers_collection_id, str(all_papers_collection_report)))
        seen.add(all_papers_collection_id)
    if not entries:
        raise ValueError(f"No usable collection entries found in {collection_report_index}")
    return entries


def _read_report_text(report_path: str) -> str:
    path = ROOT / report_path
    if not path.exists():
        raise FileNotFoundError(f"Report file not found: {path}")
    return path.read_text(encoding="utf-8").strip()


def _wrap_report(wrapper: str, report_text: str, prompt_text: str) -> str:
    return (
        f"{wrapper}\n"
        "----------Analysis Report Starts----------\n\n"
        f"{report_text}\n\n"
        "----------Analysis Report Ends----------\n"
        f"{prompt_text}"
    )


def _sanitize_with_hash(custom_id: str) -> str:
    safe = re.sub(r"[^a-zA-Z0-9_-]", "_", custom_id)
    if len(safe) <= 64:
        return safe
    digest = hashlib.sha1(custom_id.encode("utf-8")).hexdigest()[:8]
    suffix = f"___h{digest}"
    max_head_len = 64 - len(suffix)
    return f"{safe[:max_head_len]}{suffix}"


def _cache_control(ttl_mode: str) -> dict[str, str] | None:
    if ttl_mode == "none":
        return None
    if ttl_mode == "1h":
        return {"type": "ephemeral", "ttl": "1h"}
    return {"type": "ephemeral"}


def _sample_entries(
    entries: list[tuple[str, str]],
    *,
    sample_frac: float | None,
    sample_count: int | None,
    sample_seed: int,
) -> list[tuple[str, str]]:
    if sample_frac is None and sample_count is None:
        return entries
    if sample_frac is not None and not (0 < sample_frac <= 1):
        raise ValueError("--paper-sample-frac must be in (0, 1].")
    if sample_count is not None and sample_count <= 0:
        raise ValueError("--paper-sample-count must be positive.")

    target_count = sample_count
    if target_count is None and sample_frac is not None:
        target_count = max(1, math.ceil(len(entries) * sample_frac))
    assert target_count is not None
    if target_count >= len(entries):
        return entries

    rng = random.Random(sample_seed)
    selected_indices = set(rng.sample(range(len(entries)), target_count))
    return [entry for idx, entry in enumerate(entries) if idx in selected_indices]


def _build_request(
    *,
    custom_id: str,
    model: str,
    system_text: str,
    user_text: str,
    max_tokens: int,
    temperature: float,
    cache_control: dict[str, str] | None,
) -> dict[str, object]:
    system_block: dict[str, object] = {"type": "text", "text": system_text}
    if cache_control is not None:
        system_block["cache_control"] = dict(cache_control)

    user_block: dict[str, object] = {"type": "text", "text": user_text}
    if cache_control is not None:
        user_block["cache_control"] = dict(cache_control)

    params: dict[str, object] = {
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "system": [system_block],
        "messages": [{"role": "user", "content": [user_block]}],
    }
    return {
        "custom_id": _sanitize_with_hash(custom_id),
        "params": params,
    }


def _build_paper_requests(
    *,
    paper_entries: list[tuple[str, str]],
    model: str,
    system_text: str,
    prompt_text: str,
    max_tokens: int,
    temperature: float,
    n_repeats: int,
    cache_control: dict[str, str] | None,
) -> list[dict[str, object]]:
    requests: list[dict[str, object]] = []
    for paper_id, report_path in paper_entries:
        report_text = _read_report_text(report_path)
        user_text = _wrap_report(PAPER_MEMO_WRAPPER, report_text, prompt_text)
        for rep_idx in range(1, n_repeats + 1):
            requests.append(
                _build_request(
                    custom_id=f"paper_analysis_report_joint_rep{rep_idx}/{paper_id}",
                    model=model,
                    system_text=system_text,
                    user_text=user_text,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    cache_control=cache_control,
                )
            )
    return requests


def _build_collection_requests(
    *,
    collection_entries: list[tuple[str, str]],
    model: str,
    system_text: str,
    prompt_text: str,
    max_tokens: int,
    temperature: float,
    n_repeats: int,
    cache_control: dict[str, str] | None,
) -> list[dict[str, object]]:
    requests: list[dict[str, object]] = []
    for variant_id, report_path in collection_entries:
        report_text = _read_report_text(report_path)
        user_text = _wrap_report(COLLECTION_REPORT_WRAPPER, report_text, prompt_text)
        for rep_idx in range(1, n_repeats + 1):
            requests.append(
                _build_request(
                    custom_id=f"collection_analysis_report_joint_rep{rep_idx}/{variant_id}",
                    model=model,
                    system_text=system_text,
                    user_text=user_text,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    cache_control=cache_control,
                )
            )
    return requests


def _write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()

    df = pd.read_csv(args.df_pgg).sort_values("CONFIG_configId").reset_index(drop=True)
    system_text = build_joint_system_prompt(include_explanation=True)
    prompt_text = build_joint_prompt(df, include_explanation=True)

    paper_entries = _load_paper_entries(args.paper_set_csv, args.paper_report_index)
    paper_entries = _sample_entries(
        paper_entries,
        sample_frac=args.paper_sample_frac,
        sample_count=args.paper_sample_count,
        sample_seed=args.paper_sample_seed,
    )
    collection_entries = _load_collection_entries(
        args.collection_report_index,
        all_papers_collection_id=(args.all_papers_collection_id or "").strip() or None,
        all_papers_collection_report=args.all_papers_collection_report,
    )
    if args.skip_papers:
        paper_entries = []
    if args.skip_collections:
        collection_entries = []
    cache_control = _cache_control(args.cache_ttl)

    requests = []
    requests.extend(
        _build_paper_requests(
            paper_entries=paper_entries,
            model=args.model,
            system_text=system_text,
            prompt_text=prompt_text,
            max_tokens=args.max_tokens,
            temperature=args.temperature,
            n_repeats=args.n_repeats,
            cache_control=cache_control,
        )
    )
    requests.extend(
        _build_collection_requests(
            collection_entries=collection_entries,
            model=args.model,
            system_text=system_text,
            prompt_text=prompt_text,
            max_tokens=args.max_tokens,
            temperature=args.temperature,
            n_repeats=args.n_repeats,
            cache_control=cache_control,
        )
    )

    custom_ids = [request["custom_id"] for request in requests]
    if len(custom_ids) != len(set(custom_ids)):
        raise ValueError("Duplicate custom_id values detected after hashing/sanitization.")

    payload = {"requests": requests}
    _write_json(args.output_path, payload)
    print(f"Wrote {len(requests)} requests to {args.output_path}")

    manifest = {
        "output_path": str(args.output_path),
        "model": args.model,
        "max_tokens": args.max_tokens,
        "temperature": args.temperature,
        "cache_ttl_mode": args.cache_ttl,
        "cache_control": cache_control,
        "cache_breakpoint_strategy": [
            "system_text",
            "single_user_block",
        ],
        "n_repeats": args.n_repeats,
        "paper_sample_frac": args.paper_sample_frac,
        "paper_sample_count": args.paper_sample_count,
        "paper_sample_seed": args.paper_sample_seed,
        "skip_papers": args.skip_papers,
        "skip_collections": args.skip_collections,
        "n_paper_reports": len(paper_entries),
        "n_collection_reports": len(collection_entries),
        "paper_request_count": len(paper_entries) * args.n_repeats,
        "collection_request_count": len(collection_entries) * args.n_repeats,
        "total_request_count": len(requests),
        "all_papers_collection_id": args.all_papers_collection_id,
        "all_papers_collection_report": str(args.all_papers_collection_report),
        "seed_note": "Anthropic Message Batches do not expose a request seed field; repeats are tracked by rep index only.",
    }
    _write_json(args.manifest_out, manifest)
    print(f"Wrote manifest to {args.manifest_out}")


if __name__ == "__main__":
    main()
