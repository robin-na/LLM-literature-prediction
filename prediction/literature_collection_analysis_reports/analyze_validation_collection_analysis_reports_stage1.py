from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ANALYSIS_ROOT = Path(__file__).resolve().parents[1]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from jsonl_parser import jsonl_to_dataframe  # noqa: E402
from prediction_metrics import (  # noqa: E402
    _corr_np,
    _directional_accuracy_np,
    _paired_delta_ci,
    _rmse_np,
)


ROOT = ANALYSIS_ROOT.parent
OPENAI_BATCH_OUTPUT = ROOT / "openAI_batch_output"
INPUT = ROOT / "input"
REPORT_INDEX_CSV = ROOT / "literature" / "output" / "collection_analysis_reports" / "switch_sets_stage1" / "report_index.csv"

RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_stage1"

Q_COLS = [f"Q{i}" for i in range(1, 21)]
METRIC_ORDER = ["rmse", "correlation", "r2", "directional_accuracy"]
LOWER_IS_BETTER = {"rmse"}

RUN_SPECS = [
    {
        "model": "GPT-4.1",
        "mode": "joint_reasoning",
        "output_path": OPENAI_BATCH_OUTPUT / "prediction_literature_collection_analysis_report_stage1_9variants_joint_41.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_positive_case_variations_41.jsonl",
        "baseline_variation": "baseline_joint_reasoning",
    },
    {
        "model": "GPT-4.1 Mini",
        "mode": "joint_reasoning",
        "output_path": OPENAI_BATCH_OUTPUT / "prediction_literature_collection_analysis_report_stage1_9variants_joint_41mini.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41mini.jsonl",
        "baseline_variation": "baseline_joint_reasoning",
    },
    {
        "model": "GPT-4.1 Nano",
        "mode": "joint_reasoning",
        "output_path": OPENAI_BATCH_OUTPUT / "prediction_literature_collection_analysis_report_stage1_9variants_joint_41nano.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41nano.jsonl",
        "baseline_variation": "baseline_joint_reasoning",
    },
]


def load_truth() -> tuple[pd.Series, pd.Series]:
    df = pd.read_csv(INPUT / "pgg_CONFIGmerged_validation.csv").sort_values("CONFIG_configId")
    treatment = pd.Series(df["efficiency_p"].to_numpy(dtype=float) * 100.0, index=Q_COLS)
    control = pd.Series(df["efficiency_np"].to_numpy(dtype=float) * 100.0, index=Q_COLS)
    return treatment, control


def _r2_np(pred: np.ndarray, truth: np.ndarray, control: np.ndarray) -> float:
    if pred.size == 0:
        return float("nan")
    mse = float(np.mean((pred - truth) ** 2))
    null_mse = float(np.mean((truth - control) ** 2))
    if null_mse <= 0:
        return float("nan")
    return float(1.0 - mse / null_mse)


def compute_metrics(pred_row: pd.Series, treatment: pd.Series, control: pd.Series) -> dict[str, float | int]:
    pred = pd.to_numeric(pred_row, errors="coerce").reindex(Q_COLS)
    truth = treatment.reindex(Q_COLS)
    ctrl = control.reindex(Q_COLS)

    pred_arr = pred.to_numpy(dtype=float)
    truth_arr = truth.to_numpy(dtype=float)
    ctrl_arr = ctrl.to_numpy(dtype=float)
    mask = ~np.isnan(pred_arr) & ~np.isnan(truth_arr) & ~np.isnan(ctrl_arr)
    if mask.sum() == 0:
        return {"n": 0, "rmse": np.nan, "correlation": np.nan, "r2": np.nan, "directional_accuracy": np.nan}

    pred_sub = pred_arr[mask]
    truth_sub = truth_arr[mask]
    ctrl_sub = ctrl_arr[mask]
    return {
        "n": int(mask.sum()),
        "rmse": _rmse_np(pred_sub, truth_sub),
        "correlation": _corr_np(pred_sub, truth_sub),
        "r2": _r2_np(pred_sub, truth_sub, ctrl_sub),
        "directional_accuracy": float(_directional_accuracy_np(pred_sub, truth_sub, ctrl_sub)),
    }


