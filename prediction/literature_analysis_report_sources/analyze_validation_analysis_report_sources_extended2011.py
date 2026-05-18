from __future__ import annotations

import json
import sys
from pathlib import Path

ANALYSIS_ROOT = Path(__file__).resolve().parents[1]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from literature_analysis_report_sources import (  # noqa: E402
    analyze_validation_analysis_report_sources as base_analysis,
)


ROOT = ANALYSIS_ROOT.parent
OPENAI_BATCH_OUTPUT = ROOT / "openAI_batch_output"
RESULTS_DIR = ROOT / "results" / "validation" / "literature_analysis_report_sources_extended2011"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_analysis_report_sources_extended2011"

PGG_MS_ID = "PGG_MS_202502"

MERGE_SPECS = [
    {
        "model": "GPT-4.1",
        "mode": "joint_reasoning",
        "strict_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_strict243_joint_41.jsonl",
        "remaining_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_broad_remaining1769_joint_41.jsonl",
        "merged_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_41.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_positive_case_variations_41.jsonl",
        "baseline_variation": "baseline_joint_reasoning",
    },
    {
        "model": "GPT-4.1 Mini",
        "mode": "joint_reasoning",
        "strict_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_strict243_joint_41mini.jsonl",
        "remaining_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_broad_remaining1769_joint_41mini.jsonl",
        "merged_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_41mini.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41mini.jsonl",
        "baseline_variation": "baseline_joint_reasoning",
    },
    {
        "model": "GPT-4.1 Nano",
        "mode": "joint_reasoning",
        "strict_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_strict243_joint_41nano.jsonl",
        "remaining_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_broad_remaining1769_joint_41nano.jsonl",
        "merged_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_41nano.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41nano.jsonl",
        "baseline_variation": "baseline_joint_reasoning",
    },
]


def extract_source_id_from_custom_id(custom_id: str) -> str:
    return custom_id.rsplit("/", 1)[-1].strip()


def merge_output_jsonls(strict_path: Path, remaining_path: Path, merged_path: Path) -> tuple[int, int]:
    merged_path.parent.mkdir(parents=True, exist_ok=True)
    kept = 0
    skipped = 0
    seen_sources: set[str] = set()

    with merged_path.open("w", encoding="utf-8") as out_handle:
        for path in (strict_path, remaining_path):
            with path.open(encoding="utf-8") as in_handle:
                for line in in_handle:
                    item = json.loads(line)
                    custom_id = str(item.get("custom_id", "")).strip()
                    if not custom_id:
                        skipped += 1
                        continue
                    source_id = extract_source_id_from_custom_id(custom_id)
                    if not source_id or source_id == PGG_MS_ID or source_id in seen_sources:
                        skipped += 1
                        continue
                    seen_sources.add(source_id)
                    out_handle.write(json.dumps(item, ensure_ascii=False) + "\n")
                    kept += 1

    return kept, skipped


def main() -> None:
    merged_counts: list[dict[str, object]] = []
    run_specs: list[dict[str, object]] = []

    for spec in MERGE_SPECS:
        if not spec["strict_path"].exists() or not spec["remaining_path"].exists():
            continue
        kept, skipped = merge_output_jsonls(
            spec["strict_path"],
            spec["remaining_path"],
            spec["merged_path"],
        )
        merged_counts.append(
            {
                "model": spec["model"],
                "mode": spec["mode"],
                "merged_path": str(spec["merged_path"]),
                "kept_rows": kept,
                "skipped_rows": skipped,
            }
        )
        run_specs.append(
            {
                "model": spec["model"],
                "mode": spec["mode"],
                "output_path": spec["merged_path"],
                "baseline_path": spec["baseline_path"],
                "baseline_variation": spec["baseline_variation"],
            }
        )

    if not run_specs:
        raise FileNotFoundError("No paired strict/remaining output files were found to merge.")

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    base_analysis.RESULTS_DIR = RESULTS_DIR
    base_analysis.PLOTS_DIR = PLOTS_DIR
    base_analysis.RUN_SPECS = run_specs

    treatment, control = base_analysis.load_truth()
    metadata = base_analysis.load_metadata()
    rows = base_analysis.build_rows(treatment, control, metadata)
    if rows.empty:
        raise FileNotFoundError("Merged extended analysis produced no rows.")

    summary = base_analysis.summarize(rows)
    top_bottom = base_analysis.build_top_bottom(rows, k=15)
    context = base_analysis.build_context_table(rows)
    delta_summary = base_analysis.build_delta_summary(rows)

    rows_path = RESULTS_DIR / "validation_literature_analysis_report_source_rows.csv"
    summary_path = RESULTS_DIR / "validation_literature_analysis_report_source_summary.csv"
    top_bottom_path = RESULTS_DIR / "validation_literature_analysis_report_source_top_bottom.csv"
    context_path = RESULTS_DIR / "validation_literature_analysis_report_source_context.csv"
    delta_summary_path = RESULTS_DIR / "validation_literature_analysis_report_source_delta_summary.csv"
    merge_summary_path = RESULTS_DIR / "validation_literature_analysis_report_source_merge_summary.json"

    rows.to_csv(rows_path, index=False)
    summary.to_csv(summary_path, index=False)
    top_bottom.to_csv(top_bottom_path, index=False)
    context.to_csv(context_path, index=False)
    delta_summary.to_csv(delta_summary_path, index=False)
    merge_summary_path.write_text(json.dumps(merged_counts, indent=2), encoding="utf-8")

    base_analysis.plot_distributions(rows)
    base_analysis.plot_context_dumbbells(rows)
    base_analysis.plot_delta_summary_forest(delta_summary)

    print(rows_path)
    print(summary_path)
    print(top_bottom_path)
    print(context_path)
    print(delta_summary_path)
    print(merge_summary_path)
    print(PLOTS_DIR / "validation_literature_analysis_report_source_delta_distributions.png")
    print(PLOTS_DIR / "validation_literature_analysis_report_source_dumbbells.png")
    print(PLOTS_DIR / "validation_literature_analysis_report_source_delta_forest.png")


if __name__ == "__main__":
    main()
