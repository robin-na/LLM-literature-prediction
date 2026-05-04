from __future__ import annotations

from itertools import combinations
from pathlib import Path
import sys

import numpy as np
import pandas as pd
from scipy import stats

ANALYSIS_ROOT = Path(__file__).resolve().parents[1]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from analyze_validation_collection_analysis_reports_repeat5 import (
    Q_COLS,
    compute_metrics,
    load_learning_treatment_mean,
    load_truth,
)
from jsonl_parser import jsonl_to_dataframe


ROOT = Path(__file__).resolve().parents[2]
GEMINI_BATCH_OUTPUT = ROOT / "gemini_batch_output"
RESULTS_DIR = ROOT / "results" / "validation" / "gemini_literature_baseline_benchmark_repeat5"
FIGURE2_RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_mean_repeat_correlation"
EXISTING_REPEAT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5_model_sampling"
    / "validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_rows.csv"
)
EXISTING_COMPARISON_CSV = (
    ROOT
    / "results"
    / "paper"
    / "main_text_figures_mean_repeat_correlation"
    / "figure2_benchmark_report_vs_baseline_correlation_comparison_vs_avg_prediction.csv"
)

MODEL_SPECS = [
    {
        "model": "Gemini 2.5 Flash",
        "path": GEMINI_BATCH_OUTPUT / "prediction_literature_baseline-benchmark_joint_reps1to5_gemini25flash.jsonl",
    },
    {
        "model": "Gemini 2.5 Pro",
        "path": GEMINI_BATCH_OUTPUT / "prediction_literature_baseline-benchmark_joint_reps1to5_gemini25pro.jsonl",
    },
]


def summarize_series(values: pd.Series, *, conf_level: float = 0.95) -> dict[str, float]:
    arr = values.to_numpy(dtype=float)
    arr = arr[np.isfinite(arr)]
    n = int(arr.size)
    if n == 0:
        return {
            "count": 0,
            "mean": float("nan"),
            "sd": float("nan"),
            "se": float("nan"),
            "ci_low": float("nan"),
            "ci_high": float("nan"),
        }
    mean = float(arr.mean())
    if n == 1:
        return {
            "count": 1,
            "mean": mean,
            "sd": float("nan"),
            "se": float("nan"),
            "ci_low": mean,
            "ci_high": mean,
        }
    sd = float(arr.std(ddof=1))
    se = float(sd / np.sqrt(n))
    tcrit = float(stats.t.ppf((1.0 + conf_level) / 2.0, df=n - 1))
    return {
        "count": n,
        "mean": mean,
        "sd": sd,
        "se": se,
        "ci_low": mean - tcrit * se,
        "ci_high": mean + tcrit * se,
    }


def summarize_paired_difference(
    baseline: pd.Series,
    benchmark: pd.Series,
    *,
    conf_level: float = 0.95,
) -> dict[str, float | str]:
    diff = (benchmark - baseline).to_numpy(dtype=float)
    diff = diff[np.isfinite(diff)]
    summary = summarize_series(pd.Series(diff), conf_level=conf_level)
    out: dict[str, float | str] = {
        "count": summary["count"],
        "delta_mean": summary["mean"],
        "delta_sd": summary["sd"],
        "delta_se": summary["se"],
        "delta_ci_low": summary["ci_low"],
        "delta_ci_high": summary["ci_high"],
    }
    if summary["count"] >= 2:
        t_res = stats.ttest_1samp(diff, popmean=0.0)
        out["pvalue"] = float(t_res.pvalue)
        out["paired_sig_label"] = "*" if summary["ci_low"] > 0.0 or summary["ci_high"] < 0.0 else "n.s."
    else:
        out["pvalue"] = float("nan")
        out["paired_sig_label"] = "n.s."
    return out


def add_bh_adjustment(df: pd.DataFrame, *, group_col: str, p_col: str) -> pd.DataFrame:
    out = df.copy()
    out["pvalue_bh"] = np.nan
    out["bh_reject_0_05"] = False
    for group_value in out[group_col].dropna().unique():
        mask = out[group_col] == group_value
        pvals = out.loc[mask, p_col].to_numpy(dtype=float)
        if pvals.size == 0:
            continue
        order = np.argsort(pvals)
        ranked = pvals[order]
        m = float(len(ranked))
        adjusted = np.empty_like(ranked)
        adjusted[-1] = ranked[-1]
        for i in range(len(ranked) - 1, -1, -1):
            rank = i + 1.0
            candidate = ranked[i] * m / rank
            adjusted[i] = candidate if i == len(ranked) - 1 else min(candidate, adjusted[i + 1])
        adjusted = np.clip(adjusted, 0.0, 1.0)
        restored = np.empty_like(adjusted)
        restored[order] = adjusted
        out.loc[mask, "pvalue_bh"] = restored
        out.loc[mask, "bh_reject_0_05"] = restored <= 0.05
    return out


