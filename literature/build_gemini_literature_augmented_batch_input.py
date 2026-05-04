from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from batch_inputs.paper_only_variants import build_joint_prompt, build_joint_system_prompt

DEFAULT_DF_PGG = Path("input/pgg_CONFIGmerged_validation.csv")
DEFAULT_OUTPUT_DIR = Path("gemini_batch_input")
DEFAULT_MODELS = ["gemini-2.5-flash", "gemini-2.5-pro"]
DEFAULT_SEED_BASE = 20260329
DEFAULT_TEMPERATURE = 1.0

DEFAULT_PAPER_SET_CSV = Path(
    "literature/output/evidence_cards/literature_evidence_cards_cleaned/collection_switch_sets/sets/broad_all.csv"
)
DEFAULT_PAPER_REPORT_INDEX = Path("literature/output/paper_analysis_reports/broad_all/report_index.csv")
DEFAULT_COLLECTION_REPORT_INDEX = Path("literature/output/collection_analysis_reports/metadata_filters/report_index.csv")
DEFAULT_ALL_PAPERS_COLLECTION_ID = "broad_all_2011"
DEFAULT_ALL_PAPERS_COLLECTION_REPORT = Path(
    "literature/output/collection_analysis_reports/switch_sets_stage1/broad_all_2011.md"
)
DEFAULT_MANIFEST_PATH = Path(
    "literature/output/batch_input_manifests/prediction_literature_gemini_augmented_repeat5_manifest.json"
)

PAPER_OUTPUT_PREFIX = "prediction_literature_analysis_report_extended2011_joint_reps1to5"
COLLECTION_OUTPUT_PREFIX = "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5"

MODEL_TAGS = {
    "gemini-2.5-flash": "gemini25flash",
    "gemini-2.5-pro": "gemini25pro",
}

PAPER_MEMO_WRAPPER = """Below is an analysis report distilled from one academic paper.
Use it as contextual evidence about how design features may change the efficiency impact of punishment.
Respect the report's stated limitations and do not infer beyond what the report supports."""

