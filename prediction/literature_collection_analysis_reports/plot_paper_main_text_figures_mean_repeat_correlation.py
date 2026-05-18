from __future__ import annotations

import os
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D
from scipy import stats


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_mean_repeat_correlation"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_mean_repeat_correlation"
REPEAT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5_model_sampling"
    / "validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_rows.csv"
)
HUMAN_PREDICTIONS_CSV = ROOT / "science-data_and_code" / "data" / "processed_data" / "prediction_survey.csv"
VALIDATION_CSV = ROOT / "input" / "pgg_CONFIGmerged_validation.csv"
REPEAT5_SUMMARY_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5"
    / "validation_literature_collection_analysis_report_repeat5_summary.csv"
)
REPEAT5_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5"
    / "validation_literature_collection_analysis_report_repeat5_rows.csv"
)
NO_AUG_BENCHMARKS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "no_augmentation_model_comparison"
    / "validation_no_augmentation_model_comparison_benchmarks.csv"
)

MODEL_ORDER = ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
SOURCE_ORDER = ["prolific", "sspp"]
SOURCE_LABELS = {"prolific": "Laypeople", "sspp": "Experts"}
GROUP_COLORS = {
    "Laypeople": "#caa27e",
    "Experts": "#8d6748",
}
MODEL_COLORS = {
    "GPT-4.1": "#2b8cbe",
    "GPT-4.1 Mini": "#1b9e77",
    "GPT-4.1 Nano": "#8c564b",
    "GPT-5.1": "#d95f02",
    "GPT-5 Mini": "#7570b3",
    "GPT-5 Nano": "#e7298a",
}
CONDITION_COLORS = {"baseline": "#c9ced6", "benchmark": "#f2a65a"}
CONDITION_LABELS = {"baseline": "No augmentation", "benchmark": "Benchmark paper augmented"}
BENCHMARK_POSITIVE = "#f28e2b"
BENCHMARK_NEGATIVE = "#b23a48"


def corr_rows(mat: np.ndarray, truth: np.ndarray) -> np.ndarray:
    centered_mat = mat - mat.mean(axis=1, keepdims=True)
    centered_truth = truth - truth.mean()
    denom = np.sqrt((centered_mat**2).sum(axis=1) * (centered_truth**2).sum())
    out = np.full(mat.shape[0], np.nan, dtype=float)
    valid = denom > 0
    out[valid] = (centered_mat[valid] @ centered_truth) / denom[valid]
    return out


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
        for alpha, label in [(0.05, "*"), (0.01, "**"), (0.001, "***")]:
            tcrit = float(stats.t.ppf(1.0 - alpha / 2.0, df=len(diff) - 1))
            lo = summary["mean"] - tcrit * summary["se"]
            hi = summary["mean"] + tcrit * summary["se"]
            out[f"ci_{int((1 - alpha) * 1000):03d}_low"] = lo
            out[f"ci_{int((1 - alpha) * 1000):03d}_high"] = hi
            if lo > 0.0 or hi < 0.0:
                out["paired_sig_label"] = label
                break
        else:
            out["paired_sig_label"] = "n.s."
    else:
        out["pvalue"] = float("nan")
        out["paired_sig_label"] = "n.s."
    return out


def compute_share_below(values: np.ndarray, threshold: float) -> float:
    arr = np.asarray(values, dtype=float)
    arr = arr[np.isfinite(arr)]
    if arr.size == 0 or not np.isfinite(threshold):
        return float("nan")
    return float(np.mean(arr <= threshold))


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
            if i == len(ranked) - 1:
                adjusted[i] = candidate
            else:
                adjusted[i] = min(candidate, adjusted[i + 1])
        adjusted = np.clip(adjusted, 0.0, 1.0)
        restored = np.empty_like(adjusted)
        restored[order] = adjusted
        out.loc[mask, "pvalue_bh"] = restored
        out.loc[mask, "bh_reject_0_05"] = restored <= 0.05
    return out


def load_human_predictions() -> tuple[pd.DataFrame, np.ndarray]:
    rows = pd.read_csv(HUMAN_PREDICTIONS_CSV)
    rows = rows.query("prediction.between(-0.2, 1.2) and n_predictions_made == 20").copy()
    truth = (
        rows.loc[:, ["CONFIG_configId", "treatment_efficiency"]]
        .drop_duplicates()
        .sort_values("CONFIG_configId")
    )
    truth_vec = truth["treatment_efficiency"].to_numpy(dtype=float) * 100.0
    return rows, truth_vec


def build_human_matrix(rows: pd.DataFrame, source: str) -> pd.DataFrame:
    wide = (
        rows.loc[rows["source"] == source, ["CONFIG_configId", "playerID", "prediction"]]
        .pivot_table(index="CONFIG_configId", columns="playerID", values="prediction", aggfunc="mean")
        .sort_index()
    )
    return wide.loc[:, wide.notna().all(axis=0)]