def _baseline_ids() -> list[str]:
    return [f"baseline_joint_reasoning_rep{i}" for i in range(1, 6)]


def _benchmark_ids() -> list[str]:
    return [f"paper_analysis_report_joint_rep{i}/PGG_MS_202502" for i in range(1, 6)]


def _mean_prediction_metrics(rows: pd.DataFrame) -> dict[str, float]:
    treatment, control = load_truth()
    learning_mean = load_learning_treatment_mean()
    mean_row = rows.loc[:, Q_COLS].mean(axis=0)
    metrics = compute_metrics(mean_row, treatment, control, learning_mean)
    return {key: float(value) for key, value in metrics.items() if key != "n"}


def load_gemini_repeat_rows() -> pd.DataFrame:
    treatment, control = load_truth()
    learning_mean = load_learning_treatment_mean()
    rows: list[dict[str, object]] = []

    for spec in MODEL_SPECS:
        path = Path(spec["path"])
        if not path.exists():
            raise FileNotFoundError(path)
        source_df = jsonl_to_dataframe(path, platform="gemini").reindex(columns=Q_COLS)
        for condition, row_ids in [("baseline", _baseline_ids()), ("benchmark", _benchmark_ids())]:
            missing = [row_id for row_id in row_ids if row_id not in source_df.index]
            if missing:
                raise KeyError(f"Missing {condition} rows for {spec['model']}: {missing}")
            for repeat_index, row_id in enumerate(row_ids, start=1):
                pred_row = pd.to_numeric(source_df.loc[row_id], errors="coerce").reindex(Q_COLS)
                metrics = compute_metrics(pred_row, treatment, control, learning_mean)
                row: dict[str, object] = {
                    "model": spec["model"],
                    "condition": condition,
                    "repeat": repeat_index,
                    "row_id": row_id,
                    **metrics,
                }
                row.update({q: float(pred_row[q]) for q in Q_COLS})
                rows.append(row)

    out = pd.DataFrame(rows)
    return out.sort_values(["condition", "model", "repeat"]).reset_index(drop=True)


