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
LEARN_DF = ROOT / "science_data" / "data" / "processed_data" / "df_paired_learn.csv"
COLLECTION_REPORT_INDEX_CSV = (
    ROOT / "literature" / "output" / "collection_analysis_reports" / "switch_sets_stage1" / "report_index.csv"
)
BENCHMARK_REPORT_PATH = (
    ROOT
    / "literature"
    / "output"
    / "paper_analysis_reports"
    / "strict_predictive_empirical_payoff"
    / "PGG_MS_202502.md"
)
BENCHMARK_FULL_PAPER_PATH = ROOT / "paper_collection" / "papers_markdown_cleaned" / "PGG_MS_202502.md"

RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_repeat5"

Q_COLS = [f"Q{i}" for i in range(1, 21)]
METRIC_ORDER = ["rmse", "correlation", "r2", "directional_accuracy"]
LOWER_IS_BETTER = {"rmse"}

RUN_SPECS = [
    {
        "model": "GPT-4.1",
        "mode": "joint_reasoning",
        "collection_initial_path": OPENAI_BATCH_OUTPUT / "prediction_literature_collection_analysis_report_stage1_9variants_joint_41.jsonl",
        "collection_repeat_path": OPENAI_BATCH_OUTPUT / "prediction_literature_collection_plus_pggms_joint_reps2to5_41.jsonl",
        "benchmark_initial_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_strict243_joint_41.jsonl",
        "baseline_initial_path": OPENAI_BATCH_OUTPUT / "prediction_positive_case_variations_41.jsonl",
        "baseline_repeat_path": OPENAI_BATCH_OUTPUT / "prediction_positive_case_reasoning_repeats_41.jsonl",
        "baseline_initial_id": "baseline_joint_reasoning",
        "baseline_repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 5)],
        "collection_initial_template": "collection_analysis_report_joint/{variant_id}",
        "collection_repeat_template": "collection_analysis_report_joint_rep{rep}/{variant_id}",
        "benchmark_variant_id": "benchmark_pgg_ms",
        "benchmark_initial_id": "paper_analysis_report_joint/PGG_MS_202502",
        "benchmark_repeat_template": "paper_analysis_report_joint_rep{rep}/PGG_MS_202502",
        "full_benchmark_variant_id": "benchmark_pgg_ms_full",
        "full_benchmark_path": OPENAI_BATCH_OUTPUT / "prediction_literature_fullpaper_pggms_joint_reps1to5_41.jsonl",
        "full_benchmark_ids": [f"paper_full_text_joint_rep{i}/PGG_MS_202502" for i in range(1, 6)],
    },
    {
        "model": "GPT-4.1 Mini",
        "mode": "joint_reasoning",
        "collection_initial_path": OPENAI_BATCH_OUTPUT / "prediction_literature_collection_analysis_report_stage1_9variants_joint_41mini.jsonl",
        "collection_repeat_path": OPENAI_BATCH_OUTPUT / "prediction_literature_collection_plus_pggms_joint_reps2to5_41mini.jsonl",
        "benchmark_initial_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_strict243_joint_41mini.jsonl",
        "baseline_initial_path": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41mini.jsonl",
        "baseline_repeat_path": OPENAI_BATCH_OUTPUT / "prediction_positive_case_reasoning_repeats_41mini.jsonl",
        "baseline_initial_id": "baseline_joint_reasoning",
        "baseline_repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 5)],
        "collection_initial_template": "collection_analysis_report_joint/{variant_id}",
        "collection_repeat_template": "collection_analysis_report_joint_rep{rep}/{variant_id}",
        "benchmark_variant_id": "benchmark_pgg_ms",
        "benchmark_initial_id": "paper_analysis_report_joint/PGG_MS_202502",
        "benchmark_repeat_template": "paper_analysis_report_joint_rep{rep}/PGG_MS_202502",
        "full_benchmark_variant_id": "benchmark_pgg_ms_full",
        "full_benchmark_path": OPENAI_BATCH_OUTPUT / "prediction_literature_fullpaper_pggms_joint_reps1to5_41mini.jsonl",
        "full_benchmark_ids": [f"paper_full_text_joint_rep{i}/PGG_MS_202502" for i in range(1, 6)],
    },
    {
        "model": "GPT-4.1 Nano",
        "mode": "joint_reasoning",
        "collection_initial_path": OPENAI_BATCH_OUTPUT / "prediction_literature_collection_analysis_report_stage1_9variants_joint_41nano.jsonl",
        "collection_repeat_path": OPENAI_BATCH_OUTPUT / "prediction_literature_collection_plus_pggms_joint_reps2to5_41nano.jsonl",
        "benchmark_initial_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_strict243_joint_41nano.jsonl",
        "baseline_initial_path": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41nano.jsonl",
        "baseline_repeat_path": OPENAI_BATCH_OUTPUT / "prediction_positive_case_reasoning_repeats_41nano.jsonl",
        "baseline_initial_id": "baseline_joint_reasoning",
        "baseline_repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 5)],
        "collection_initial_template": "collection_analysis_report_joint/{variant_id}",
        "collection_repeat_template": "collection_analysis_report_joint_rep{rep}/{variant_id}",
        "benchmark_variant_id": "benchmark_pgg_ms",
        "benchmark_initial_id": "paper_analysis_report_joint/PGG_MS_202502",
        "benchmark_repeat_template": "paper_analysis_report_joint_rep{rep}/PGG_MS_202502",
        "full_benchmark_variant_id": "benchmark_pgg_ms_full",
        "full_benchmark_path": OPENAI_BATCH_OUTPUT / "prediction_literature_fullpaper_pggms_joint_reps1to5_41nano.jsonl",
        "full_benchmark_ids": [f"paper_full_text_joint_rep{i}/PGG_MS_202502" for i in range(1, 6)],
    },
    {
        "model": "GPT-5.1",
        "mode": "joint_reasoning",
        "suite_path": OPENAI_BATCH_OUTPUT / "prediction_literature_joint_suite_reps1to5_gpt51.jsonl",
        "baseline_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 6)],
        "collection_repeat_template": "collection_analysis_report_joint_rep{rep}/{variant_id}",
        "collection_rep_range": range(1, 6),
        "benchmark_variant_id": "benchmark_pgg_ms",
        "benchmark_ids": [f"paper_analysis_report_joint_rep{i}/PGG_MS_202502" for i in range(1, 6)],
        "full_benchmark_variant_id": "benchmark_pgg_ms_full",
        "full_benchmark_path": OPENAI_BATCH_OUTPUT / "prediction_literature_fullpaper_pggms_joint_reps1to5_gpt51.jsonl",
        "full_benchmark_ids": [f"paper_full_text_joint_rep{i}/PGG_MS_202502" for i in range(1, 6)],
    },
    {
        "model": "GPT-5 Mini",
        "mode": "joint_reasoning",
        "suite_path": OPENAI_BATCH_OUTPUT / "prediction_literature_joint_suite_reps1to5_gpt5mini.jsonl",
        "baseline_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 6)],
        "collection_repeat_template": "collection_analysis_report_joint_rep{rep}/{variant_id}",
        "collection_rep_range": range(1, 6),
        "benchmark_variant_id": "benchmark_pgg_ms",
        "benchmark_ids": [f"paper_analysis_report_joint_rep{i}/PGG_MS_202502" for i in range(1, 6)],
        "full_benchmark_variant_id": "benchmark_pgg_ms_full",
        "full_benchmark_path": OPENAI_BATCH_OUTPUT / "prediction_literature_fullpaper_pggms_joint_reps1to5_gpt5mini.jsonl",
        "full_benchmark_ids": [f"paper_full_text_joint_rep{i}/PGG_MS_202502" for i in range(1, 6)],
    },
    {
        "model": "GPT-5 Nano",
        "mode": "joint_reasoning",
        "suite_path": OPENAI_BATCH_OUTPUT / "prediction_literature_joint_suite_reps1to5_gpt5nano.jsonl",
        "baseline_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 6)],
        "collection_repeat_template": "collection_analysis_report_joint_rep{rep}/{variant_id}",
        "collection_rep_range": range(1, 6),
        "benchmark_variant_id": "benchmark_pgg_ms",
        "benchmark_ids": [f"paper_analysis_report_joint_rep{i}/PGG_MS_202502" for i in range(1, 6)],
        "full_benchmark_variant_id": "benchmark_pgg_ms_full",
        "full_benchmark_path": OPENAI_BATCH_OUTPUT / "prediction_literature_fullpaper_pggms_joint_reps1to5_gpt5nano.jsonl",
        "full_benchmark_ids": [f"paper_full_text_joint_rep{i}/PGG_MS_202502" for i in range(1, 6)],
    },
]


