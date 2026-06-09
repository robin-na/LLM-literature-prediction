from __future__ import annotations

import sys
from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd

ANALYSIS_ROOT = Path(__file__).resolve().parents[1]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from jsonl_parser import jsonl_to_dataframe  # noqa: E402
from prediction_metrics import _corr_np, _rmse_np  # noqa: E402
from prediction_metrics import _directional_accuracy_np as _da_np  # noqa: E402


ROOT = ANALYSIS_ROOT.parent
INPUT = ROOT / "input"
VAL_DF = ROOT / "science_data" / "data" / "processed_data" / "df_paired_val.csv"
LEARN_DF = ROOT / "science_data" / "data" / "processed_data" / "df_paired_learn.csv"
OPENAI_BATCH_OUTPUT = ROOT / "openAI_batch_output"
BACKFILL_OUTPUT_DIR = OPENAI_BATCH_OUTPUT / "backfill_repeat5_missing"
METADATA_FILTER_INDEX_CSV = (
    ROOT / "literature" / "output" / "collection_analysis_reports" / "metadata_filters" / "report_index.csv"
)
REPEAT5_AVG_PREDICTIONS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5"
    / "validation_literature_collection_analysis_report_repeat5_avg_predictions.csv"
)
REPEAT5_BASELINE_AVG_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5"
    / "validation_literature_collection_analysis_report_repeat5_baseline_avg_predictions.csv"
)
RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_metadata_filters"

Q_COLS = [f"Q{i}" for i in range(1, 21)]
METRIC_ORDER = ["correlation", "r2", "rmse", "directional_accuracy"]
LOWER_IS_BETTER = {"rmse"}
ALL_PAPERS_VARIANT_ID = "broad_all_2011"
BENCHMARK_VARIANT_ID = "benchmark_pgg_ms"
MODEL_ORDER = ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]

MODEL_SPECS = {
    "GPT-4.1": OPENAI_BATCH_OUTPUT / "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_41.jsonl",
    "GPT-4.1 Mini": OPENAI_BATCH_OUTPUT / "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_41mini.jsonl",
    "GPT-4.1 Nano": OPENAI_BATCH_OUTPUT / "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_41nano.jsonl",
    "GPT-5.1": OPENAI_BATCH_OUTPUT / "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_gpt51.jsonl",
    "GPT-5 Mini": OPENAI_BATCH_OUTPUT / "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_gpt5mini.jsonl",
    "GPT-5 Nano": OPENAI_BATCH_OUTPUT / "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_gpt5nano.jsonl",
}
MODEL_BACKFILL_SPECS = {
    "GPT-4.1": BACKFILL_OUTPUT_DIR / "prediction_repeat5_backfill_missing_41.jsonl",
    "GPT-4.1 Mini": BACKFILL_OUTPUT_DIR / "prediction_repeat5_backfill_missing_41mini.jsonl",
    "GPT-4.1 Nano": BACKFILL_OUTPUT_DIR / "prediction_repeat5_backfill_missing_41nano.jsonl",
    "GPT-5.1": BACKFILL_OUTPUT_DIR / "prediction_repeat5_backfill_missing_gpt51.jsonl",
    "GPT-5 Mini": BACKFILL_OUTPUT_DIR / "prediction_repeat5_backfill_missing_gpt5mini.jsonl",
    "GPT-5 Nano": BACKFILL_OUTPUT_DIR / "prediction_repeat5_backfill_missing_gpt5nano.jsonl",
}


def _r2_np(pred: np.ndarray, truth: np.ndarray, learning_mean: np.ndarray) -> float:
    if pred.size == 0:
        return float("nan")
    mse = float(np.mean((pred - truth) ** 2))
    null_mse = float(np.mean((truth - learning_mean) ** 2))
    if null_mse <= 0:
        return float("nan")
    return float(1.0 - mse / null_mse)


def load_truth_arrays() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    val = pd.read_csv(VAL_DF).sort_values("CONFIG_configId")
    learn = pd.read_csv(LEARN_DF)
    truth = val["treatment_itt_efficiency"].to_numpy(dtype=float) * 100.0
    control = val["control_itt_efficiency"].to_numpy(dtype=float) * 100.0
    learning_mean = np.full_like(truth, float(learn["treatment_itt_efficiency"].mean() * 100.0))
    return truth, control, learning_mean


def compute_metrics(pred_row: pd.Series, truth: np.ndarray, control: np.ndarray, learning_mean: np.ndarray) -> dict[str, float | int]:
    pred = pd.to_numeric(pred_row, errors="coerce").reindex(Q_COLS)
    pred_arr = pred.to_numpy(dtype=float)
    mask = ~np.isnan(pred_arr) & ~np.isnan(truth) & ~np.isnan(control) & ~np.isnan(learning_mean)
    if mask.sum() == 0:
        return {"n": 0, "correlation": np.nan, "r2": np.nan, "rmse": np.nan, "directional_accuracy": np.nan}

    pred_sub = pred_arr[mask]
    truth_sub = truth[mask]
    control_sub = control[mask]
    learning_sub = learning_mean[mask]
    return {
        "n": int(mask.sum()),
        "correlation": _corr_np(pred_sub, truth_sub),
        "r2": _r2_np(pred_sub, truth_sub, learning_sub),
        "rmse": _rmse_np(pred_sub, truth_sub),
        "directional_accuracy": float(_da_np(pred_sub, truth_sub, control_sub)),
    }