def build_gemini_condition_summary(repeat_rows: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    plot_rows: list[dict[str, object]] = []
    comparison_rows: list[dict[str, object]] = []

    for model in [str(spec["model"]) for spec in MODEL_SPECS]:
        sub = repeat_rows.loc[repeat_rows["model"] == model].copy()
        by_condition: dict[str, dict[str, float]] = {}
        avg_metrics: dict[str, dict[str, float]] = {}
        for condition in ["baseline", "benchmark"]:
            cond_rows = sub.loc[sub["condition"] == condition].copy()
            cond_summary = summarize_series(cond_rows["correlation"])
            by_condition[condition] = cond_summary
            avg_metrics[condition] = _mean_prediction_metrics(cond_rows)
            plot_rows.append(
                {
                    "model": model,
                    "condition": condition,
                    "correlation": cond_summary["mean"],
                    "repeat_sd": cond_summary["sd"],
                    "repeat_se": cond_summary["se"],
                    "ci_low": cond_summary["ci_low"],
                    "ci_high": cond_summary["ci_high"],
                    "n_repeats": cond_summary["count"],
                }
            )

        paired = (
            sub.loc[:, ["repeat", "condition", "correlation"]]
            .pivot(index="repeat", columns="condition", values="correlation")
            .dropna()
        )
        paired_summary = summarize_paired_difference(paired["baseline"], paired["benchmark"])
        comparison_rows.append(
            {
                "model": model,
                "baseline_avg_prediction_correlation": avg_metrics["baseline"]["correlation"],
                "baseline_mean_repeat_correlation": by_condition["baseline"]["mean"],
                "baseline_shift_mean_repeat_minus_avg_prediction": (
                    by_condition["baseline"]["mean"] - avg_metrics["baseline"]["correlation"]
                ),
                "benchmark_avg_prediction_correlation": avg_metrics["benchmark"]["correlation"],
                "benchmark_mean_repeat_correlation": by_condition["benchmark"]["mean"],
                "benchmark_shift_mean_repeat_minus_avg_prediction": (
                    by_condition["benchmark"]["mean"] - avg_metrics["benchmark"]["correlation"]
                ),
                "delta_avg_prediction_correlation": (
                    avg_metrics["benchmark"]["correlation"] - avg_metrics["baseline"]["correlation"]
                ),
                "delta_mean_repeat_correlation": paired_summary["delta_mean"],
                "delta_shift_mean_repeat_minus_avg_prediction": (
                    float(paired_summary["delta_mean"])
                    - (avg_metrics["benchmark"]["correlation"] - avg_metrics["baseline"]["correlation"])
                ),
            }
        )

    return pd.DataFrame(plot_rows), pd.DataFrame(comparison_rows)


def build_figure2_tables(
    all_repeat_rows: pd.DataFrame,
    all_comparison_rows: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    plot_rows: list[dict[str, object]] = []
    delta_rows: list[dict[str, object]] = []

    model_order = (
        all_repeat_rows.loc[all_repeat_rows["condition"] == "baseline"]
        .groupby("model", observed=False)["correlation"]
        .mean()
        .sort_values(ascending=False)
        .index.tolist()
    )

    for model in model_order:
        sub = all_repeat_rows.loc[all_repeat_rows["model"] == model].copy()
        by_condition: dict[str, dict[str, float]] = {}
        for condition in ["baseline", "benchmark"]:
            cond_summary = summarize_series(sub.loc[sub["condition"] == condition, "correlation"])
            by_condition[condition] = cond_summary
            plot_rows.append(
                {
                    "model": model,
                    "condition": condition,
                    "correlation": cond_summary["mean"],
                    "repeat_sd": cond_summary["sd"],
                    "repeat_se": cond_summary["se"],
                    "ci_low": cond_summary["ci_low"],
                    "ci_high": cond_summary["ci_high"],
                    "n_repeats": cond_summary["count"],
                }
            )

        paired = (
            sub.loc[:, ["repeat", "condition", "correlation"]]
            .pivot(index="repeat", columns="condition", values="correlation")
            .dropna()
        )
        paired_summary = summarize_paired_difference(paired["baseline"], paired["benchmark"])
        delta_rows.append(
            {
                "model": model,
                "baseline_mean_repeat_correlation": by_condition["baseline"]["mean"],
                "benchmark_mean_repeat_correlation": by_condition["benchmark"]["mean"],
                "delta_mean_repeat_correlation": paired_summary["delta_mean"],
                "delta_repeat_ci_low": paired_summary["delta_ci_low"],
                "delta_repeat_ci_high": paired_summary["delta_ci_high"],
                "delta_repeat_sd": paired_summary["delta_sd"],
                "delta_repeat_se": paired_summary["delta_se"],
                "n_repeats": paired_summary["count"],
                "repeat_pvalue": paired_summary["pvalue"],
                "paired_sig_label": paired_summary["paired_sig_label"],
            }
        )

    plot_df = pd.DataFrame(plot_rows)
    plot_df["model"] = pd.Categorical(plot_df["model"], categories=model_order, ordered=True)
    plot_df = plot_df.sort_values(["model", "condition"]).reset_index(drop=True)

    delta_df = pd.DataFrame(delta_rows)
    delta_df["model"] = pd.Categorical(delta_df["model"], categories=model_order, ordered=True)
    delta_df = delta_df.sort_values("model").reset_index(drop=True)

    comparison_df = all_comparison_rows.copy()
    comparison_df["model"] = pd.Categorical(comparison_df["model"], categories=model_order, ordered=True)
    comparison_df = comparison_df.sort_values("model").reset_index(drop=True)

    repeat_detail = all_repeat_rows.loc[:, ["model", "condition", "repeat", "correlation"]].copy()
    repeat_detail["model"] = pd.Categorical(repeat_detail["model"], categories=model_order, ordered=True)
    repeat_detail = repeat_detail.sort_values(["model", "condition", "repeat"]).reset_index(drop=True)

    pairwise_rows: list[dict[str, object]] = []
    global_rows: list[dict[str, object]] = []
    for condition in ["baseline", "benchmark"]:
        part = all_repeat_rows.loc[all_repeat_rows["condition"] == condition, ["model", "correlation"]].copy()
        groups = [g["correlation"].to_numpy(dtype=float) for _, g in part.groupby("model", sort=True)]
        anova_f, anova_p = stats.f_oneway(*groups)
        kruskal_h, kruskal_p = stats.kruskal(*groups)
        global_rows.append(
            {
                "condition": condition,
                "n_models": int(part["model"].nunique()),
                "n_repeats_per_model": int(part.groupby("model").size().min()),
                "anova_f": float(anova_f),
                "anova_pvalue": float(anova_p),
                "kruskal_h": float(kruskal_h),
                "kruskal_pvalue": float(kruskal_p),
            }
        )

        model_to_values = {
            model: sub["correlation"].to_numpy(dtype=float)
            for model, sub in part.groupby("model", sort=True)
        }
        for model_a, model_b in combinations(sorted(model_to_values), 2):
            vals_a = model_to_values[model_a]
            vals_b = model_to_values[model_b]
            mean_diff = float(vals_a.mean() - vals_b.mean())
            n_a = len(vals_a)
            n_b = len(vals_b)
            var_a = float(np.var(vals_a, ddof=1))
            var_b = float(np.var(vals_b, ddof=1))
            se = float(np.sqrt(var_a / n_a + var_b / n_b))
            df_num = (var_a / n_a + var_b / n_b) ** 2
            df_den = ((var_a / n_a) ** 2) / (n_a - 1) + ((var_b / n_b) ** 2) / (n_b - 1)
            welch_df = float(df_num / df_den) if df_den > 0 else float("nan")
            tcrit = float(stats.t.ppf(0.975, welch_df)) if np.isfinite(welch_df) else float("nan")
            ci_low = mean_diff - tcrit * se if np.isfinite(tcrit) else float("nan")
            ci_high = mean_diff + tcrit * se if np.isfinite(tcrit) else float("nan")
            pairwise_rows.append(
                {
                    "condition": condition,
                    "model_a": model_a,
                    "model_b": model_b,
                    "mean_diff_a_minus_b": mean_diff,
                    "ci95_low": ci_low,
                    "ci95_high": ci_high,
                    "welch_df": welch_df,
                    "pvalue": float(stats.ttest_ind(vals_a, vals_b, equal_var=False).pvalue),
                    "ci95_excludes_zero": bool(
                        np.isfinite(ci_low) and np.isfinite(ci_high) and (ci_low > 0.0 or ci_high < 0.0)
                    ),
                }
            )

    pairwise_df = add_bh_adjustment(pd.DataFrame(pairwise_rows), group_col="condition", p_col="pvalue")
    pairwise_df["model_a"] = pd.Categorical(pairwise_df["model_a"], categories=model_order, ordered=True)
    pairwise_df["model_b"] = pd.Categorical(pairwise_df["model_b"], categories=model_order, ordered=True)
    pairwise_df = pairwise_df.sort_values(["condition", "model_a", "model_b"]).reset_index(drop=True)

    global_df = pd.DataFrame(global_rows).sort_values("condition").reset_index(drop=True)
    return plot_df, delta_df, comparison_df, pairwise_df, global_df, repeat_detail


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE2_RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    gemini_repeat_rows = load_gemini_repeat_rows()
    gemini_plot_rows, gemini_comparison_rows = build_gemini_condition_summary(gemini_repeat_rows)

    gemini_repeat_rows.to_csv(RESULTS_DIR / "gemini_literature_baseline_benchmark_repeat_rows.csv", index=False)
    gemini_plot_rows.to_csv(RESULTS_DIR / "gemini_literature_baseline_benchmark_plot_rows.csv", index=False)
    gemini_comparison_rows.to_csv(
        RESULTS_DIR / "gemini_literature_baseline_benchmark_comparison_vs_avg_prediction.csv",
        index=False,
    )

    existing_repeat_rows = pd.read_csv(EXISTING_REPEAT_ROWS_CSV)
    existing_comparison_rows = pd.read_csv(EXISTING_COMPARISON_CSV)

    all_repeat_rows = pd.concat([existing_repeat_rows, gemini_repeat_rows], ignore_index=True)
    all_comparison_rows = pd.concat([existing_comparison_rows, gemini_comparison_rows], ignore_index=True)

    plot_df, delta_df, comparison_df, pairwise_df, global_df, repeat_detail = build_figure2_tables(
        all_repeat_rows,
        all_comparison_rows,
    )

    plot_df.to_csv(
        FIGURE2_RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_plot_rows_with_gemini.csv",
        index=False,
    )
    delta_df.to_csv(
        FIGURE2_RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_summary_with_gemini.csv",
        index=False,
    )
    comparison_df.to_csv(
        FIGURE2_RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_comparison_vs_avg_prediction_with_gemini.csv",
        index=False,
    )
    pairwise_df.to_csv(
        FIGURE2_RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_pairwise_model_differences_with_gemini.csv",
        index=False,
    )
    global_df.to_csv(
        FIGURE2_RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_global_model_tests_with_gemini.csv",
        index=False,
    )
    repeat_detail.to_csv(
        FIGURE2_RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_repeat_rows_with_gemini.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