def compute_delta_ci(
    pred_row: pd.Series,
    baseline_row: pd.Series,
    treatment: pd.Series,
    control: pd.Series,
    *,
    rng: np.random.Generator,
    n_boot: int,
) -> dict[str, float]:
    pred = pd.to_numeric(pred_row, errors="coerce").reindex(Q_COLS)
    baseline = pd.to_numeric(baseline_row, errors="coerce").reindex(Q_COLS)
    truth = treatment.reindex(Q_COLS)
    ctrl = control.reindex(Q_COLS)

    pred_arr = pred.to_numpy(dtype=float)
    baseline_arr = baseline.to_numpy(dtype=float)
    truth_arr = truth.to_numpy(dtype=float)
    ctrl_arr = ctrl.to_numpy(dtype=float)

    mask = ~np.isnan(pred_arr) & ~np.isnan(baseline_arr) & ~np.isnan(truth_arr) & ~np.isnan(ctrl_arr)

    delta_rmse, delta_rmse_lo, delta_rmse_hi = _paired_delta_ci(
        _rmse_np,
        pred_arr,
        baseline_arr,
        truth_arr,
        None,
        mask,
        rng,
        n_boot,
    )
    delta_corr, delta_corr_lo, delta_corr_hi = _paired_delta_ci(
        _corr_np,
        pred_arr,
        baseline_arr,
        truth_arr,
        None,
        mask,
        rng,
        n_boot,
    )
    delta_r2, delta_r2_lo, delta_r2_hi = _paired_delta_ci(
        _r2_np,
        pred_arr,
        baseline_arr,
        truth_arr,
        ctrl_arr,
        mask,
        rng,
        n_boot,
    )
    delta_dir, delta_dir_lo, delta_dir_hi = _paired_delta_ci(
        _directional_accuracy_np,
        pred_arr,
        baseline_arr,
        truth_arr,
        ctrl_arr,
        mask,
        rng,
        n_boot,
    )

    return {
        "delta_rmse": delta_rmse,
        "delta_rmse_ci_low": delta_rmse_lo,
        "delta_rmse_ci_high": delta_rmse_hi,
        "delta_correlation": delta_corr,
        "delta_correlation_ci_low": delta_corr_lo,
        "delta_correlation_ci_high": delta_corr_hi,
        "delta_r2": delta_r2,
        "delta_r2_ci_low": delta_r2_lo,
        "delta_r2_ci_high": delta_r2_hi,
        "delta_directional_accuracy": delta_dir,
        "delta_directional_accuracy_ci_low": delta_dir_lo,
        "delta_directional_accuracy_ci_high": delta_dir_hi,
    }


def extract_variant_id(variation: str) -> str:
    return str(variation).rsplit("/", 1)[-1].strip()


def load_variant_metadata() -> dict[str, dict[str, str]]:
    df = pd.read_csv(REPORT_INDEX_CSV)
    out: dict[str, dict[str, str]] = {}
    for row in df.to_dict("records"):
        out[str(row["variant_id"])] = {
            "custom_id": str(row.get("custom_id", "") or ""),
            "variant_kind": str(row.get("variant_kind", "") or ""),
            "count": str(row.get("count", "") or ""),
            "description": str(row.get("description", "") or ""),
            "report_path": str(row.get("report_path", "") or ""),
        }
    return out