def load_truth() -> tuple[pd.Series, pd.Series]:
    df = pd.read_csv(INPUT / "pgg_CONFIGmerged_validation.csv").sort_values("CONFIG_configId")
    treatment = pd.Series(df["efficiency_p"].to_numpy(dtype=float) * 100.0, index=Q_COLS)
    control = pd.Series(df["efficiency_np"].to_numpy(dtype=float) * 100.0, index=Q_COLS)
    return treatment, control


def load_learning_treatment_mean() -> float:
    df = pd.read_csv(LEARN_DF)
    return float(df["treatment_itt_efficiency"].mean() * 100.0)


def _r2_np(pred: np.ndarray, truth: np.ndarray, learning_mean: np.ndarray) -> float:
    if pred.size == 0:
        return float("nan")
    mse = float(np.mean((pred - truth) ** 2))
    null_mse = float(np.mean((truth - learning_mean) ** 2))
    if null_mse <= 0:
        return float("nan")
    return float(1.0 - mse / null_mse)


def compute_metrics(
    pred_row: pd.Series,
    treatment: pd.Series,
    control: pd.Series,
    learning_mean: float,
) -> dict[str, float | int]:
    pred = pd.to_numeric(pred_row, errors="coerce").reindex(Q_COLS)
    truth = treatment.reindex(Q_COLS)
    ctrl = control.reindex(Q_COLS)
    learning = pd.Series(float(learning_mean), index=Q_COLS)

    pred_arr = pred.to_numpy(dtype=float)
    truth_arr = truth.to_numpy(dtype=float)
    ctrl_arr = ctrl.to_numpy(dtype=float)
    learning_arr = learning.to_numpy(dtype=float)
    mask = ~np.isnan(pred_arr) & ~np.isnan(truth_arr) & ~np.isnan(ctrl_arr) & ~np.isnan(learning_arr)
    if mask.sum() == 0:
        return {"n": 0, "rmse": np.nan, "correlation": np.nan, "r2": np.nan, "directional_accuracy": np.nan}

    pred_sub = pred_arr[mask]
    truth_sub = truth_arr[mask]
    ctrl_sub = ctrl_arr[mask]
    learning_sub = learning_arr[mask]
    return {
        "n": int(mask.sum()),
        "rmse": _rmse_np(pred_sub, truth_sub),
        "correlation": _corr_np(pred_sub, truth_sub),
        "r2": _r2_np(pred_sub, truth_sub, learning_sub),
        "directional_accuracy": float(_directional_accuracy_np(pred_sub, truth_sub, ctrl_sub)),
    }