def build_figure1_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    human_rows, truth_vec = load_human_predictions()
    validation = pd.read_csv(VALIDATION_CSV).sort_values("CONFIG_configId")
    control_vec = validation["efficiency_np"].to_numpy(dtype=float) * 100.0
    repeat_rows = pd.read_csv(REPEAT_ROWS_CSV)
    baseline_repeat = repeat_rows.loc[repeat_rows["condition"] == "baseline"].copy()
    current_summary = pd.read_csv(REPEAT5_SUMMARY_CSV).loc[:, ["model", "baseline_correlation"]]

    plot_rows: list[dict[str, object]] = []
    for source in SOURCE_ORDER:
        group = SOURCE_LABELS[source]
        mat = build_human_matrix(human_rows, source).to_numpy(dtype=float).T * 100.0
        participant_corr = corr_rows(mat, truth_vec)
        plot_rows.extend(
            {"group": group, "value": float(value), "kind": "individual", "label": group}
            for value in participant_corr
            if np.isfinite(value)
        )
    plot_df = pd.DataFrame(plot_rows)

    ref_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []
    for model in MODEL_ORDER:
        sub = baseline_repeat.loc[baseline_repeat["model"] == model, "correlation"]
        if sub.empty:
            continue
        summary = summarize_series(sub)
        current_value = current_summary.loc[current_summary["model"] == model, "baseline_correlation"]
        current_corr = float(current_value.iloc[0]) if not current_value.empty else float("nan")
        summary_rows.append(
            {
                "model": model,
                "mean_repeat_correlation": summary["mean"],
                "repeat_sd": summary["sd"],
                "repeat_se": summary["se"],
                "repeat_ci_low": summary["ci_low"],
                "repeat_ci_high": summary["ci_high"],
                "repeat_min": float(sub.min()),
                "repeat_max": float(sub.max()),
                "n_repeats": summary["count"],
                "avg_prediction_correlation": current_corr,
                "mean_repeat_minus_avg_prediction": summary["mean"] - current_corr,
            }
        )
        ref_rows.append(
            {
                "label": model,
                "value": summary["mean"],
                "ci_low": summary["ci_low"],
                "ci_high": summary["ci_high"],
                "kind": "llm_model",
            }
        )
    ref_rows.append(
        {
            "label": "No treatment effect",
            "value": float(np.corrcoef(control_vec, truth_vec)[0, 1]),
            "ci_low": float("nan"),
            "ci_high": float("nan"),
            "kind": "null_baseline",
        }
    )

    plot_df["group"] = pd.Categorical(plot_df["group"], categories=["Laypeople", "Experts"], ordered=True)
    reference_df = pd.DataFrame(ref_rows).sort_values(["kind", "value"]).reset_index(drop=True)
    summary_df = pd.DataFrame(summary_rows).sort_values("mean_repeat_correlation", ascending=False).reset_index(drop=True)
    return plot_df.sort_values("group").reset_index(drop=True), reference_df, summary_df