def build_rows(
    treatment: pd.Series,
    control: pd.Series,
    metadata: dict[str, dict[str, str]],
    *,
    n_boot: int = 5000,
    seed: int = 42,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    rng = np.random.default_rng(seed)

    for spec in RUN_SPECS:
        output_path = spec["output_path"]
        baseline_path = spec["baseline_path"]
        if not output_path.exists() or not baseline_path.exists():
            continue

        pred_df = jsonl_to_dataframe(output_path).reindex(columns=Q_COLS)
        base_df = jsonl_to_dataframe(baseline_path).reindex(columns=Q_COLS)
        baseline_variation = spec["baseline_variation"]
        if baseline_variation not in base_df.index:
            continue

        baseline_row = base_df.loc[baseline_variation]
        baseline_metrics = compute_metrics(baseline_row, treatment, control)

        for variation, pred_row in pred_df.iterrows():
            variant_id = extract_variant_id(str(variation))
            variant_meta = metadata.get(variant_id, {})
            metrics = compute_metrics(pred_row, treatment, control)
            delta_ci = compute_delta_ci(
                pred_row,
                baseline_row,
                treatment,
                control,
                rng=rng,
                n_boot=n_boot,
            )

            row: dict[str, object] = {
                "model": spec["model"],
                "mode": spec["mode"],
                "variation": variation,
                "variant_id": variant_id,
                "variant_kind": variant_meta.get("variant_kind", ""),
                "count": pd.to_numeric(variant_meta.get("count", np.nan), errors="coerce"),
                "description": variant_meta.get("description", ""),
                "report_path": variant_meta.get("report_path", ""),
                "baseline_variation": baseline_variation,
                "baseline_n": baseline_metrics["n"],
                "n": metrics["n"],
            }
            for metric in METRIC_ORDER:
                row[metric] = metrics[metric]
                row[f"baseline_{metric}"] = baseline_metrics[metric]
                row[f"delta_{metric}"] = delta_ci[f"delta_{metric}"]
                row[f"delta_{metric}_ci_low"] = delta_ci[f"delta_{metric}_ci_low"]
                row[f"delta_{metric}_ci_high"] = delta_ci[f"delta_{metric}_ci_high"]
                if metric in LOWER_IS_BETTER:
                    improved = float(metrics[metric]) < float(baseline_metrics[metric])
                    sig_improved = float(delta_ci[f"delta_{metric}_ci_high"]) < 0.0
                else:
                    improved = float(metrics[metric]) > float(baseline_metrics[metric])
                    sig_improved = float(delta_ci[f"delta_{metric}_ci_low"]) > 0.0
                row[f"improved_{metric}"] = improved
                row[f"sig_improved_{metric}"] = sig_improved
            rows.append(row)

    out = pd.DataFrame.from_records(rows)
    if out.empty:
        return out
    return out.sort_values(["model", "variant_id"]).reset_index(drop=True)


def rank_rows(rows: pd.DataFrame) -> pd.DataFrame:
    ranked = rows.copy()
    for metric in METRIC_ORDER:
        ascending = metric in LOWER_IS_BETTER
        ranked[f"rank_{metric}"] = ranked.groupby("model")[metric].rank(
            ascending=ascending,
            method="min",
        )
    return ranked


def summarize(rows: pd.DataFrame) -> pd.DataFrame:
    records: list[dict[str, object]] = []
    for model, part in rows.groupby("model", dropna=False):
        rec: dict[str, object] = {
            "model": model,
            "n_variants": len(part),
        }
        for metric in METRIC_ORDER:
            ascending = metric in LOWER_IS_BETTER
            best = part.sort_values(metric, ascending=ascending).iloc[0]
            worst = part.sort_values(metric, ascending=not ascending).iloc[0]
            rec[f"baseline_{metric}"] = float(part[f"baseline_{metric}"].iloc[0])
            rec[f"mean_{metric}"] = float(part[metric].mean())
            rec[f"share_improved_{metric}"] = float(part[f"improved_{metric}"].mean())
            rec[f"sig_improved_count_{metric}"] = int(part[f"sig_improved_{metric}"].sum())
            rec[f"best_variant_{metric}"] = best["variant_id"]
            rec[f"best_value_{metric}"] = float(best[metric])
            rec[f"best_delta_{metric}"] = float(best[f"delta_{metric}"])
            rec[f"worst_variant_{metric}"] = worst["variant_id"]
            rec[f"worst_value_{metric}"] = float(worst[metric])
            rec[f"worst_delta_{metric}"] = float(worst[f"delta_{metric}"])
        records.append(rec)
    return pd.DataFrame.from_records(records).sort_values("model").reset_index(drop=True)


def build_top_bottom(rows: pd.DataFrame, k: int = 3) -> pd.DataFrame:
    out: list[dict[str, object]] = []
    for model, part in rows.groupby("model", dropna=False):
        for metric in METRIC_ORDER:
            ascending = metric in LOWER_IS_BETTER
            ranked = part.sort_values(metric, ascending=ascending).reset_index(drop=True)
            for bucket, bucket_df in [("top", ranked.head(k)), ("bottom", ranked.tail(k))]:
                display_df = bucket_df if bucket == "top" else bucket_df.iloc[::-1]
                for rank, (_, row) in enumerate(display_df.iterrows(), start=1):
                    out.append(
                        {
                            "model": model,
                            "metric": metric,
                            "bucket": bucket,
                            "rank": rank,
                            "variant_id": row["variant_id"],
                            "variant_kind": row["variant_kind"],
                            "count": row["count"],
                            "description": row["description"],
                            "raw_value": row[metric],
                            "baseline_value": row[f"baseline_{metric}"],
                            "delta_value": row[f"delta_{metric}"],
                            "delta_ci_low": row[f"delta_{metric}_ci_low"],
                            "delta_ci_high": row[f"delta_{metric}_ci_high"],
                            "sig_improved": row[f"sig_improved_{metric}"],
                        }
                    )
    return pd.DataFrame.from_records(out)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    treatment, control = load_truth()
    metadata = load_variant_metadata()
    rows = build_rows(treatment, control, metadata)
    if rows.empty:
        raise FileNotFoundError("No collection-analysis-report output files were found for the configured run specs.")

    ranked = rank_rows(rows)
    summary = summarize(ranked)
    top_bottom = build_top_bottom(ranked, k=3)

    rows_path = RESULTS_DIR / "validation_literature_collection_analysis_report_rows.csv"
    ranked_path = RESULTS_DIR / "validation_literature_collection_analysis_report_ranked.csv"
    summary_path = RESULTS_DIR / "validation_literature_collection_analysis_report_summary.csv"
    top_bottom_path = RESULTS_DIR / "validation_literature_collection_analysis_report_top_bottom.csv"

    rows.to_csv(rows_path, index=False)
    ranked.to_csv(ranked_path, index=False)
    summary.to_csv(summary_path, index=False)
    top_bottom.to_csv(top_bottom_path, index=False)

    print(rows_path)
    print(ranked_path)
    print(summary_path)
    print(top_bottom_path)


if __name__ == "__main__":
    main()