def compute_delta_ci(
    pred_row: pd.Series,
    baseline_row: pd.Series,
    treatment: pd.Series,
    control: pd.Series,
    learning_mean: float,
    *,
    rng: np.random.Generator,
    n_boot: int,
) -> dict[str, float]:
    pred = pd.to_numeric(pred_row, errors="coerce").reindex(Q_COLS)
    baseline = pd.to_numeric(baseline_row, errors="coerce").reindex(Q_COLS)
    truth = treatment.reindex(Q_COLS)
    ctrl = control.reindex(Q_COLS)
    learning = pd.Series(float(learning_mean), index=Q_COLS)

    pred_arr = pred.to_numpy(dtype=float)
    baseline_arr = baseline.to_numpy(dtype=float)
    truth_arr = truth.to_numpy(dtype=float)
    ctrl_arr = ctrl.to_numpy(dtype=float)
    learning_arr = learning.to_numpy(dtype=float)

    mask = ~np.isnan(pred_arr) & ~np.isnan(baseline_arr) & ~np.isnan(truth_arr) & ~np.isnan(ctrl_arr) & ~np.isnan(learning_arr)

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
        learning_arr,
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


def load_variant_metadata() -> dict[str, dict[str, object]]:
    df = pd.read_csv(COLLECTION_REPORT_INDEX_CSV)
    out: dict[str, dict[str, object]] = {}
    for row in df.to_dict("records"):
        out[str(row["variant_id"])] = {
            "variant_kind": str(row.get("variant_kind", "") or ""),
            "count": pd.to_numeric(row.get("count", np.nan), errors="coerce"),
            "description": str(row.get("description", "") or ""),
            "report_path": str(row.get("report_path", "") or ""),
        }
    out["benchmark_pgg_ms"] = {
        "variant_kind": "benchmark_paper",
        "count": 1,
        "description": "Benchmark paper describing the experiment and dataset (PGG_MS_202502).",
        "report_path": str(BENCHMARK_REPORT_PATH.relative_to(ROOT)),
    }
    out["benchmark_pgg_ms_full"] = {
        "variant_kind": "benchmark_paper_full_text",
        "count": 1,
        "description": "Benchmark paper using the full cleaned PGG_MS_202502 manuscript text directly.",
        "report_path": str(BENCHMARK_FULL_PAPER_PATH.relative_to(ROOT)),
    }
    return out