def build_figure1_percentile_summary(
    plot_df: pd.DataFrame,
    model_summary_df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    repeat_rows = pd.read_csv(REPEAT_ROWS_CSV)
    baseline_repeat = (
        repeat_rows.loc[repeat_rows["condition"] == "baseline", ["model", "repeat", "correlation"]]
        .dropna(subset=["correlation"])
        .copy()
    )
    human_values = {
        group: plot_df.loc[plot_df["group"] == group, "value"].to_numpy(dtype=float)
        for group in ["Laypeople", "Experts"]
    }
    repeat_detail_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []

    ordered_models = model_summary_df["model"].tolist()
    for model in ordered_models:
        model_repeats = (
            baseline_repeat.loc[baseline_repeat["model"] == model, ["repeat", "correlation"]]
            .sort_values("repeat")
            .reset_index(drop=True)
        )
        if model_repeats.empty:
            continue
        model_summary = model_summary_df.loc[model_summary_df["model"] == model].iloc[0]
        row: dict[str, object] = {
            "model": model,
            "mean_repeat_correlation": float(model_summary["mean_repeat_correlation"]),
            "repeat_ci_low": float(model_summary["repeat_ci_low"]),
            "repeat_ci_high": float(model_summary["repeat_ci_high"]),
            "repeat_min": float(model_summary["repeat_min"]),
            "repeat_max": float(model_summary["repeat_max"]),
            "n_repeats": int(model_summary["n_repeats"]),
        }
        for group in ["Laypeople", "Experts"]:
            slug = group.lower()
            group_values = human_values[group]
            share_at_mean = compute_share_below(group_values, float(model_summary["mean_repeat_correlation"]))
            repeat_percentiles = model_repeats["correlation"].apply(lambda x: compute_share_below(group_values, float(x)))
            repeat_summary = summarize_series(repeat_percentiles)
            repeat_min = float(np.clip(repeat_percentiles.min(), 0.0, 1.0))
            repeat_max = float(np.clip(repeat_percentiles.max(), 0.0, 1.0))
            repeat_mean = float(np.clip(repeat_summary["mean"], 0.0, 1.0))
            repeat_ci_low = float(np.clip(repeat_summary["ci_low"], 0.0, 1.0))
            repeat_ci_high = float(np.clip(repeat_summary["ci_high"], 0.0, 1.0))
            row[f"share_{slug}_below_at_mean_repeat_correlation"] = share_at_mean
            row[f"pct_{slug}_below_at_mean_repeat_correlation"] = share_at_mean * 100.0
            row[f"share_{slug}_below_repeat_mean"] = repeat_mean
            row[f"share_{slug}_below_repeat_ci_low"] = repeat_ci_low
            row[f"share_{slug}_below_repeat_ci_high"] = repeat_ci_high
            row[f"share_{slug}_below_repeat_min"] = repeat_min
            row[f"share_{slug}_below_repeat_max"] = repeat_max
            row[f"pct_{slug}_below_repeat_mean"] = repeat_mean * 100.0
            row[f"pct_{slug}_below_repeat_ci_low"] = repeat_ci_low * 100.0
            row[f"pct_{slug}_below_repeat_ci_high"] = repeat_ci_high * 100.0
            row[f"pct_{slug}_below_repeat_min"] = repeat_min * 100.0
            row[f"pct_{slug}_below_repeat_max"] = repeat_max * 100.0
            row[f"n_{slug}"] = int(group_values.size)
            for repeat_value in model_repeats.itertuples(index=False):
                repeat_detail_rows.append(
                    {
                        "model": model,
                        "repeat": repeat_value.repeat,
                        "group": group,
                        "correlation": float(repeat_value.correlation),
                        "share_below": compute_share_below(group_values, float(repeat_value.correlation)),
                    }
                )
        summary_rows.append(row)

    percentile_summary = pd.DataFrame(summary_rows)
    percentile_summary["model"] = pd.Categorical(percentile_summary["model"], categories=ordered_models, ordered=True)
    percentile_summary = percentile_summary.sort_values("model").reset_index(drop=True)

    percentile_repeat_rows = pd.DataFrame(repeat_detail_rows)
    percentile_repeat_rows["pct_below"] = percentile_repeat_rows["share_below"] * 100.0
    percentile_repeat_rows["model"] = pd.Categorical(percentile_repeat_rows["model"], categories=ordered_models, ordered=True)
    percentile_repeat_rows = percentile_repeat_rows.sort_values(["model", "group", "repeat"]).reset_index(drop=True)

    groups = [
        sub["correlation"].to_numpy(dtype=float)
        for _, sub in baseline_repeat.groupby("model", sort=False)
    ]
    anova_f, anova_p = stats.f_oneway(*groups)
    kruskal_h, kruskal_p = stats.kruskal(*groups)
    global_df = pd.DataFrame(
        [
            {
                "condition": "baseline",
                "n_models": int(baseline_repeat["model"].nunique()),
                "n_repeats_per_model": int(baseline_repeat.groupby("model").size().min()),
                "anova_f": float(anova_f),
                "anova_pvalue": float(anova_p),
                "kruskal_h": float(kruskal_h),
                "kruskal_pvalue": float(kruskal_p),
            }
        ]
    )

    pairwise_rows: list[dict[str, object]] = []
    model_to_values = {
        model: sub["correlation"].to_numpy(dtype=float)
        for model, sub in baseline_repeat.groupby("model", sort=True)
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
                "condition": "baseline",
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
    pairwise_df["model_a"] = pd.Categorical(pairwise_df["model_a"], categories=ordered_models, ordered=True)
    pairwise_df["model_b"] = pd.Categorical(pairwise_df["model_b"], categories=ordered_models, ordered=True)
    pairwise_df = pairwise_df.sort_values(["model_a", "model_b"]).reset_index(drop=True)
    return percentile_summary, percentile_repeat_rows, global_df, pairwise_df


def build_figure2_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, float]:
    repeat_rows = pd.read_csv(REPEAT_ROWS_CSV)
    current_summary = pd.read_csv(REPEAT5_SUMMARY_CSV).loc[:, ["model", "baseline_correlation"]]
    current_benchmark = (
        pd.read_csv(REPEAT5_ROWS_CSV)
        .loc[lambda x: x["variant_id"] == "benchmark_pgg_ms", ["model", "correlation", "delta_correlation"]]
        .rename(
            columns={
                "correlation": "benchmark_avg_prediction_correlation",
                "delta_correlation": "delta_avg_prediction_correlation",
            }
        )
    )

    plot_rows: list[dict[str, object]] = []
    delta_rows: list[dict[str, object]] = []
    comparison_rows: list[dict[str, object]] = []
    repeat_detail = repeat_rows.loc[:, ["model", "condition", "repeat", "correlation"]].copy()

    for model in MODEL_ORDER:
        sub = repeat_rows.loc[repeat_rows["model"] == model].copy()
        if sub.empty:
            continue
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
        current_base = current_summary.loc[current_summary["model"] == model, "baseline_correlation"]
        current_bench = current_benchmark.loc[
            current_benchmark["model"] == model,
            "benchmark_avg_prediction_correlation",
        ]
        current_delta = current_benchmark.loc[
            current_benchmark["model"] == model,
            "delta_avg_prediction_correlation",
        ]
        baseline_avg_pred = float(current_base.iloc[0]) if not current_base.empty else float("nan")
        benchmark_avg_pred = float(current_bench.iloc[0]) if not current_bench.empty else float("nan")
        delta_avg_pred = float(current_delta.iloc[0]) if not current_delta.empty else float("nan")

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
        comparison_rows.append(
            {
                "model": model,
                "baseline_avg_prediction_correlation": baseline_avg_pred,
                "baseline_mean_repeat_correlation": by_condition["baseline"]["mean"],
                "baseline_shift_mean_repeat_minus_avg_prediction": by_condition["baseline"]["mean"] - baseline_avg_pred,
                "benchmark_avg_prediction_correlation": benchmark_avg_pred,
                "benchmark_mean_repeat_correlation": by_condition["benchmark"]["mean"],
                "benchmark_shift_mean_repeat_minus_avg_prediction": by_condition["benchmark"]["mean"] - benchmark_avg_pred,
                "delta_avg_prediction_correlation": delta_avg_pred,
                "delta_mean_repeat_correlation": paired_summary["delta_mean"],
                "delta_shift_mean_repeat_minus_avg_prediction": paired_summary["delta_mean"] - delta_avg_pred,
            }
        )

    plot_df = pd.DataFrame(plot_rows)
    baseline_order = (
        plot_df.loc[plot_df["condition"] == "baseline", ["model", "correlation"]]
        .sort_values("correlation", ascending=False)["model"]
        .tolist()
    )
    plot_df["model"] = pd.Categorical(plot_df["model"], categories=baseline_order, ordered=True)
    plot_df = plot_df.sort_values(["model", "condition"]).reset_index(drop=True)

    delta_df = pd.DataFrame(delta_rows)
    delta_df["model"] = pd.Categorical(delta_df["model"], categories=baseline_order, ordered=True)
    delta_df = delta_df.sort_values("model").reset_index(drop=True)

    comparison_df = pd.DataFrame(comparison_rows)
    comparison_df["model"] = pd.Categorical(comparison_df["model"], categories=baseline_order, ordered=True)
    comparison_df = comparison_df.sort_values("model").reset_index(drop=True)

    pairwise_rows: list[dict[str, object]] = []
    global_rows: list[dict[str, object]] = []
    for condition in ["baseline", "benchmark"]:
        part = repeat_rows.loc[repeat_rows["condition"] == condition, ["model", "correlation"]].copy()
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
            df = float(df_num / df_den) if df_den > 0 else float("nan")
            tcrit = float(stats.t.ppf(0.975, df)) if np.isfinite(df) else float("nan")
            ci_low = mean_diff - tcrit * se if np.isfinite(tcrit) else float("nan")
            ci_high = mean_diff + tcrit * se if np.isfinite(tcrit) else float("nan")
            pvalue = float(stats.ttest_ind(vals_a, vals_b, equal_var=False).pvalue)
            pairwise_rows.append(
                {
                    "condition": condition,
                    "model_a": model_a,
                    "model_b": model_b,
                    "mean_diff_a_minus_b": mean_diff,
                    "ci95_low": ci_low,
                    "ci95_high": ci_high,
                    "welch_df": df,
                    "pvalue": pvalue,
                    "ci95_excludes_zero": bool(
                        np.isfinite(ci_low)
                        and np.isfinite(ci_high)
                        and (ci_low > 0.0 or ci_high < 0.0)
                    ),
                }
            )

    pairwise_df = add_bh_adjustment(pd.DataFrame(pairwise_rows), group_col="condition", p_col="pvalue")
    global_df = pd.DataFrame(global_rows)

    benchmarks = pd.read_csv(NO_AUG_BENCHMARKS_CSV)
    ceiling = float(benchmarks.loc[benchmarks["benchmark"] == "Noise ceiling", "correlation"].iloc[0])
    return plot_df, delta_df, comparison_df, pairwise_df, global_df, repeat_detail, ceiling


def plot_figure1_panel_b_cdf(plot_df: pd.DataFrame, reference_df: pd.DataFrame) -> pd.DataFrame:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(8.2, 6.6), layout="constrained")
    human_counts = {
        group: int(plot_df.loc[plot_df["group"] == group].shape[0])
        for group in ["Laypeople", "Experts"]
    }

    density_order = ["Laypeople", "Experts"]
    for group in density_order:
        vals = plot_df.loc[plot_df["group"] == group, "value"].to_numpy(dtype=float)
        sns.ecdfplot(
            x=vals,
            stat="proportion",
            linewidth=2.4,
            color=GROUP_COLORS[group],
            label=group,
            ax=ax,
        )

    x_min, x_max = -0.7, 0.86
    reference_df = reference_df.sort_values("value").reset_index(drop=True)
    llm_refs = reference_df.loc[reference_df["kind"] == "llm_model"].copy()
    null_ref = reference_df.loc[reference_df["kind"] == "null_baseline"].copy()

    percentile_rows: list[dict[str, object]] = []
    for _, row in llm_refs.iterrows():
        value = float(row["value"])
        label = str(row["label"])
        ax.axvline(value, color=MODEL_COLORS[label], linewidth=1.4, alpha=0.95, zorder=3)
        percentile_row: dict[str, object] = {"label": label, "value": value, "kind": "llm_model"}
        for group in density_order:
            group_vals = plot_df.loc[plot_df["group"] == group, "value"].to_numpy(dtype=float)
            percentile_row[f"share_{group.lower()}_below"] = float(np.mean(group_vals <= value))
        percentile_rows.append(percentile_row)

    if not null_ref.empty:
        null_value = float(null_ref["value"].iloc[0])
        ax.axvline(null_value, color="#111827", linewidth=1.8, linestyle="--", alpha=0.9, zorder=2)
        percentile_row = {"label": "No treatment effect", "value": null_value, "kind": "null_baseline"}
        for group in density_order:
            group_vals = plot_df.loc[plot_df["group"] == group, "value"].to_numpy(dtype=float)
            percentile_row[f"share_{group.lower()}_below"] = float(np.mean(group_vals <= null_value))
        percentile_rows.append(percentile_row)

    percentile_df = pd.DataFrame(percentile_rows)
    percentile_groups = [
        ("Laypeople", "share_laypeople_below", GROUP_COLORS["Laypeople"]),
        ("Experts", "share_experts_below", GROUP_COLORS["Experts"]),
    ]
    for _, row in percentile_df.loc[percentile_df["kind"] == "llm_model"].iterrows():
        value = float(row["value"])
        for _, share_col, color in percentile_groups:
            share = float(row[share_col])
            ax.hlines(
                y=share,
                xmin=x_min,
                xmax=value,
                color=color,
                linewidth=0.9,
                alpha=0.55,
                linestyle="--",
                zorder=1,
            )

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(0.0, 1.02)
    ax.set_xticks(np.arange(-0.7, 0.81, 0.1))
    ax.set_yticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel("Correlation with true treatment outcome")
    ax.set_ylabel("Cumulative share of human forecasters")
    ax.grid(False)

    legend_items = [
        Line2D([0], [0], color=GROUP_COLORS["Laypeople"], linewidth=2.4, label=f"Laypeople (n={human_counts['Laypeople']})"),
        Line2D([0], [0], color=GROUP_COLORS["Experts"], linewidth=2.4, label=f"Experts (n={human_counts['Experts']})"),
        Line2D([0], [0], color="#111827", linewidth=1.8, linestyle="--", label="No-treatment-effect baseline"),
    ]
    llm_order = llm_refs.sort_values("value")["label"].tolist()
    for model in llm_order:
        legend_items.append(
            Line2D([0], [0], color=MODEL_COLORS[model], linewidth=1.4, label=model)
        )
    ax.legend(
        handles=legend_items,
        loc="upper left",
        bbox_to_anchor=(0.0, -0.17),
        ncol=3,
        frameon=False,
        columnspacing=1.0,
        handlelength=2.0,
        borderaxespad=0.0,
    )

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure1_panel_b_baseline_vs_humans_correlation_cdf.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)
    percentile_df["pct_laypeople_below"] = percentile_df["share_laypeople_below"] * 100.0
    percentile_df["pct_experts_below"] = percentile_df["share_experts_below"] * 100.0
    return percentile_df