def _corr_rowwise(pred: np.ndarray, truth: np.ndarray) -> np.ndarray:
    pred_mean = pred.mean(axis=1, keepdims=True)
    pred_center = pred - pred_mean
    truth_center = truth - truth.mean()
    num = np.sum(pred_center * truth_center[None, :], axis=1)
    denom = np.sqrt(np.sum(pred_center**2, axis=1) * np.sum(truth_center**2))
    return np.divide(
        num,
        denom,
        out=np.full(pred.shape[0], np.nan, dtype=np.float32),
        where=denom > 0,
    )


def _resolve_row_ids(df: pd.DataFrame, row_ids: list[str]) -> list[str] | None:
    resolved: list[str] = []
    for row_id in row_ids:
        if row_id in df.index:
            resolved.append(row_id)
            continue
        prefixed = f"validation/{row_id}"
        if prefixed in df.index:
            resolved.append(prefixed)
            continue
        return None
    return resolved


def _mean_rows(df: pd.DataFrame, row_ids: list[str]) -> pd.Series:
    rows = [pd.to_numeric(df.loc[row_id], errors="coerce").reindex(Q_COLS) for row_id in row_ids]
    mat = pd.concat(rows, axis=1)
    mat.columns = [f"run{i + 1}" for i in range(len(rows))]
    return mat.mean(axis=1, skipna=True)


def load_metadata_filter_index() -> pd.DataFrame:
    return pd.read_csv(METADATA_FILTER_INDEX_CSV)