def _mean_rows(df: pd.DataFrame, row_ids: list[str]) -> pd.Series:
    rows = [pd.to_numeric(df.loc[row_id], errors="coerce").reindex(Q_COLS) for row_id in row_ids]
    mat = pd.concat(rows, axis=1)
    mat.columns = [f"run{i+1}" for i in range(len(rows))]
    return mat.mean(axis=1, skipna=True)


def _empty_q_df() -> pd.DataFrame:
    return pd.DataFrame(columns=Q_COLS, dtype=float)


def _load_source_tables(spec: dict[str, object]) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    if "suite_path" in spec:
        suite_df = jsonl_to_dataframe(spec["suite_path"]).reindex(columns=Q_COLS)
        full_path = Path(spec["full_benchmark_path"])
        full_benchmark_df = (
            jsonl_to_dataframe(full_path).reindex(columns=Q_COLS) if full_path.exists() else _empty_q_df()
        )
        return suite_df, suite_df, suite_df, full_benchmark_df

    collection_initial_df = jsonl_to_dataframe(spec["collection_initial_path"]).reindex(columns=Q_COLS)
    collection_repeat_df = jsonl_to_dataframe(spec["collection_repeat_path"]).reindex(columns=Q_COLS)
    benchmark_initial_df = jsonl_to_dataframe(spec["benchmark_initial_path"]).reindex(columns=Q_COLS)
    baseline_initial_df = jsonl_to_dataframe(spec["baseline_initial_path"]).reindex(columns=Q_COLS)
    baseline_repeat_df = jsonl_to_dataframe(spec["baseline_repeat_path"]).reindex(columns=Q_COLS)
    full_path = Path(spec["full_benchmark_path"])
    full_benchmark_df = (
        jsonl_to_dataframe(full_path).reindex(columns=Q_COLS) if full_path.exists() else _empty_q_df()
    )

    baseline_source_df = pd.concat([baseline_initial_df, baseline_repeat_df], axis=0)
    collection_source_df = pd.concat([collection_initial_df, collection_repeat_df], axis=0)
    benchmark_source_df = pd.concat([benchmark_initial_df, collection_repeat_df], axis=0)
    return baseline_source_df, collection_source_df, benchmark_source_df, full_benchmark_df