def plot_figure1_panel_b_summary(
    plot_df: pd.DataFrame,
    reference_df: pd.DataFrame,
    model_summary_df: pd.DataFrame,
    percentile_summary_df: pd.DataFrame,
    percentile_repeat_rows: pd.DataFrame,
    baseline_global_df: pd.DataFrame,
) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    model_order = model_summary_df["model"].tolist()
    row_labels = [*reversed(model_order), "Experts", "Laypeople"]
    row_to_y = {label: idx for idx, label in enumerate(row_labels)}
    fig, (ax_corr, ax_pct) = plt.subplots(
        1,
        2,
        figsize=(13.2, 6.6),
        gridspec_kw={"width_ratios": [1.08, 1.0]},
        sharey=True,
    )
    human_line = "#4b5563"
    repeat_color = "#9ca3af"
    model_line = "#111827"

    human_specs = [("Laypeople", GROUP_COLORS["Laypeople"]), ("Experts", GROUP_COLORS["Experts"])]
    for group, fill_color in human_specs:
        y = row_to_y[group]
        values = plot_df.loc[plot_df["group"] == group, "value"].to_numpy(dtype=float)
        violin = ax_corr.violinplot(
            [values],
            positions=[y],
            vert=False,
            widths=0.72,
            showmeans=False,
            showmedians=False,
            showextrema=False,
        )
        for body in violin["bodies"]:
            body.set_facecolor(fill_color)
            body.set_edgecolor(fill_color)
            body.set_alpha(0.28)
            body.set_linewidth(0.8)
        q25, vmed, q75 = np.quantile(values, [0.25, 0.5, 0.75])
        ax_corr.hlines(y, q25, q75, color=fill_color, linewidth=2.6, zorder=3)
        ax_corr.scatter([vmed], [y], s=34, color=fill_color, edgecolor="white", linewidth=0.7, zorder=4)

    baseline_repeat = pd.read_csv(REPEAT_ROWS_CSV)
    baseline_repeat = baseline_repeat.loc[baseline_repeat["condition"] == "baseline", ["model", "repeat", "correlation"]]
    for model in model_order:
        y = row_to_y[model]
        model_row = model_summary_df.loc[model_summary_df["model"] == model].iloc[0]
        repeats = (
            baseline_repeat.loc[baseline_repeat["model"] == model, "correlation"]
            .dropna()
            .to_numpy(dtype=float)
        )
        if repeats.size:
            jitter = np.linspace(-0.13, 0.13, repeats.size) if repeats.size > 1 else np.array([0.0])
            ax_corr.scatter(
                repeats,
                np.full(repeats.size, y) + jitter,
                s=20,
                color=repeat_color,
                alpha=0.45,
                linewidths=0.0,
                zorder=3,
            )
        mean_value = float(model_row["mean_repeat_correlation"])
        spread_low = float(model_row["repeat_min"])
        spread_high = float(model_row["repeat_max"])
        ax_corr.errorbar(
            mean_value,
            y,
            xerr=np.array([[mean_value - spread_low], [spread_high - mean_value]]),
            fmt="o",
            color=model_line,
            ecolor=model_line,
            elinewidth=2.0,
            capsize=3.2,
            markersize=7.0,
            markeredgecolor="white",
            markeredgewidth=0.7,
            zorder=5,
        )
        ax_corr.text(
            0.985,
            y,
            f"{mean_value:.2f}",
            transform=ax_corr.get_yaxis_transform(),
            ha="right",
            va="center",
            fontsize=9.2,
            color=model_line,
            bbox={"boxstyle": "round,pad=0.12", "facecolor": "white", "edgecolor": "none", "alpha": 0.92},
            zorder=6,
        )

    null_ref = reference_df.loc[reference_df["kind"] == "null_baseline"]
    if not null_ref.empty:
        null_value = float(null_ref["value"].iloc[0])
        ax_corr.axvline(null_value, color="#111827", linewidth=1.6, linestyle="--", zorder=1)
        for group, fill_color in human_specs:
            y = row_to_y[group]
            values = plot_df.loc[plot_df["group"] == group, "value"].to_numpy(dtype=float)
            pct_worse = 100.0 * float(np.mean(values <= null_value))
            ax_corr.text(
                0.035,
                y,
                f"{pct_worse:.0f}% underperform\n0-treatment baseline",
                transform=ax_corr.get_yaxis_transform(),
                ha="left",
                va="center",
                fontsize=8.8,
                color=fill_color,
                bbox={"boxstyle": "round,pad=0.16", "facecolor": "white", "edgecolor": "none", "alpha": 0.88},
                zorder=6,
            )

    ax_corr.set_xlim(-0.7, 0.86)
    ax_corr.set_xticks(np.arange(-0.7, 0.81, 0.2))
    ax_corr.set_xticks(np.arange(-0.7, 0.81, 0.1), minor=True)
    ax_corr.set_xlabel(r"$\mathrm{Corr}(y_{\mathrm{true}}, y_{\mathrm{pred}})$")
    ax_corr.set_ylabel("Predictors (no literature provided)")
    ax_corr.set_yticks([row_to_y[label] for label in row_labels], row_labels)
    ax_corr.invert_yaxis()
    ax_corr.grid(axis="x", which="minor", color="#e5e7eb", linewidth=0.8)
    ax_corr.grid(axis="x", which="major", color="#e5e7eb", linewidth=0.0)
    ax_corr.grid(axis="y", visible=False)
    null_legend = [
        Line2D(
            [0],
            [0],
            color="#111827",
            linewidth=1.6,
            linestyle="--",
            label="Predict 0 treatment effect",
        )
    ]
    ax_corr.legend(
        handles=null_legend,
        frameon=False,
        loc="lower left",
        bbox_to_anchor=(0.02, 0.02),
        handlelength=2.3,
        borderaxespad=0.0,
    )

    percentile_lookup = percentile_summary_df.set_index("model")
    pct_specs = [
        ("Laypeople", "laypeople", -0.14, GROUP_COLORS["Laypeople"], "o"),
        ("Experts", "experts", 0.14, GROUP_COLORS["Experts"], "s"),
    ]
    for model in model_order:
        y = row_to_y[model]
        row = percentile_lookup.loc[model]
        for display_group, slug, offset, color, marker in pct_specs:
            x = float(row[f"pct_{slug}_below_repeat_mean"])
            spread_low = float(row[f"pct_{slug}_below_repeat_min"])
            spread_high = float(row[f"pct_{slug}_below_repeat_max"])
            ax_pct.errorbar(
                x,
                y + offset,
                xerr=np.array([[x - spread_low], [spread_high - x]]),
                fmt=marker,
                color=color,
                ecolor=color,
                elinewidth=1.8,
                capsize=2.6,
                markersize=6.5,
                markeredgecolor="white",
                markeredgewidth=0.7,
                zorder=4,
            )
            ax_pct.text(
                103.0,
                y + offset,
                f"{x:.0f}%",
                color=color,
                fontsize=9.2,
                va="center",
                ha="left",
                )

    ax_pct.set_xlim(0.0, 115.0)
    ax_pct.set_xticks(np.arange(0.0, 101.0, 20.0))
    ax_pct.set_xlabel("% of individual humans outperformed by LLM")
    ax_pct.tick_params(axis="y", left=False, labelleft=False)
    ax_pct.invert_yaxis()
    ax_pct.grid(axis="x", color="#e5e7eb", linewidth=0.8)
    ax_pct.grid(axis="y", visible=False)

    pct_legend = [
        Line2D([0], [0], marker="o", linestyle="-", color=GROUP_COLORS["Laypeople"], markerfacecolor=GROUP_COLORS["Laypeople"], markersize=6, label="Laypeople percentile across repeats (min-max)"),
        Line2D([0], [0], marker="s", linestyle="-", color=GROUP_COLORS["Experts"], markerfacecolor=GROUP_COLORS["Experts"], markersize=6, label="Experts percentile across repeats (min-max)"),
    ]
    ax_pct.legend(
        handles=pct_legend,
        frameon=False,
        loc="upper left",
        bbox_to_anchor=(0.02, 0.98),
        ncol=1,
        handlelength=1.8,
        borderaxespad=0.0,
    )
    fig.subplots_adjust(bottom=0.12, top=0.90, wspace=0.16)

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure1_panel_b_baseline_vs_humans_summary.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_figure2(plot_df: pd.DataFrame, delta_df: pd.DataFrame, repeat_detail: pd.DataFrame, ceiling: float) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(10.4, 6.1))

    model_order = plot_df["model"].cat.categories.tolist()
    y_positions = np.arange(len(model_order))
    offsets = {"baseline": -0.18, "benchmark": 0.18}
    delta_lookup = delta_df.set_index("model")
    bracket_color = "#6b7280"

    ax.axvline(ceiling, color="#0f766e", linestyle="--", linewidth=1.4, zorder=1)

    for condition in ["baseline", "benchmark"]:
        part = (
            plot_df.loc[plot_df["condition"] == condition]
            .set_index("model")
            .reindex(model_order)
            .reset_index()
        )
        y = y_positions + offsets[condition]
        ax.barh(
            y,
            part["correlation"].to_numpy(dtype=float),
            color=CONDITION_COLORS[condition],
            edgecolor="#4b5563",
            linewidth=0.8,
            height=0.32,
            zorder=2,
            label=CONDITION_LABELS[condition],
        )
        xerr = np.vstack(
            [
                part["correlation"].to_numpy(dtype=float) - part["ci_low"].to_numpy(dtype=float),
                part["ci_high"].to_numpy(dtype=float) - part["correlation"].to_numpy(dtype=float),
            ]
        )
        ax.errorbar(
            part["correlation"].to_numpy(dtype=float),
            y,
            xerr=xerr,
            fmt="none",
            ecolor=(17 / 255, 24 / 255, 39 / 255, 0.35),
            elinewidth=1.0,
            capsize=2.8,
            zorder=4,
        )

        for idx, model in enumerate(model_order):
            repeats = repeat_detail.loc[
                (repeat_detail["model"] == model) & (repeat_detail["condition"] == condition),
                "correlation",
            ].to_numpy(dtype=float)
            if repeats.size == 0:
                continue
            jitter = np.linspace(-0.08, 0.08, repeats.size) if repeats.size > 1 else np.array([0.0])
            ax.scatter(
                repeats,
                np.full(repeats.size, y_positions[idx] + offsets[condition]) + jitter,
                s=18,
                color="#111827",
                alpha=0.65,
                linewidths=0.0,
                zorder=5,
            )

    bracket_x = 0.944
    bracket_left = 0.929
    for idx, model in enumerate(model_order):
        row = delta_lookup.loc[model]
        y0 = y_positions[idx] + offsets["baseline"]
        y1 = y_positions[idx] + offsets["benchmark"]
        ax.plot(
            [bracket_left, bracket_x, bracket_x, bracket_left],
            [y0, y0, y1, y1],
            color=bracket_color,
            linewidth=1.2,
            zorder=4,
            clip_on=True,
        )
        sig_label = str(row["paired_sig_label"])
        text_color = (
            BENCHMARK_POSITIVE
            if float(row["delta_mean_repeat_correlation"]) >= 0.0 and sig_label != "n.s."
            else BENCHMARK_NEGATIVE
            if float(row["delta_mean_repeat_correlation"]) < 0.0 and sig_label != "n.s."
            else bracket_color
        )
        ax.text(
            bracket_x + 0.008,
            (y0 + y1) / 2.0,
            sig_label,
            ha="left",
            va="center",
            fontsize=11.2,
            fontstyle="italic" if sig_label == "n.s." else "normal",
            fontweight="semibold" if sig_label != "n.s." else "normal",
            color=text_color,
            zorder=6,
            clip_on=True,
            bbox={"boxstyle": "round,pad=0.08", "facecolor": "white", "edgecolor": "none"},
        )

    ax.set_xlim(0.0, 1.0)
    ax.set_xticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel("Mean correlation with true treatment outcome across 5 repeats")
    ax.set_yticks(y_positions, model_order)
    ax.invert_yaxis()
    ax.grid(False)

    legend_items = [
        Line2D([0], [0], color=CONDITION_COLORS["baseline"], linewidth=8, label=CONDITION_LABELS["baseline"]),
        Line2D([0], [0], color=CONDITION_COLORS["benchmark"], linewidth=8, label=CONDITION_LABELS["benchmark"]),
        Line2D([0], [0], marker="o", linestyle="", color="#111827", markersize=5, alpha=0.65, label="Individual repeats"),
        Line2D([0], [0], color="#0f766e", linestyle="--", linewidth=1.4, label="Estimated noise ceiling"),
    ]
    ax.legend(
        handles=legend_items,
        frameon=False,
        loc="upper left",
        bbox_to_anchor=(0.0, -0.2),
        ncol=2,
        columnspacing=1.2,
        handlelength=2.4,
        borderaxespad=0.0,
    )
    fig.text(
        0.99,
        0.045,
        "* repeat-paired 95% CI excludes 0   ** 99% CI excludes 0   *** 99.9% CI excludes 0   n.s. otherwise",
        ha="right",
        va="bottom",
        fontsize=9.0,
        color="#4b5563",
    )
    fig.text(
        0.01,
        0.02,
        "Error bars are t-based 95% CIs across the five repeat-level correlations.",
        ha="left",
        va="bottom",
        fontsize=9.0,
        color="#4b5563",
    )
    fig.subplots_adjust(bottom=0.30, right=0.95)

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure2_benchmark_report_vs_baseline_correlation.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    figure1_rows, figure1_refs, figure1_model_summary = build_figure1_data()
    (
        figure1_percentile_summary,
        figure1_percentile_repeat_rows,
        figure1_baseline_global,
        figure1_baseline_pairwise,
    ) = build_figure1_percentile_summary(figure1_rows, figure1_model_summary)
    figure2_plot_rows, figure2_delta, figure2_comparison, figure2_pairwise, figure2_global, figure2_repeat_detail, figure2_ceiling = build_figure2_data()

    figure1_rows.to_csv(RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_rows.csv", index=False)
    figure1_refs.to_csv(RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_reference_lines.csv", index=False)
    figure1_model_summary.to_csv(RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_model_summary.csv", index=False)
    figure1_percentile_summary.to_csv(RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_percentile_summary.csv", index=False)
    figure1_percentile_repeat_rows.to_csv(RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_percentile_repeat_rows.csv", index=False)
    figure1_baseline_global.to_csv(RESULTS_DIR / "figure1_panel_b_baseline_model_global_tests.csv", index=False)
    figure1_baseline_pairwise.to_csv(RESULTS_DIR / "figure1_panel_b_baseline_model_pairwise_differences.csv", index=False)
    figure2_plot_rows.to_csv(RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_plot_rows.csv", index=False)
    figure2_delta.to_csv(RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_summary.csv", index=False)
    figure2_comparison.to_csv(RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_comparison_vs_avg_prediction.csv", index=False)
    figure2_pairwise.to_csv(RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_pairwise_model_differences.csv", index=False)
    figure2_global.to_csv(RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_global_model_tests.csv", index=False)
    figure2_repeat_detail.to_csv(RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_repeat_rows.csv", index=False)

    figure1_cdf_percentiles = plot_figure1_panel_b_cdf(figure1_rows, figure1_refs)
    figure1_cdf_percentiles.to_csv(
        RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_percentiles.csv",
        index=False,
    )
    plot_figure1_panel_b_summary(
        figure1_rows,
        figure1_refs,
        figure1_model_summary,
        figure1_percentile_summary,
        figure1_percentile_repeat_rows,
        figure1_baseline_global,
    )
    plot_figure2(figure2_plot_rows, figure2_delta, figure2_repeat_detail, figure2_ceiling)


if __name__ == "__main__":
    main()
