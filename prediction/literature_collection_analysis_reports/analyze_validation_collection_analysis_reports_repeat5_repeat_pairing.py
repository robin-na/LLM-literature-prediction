from __future__ import annotations

from itertools import permutations
from pathlib import Path
import sys

import numpy as np
import pandas as pd


ANALYSIS_ROOT = Path(__file__).resolve().parents[1]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from literature_collection_analysis_reports.analyze_validation_collection_analysis_reports_repeat5 import (  # noqa: E402
    Q_COLS,
    RUN_SPECS,
    _all_paths_exist,
    _baseline_ids,
    _benchmark_ids,
    _collection_ids,
    _full_benchmark_ids,
    _load_source_tables,
    compute_metrics,
    load_learning_treatment_mean,
    load_truth,
    load_variant_metadata,
)


ROOT = ANALYSIS_ROOT.parent
RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_repeat5_repeat_pairing"
MODEL_ORDER = ["GPT-4.1", "GPT-4.1 Mini", "GPT-5.1", "GPT-5 Mini"]
METRICS = ["correlation", "rmse", "r2"]


def load_repeat_level_rows() -> pd.DataFrame:
    metadata = load_variant_metadata()
    treatment, control = load_truth()
    learning_mean = load_learning_treatment_mean()
    rows: list[dict[str, object]] = []

    for spec in RUN_SPECS:
        model = str(spec["model"])
        if model not in MODEL_ORDER or not _all_paths_exist(spec):
            continue

        baseline_df, collection_df, benchmark_df, full_benchmark_df = _load_source_tables(spec)

        for repeat_idx, row_id in enumerate(_baseline_ids(spec), start=1):
            pred = pd.to_numeric(baseline_df.loc[row_id], errors="coerce").reindex(Q_COLS)
            rows.append(
                {
                    "model": model,
                    "variant_id": "baseline",
                    "variant_kind": "baseline",
                    "repeat": repeat_idx,
                    "row_id": row_id,
                    **compute_metrics(pred, treatment, control, learning_mean),
                }
            )

        for variant_id, meta in metadata.items():
            if variant_id == str(spec["benchmark_variant_id"]):
                ids = _benchmark_ids(spec)
                source_df = benchmark_df
            elif variant_id == str(spec["full_benchmark_variant_id"]):
                ids = _full_benchmark_ids(spec)
                source_df = full_benchmark_df
            else:
                ids = _collection_ids(spec, variant_id)
                source_df = collection_df

            if not ids or any(row_id not in source_df.index for row_id in ids):
                continue

            for repeat_idx, row_id in enumerate(ids, start=1):
                pred = pd.to_numeric(source_df.loc[row_id], errors="coerce").reindex(Q_COLS)
                rows.append(
                    {
                        "model": model,
                        "variant_id": variant_id,
                        "variant_kind": str(meta.get("variant_kind", "") or ""),
                        "repeat": repeat_idx,
                        "row_id": row_id,
                        **compute_metrics(pred, treatment, control, learning_mean),
                    }
                )

    out = pd.DataFrame(rows)
    out["model"] = pd.Categorical(out["model"], categories=MODEL_ORDER, ordered=True)
    return out.sort_values(["model", "variant_id", "repeat"]).reset_index(drop=True)


def build_pairing_summary(repeat_rows: pd.DataFrame) -> pd.DataFrame:
    out_rows: list[dict[str, object]] = []

    for model, part in repeat_rows.groupby("model", observed=True):
        baseline = part.loc[part["variant_id"] == "baseline"].set_index("repeat").sort_index()
        for (variant_id, variant_kind), vpart in part.loc[part["variant_id"] != "baseline"].groupby(
            ["variant_id", "variant_kind"],
            observed=True,
        ):
            variant = vpart.set_index("repeat").sort_index()
            merged = baseline[METRICS].join(variant[METRICS], lsuffix="_base", rsuffix="_aug", how="inner")
            if len(merged) != 5:
                continue

            row: dict[str, object] = {
                "model": str(model),
                "variant_id": str(variant_id),
                "variant_kind": str(variant_kind),
            }
            for metric in METRICS:
                base_vals = merged[f"{metric}_base"].to_numpy(dtype=float)
                aug_vals = merged[f"{metric}_aug"].to_numpy(dtype=float)
                row[f"{metric}_aligned_corr"] = float(np.corrcoef(base_vals, aug_vals)[0, 1])

                perm_vars = np.array(
                    [
                        float(np.var(aug_vals - base_vals[list(perm)], ddof=0))
                        for perm in permutations(range(len(base_vals)))
                    ],
                    dtype=float,
                )
                matched_var = float(np.var(aug_vals - base_vals, ddof=0))
                row[f"{metric}_matched_delta_var"] = matched_var
                row[f"{metric}_perm_mean_delta_var"] = float(perm_vars.mean())
                row[f"{metric}_matched_var_ratio"] = (
                    float(matched_var / perm_vars.mean()) if perm_vars.mean() > 0 else float("nan")
                )

            out_rows.append(row)

    return pd.DataFrame(out_rows).sort_values(["model", "variant_id"]).reset_index(drop=True)


def build_repeat_effect_summary(repeat_rows: pd.DataFrame) -> pd.DataFrame:
    out_rows: list[dict[str, object]] = []

    for model, part in repeat_rows.groupby("model", observed=True):
        subsets = {
            "all_conditions": part,
            "baseline_plus_benchmark": part.loc[part["variant_id"].isin(["baseline", "benchmark_pgg_ms"])],
        }
        for subset_name, subset in subsets.items():
            for metric in METRICS:
                grand_mean = float(subset[metric].mean())
                variant_means = subset.groupby("variant_id", observed=True)[metric].mean()
                repeat_means = subset.groupby("repeat", observed=True)[metric].mean()

                ss_variant = float(
                    sum(
                        int((subset["variant_id"] == variant_id).sum()) * float((value - grand_mean) ** 2)
                        for variant_id, value in variant_means.items()
                    )
                )
                ss_repeat = float(
                    sum(
                        int((subset["repeat"] == repeat).sum()) * float((value - grand_mean) ** 2)
                        for repeat, value in repeat_means.items()
                    )
                )

                merged = subset.merge(variant_means.rename("variant_mean"), on="variant_id").merge(
                    repeat_means.rename("repeat_mean"),
                    on="repeat",
                )
                resid = merged[metric] - merged["variant_mean"] - merged["repeat_mean"] + grand_mean
                ss_resid = float((resid**2).sum())
                total = ss_variant + ss_repeat + ss_resid

                out_rows.append(
                    {
                        "model": str(model),
                        "subset": subset_name,
                        "metric": metric,
                        "eta_repeat": float(ss_repeat / total) if total > 0 else float("nan"),
                        "eta_variant": float(ss_variant / total) if total > 0 else float("nan"),
                    }
                )

    return pd.DataFrame(out_rows).sort_values(["model", "subset", "metric"]).reset_index(drop=True)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    repeat_rows = load_repeat_level_rows()
    pairing_summary = build_pairing_summary(repeat_rows)
    repeat_effect_summary = build_repeat_effect_summary(repeat_rows)

    repeat_rows.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_repeat_pairing_repeat_rows.csv",
        index=False,
    )
    pairing_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_repeat_pairing_pairing_summary.csv",
        index=False,
    )
    repeat_effect_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_repeat_pairing_repeat_effect_summary.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