def _baseline_ids(spec: dict[str, object]) -> list[str]:
    if "baseline_ids" in spec:
        return [str(x) for x in spec["baseline_ids"]]
    return [str(spec["baseline_initial_id"]), *[str(x) for x in spec["baseline_repeat_ids"]]]


def _benchmark_ids(spec: dict[str, object]) -> list[str]:
    if "benchmark_ids" in spec:
        return [str(x) for x in spec["benchmark_ids"]]
    return [
        str(spec["benchmark_initial_id"]),
        *[str(spec["benchmark_repeat_template"]).format(rep=rep) for rep in range(2, 6)],
    ]


def _full_benchmark_ids(spec: dict[str, object]) -> list[str]:
    return [str(x) for x in spec.get("full_benchmark_ids", [])]


def _collection_ids(spec: dict[str, object], variant_id: str) -> list[str]:
    if "collection_rep_range" in spec:
        return [
            str(spec["collection_repeat_template"]).format(rep=rep, variant_id=variant_id)
            for rep in spec["collection_rep_range"]
        ]
    collection_ids = [str(spec["collection_initial_template"]).format(variant_id=variant_id)]
    collection_ids += [
        str(spec["collection_repeat_template"]).format(rep=rep, variant_id=variant_id)
        for rep in range(2, 6)
    ]
    return collection_ids


def _all_paths_exist(spec: dict[str, object]) -> bool:
    if "suite_path" in spec:
        return Path(spec["suite_path"]).exists()
    paths = [
        spec["collection_initial_path"],
        spec["collection_repeat_path"],
        spec["benchmark_initial_path"],
        spec["baseline_initial_path"],
        spec["baseline_repeat_path"],
    ]
    return all(Path(p).exists() for p in paths)