COLLECTION_REPORT_WRAPPER = """Below is an analysis report synthesized from multiple academic papers.
Use it as contextual evidence about how design features may change the efficiency impact of punishment.
Respect the report's stated limitations and do not infer beyond what the report supports."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build Gemini batch JSONLs for the large literature augmentation families used in the GPT runs: "
            "2011 individual paper analysis reports and metadata-filter collection analysis reports, each "
            "repeated 5 times with deterministic seeds."
        )
    )
    parser.add_argument(
        "--df-pgg",
        type=Path,
        default=DEFAULT_DF_PGG,
        help="Validation target CSV used to build the 20-question joint prediction prompt.",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=DEFAULT_MODELS,
        choices=DEFAULT_MODELS,
        help="Gemini models to generate JSONLs for.",
    )
    parser.add_argument(
        "--paper-set-csv",
        type=Path,
        default=DEFAULT_PAPER_SET_CSV,
        help="Paper-id list for the extended2011 run. Order from this file is preserved.",
    )
    parser.add_argument(
        "--paper-report-index",
        type=Path,
        default=DEFAULT_PAPER_REPORT_INDEX,
        help="Report index CSV for the rendered single-paper analysis reports.",
    )
    parser.add_argument(
        "--collection-report-index",
        type=Path,
        default=DEFAULT_COLLECTION_REPORT_INDEX,
        help="Report index CSV for the rendered collection analysis reports.",
    )
    parser.add_argument(
        "--all-papers-collection-id",
        default=DEFAULT_ALL_PAPERS_COLLECTION_ID,
        help="Variant id to use for the all-papers collection report.",
    )
    parser.add_argument(
        "--all-papers-collection-report",
        type=Path,
        default=DEFAULT_ALL_PAPERS_COLLECTION_REPORT,
        help="Markdown report path for the all-papers collection report to append if missing.",
    )
    parser.add_argument(
        "--n-repeats",
        type=int,
        default=5,
        help="Number of repeated runs per source report. Default: 5.",
    )
    parser.add_argument(
        "--seed-base",
        type=int,
        default=DEFAULT_SEED_BASE,
        help=(
            "Deterministic seed base. Repeat k uses seed (seed_base + k - 1). "
            "Use a negative value to omit seeds."
        ),
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=DEFAULT_TEMPERATURE,
        help="Gemini sampling temperature.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for the output Gemini JSONLs.",
    )
    parser.add_argument(
        "--manifest-out",
        type=Path,
        default=DEFAULT_MANIFEST_PATH,
        help="Optional JSON manifest summarizing counts and seed mapping.",
    )
    return parser.parse_args()


def _model_tag(model: str) -> str:
    return MODEL_TAGS[model]


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


def _load_paper_report_entries(paper_set_csv: Path, paper_report_index: Path) -> list[tuple[str, str]]:
    paper_order = [(row.get("custom_id") or "").strip() for row in _load_csv_rows(paper_set_csv)]
    paper_order = [paper_id for paper_id in paper_order if paper_id]
    if not paper_order:
        raise ValueError(f"No custom_id rows found in {paper_set_csv}")

    report_map = _load_report_index_map(paper_report_index, id_field="custom_id")
    missing = [paper_id for paper_id in paper_order if paper_id not in report_map]
    if missing:
        raise KeyError(
            f"Missing {len(missing)} paper reports from {paper_report_index}; example ids: {missing[:5]}"
        )

    return [(paper_id, report_map[paper_id]) for paper_id in paper_order]


def _load_collection_report_entries(
    collection_report_index: Path,
    *,
    all_papers_collection_id: str | None,
    all_papers_collection_report: Path | None,
) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    seen_ids: set[str] = set()
    for row in _load_csv_rows(collection_report_index):
        variant_id = (row.get("variant_id") or "").strip()
        report_path = (row.get("report_path") or "").strip()
        if variant_id and report_path and variant_id not in seen_ids:
            entries.append((variant_id, report_path))
            seen_ids.add(variant_id)

    if all_papers_collection_id and all_papers_collection_report:
        report_path = str(all_papers_collection_report)
        if all_papers_collection_id not in seen_ids:
            entries.append((all_papers_collection_id, report_path))
            seen_ids.add(all_papers_collection_id)

    if not entries:
        raise ValueError(f"No variant_id/report_path rows found in {collection_report_index}")
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


def _generation_config(*, temperature: float, seed_base: int | None, rep_idx: int) -> dict[str, object]:
    config: dict[str, object] = {
        "response_mime_type": "application/json",
        "temperature": temperature,
    }
    if seed_base is not None:
        config["seed"] = seed_base + rep_idx - 1
    return config


def _build_record(
    *,
    key: str,
    model: str,
    system_text: str,
    user_text: str,
    temperature: float,
    seed_base: int | None,
    rep_idx: int,
) -> dict[str, object]:
    return {
        "key": key,
        "request": {
            "system_instruction": {"parts": [{"text": system_text}]},
            "contents": [{"role": "user", "parts": [{"text": user_text}]}],
            "generation_config": _generation_config(
                temperature=temperature,
                seed_base=seed_base,
                rep_idx=rep_idx,
            ),
            "model": model,
        },
    }


def _build_paper_records(
    *,
    entries: list[tuple[str, str]],
    model: str,
    system_text: str,
    prompt_text: str,
    temperature: float,
    seed_base: int | None,
    n_repeats: int,
) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for paper_id, report_path in entries:
        report_text = _read_report_text(report_path)
        user_text = _wrap_report(PAPER_MEMO_WRAPPER, report_text, prompt_text)
        for rep_idx in range(1, n_repeats + 1):
            records.append(
                _build_record(
                    key=f"paper_analysis_report_joint_rep{rep_idx}/{paper_id}",
                    model=model,
                    system_text=system_text,
                    user_text=user_text,
                    temperature=temperature,
                    seed_base=seed_base,
                    rep_idx=rep_idx,
                )
            )
    return records


def _build_collection_records(
    *,
    entries: list[tuple[str, str]],
    model: str,
    system_text: str,
    prompt_text: str,
    temperature: float,
    seed_base: int | None,
    n_repeats: int,
) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for variant_id, report_path in entries:
        report_text = _read_report_text(report_path)
        user_text = _wrap_report(COLLECTION_REPORT_WRAPPER, report_text, prompt_text)
        for rep_idx in range(1, n_repeats + 1):
            records.append(
                _build_record(
                    key=f"collection_analysis_report_joint_rep{rep_idx}/{variant_id}",
                    model=model,
                    system_text=system_text,
                    user_text=user_text,
                    temperature=temperature,
                    seed_base=seed_base,
                    rep_idx=rep_idx,
                )
            )
    return records


def _write_jsonl(path: Path, records: list[dict[str, object]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return len(records)


def _write_manifest(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    seed_base = None if args.seed_base < 0 else args.seed_base

    df = pd.read_csv(args.df_pgg).sort_values("CONFIG_configId").reset_index(drop=True)
    system_text = build_joint_system_prompt(include_explanation=True)
    prompt_text = build_joint_prompt(df, include_explanation=True)

    paper_entries = _load_paper_report_entries(args.paper_set_csv, args.paper_report_index)
    collection_entries = _load_collection_report_entries(
        args.collection_report_index,
        all_papers_collection_id=(args.all_papers_collection_id or "").strip() or None,
        all_papers_collection_report=args.all_papers_collection_report,
    )

    manifest: dict[str, object] = {
        "paper_set_csv": str(args.paper_set_csv),
        "paper_report_index": str(args.paper_report_index),
        "collection_report_index": str(args.collection_report_index),
        "all_papers_collection_id": args.all_papers_collection_id,
        "all_papers_collection_report": str(args.all_papers_collection_report),
        "n_paper_reports": len(paper_entries),
        "n_collection_reports": len(collection_entries),
        "n_repeats": args.n_repeats,
        "temperature": args.temperature,
        "seed_base": seed_base,
        "repeat_seed_map": (
            {f"rep{rep_idx}": seed_base + rep_idx - 1 for rep_idx in range(1, args.n_repeats + 1)}
            if seed_base is not None
            else {}
        ),
        "paper_output_prefix": PAPER_OUTPUT_PREFIX,
        "collection_output_prefix": COLLECTION_OUTPUT_PREFIX,
        "models": {},
    }

    for model in args.models:
        paper_records = _build_paper_records(
            entries=paper_entries,
            model=model,
            system_text=system_text,
            prompt_text=prompt_text,
            temperature=args.temperature,
            seed_base=seed_base,
            n_repeats=args.n_repeats,
        )
        collection_records = _build_collection_records(
            entries=collection_entries,
            model=model,
            system_text=system_text,
            prompt_text=prompt_text,
            temperature=args.temperature,
            seed_base=seed_base,
            n_repeats=args.n_repeats,
        )

        paper_output = args.output_dir / f"{PAPER_OUTPUT_PREFIX}_{_model_tag(model)}.jsonl"
        collection_output = args.output_dir / f"{COLLECTION_OUTPUT_PREFIX}_{_model_tag(model)}.jsonl"

        paper_count = _write_jsonl(paper_output, paper_records)
        collection_count = _write_jsonl(collection_output, collection_records)

        manifest["models"][model] = {
            "paper_output": str(paper_output),
            "paper_request_count": paper_count,
            "collection_output": str(collection_output),
            "collection_request_count": collection_count,
        }

        print(f"Wrote {paper_count} requests to {paper_output}")
        print(f"Wrote {collection_count} requests to {collection_output}")

    if args.manifest_out:
        _write_manifest(args.manifest_out, manifest)
        print(f"Wrote manifest to {args.manifest_out}")


if __name__ == "__main__":
    main()