def load_metadata_filter_avg_predictions(index_df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for model in MODEL_ORDER:
        path = MODEL_SPECS[model]
        if not path.exists():
            continue
        source_df = jsonl_to_dataframe(path).reindex(columns=Q_COLS)
        backfill_path = MODEL_BACKFILL_SPECS.get(model)
        if backfill_path and backfill_path.exists():
            backfill_df = jsonl_to_dataframe(backfill_path).reindex(columns=Q_COLS)
            if not backfill_df.empty:
                mask = backfill_df.index.to_series().astype(str).str.startswith("collection_analysis_report_joint_rep")
                if mask.any():
                    source_df = pd.concat([source_df, backfill_df.loc[mask]], axis=0)
                    source_df = source_df[~source_df.index.duplicated(keep="last")]
        for meta in index_df.to_dict("records"):
            variant_id = str(meta["variant_id"])
            requested_ids = [f"collection_analysis_report_joint_rep{rep}/{variant_id}" for rep in range(1, 6)]
            resolved_ids = _resolve_row_ids(source_df, requested_ids)
            if resolved_ids is None:
                continue
            avg_preds = _mean_rows(source_df, resolved_ids)
            rows.append(
                {
                    "model": model,
                    "variant_id": variant_id,
                    "variant_kind": str(meta.get("variant_kind", "") or ""),
                    "variant_group": "metadata_filter",
                    "count": pd.to_numeric(meta.get("count", np.nan), errors="coerce"),
                    "description": str(meta.get("description", "") or ""),
                    "report_path": str(meta.get("report_path", "") or ""),
                    "n_runs": len(resolved_ids),
                    **avg_preds.to_dict(),
                }
            )
    return pd.DataFrame(rows)


def load_reference_avg_predictions(available_models: list[str], variant_id: str, variant_group: str) -> pd.DataFrame:
    df = pd.read_csv(REPEAT5_AVG_PREDICTIONS_CSV)
    df = df.loc[(df["variant_id"] == variant_id) & (df["model"].isin(available_models))].copy()
    if df.empty:
        return df
    df["variant_group"] = variant_group
    return df[
        ["model", "variant_id", "variant_kind", "variant_group", "count", "description", "report_path", "n_runs", *Q_COLS]
    ].reset_index(drop=True)


def load_baseline_avg_predictions(available_models: list[str]) -> pd.DataFrame:
    df = pd.read_csv(REPEAT5_BASELINE_AVG_CSV)
    return df.loc[df["model"].isin(available_models), ["model", "mode", "variant_id", "variant_kind", "count", "description", "report_path", "n_runs", *Q_COLS]].reset_index(drop=True)


def build_rows(
    avg_pred_df: pd.DataFrame,
    baseline_avg_df: pd.DataFrame,
    truth: np.ndarray,
    control: np.ndarray,
    learning_mean: np.ndarray,
    *,
    n_boot: int = 5000,
    seed: int = 42,
    chunk_size: int = 32,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []

    truth_f = truth.astype(np.float32)
    control_f = control.astype(np.float32)
    learning_mean_f = np.float32(float(learning_mean[0]))
    true_dir = np.sign(truth_f - control_f).astype(np.float32)
    null_mse_full = float(np.mean((truth_f - learning_mean_f) ** 2))

    rng = np.random.default_rng(seed)
    boot_idx = rng.integers(0, len(truth_f), size=(n_boot, len(truth_f)), dtype=np.int16)
    truth_bs = truth_f[boot_idx].astype(np.float32)
    control_bs = control_f[boot_idx].astype(np.float32)
    true_dir_bs = np.sign(truth_bs - control_bs).astype(np.float32)
    null_mse_bs = np.mean((truth_bs - learning_mean_f) ** 2, axis=1).astype(np.float32)
    truth_mean_bs = truth_bs.mean(axis=1, keepdims=True)
    truth_center_bs = truth_bs - truth_mean_bs
    truth_ss_bs = np.sum(truth_center_bs**2, axis=1).astype(np.float32)

    for model, pred_part in avg_pred_df.groupby("model", dropna=False, observed=False):
        baseline_part = baseline_avg_df.loc[baseline_avg_df["model"] == model].copy()
        if baseline_part.empty:
            continue
        baseline = baseline_part.iloc[0][Q_COLS].to_numpy(dtype=np.float32)
        base_bs = baseline[boot_idx].astype(np.float32)

        base_mse_full = float(np.mean((baseline - truth_f) ** 2))
        base_rmse = float(np.sqrt(base_mse_full))
        base_corr = float(np.corrcoef(baseline, truth_f)[0, 1])
        base_r2 = float(1.0 - base_mse_full / null_mse_full)
        base_da = float(np.mean(np.sign(baseline - control_f) == true_dir))

        base_mse_bs = np.mean((base_bs - truth_bs) ** 2, axis=1).astype(np.float32)
        base_rmse_bs = np.sqrt(base_mse_bs).astype(np.float32)
        base_r2_bs = (1.0 - base_mse_bs / null_mse_bs).astype(np.float32)
        base_da_bs = np.mean(np.sign(base_bs - control_bs) == true_dir_bs, axis=1).astype(np.float32)
        base_mean_bs = base_bs.mean(axis=1, keepdims=True)
        base_center_bs = base_bs - base_mean_bs
        base_num_bs = np.sum(base_center_bs * truth_center_bs, axis=1)
        base_den_bs = np.sqrt(np.sum(base_center_bs**2, axis=1) * truth_ss_bs)
        base_corr_bs = np.divide(
            base_num_bs,
            base_den_bs,
            out=np.full(n_boot, np.nan, dtype=np.float32),
            where=base_den_bs > 0,
        )

        preds = pred_part[Q_COLS].to_numpy(dtype=np.float32)
        mse_full = np.mean((preds - truth_f[None, :]) ** 2, axis=1)
        rmse_full = np.sqrt(mse_full)
        corr_full = _corr_rowwise(preds, truth_f)
        r2_full = 1.0 - mse_full / null_mse_full
        da_full = np.mean(np.sign(preds - control_f[None, :]) == true_dir[None, :], axis=1)

        pred_part = pred_part.reset_index(drop=True)
        for start in range(0, preds.shape[0], chunk_size):
            end = min(start + chunk_size, preds.shape[0])
            pred_chunk = preds[start:end]
            meta_chunk = pred_part.iloc[start:end]

            pred_bs = pred_chunk[:, boot_idx]
            mse_bs = np.mean((pred_bs - truth_bs[None, :, :]) ** 2, axis=2)
            rmse_bs = np.sqrt(mse_bs)
            r2_bs = 1.0 - mse_bs / null_mse_bs[None, :]
            da_bs = np.mean(np.sign(pred_bs - control_bs[None, :, :]) == true_dir_bs[None, :, :], axis=2)

            pred_mean_bs = pred_bs.mean(axis=2)
            pred_center_bs = pred_bs - pred_mean_bs[:, :, None]
            pred_num_bs = np.sum(pred_center_bs * truth_center_bs[None, :, :], axis=2)
            pred_den_bs = np.sqrt(np.sum(pred_center_bs**2, axis=2) * truth_ss_bs[None, :])
            corr_bs = np.divide(
                pred_num_bs,
                pred_den_bs,
                out=np.full((end - start, n_boot), np.nan, dtype=np.float32),
                where=pred_den_bs > 0,
            )

            delta_arrays = {
                "rmse": rmse_bs - base_rmse_bs[None, :],
                "correlation": corr_bs - base_corr_bs[None, :],
                "r2": r2_bs - base_r2_bs[None, :],
                "directional_accuracy": da_bs - base_da_bs[None, :],
            }

            for j, (_, pred_rec) in enumerate(meta_chunk.iterrows()):
                row: dict[str, object] = {
                    "model": model,
                    "variant_id": pred_rec["variant_id"],
                    "variant_kind": pred_rec["variant_kind"],
                    "variant_group": pred_rec["variant_group"],
                    "count": pred_rec["count"],
                    "description": pred_rec["description"],
                    "report_path": pred_rec["report_path"],
                    "n_runs": int(pred_rec["n_runs"]),
                    "baseline_n": len(truth_f),
                    "n": len(truth_f),
                    "rmse": float(rmse_full[start + j]),
                    "baseline_rmse": base_rmse,
                    "correlation": float(corr_full[start + j]),
                    "baseline_correlation": base_corr,
                    "r2": float(r2_full[start + j]),
                    "baseline_r2": base_r2,
                    "directional_accuracy": float(da_full[start + j]),
                    "baseline_directional_accuracy": base_da,
                }

                delta_full = {
                    "rmse": float(rmse_full[start + j] - base_rmse),
                    "correlation": float(corr_full[start + j] - base_corr),
                    "r2": float(r2_full[start + j] - base_r2),
                    "directional_accuracy": float(da_full[start + j] - base_da),
                }

                for metric in METRIC_ORDER:
                    delta_boot = delta_arrays[metric][j]
                    finite = delta_boot[np.isfinite(delta_boot)]
                    ci_low, ci_high = (
                        np.nanpercentile(finite, [2.5, 97.5]) if finite.size else (np.nan, np.nan)
                    )
                    row[f"delta_{metric}"] = delta_full[metric]
                    row[f"delta_{metric}_ci_low"] = float(ci_low)
                    row[f"delta_{metric}_ci_high"] = float(ci_high)
                    if metric in LOWER_IS_BETTER:
                        row[f"improved_{metric}"] = bool(delta_full[metric] < 0)
                        row[f"sig_improve_{metric}"] = bool(ci_high < 0)
                        row[f"sig_worsen_{metric}"] = bool(ci_low > 0)
                    else:
                        row[f"improved_{metric}"] = bool(delta_full[metric] > 0)
                        row[f"sig_improve_{metric}"] = bool(ci_low > 0)
                        row[f"sig_worsen_{metric}"] = bool(ci_high < 0)
                rows.append(row)

    out = pd.DataFrame(rows)
    if out.empty:
        return out
    for metric in METRIC_ORDER:
        out[f"{metric}_sig_category"] = np.select(
            [out[f"sig_improve_{metric}"], out[f"sig_worsen_{metric}"]],
            ["Significant improvement", "Significant worsening"],
            default="Not significant",
        )
    out["model"] = pd.Categorical(out["model"], categories=MODEL_ORDER, ordered=True)
    return out.sort_values(["model", "variant_group", "variant_id"]).reset_index(drop=True)


def summarize_rows(rows: pd.DataFrame) -> pd.DataFrame:
    recs: list[dict[str, object]] = []
    meta_rows = rows.loc[rows["variant_group"] == "metadata_filter"].copy()
    for model in [m for m in MODEL_ORDER if m in set(rows["model"].astype(str))]:
        part = rows.loc[rows["model"].astype(str) == model].copy()
        meta_part = meta_rows.loc[meta_rows["model"].astype(str) == model].copy()
        all_papers = part.loc[part["variant_id"] == ALL_PAPERS_VARIANT_ID].copy()
        benchmark = part.loc[part["variant_id"] == BENCHMARK_VARIANT_ID].copy()
        rec: dict[str, object] = {
            "model": model,
            "n_variants_total": int(len(part)),
            "n_metadata_filters": int(len(meta_part)),
        }
        for metric in METRIC_ORDER:
            baseline_value = float(part[f"baseline_{metric}"].iloc[0])
            rec[f"baseline_{metric}"] = baseline_value
            if not meta_part.empty:
                meta_values = pd.to_numeric(meta_part[metric], errors="coerce")
                rec[f"metadata_mean_{metric}"] = float(meta_values.mean())
                rec[f"metadata_median_{metric}"] = float(meta_values.median())
                rec[f"metadata_n_sig_improved_{metric}"] = int(meta_part[f"sig_improve_{metric}"].sum())
                rec[f"metadata_n_sig_worsened_{metric}"] = int(meta_part[f"sig_worsen_{metric}"].sum())
                rec[f"metadata_share_sig_improved_{metric}"] = float(meta_part[f"sig_improve_{metric}"].mean())
                rec[f"metadata_share_sig_worsened_{metric}"] = float(meta_part[f"sig_worsen_{metric}"].mean())
                if metric in LOWER_IS_BETTER:
                    rec[f"metadata_share_improved_{metric}"] = float((meta_values < baseline_value).mean())
                    best_row = meta_part.sort_values(metric, ascending=True).iloc[0]
                else:
                    rec[f"metadata_share_improved_{metric}"] = float((meta_values > baseline_value).mean())
                    best_row = meta_part.sort_values(metric, ascending=False).iloc[0]
                rec[f"best_metadata_variant_{metric}"] = best_row["variant_id"]
                rec[f"best_metadata_value_{metric}"] = float(best_row[metric])
            if not all_papers.empty:
                rec[f"all_papers_{metric}"] = float(all_papers[metric].iloc[0])
                rec[f"all_papers_delta_{metric}"] = float(all_papers[f"delta_{metric}"].iloc[0])
            if not benchmark.empty:
                rec[f"benchmark_{metric}"] = float(benchmark[metric].iloc[0])
                rec[f"benchmark_delta_{metric}"] = float(benchmark[f"delta_{metric}"].iloc[0])
        recs.append(rec)

    out = pd.DataFrame(recs)
    out["model"] = pd.Categorical(out["model"], categories=MODEL_ORDER, ordered=True)
    return out.sort_values("model").reset_index(drop=True)


def build_top_variants(rows: pd.DataFrame, n_per_metric: int = 15) -> pd.DataFrame:
    meta_rows = rows.loc[rows["variant_group"] == "metadata_filter"].copy()
    top_rows: list[dict[str, object]] = []
    for model in [m for m in MODEL_ORDER if m in set(meta_rows["model"].astype(str))]:
        model_part = meta_rows.loc[meta_rows["model"].astype(str) == model].copy()
        for metric in ["correlation", "r2", "rmse"]:
            ascending = metric in LOWER_IS_BETTER
            ranked = model_part.sort_values(metric, ascending=ascending).head(n_per_metric).reset_index(drop=True)
            for rank, (_, row) in enumerate(ranked.iterrows(), start=1):
                top_rows.append(
                    {
                        "model": model,
                        "metric": metric,
                        "rank": rank,
                        "variant_id": row["variant_id"],
                        "count": row["count"],
                        "value": row[metric],
                        "baseline_value": row[f"baseline_{metric}"],
                        "delta_value": row[f"delta_{metric}"],
                        "description": row["description"],
                    }
                )
    return pd.DataFrame(top_rows)


def mean_pairwise_correlation(arrays: list[np.ndarray]) -> float:
    vals: list[float] = []
    for a, b in combinations(arrays, 2):
        if np.std(a) == 0 or np.std(b) == 0:
            vals.append(np.nan)
        else:
            vals.append(float(np.corrcoef(a, b)[0, 1]))
    return float(np.nanmean(np.asarray(vals, dtype=float)))


def pairwise_correlation_matrix(model_to_vec: dict[str, np.ndarray], model_order: list[str]) -> pd.DataFrame:
    data = np.full((len(model_order), len(model_order)), np.nan, dtype=float)
    for i, left in enumerate(model_order):
        for j, right in enumerate(model_order):
            a = model_to_vec[left]
            b = model_to_vec[right]
            if i == j:
                data[i, j] = 1.0
            elif np.std(a) == 0 or np.std(b) == 0:
                data[i, j] = np.nan
            else:
                data[i, j] = float(np.corrcoef(a, b)[0, 1])
    return pd.DataFrame(data, index=model_order, columns=model_order)


def spearman_corr(x: np.ndarray, y: np.ndarray) -> float:
    if len(x) < 2 or len(y) < 2:
        return float("nan")
    xr = pd.Series(x).rank(method="average").to_numpy(dtype=float)
    yr = pd.Series(y).rank(method="average").to_numpy(dtype=float)
    return float(np.corrcoef(xr, yr)[0, 1])


def pearson_corr(x: np.ndarray, y: np.ndarray) -> float:
    if len(x) < 2 or len(y) < 2:
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def build_convergence_outputs(
    avg_pred_df: pd.DataFrame,
    baseline_avg_df: pd.DataFrame,
    available_models: list[str],
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    truth_df = pd.read_csv(VAL_DF).sort_values("CONFIG_configId")
    truth = truth_df["treatment_itt_efficiency"].to_numpy(dtype=float) * 100.0
    control = truth_df["control_itt_efficiency"].to_numpy(dtype=float) * 100.0
    effect_truth = truth_df["treatment_effect"].to_numpy(dtype=float) * 100.0

    baseline_vectors = {
        model: pd.to_numeric(
            baseline_avg_df.loc[baseline_avg_df["model"] == model, Q_COLS].iloc[0],
            errors="coerce",
        ).to_numpy(dtype=float)
        for model in available_models
    }
    baseline_mean_pairwise_corr = mean_pairwise_correlation([baseline_vectors[model] for model in available_models])
    baseline_mean_corr_to_truth = float(
        np.mean([np.corrcoef(baseline_vectors[model], truth)[0, 1] for model in available_models if np.std(baseline_vectors[model]) > 0])
    )
    baseline_effect_vectors = {model: baseline_vectors[model] - control for model in available_models}
    baseline_mean_pairwise_corr_effect = mean_pairwise_correlation([baseline_effect_vectors[model] for model in available_models])
    baseline_mean_corr_to_truth_effect = float(
        np.mean(
            [
                np.corrcoef(baseline_effect_vectors[model], effect_truth)[0, 1]
                for model in available_models
                if np.std(baseline_effect_vectors[model]) > 0
            ]
        )
    )

    model_variant_sets = []
    for model in available_models:
        model_variant_sets.append(set(avg_pred_df.loc[avg_pred_df["model"] == model, "variant_id"].astype(str)))
    common_variants = sorted(set.intersection(*model_variant_sets))

    rows: list[dict[str, object]] = []
    for variant_id in common_variants:
        part = avg_pred_df.loc[avg_pred_df["variant_id"] == variant_id].copy()
        if set(part["model"].astype(str)) != set(available_models):
            continue
        vectors = {
            str(row["model"]): pd.to_numeric(row[Q_COLS], errors="coerce").to_numpy(dtype=float)
            for _, row in part.iterrows()
        }
        effect_vectors = {model: vectors[model] - control for model in available_models}
        mean_pairwise_corr = mean_pairwise_correlation([vectors[model] for model in available_models])
        mean_corr_to_truth = float(
            np.mean([np.corrcoef(vectors[model], truth)[0, 1] for model in available_models if np.std(vectors[model]) > 0])
        )
        mean_pairwise_corr_effect = mean_pairwise_correlation([effect_vectors[model] for model in available_models])
        mean_corr_to_truth_effect = float(
            np.mean(
                [
                    np.corrcoef(effect_vectors[model], effect_truth)[0, 1]
                    for model in available_models
                    if np.std(effect_vectors[model]) > 0
                ]
            )
        )
        rows.append(
            {
                "variant_id": variant_id,
                "variant_group": str(part["variant_group"].iloc[0]),
                "count": pd.to_numeric(part["count"].iloc[0], errors="coerce"),
                "description": str(part["description"].iloc[0]),
                "mean_pairwise_corr_raw": mean_pairwise_corr,
                "delta_mean_pairwise_corr_raw_vs_baseline": mean_pairwise_corr - baseline_mean_pairwise_corr,
                "mean_corr_to_truth_raw": mean_corr_to_truth,
                "delta_mean_corr_to_truth_raw_vs_baseline": mean_corr_to_truth - baseline_mean_corr_to_truth,
                "mean_pairwise_corr_effect": mean_pairwise_corr_effect,
                "delta_mean_pairwise_corr_effect_vs_baseline": mean_pairwise_corr_effect - baseline_mean_pairwise_corr_effect,
                "mean_corr_to_truth_effect": mean_corr_to_truth_effect,
                "delta_mean_corr_to_truth_effect_vs_baseline": mean_corr_to_truth_effect - baseline_mean_corr_to_truth_effect,
            }
        )

    convergence_df = pd.DataFrame(rows).sort_values(["variant_group", "variant_id"]).reset_index(drop=True)
    metadata_conv = convergence_df.loc[convergence_df["variant_group"] == "metadata_filter"].copy()
    all_papers = convergence_df.loc[convergence_df["variant_id"] == ALL_PAPERS_VARIANT_ID].copy()
    benchmark = convergence_df.loc[convergence_df["variant_id"] == BENCHMARK_VARIANT_ID].copy()
    if metadata_conv.empty or all_papers.empty or benchmark.empty:
        raise ValueError("Expected metadata-filter variants plus all-papers and benchmark variants in the convergence dataset.")

    best_metadata_accuracy = metadata_conv.sort_values("mean_corr_to_truth_raw", ascending=False).iloc[0]
    best_metadata_convergence = metadata_conv.sort_values("delta_mean_pairwise_corr_raw_vs_baseline", ascending=False).iloc[0]
    best_metadata_accuracy_effect = metadata_conv.sort_values("mean_corr_to_truth_effect", ascending=False).iloc[0]
    best_metadata_convergence_effect = metadata_conv.sort_values("delta_mean_pairwise_corr_effect_vs_baseline", ascending=False).iloc[0]

    summary_df = pd.DataFrame(
        [
            {
                "models": ",".join(available_models),
                "n_models": len(available_models),
                "n_metadata_variants": int(len(metadata_conv)),
                "baseline_mean_pairwise_corr_raw": baseline_mean_pairwise_corr,
                "baseline_mean_corr_to_truth_raw": baseline_mean_corr_to_truth,
                "baseline_mean_pairwise_corr_effect": baseline_mean_pairwise_corr_effect,
                "baseline_mean_corr_to_truth_effect": baseline_mean_corr_to_truth_effect,
                "share_metadata_variants_higher_pairwise_corr_raw": float(
                    (metadata_conv["delta_mean_pairwise_corr_raw_vs_baseline"] > 0).mean()
                ),
                "share_metadata_variants_higher_pairwise_corr_effect": float(
                    (metadata_conv["delta_mean_pairwise_corr_effect_vs_baseline"] > 0).mean()
                ),
                "mean_metadata_delta_pairwise_corr_raw": float(metadata_conv["delta_mean_pairwise_corr_raw_vs_baseline"].mean()),
                "median_metadata_delta_pairwise_corr_raw": float(metadata_conv["delta_mean_pairwise_corr_raw_vs_baseline"].median()),
                "mean_metadata_delta_corr_to_truth_raw": float(metadata_conv["delta_mean_corr_to_truth_raw_vs_baseline"].mean()),
                "mean_metadata_delta_pairwise_corr_effect": float(metadata_conv["delta_mean_pairwise_corr_effect_vs_baseline"].mean()),
                "median_metadata_delta_pairwise_corr_effect": float(metadata_conv["delta_mean_pairwise_corr_effect_vs_baseline"].median()),
                "mean_metadata_delta_corr_to_truth_effect": float(metadata_conv["delta_mean_corr_to_truth_effect_vs_baseline"].mean()),
                "spearman_metadata_delta_corr_raw_vs_delta_truth_corr_raw": spearman_corr(
                    metadata_conv["delta_mean_pairwise_corr_raw_vs_baseline"].to_numpy(dtype=float),
                    metadata_conv["delta_mean_corr_to_truth_raw_vs_baseline"].to_numpy(dtype=float),
                ),
                "pearson_metadata_delta_corr_raw_vs_delta_truth_corr_raw": pearson_corr(
                    metadata_conv["delta_mean_pairwise_corr_raw_vs_baseline"].to_numpy(dtype=float),
                    metadata_conv["delta_mean_corr_to_truth_raw_vs_baseline"].to_numpy(dtype=float),
                ),
                "spearman_metadata_delta_corr_effect_vs_delta_truth_corr_effect": spearman_corr(
                    metadata_conv["delta_mean_pairwise_corr_effect_vs_baseline"].to_numpy(dtype=float),
                    metadata_conv["delta_mean_corr_to_truth_effect_vs_baseline"].to_numpy(dtype=float),
                ),
                "pearson_metadata_delta_corr_effect_vs_delta_truth_corr_effect": pearson_corr(
                    metadata_conv["delta_mean_pairwise_corr_effect_vs_baseline"].to_numpy(dtype=float),
                    metadata_conv["delta_mean_corr_to_truth_effect_vs_baseline"].to_numpy(dtype=float),
                ),
                "all_papers_delta_pairwise_corr_raw": float(all_papers["delta_mean_pairwise_corr_raw_vs_baseline"].iloc[0]),
                "all_papers_delta_corr_to_truth_raw": float(all_papers["delta_mean_corr_to_truth_raw_vs_baseline"].iloc[0]),
                "all_papers_delta_pairwise_corr_effect": float(all_papers["delta_mean_pairwise_corr_effect_vs_baseline"].iloc[0]),
                "all_papers_delta_corr_to_truth_effect": float(all_papers["delta_mean_corr_to_truth_effect_vs_baseline"].iloc[0]),
                "benchmark_delta_pairwise_corr_raw": float(benchmark["delta_mean_pairwise_corr_raw_vs_baseline"].iloc[0]),
                "benchmark_delta_corr_to_truth_raw": float(benchmark["delta_mean_corr_to_truth_raw_vs_baseline"].iloc[0]),
                "benchmark_delta_pairwise_corr_effect": float(benchmark["delta_mean_pairwise_corr_effect_vs_baseline"].iloc[0]),
                "benchmark_delta_corr_to_truth_effect": float(benchmark["delta_mean_corr_to_truth_effect_vs_baseline"].iloc[0]),
                "best_metadata_accuracy_variant_id": str(best_metadata_accuracy["variant_id"]),
                "best_metadata_accuracy_corr": float(best_metadata_accuracy["mean_corr_to_truth_raw"]),
                "best_metadata_convergence_variant_id": str(best_metadata_convergence["variant_id"]),
                "best_metadata_convergence_delta_pairwise_corr": float(best_metadata_convergence["delta_mean_pairwise_corr_raw_vs_baseline"]),
                "best_metadata_accuracy_effect_variant_id": str(best_metadata_accuracy_effect["variant_id"]),
                "best_metadata_accuracy_effect_corr": float(best_metadata_accuracy_effect["mean_corr_to_truth_effect"]),
                "best_metadata_convergence_effect_variant_id": str(best_metadata_convergence_effect["variant_id"]),
                "best_metadata_convergence_effect_delta_pairwise_corr": float(
                    best_metadata_convergence_effect["delta_mean_pairwise_corr_effect_vs_baseline"]
                ),
            }
        ]
    )

    baseline_matrix = pairwise_correlation_matrix(baseline_vectors, available_models)
    baseline_effect_matrix = pairwise_correlation_matrix(baseline_effect_vectors, available_models)
    all_papers_vectors = {
        model: pd.to_numeric(
            avg_pred_df.loc[
                (avg_pred_df["model"] == model) & (avg_pred_df["variant_id"] == ALL_PAPERS_VARIANT_ID),
                Q_COLS,
            ].iloc[0],
            errors="coerce",
        ).to_numpy(dtype=float)
        for model in available_models
    }
    all_papers_matrix = pairwise_correlation_matrix(all_papers_vectors, available_models)
    all_papers_effect_vectors = {model: all_papers_vectors[model] - control for model in available_models}
    all_papers_effect_matrix = pairwise_correlation_matrix(all_papers_effect_vectors, available_models)
    benchmark_vectors = {
        model: pd.to_numeric(
            avg_pred_df.loc[
                (avg_pred_df["model"] == model) & (avg_pred_df["variant_id"] == BENCHMARK_VARIANT_ID),
                Q_COLS,
            ].iloc[0],
            errors="coerce",
        ).to_numpy(dtype=float)
        for model in available_models
    }
    benchmark_matrix = pairwise_correlation_matrix(benchmark_vectors, available_models)
    benchmark_effect_vectors = {model: benchmark_vectors[model] - control for model in available_models}
    benchmark_effect_matrix = pairwise_correlation_matrix(benchmark_effect_vectors, available_models)
    return (
        convergence_df,
        summary_df,
        baseline_matrix,
        all_papers_matrix,
        benchmark_matrix,
        baseline_effect_matrix,
        all_papers_effect_matrix,
        benchmark_effect_matrix,
    )


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    metadata_index = load_metadata_filter_index()
    metadata_avg_df = load_metadata_filter_avg_predictions(metadata_index)
    if metadata_avg_df.empty:
        raise ValueError("No metadata-filter prediction files were found or parsed.")

    metadata_models = [model for model in MODEL_ORDER if model in set(metadata_avg_df["model"].astype(str))]
    all_papers_avg_df = load_reference_avg_predictions(metadata_models, ALL_PAPERS_VARIANT_ID, "all_papers")
    benchmark_avg_df = load_reference_avg_predictions(metadata_models, BENCHMARK_VARIANT_ID, "benchmark_report")
    baseline_avg_df = load_baseline_avg_predictions(metadata_models)

    available_models = [
        model
        for model in MODEL_ORDER
        if model in set(metadata_avg_df["model"].astype(str))
        and model in set(all_papers_avg_df["model"].astype(str))
        and model in set(benchmark_avg_df["model"].astype(str))
        and model in set(baseline_avg_df["model"].astype(str))
    ]
    if len(available_models) < 2:
        raise ValueError("Need at least two models with metadata-filter, baseline, and all-papers coverage.")

    metadata_avg_df = metadata_avg_df.loc[metadata_avg_df["model"].isin(available_models)].copy()
    all_papers_avg_df = all_papers_avg_df.loc[all_papers_avg_df["model"].isin(available_models)].copy()
    benchmark_avg_df = benchmark_avg_df.loc[benchmark_avg_df["model"].isin(available_models)].copy()
    baseline_avg_df = baseline_avg_df.loc[baseline_avg_df["model"].isin(available_models)].copy()
    avg_pred_df = pd.concat([metadata_avg_df, all_papers_avg_df, benchmark_avg_df], ignore_index=True, sort=False)
    avg_pred_df["model"] = pd.Categorical(avg_pred_df["model"], categories=MODEL_ORDER, ordered=True)
    avg_pred_df = avg_pred_df.sort_values(["model", "variant_group", "variant_id"]).reset_index(drop=True)

    truth, control, learning_mean = load_truth_arrays()
    rows_df = build_rows(avg_pred_df, baseline_avg_df, truth, control, learning_mean)
    summary_df = summarize_rows(rows_df)
    top_variants_df = build_top_variants(rows_df)
    (
        convergence_df,
        convergence_summary_df,
        baseline_matrix,
        all_papers_matrix,
        benchmark_matrix,
        baseline_effect_matrix,
        all_papers_effect_matrix,
        benchmark_effect_matrix,
    ) = build_convergence_outputs(
        avg_pred_df,
        baseline_avg_df,
        available_models,
    )

    avg_pred_df.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_avg_predictions.csv",
        index=False,
    )
    baseline_avg_df.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_baseline_avg_predictions.csv",
        index=False,
    )
    rows_df.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_rows.csv",
        index=False,
    )
    summary_df.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_summary.csv",
        index=False,
    )
    top_variants_df.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_top_variants.csv",
        index=False,
    )
    convergence_df.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_convergence_dataset.csv",
        index=False,
    )
    convergence_summary_df.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_convergence_summary.csv",
        index=False,
    )
    baseline_matrix.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_baseline_pairwise_corr.csv",
        index=True,
    )
    all_papers_matrix.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_all_papers_pairwise_corr.csv",
        index=True,
    )
    benchmark_matrix.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_benchmark_pairwise_corr.csv",
        index=True,
    )
    baseline_effect_matrix.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_baseline_treatment_effect_pairwise_corr.csv",
        index=True,
    )
    all_papers_effect_matrix.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_all_papers_treatment_effect_pairwise_corr.csv",
        index=True,
    )
    benchmark_effect_matrix.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_benchmark_treatment_effect_pairwise_corr.csv",
        index=True,
    )


if __name__ == "__main__":
    main()