def build_average_predictions(
    metadata: dict[str, dict[str, object]],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows: list[dict[str, object]] = []
    baseline_rows: list[dict[str, object]] = []

    for spec in RUN_SPECS:
        if not _all_paths_exist(spec):
            continue

        baseline_source_df, collection_source_df, benchmark_source_df, full_benchmark_source_df = _load_source_tables(spec)
        baseline_ids = _baseline_ids(spec)
        if any(row_id not in baseline_source_df.index for row_id in baseline_ids):
            continue

        baseline_avg = _mean_rows(baseline_source_df, baseline_ids)
        baseline_rows.append(
            {
                "model": spec["model"],
                "mode": spec["mode"],
                "variant_id": "baseline_no_augmentation",
                "variant_kind": "baseline",
                "count": np.nan,
                "description": "Five-run average of the matched no-augmentation baseline.",
                "report_path": "",
                "n_runs": len(baseline_ids),
                **baseline_avg.to_dict(),
            }
        )

        for variant_id, meta in metadata.items():
            if variant_id == spec["benchmark_variant_id"]:
                benchmark_ids = _benchmark_ids(spec)
                if any(row_id not in benchmark_source_df.index for row_id in benchmark_ids):
                    continue
                avg_preds = _mean_rows(benchmark_source_df, benchmark_ids)
                n_runs = len(benchmark_ids)
            elif variant_id == spec.get("full_benchmark_variant_id"):
                full_benchmark_ids = _full_benchmark_ids(spec)
                if any(row_id not in full_benchmark_source_df.index for row_id in full_benchmark_ids):
                    continue
                avg_preds = _mean_rows(full_benchmark_source_df, full_benchmark_ids)
                n_runs = len(full_benchmark_ids)
            else:
                collection_ids = _collection_ids(spec, variant_id)
                if any(row_id not in collection_source_df.index for row_id in collection_ids):
                    continue
                avg_preds = _mean_rows(collection_source_df, collection_ids)
                n_runs = len(collection_ids)

            rows.append(
                {
                    "model": spec["model"],
                    "mode": spec["mode"],
                    "variant_id": variant_id,
                    "variant_kind": meta["variant_kind"],
                    "count": meta["count"],
                    "description": meta["description"],
                    "report_path": meta["report_path"],
                    "n_runs": n_runs,
                    **avg_preds.to_dict(),
                }
            )

    return pd.DataFrame(rows), pd.DataFrame(baseline_rows)


def build_rows(
    avg_pred_df: pd.DataFrame,
    baseline_avg_df: pd.DataFrame,
    treatment: pd.Series,
    control: pd.Series,
    learning_mean: float,
    *,
    n_boot: int = 5000,
    seed: int = 42,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    rng = np.random.default_rng(seed)

    for (model, mode), pred_part in avg_pred_df.groupby(["model", "mode"], dropna=False):
        baseline_part = baseline_avg_df[
            (baseline_avg_df["model"] == model) & (baseline_avg_df["mode"] == mode)
        ]
        if baseline_part.empty:
            continue
        baseline_row = baseline_part.iloc[0][Q_COLS]
        baseline_metrics = compute_metrics(baseline_row, treatment, control, learning_mean)

        for _, pred_rec in pred_part.iterrows():
            pred_row = pred_rec[Q_COLS]
            metrics = compute_metrics(pred_row, treatment, control, learning_mean)
            delta_ci = compute_delta_ci(
                pred_row,
                baseline_row,
                treatment,
                control,
                learning_mean,
                rng=rng,
                n_boot=n_boot,
            )

            row: dict[str, object] = {
                "model": model,
                "mode": mode,
                "variant_id": pred_rec["variant_id"],
                "variant_kind": pred_rec["variant_kind"],
                "count": pred_rec["count"],
                "description": pred_rec["description"],
                "report_path": pred_rec["report_path"],
                "n_runs": int(pred_rec["n_runs"]),
                "baseline_variation": "baseline_joint_reasoning_avg5",
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
            rec[f"best_variant_kind_{metric}"] = best["variant_kind"]
            rec[f"best_value_{metric}"] = float(best[metric])
            rec[f"best_delta_{metric}"] = float(best[f"delta_{metric}"])
            rec[f"worst_variant_{metric}"] = worst["variant_id"]
            rec[f"worst_variant_kind_{metric}"] = worst["variant_kind"]
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
    learning_mean = load_learning_treatment_mean()
    metadata = load_variant_metadata()
    avg_pred_df, baseline_avg_df = build_average_predictions(metadata)
    if avg_pred_df.empty or baseline_avg_df.empty:
        raise FileNotFoundError("No complete repeat-5 collection/benchmark prediction sets were found.")

    rows = build_rows(avg_pred_df, baseline_avg_df, treatment, control, learning_mean)
    if rows.empty:
        raise FileNotFoundError("No repeat-5 collection/benchmark rows could be evaluated.")

    ranked = rank_rows(rows)
    summary = summarize(ranked)
    top_bottom = build_top_bottom(ranked, k=3)

    avg_pred_path = RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_avg_predictions.csv"
    baseline_avg_path = RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_baseline_avg_predictions.csv"
    rows_path = RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_rows.csv"
    ranked_path = RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_ranked.csv"
    summary_path = RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_summary.csv"
    top_bottom_path = RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_top_bottom.csv"

    avg_pred_df.to_csv(avg_pred_path, index=False)
    baseline_avg_df.to_csv(baseline_avg_path, index=False)
    rows.to_csv(rows_path, index=False)
    ranked.to_csv(ranked_path, index=False)
    summary.to_csv(summary_path, index=False)
    top_bottom.to_csv(top_bottom_path, index=False)

    print(avg_pred_path)
    print(baseline_avg_path)
    print(rows_path)
    print(ranked_path)
    print(summary_path)
    print(top_bottom_path)


if __name__ == "__main__":
    main()
