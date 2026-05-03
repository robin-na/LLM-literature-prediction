from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text"
REPEAT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5_model_sampling"
    / "validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_rows.csv"
)
REPEAT5_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5"
    / "validation_literature_collection_analysis_report_repeat5_rows.csv"
)
REPEAT5_AVG_PRED_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5"
    / "validation_literature_collection_analysis_report_repeat5_avg_predictions.csv"
)
REPEAT5_BASELINE_AVG_PRED_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5"
    / "validation_literature_collection_analysis_report_repeat5_baseline_avg_predictions.csv"
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
NO_AUG_BENCHMARKS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "no_augmentation_model_comparison"
    / "validation_no_augmentation_model_comparison_benchmarks.csv"
)
SINGLE_PAPER_SIGNIFICANCE_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_analysis_report_sources_repeat5"
    / "validation_literature_analysis_report_source_significance.csv"
)
COLLECTION_METADATA_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_metadata_filters"
    / "validation_literature_collection_analysis_report_metadata_filters_rows.csv"
)

MODEL_ORDER = ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
FIGURE3_MODEL_ORDER = ["GPT-5 Mini", "GPT-5 Nano", "GPT-4.1", "GPT-4.1 Mini", "GPT-5.1"]
SOURCE_ORDER = ["prolific", "sspp"]
SOURCE_LABELS = {"prolific": "Laypeople", "sspp": "Experts"}
GROUP_ORDER = ["Laypeople", "Experts", "Baseline LLM runs"]

GROUP_COLORS = {
    "Laypeople": "#caa27e",
    "Experts": "#8d6748",
    "Baseline LLM runs": "#6f86a6",
}
POINT_COLORS = {
    "Laypeople": "#9c6644",
    "Experts": "#5e412f",
    "Baseline LLM runs": "#43536a",
}
MODEL_COLORS = {
    "GPT-4.1": "#2b8cbe",
    "GPT-4.1 Mini": "#1b9e77",
    "GPT-4.1 Nano": "#8c564b",
    "GPT-5.1": "#d95f02",
    "GPT-5 Mini": "#7570b3",
    "GPT-5 Nano": "#e7298a",
}
BENCHMARK_POSITIVE = "#f28e2b"
BENCHMARK_NEGATIVE = "#b23a48"
HUMAN_CROWD_COLOR = "#0f766e"


def corr_rows(mat: np.ndarray, truth: np.ndarray) -> np.ndarray:
    centered_mat = mat - mat.mean(axis=1, keepdims=True)
    centered_truth = truth - truth.mean()
    denom = np.sqrt((centered_mat**2).sum(axis=1) * (centered_truth**2).sum())
    out = np.full(mat.shape[0], np.nan, dtype=float)
    valid = denom > 0
    out[valid] = (centered_mat[valid] @ centered_truth) / denom[valid]
    return out


def corr_with_question_bootstrap_ci(
    pred: np.ndarray,
    truth: np.ndarray,
    *,
    n_boot: int = 5000,
    seed: int = 42,
) -> tuple[float, float, float]:
    pred = np.asarray(pred, dtype=float)
    truth = np.asarray(truth, dtype=float)
    mask = ~np.isnan(pred) & ~np.isnan(truth)
    pred = pred[mask]
    truth = truth[mask]
    value = float(corr_rows(pred[None, :], truth)[0])
    rng = np.random.default_rng(seed)
    boot = np.empty(n_boot, dtype=float)
    idx = np.arange(pred.size)
    for i in range(n_boot):
        sample = rng.choice(idx, size=idx.size, replace=True)
        boot[i] = corr_rows(pred[sample][None, :], truth[sample])[0]
    finite_boot = boot[np.isfinite(boot)]
    lo, hi = np.nanpercentile(finite_boot, [2.5, 97.5])
    return value, float(lo), float(hi)


def paired_corr_delta_bootstrap(
    baseline: np.ndarray,
    benchmark: np.ndarray,
    truth: np.ndarray,
    *,
    n_boot: int = 50000,
    seed: int = 42,
) -> tuple[float, dict[str, float], str]:
    baseline = np.asarray(baseline, dtype=float)
    benchmark = np.asarray(benchmark, dtype=float)
    truth = np.asarray(truth, dtype=float)
    mask = ~np.isnan(baseline) & ~np.isnan(benchmark) & ~np.isnan(truth)
    baseline = baseline[mask]
    benchmark = benchmark[mask]
    truth = truth[mask]
    observed = float(corr_rows(benchmark[None, :], truth)[0] - corr_rows(baseline[None, :], truth)[0])
    if baseline.size == 0:
        return observed, {
            "ci95_low": float("nan"),
            "ci95_high": float("nan"),
            "ci99_low": float("nan"),
            "ci99_high": float("nan"),
            "ci999_low": float("nan"),
            "ci999_high": float("nan"),
        }, "n.s."

    rng = np.random.default_rng(seed)
    idx = np.arange(baseline.size)
    delta = np.empty(n_boot, dtype=float)
    for i in range(n_boot):
        sample = rng.choice(idx, size=idx.size, replace=True)
        delta[i] = float(
            corr_rows(benchmark[sample][None, :], truth[sample])[0]
            - corr_rows(baseline[sample][None, :], truth[sample])[0]
        )
    finite_delta = delta[np.isfinite(delta)]
    ci95_low, ci95_high = np.nanpercentile(finite_delta, [2.5, 97.5])
    ci99_low, ci99_high = np.nanpercentile(finite_delta, [0.5, 99.5])
    ci999_low, ci999_high = np.nanpercentile(finite_delta, [0.05, 99.95])
    ci_dict = {
        "ci95_low": float(ci95_low),
        "ci95_high": float(ci95_high),
        "ci99_low": float(ci99_low),
        "ci99_high": float(ci99_high),
        "ci999_low": float(ci999_low),
        "ci999_high": float(ci999_high),
    }
    sig_label = ci_to_sig_label(ci_dict)
    return observed, ci_dict, sig_label


def ci_to_sig_label(ci_dict: dict[str, float]) -> str:
    if np.isfinite(ci_dict["ci999_low"]) and np.isfinite(ci_dict["ci999_high"]) and (
        ci_dict["ci999_low"] > 0.0 or ci_dict["ci999_high"] < 0.0
    ):
        return "***"
    if np.isfinite(ci_dict["ci99_low"]) and np.isfinite(ci_dict["ci99_high"]) and (
        ci_dict["ci99_low"] > 0.0 or ci_dict["ci99_high"] < 0.0
    ):
        return "**"
    if np.isfinite(ci_dict["ci95_low"]) and np.isfinite(ci_dict["ci95_high"]) and (
        ci_dict["ci95_low"] > 0.0 or ci_dict["ci95_high"] < 0.0
    ):
        return "*"
    return "n.s."


def load_repeat_rows() -> pd.DataFrame:
    rows = pd.read_csv(REPEAT_ROWS_CSV)
    rows["model"] = pd.Categorical(rows["model"], categories=MODEL_ORDER, ordered=True)
    rows["condition"] = pd.Categorical(rows["condition"], categories=["baseline", "benchmark"], ordered=True)
    return rows.sort_values(["condition", "model", "repeat"]).reset_index(drop=True)


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


def build_figure1_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    human_rows, truth_vec = load_human_predictions()
    validation = pd.read_csv(VALIDATION_CSV).sort_values("CONFIG_configId")
    control_vec = validation["efficiency_np"].to_numpy(dtype=float) * 100.0
    summary = pd.read_csv(REPEAT5_SUMMARY_CSV)

    plot_rows: list[dict[str, object]] = []
    reference_rows: list[dict[str, object]] = []

    for source in SOURCE_ORDER:
        group = SOURCE_LABELS[source]
        mat = build_human_matrix(human_rows, source).to_numpy(dtype=float).T * 100.0
        participant_corr = corr_rows(mat, truth_vec)
        plot_rows.extend(
            {"group": group, "value": float(value), "kind": "individual", "label": group}
            for value in participant_corr
            if np.isfinite(value)
        )
    for _, row in summary.loc[:, ["model", "baseline_correlation"]].iterrows():
        reference_rows.append(
            {
                "label": str(row["model"]),
                "value": float(row["baseline_correlation"]),
                "kind": "llm_model",
            }
        )
    reference_rows.append(
        {
            "label": "No treatment effect",
            "value": float(np.corrcoef(control_vec, truth_vec)[0, 1]),
            "kind": "null_baseline",
        }
    )

    plot_df = pd.DataFrame(plot_rows)
    plot_df["group"] = pd.Categorical(plot_df["group"], categories=GROUP_ORDER, ordered=True)
    reference_df = pd.DataFrame(reference_rows)
    return plot_df.sort_values("group").reset_index(drop=True), reference_df.sort_values(["kind", "value"]).reset_index(drop=True)


def build_figure2_data() -> tuple[pd.DataFrame, pd.DataFrame, float]:
    validation = pd.read_csv(VALIDATION_CSV).sort_values("CONFIG_configId")
    truth = validation["efficiency_p"].to_numpy(dtype=float) * 100.0

    avg_pred = pd.read_csv(REPEAT5_AVG_PRED_CSV)
    baseline_avg = pd.read_csv(REPEAT5_BASELINE_AVG_PRED_CSV)
    q_cols = [f"Q{i}" for i in range(1, 21)]

    plot_rows: list[dict[str, object]] = []
    delta_rows: list[dict[str, object]] = []
    for model in MODEL_ORDER:
        baseline_row = baseline_avg.loc[baseline_avg["model"] == model]
        benchmark_row = avg_pred.loc[(avg_pred["model"] == model) & (avg_pred["variant_id"] == "benchmark_pgg_ms")]
        if baseline_row.empty or benchmark_row.empty:
            continue

        baseline_vec = baseline_row.iloc[0][q_cols].to_numpy(dtype=float)
        benchmark_vec = benchmark_row.iloc[0][q_cols].to_numpy(dtype=float)
        baseline_corr, baseline_lo, baseline_hi = corr_with_question_bootstrap_ci(baseline_vec, truth, seed=100 + MODEL_ORDER.index(model))
        benchmark_corr, benchmark_lo, benchmark_hi = corr_with_question_bootstrap_ci(benchmark_vec, truth, seed=200 + MODEL_ORDER.index(model))
        delta_corr, delta_ci, sig_label = paired_corr_delta_bootstrap(
            baseline_vec,
            benchmark_vec,
            truth,
            seed=300 + MODEL_ORDER.index(model),
        )
        delta_sig = bool((delta_ci["ci95_low"] > 0.0) or (delta_ci["ci95_high"] < 0.0))
        delta_direction = "improve" if float(delta_corr) >= 0.0 else "worsen"

        plot_rows.extend(
            [
                {
                    "model": model,
                    "condition": "baseline",
                    "correlation": baseline_corr,
                    "ci_low": baseline_lo,
                    "ci_high": baseline_hi,
                    "delta_correlation": delta_corr,
                    "delta_significant": delta_sig,
                    "delta_direction": delta_direction,
                    "paired_sig_label": sig_label,
                },
                {
                    "model": model,
                    "condition": "benchmark",
                    "correlation": benchmark_corr,
                    "ci_low": benchmark_lo,
                    "ci_high": benchmark_hi,
                    "delta_correlation": delta_corr,
                    "delta_significant": delta_sig,
                    "delta_direction": delta_direction,
                    "paired_sig_label": sig_label,
                },
            ]
        )
        delta_rows.append(
            {
                "model": model,
                "baseline_correlation": baseline_corr,
                "correlation": benchmark_corr,
                "delta_correlation": delta_corr,
                "delta_correlation_ci_low": delta_ci["ci95_low"],
                "delta_correlation_ci_high": delta_ci["ci95_high"],
                "delta_correlation_ci99_low": delta_ci["ci99_low"],
                "delta_correlation_ci99_high": delta_ci["ci99_high"],
                "delta_correlation_ci999_low": delta_ci["ci999_low"],
                "delta_correlation_ci999_high": delta_ci["ci999_high"],
                "delta_significant": delta_sig,
                "paired_sig_label": sig_label,
            }
        )

    benchmarks = pd.read_csv(NO_AUG_BENCHMARKS_CSV)
    ceiling = float(
        benchmarks.loc[benchmarks["benchmark"] == "Noise ceiling", "correlation"].iloc[0]
    )

    plot_df = pd.DataFrame(plot_rows)
    baseline_order = (
        plot_df.loc[plot_df["condition"] == "baseline", ["model", "correlation"]]
        .sort_values("correlation", ascending=False)
        ["model"]
        .tolist()
    )
    plot_df["model"] = pd.Categorical(plot_df["model"], categories=baseline_order, ordered=True)
    plot_df = plot_df.sort_values(["model", "condition"]).reset_index(drop=True)
    delta_df = pd.DataFrame(delta_rows)
    delta_df["model"] = pd.Categorical(delta_df["model"], categories=baseline_order, ordered=True)
    delta_df = delta_df.sort_values("model").reset_index(drop=True)
    return plot_df, delta_df, ceiling


def build_figure3_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    df = pd.read_csv(SINGLE_PAPER_SIGNIFICANCE_CSV)
    benchmark_rows = pd.read_csv(REPEAT5_ROWS_CSV)
    benchmark_lookup = (
        benchmark_rows.loc[benchmark_rows["variant_id"] == "benchmark_pgg_ms", ["model", "correlation"]]
        .rename(columns={"correlation": "benchmark_correlation"})
        .drop_duplicates()
    )
    df = df.loc[df["model"].isin(FIGURE3_MODEL_ORDER)].copy()
    df["model"] = pd.Categorical(df["model"], categories=FIGURE3_MODEL_ORDER, ordered=True)
    plot_df = (
        df.loc[:, ["model", "source_id", "correlation", "baseline_correlation"]]
        .sort_values(["model", "correlation"])
        .reset_index(drop=True)
    )
    baseline_rows: list[dict[str, object]] = []
    for model in FIGURE3_MODEL_ORDER:
        sub = plot_df.loc[plot_df["model"] == model].copy()
        if sub.empty:
            continue
        baseline = float(sub["baseline_correlation"].iloc[0])
        mean_aug = float(sub["correlation"].mean())
        share_below = float((sub["correlation"] <= baseline).mean())
        baseline_rows.append(
            {
                "model": model,
                "baseline_correlation": baseline,
                "mean_augmented_correlation": mean_aug,
                "share_augmented_papers_below_baseline": share_below,
                "share_augmented_papers_above_baseline": 1.0 - share_below,
                "n_papers": int(sub.shape[0]),
            }
        )
    baseline_df = pd.DataFrame(baseline_rows)
    baseline_df = baseline_df.merge(benchmark_lookup, on="model", how="left")
    baseline_df["model"] = pd.Categorical(baseline_df["model"], categories=FIGURE3_MODEL_ORDER, ordered=True)
    baseline_df = baseline_df.sort_values("model").reset_index(drop=True)
    return plot_df, baseline_df


def build_figure4_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    df = pd.read_csv(COLLECTION_METADATA_ROWS_CSV)
    df = df.loc[(df["variant_group"] == "metadata_filter") & (df["model"].isin(FIGURE3_MODEL_ORDER))].copy()
    benchmark_lookup = (
        pd.read_csv(REPEAT5_ROWS_CSV)
        .loc[lambda x: x["variant_id"] == "benchmark_pgg_ms", ["model", "correlation"]]
        .rename(columns={"correlation": "benchmark_correlation"})
        .drop_duplicates()
    )
    df["model"] = pd.Categorical(df["model"], categories=FIGURE3_MODEL_ORDER, ordered=True)
    plot_df = (
        df.loc[:, ["model", "variant_id", "correlation", "baseline_correlation"]]
        .sort_values(["model", "correlation"])
        .reset_index(drop=True)
    )
    rows: list[dict[str, object]] = []
    for model in FIGURE3_MODEL_ORDER:
        sub = plot_df.loc[plot_df["model"] == model].copy()
        if sub.empty:
            continue
        rows.append(
            {
                "model": model,
                "baseline_correlation": float(sub["baseline_correlation"].iloc[0]),
                "mean_augmented_correlation": float(sub["correlation"].mean()),
                "n_collections": int(sub.shape[0]),
            }
        )
    summary_df = pd.DataFrame(rows).merge(benchmark_lookup, on="model", how="left")
    summary_df["model"] = pd.Categorical(summary_df["model"], categories=FIGURE3_MODEL_ORDER, ordered=True)
    summary_df = summary_df.sort_values("model").reset_index(drop=True)
    return plot_df, summary_df


def load_noise_ceiling() -> float:
    benchmarks = pd.read_csv(NO_AUG_BENCHMARKS_CSV)
    return float(benchmarks.loc[benchmarks["benchmark"] == "Noise ceiling", "correlation"].iloc[0])


def plot_figure1_panel_b(plot_df: pd.DataFrame, reference_df: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(7.8, 6.0), layout="constrained")
    human_counts = {
        group: int(plot_df.loc[plot_df["group"] == group].shape[0])
        for group in ["Laypeople", "Experts"]
    }
    density_order = ["Laypeople", "Experts"]
    for group in density_order:
        vals = plot_df.loc[plot_df["group"] == group, "value"].to_numpy(dtype=float)
        sns.kdeplot(
            x=vals,
            fill=False,
            linewidth=2.4,
            color=GROUP_COLORS[group],
            label=group,
            bw_adjust=0.9,
            cut=0,
            ax=ax,
        )
    density_lines = list(ax.lines)
    ymax = max(float(np.nanmax(line.get_ydata())) for line in density_lines if len(line.get_ydata()) > 0)

    reference_df = reference_df.sort_values("value").reset_index(drop=True)
    llm_refs = reference_df.loc[reference_df["kind"] == "llm_model"].copy()
    null_ref = reference_df.loc[reference_df["kind"] == "null_baseline"].copy()

    for _, row in llm_refs.iterrows():
        ax.axvline(float(row["value"]), color=MODEL_COLORS[str(row["label"])], linewidth=2.0, alpha=0.95, zorder=4)
    if not null_ref.empty:
        null_value = float(null_ref["value"].iloc[0])
        ax.axvline(null_value, color="#111827", linewidth=1.8, linestyle="--", alpha=0.9, zorder=3)
    label_levels = np.linspace(ymax * 1.02, ymax * 1.18, num=max(len(llm_refs), 1))
    for level, (_, row) in zip(label_levels, llm_refs.iterrows()):
        value = float(row["value"])
        label = str(row["label"]).replace("GPT-", "").replace(".1", ".1").replace(" Mini", " mini").replace(" Nano", " nano")
        ax.text(value, level, label, rotation=90, ha="center", va="bottom", fontsize=8.5, color=MODEL_COLORS[str(row["label"])])
    if not null_ref.empty:
        ax.text(null_value, ymax * 1.02, "no TE", rotation=90, ha="center", va="bottom", fontsize=8.5, color="#111827")

    ax.set_xlim(-0.7, 0.86)
    ax.set_ylim(0.0, ymax * 1.25)
    ax.set_xlabel("Correlation with true treatment outcome")
    ax.set_ylabel("Density")

    legend_items = [
        Line2D([0], [0], color=GROUP_COLORS["Laypeople"], linewidth=2.4, label=f"Laypeople (n={human_counts['Laypeople']})"),
        Line2D([0], [0], color=GROUP_COLORS["Experts"], linewidth=2.4, label=f"Experts (n={human_counts['Experts']})"),
        Line2D([0], [0], color="#111827", linewidth=1.8, linestyle="--", label="No-treatment-effect baseline"),
    ]
    ax.legend(handles=legend_items, frameon=False, loc="upper left")

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure1_panel_b_baseline_vs_humans_correlation.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


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


def plot_figure2(plot_df: pd.DataFrame, delta_df: pd.DataFrame, ceiling: float) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(10.2, 5.9))

    model_order = plot_df["model"].cat.categories.tolist()
    y_positions = np.arange(len(model_order))
    offsets = {"baseline": -0.18, "benchmark": 0.18}
    colors = {"baseline": "#c9ced6", "benchmark": "#f2a65a"}
    labels = {"baseline": "No augmentation", "benchmark": "Benchmark paper augmented"}
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
            color=colors[condition],
            edgecolor="#4b5563",
            linewidth=0.8,
            height=0.32,
            zorder=2,
            label=labels[condition],
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
            ecolor=(17 / 255, 24 / 255, 39 / 255, 0.28),
            elinewidth=0.9,
            capsize=2.5,
            zorder=3,
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
            if float(row["delta_correlation"]) >= 0.0 and sig_label != "n.s."
            else BENCHMARK_NEGATIVE
            if float(row["delta_correlation"]) < 0.0 and sig_label != "n.s."
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
            zorder=5,
            clip_on=True,
            bbox={"boxstyle": "round,pad=0.08", "facecolor": "white", "edgecolor": "none"},
        )

    ax.set_xlim(0.0, 1.0)
    ax.set_xticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel("Correlation with true treatment outcome")
    ax.set_yticks(y_positions, model_order)
    ax.invert_yaxis()
    ax.grid(False)

    legend_items = [
        Line2D([0], [0], color=colors["baseline"], linewidth=8, label=labels["baseline"]),
        Line2D([0], [0], color=colors["benchmark"], linewidth=8, label=labels["benchmark"]),
        Line2D([0], [0], color="#0f766e", linestyle="--", linewidth=1.4, label="Estimated noise ceiling"),
    ]
    ax.legend(
        handles=legend_items,
        frameon=False,
        loc="upper left",
        bbox_to_anchor=(0.0, -0.16),
        ncol=3,
        columnspacing=1.2,
        handlelength=2.4,
        borderaxespad=0.0,
    )
    fig.text(
        0.99,
        0.02,
        "* paired 95% CI excludes 0   ** paired 99% CI excludes 0   *** paired 99.9% CI excludes 0   n.s. otherwise",
        ha="right",
        va="bottom",
        fontsize=9.2,
        color="#4b5563",
    )
    fig.subplots_adjust(bottom=0.24, right=0.95)

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure2_benchmark_report_vs_baseline_correlation.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_figure3(plot_df: pd.DataFrame, baseline_df: pd.DataFrame) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(9.8, 6.2))

    x_min, x_max = 0.0, 0.90
    baseline_min = float(baseline_df["baseline_correlation"].min())
    baseline_max = float(baseline_df["baseline_correlation"].max())
    benchmark_min = float(baseline_df["benchmark_correlation"].min())
    benchmark_max = float(baseline_df["benchmark_correlation"].max())

    for model in FIGURE3_MODEL_ORDER:
        sub = plot_df.loc[plot_df["model"] == model]
        if sub.empty:
            continue
        vals = sub["correlation"].to_numpy(dtype=float)
        sns.ecdfplot(
            x=vals,
            stat="proportion",
            linewidth=2.0,
            color=MODEL_COLORS[model],
            alpha=0.78,
            ax=ax,
        )
        model_refs = baseline_df.loc[baseline_df["model"] == model].iloc[0]
        baseline = float(model_refs["baseline_correlation"])
        ax.axvline(
            baseline,
            color=MODEL_COLORS[model],
            linewidth=1.0,
            linestyle="--",
            alpha=0.95,
            zorder=3,
        )
        benchmark = float(model_refs["benchmark_correlation"])
        ax.axvline(
            benchmark,
            color=MODEL_COLORS[model],
            linewidth=1.0,
            linestyle=":",
            alpha=0.95,
            zorder=3,
        )

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(0.0, 1.02)
    ax.set_xticks(np.arange(0.0, 0.91, 0.1))
    ax.set_yticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel("Correlation with true treatment outcome")
    ax.set_ylabel("Cumulative share")
    ax.grid(False)

    def add_range_marker(x0: float, x1: float, y_axes: float, color: str, label: str) -> None:
        transform = ax.get_xaxis_transform()
        ax.plot([x0, x1], [y_axes, y_axes], color=color, linewidth=1.5, zorder=4, clip_on=False, transform=transform)
        ax.plot([x0, x0], [y_axes - 0.02, y_axes + 0.02], color=color, linewidth=1.5, zorder=4, clip_on=False, transform=transform)
        ax.plot([x1, x1], [y_axes - 0.02, y_axes + 0.02], color=color, linewidth=1.5, zorder=4, clip_on=False, transform=transform)
        ax.text(
            (x0 + x1) / 2.0,
            y_axes + 0.01,
            label,
            ha="center",
            va="bottom",
            fontsize=9.2,
            color=color,
            transform=transform,
            bbox={"boxstyle": "round,pad=0.08", "facecolor": "white", "edgecolor": "none"},
            clip_on=False,
        )

    add_range_marker(baseline_min, baseline_max, 1.01, "#6b7280", "No augmentation")
    add_range_marker(benchmark_min, benchmark_max, 1.065, "#b45309", "Benchmark paper augmented")

    legend_items = [
        Line2D([0], [0], color=MODEL_COLORS[model], linewidth=2.0, alpha=0.78, label=model)
        for model in FIGURE3_MODEL_ORDER
    ]
    legend_items.append(
        Line2D([0], [0], color="#4b5563", linewidth=1.15, linestyle="--", label="No augmentation")
    )
    legend_items.append(
        Line2D([0], [0], color="#4b5563", linewidth=1.15, linestyle=":", label="Benchmark paper augmented")
    )
    ax.legend(
        handles=legend_items,
        loc="upper left",
        bbox_to_anchor=(0.0, -0.18),
        ncol=3,
        frameon=False,
        columnspacing=1.1,
        handlelength=2.2,
        borderaxespad=0.0,
    )
    fig.subplots_adjust(bottom=0.24, top=0.84)

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure3_individual_paper_augmentation_cdf_correlation.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_figure3_density(plot_df: pd.DataFrame, baseline_df: pd.DataFrame) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, axes = plt.subplots(
        len(FIGURE3_MODEL_ORDER),
        1,
        figsize=(8.8, 7.6),
        sharex=True,
        gridspec_kw={"hspace": 0.08},
    )

    x_min, x_max = 0.0, 0.90
    noise_ceiling = load_noise_ceiling()
    for ax, model in zip(axes, FIGURE3_MODEL_ORDER):
        sub = plot_df.loc[plot_df["model"] == model]
        refs = baseline_df.loc[baseline_df["model"] == model].iloc[0]
        vals = sub["correlation"].to_numpy(dtype=float)

        sns.kdeplot(
            x=vals,
            ax=ax,
            color=MODEL_COLORS[model],
            fill=True,
            alpha=0.18,
            linewidth=1.8,
            bw_adjust=0.9,
            cut=0,
            clip=(x_min, x_max),
        )
        ax.axvline(
            float(refs["mean_augmented_correlation"]),
            color=MODEL_COLORS[model],
            linewidth=1.4,
            alpha=0.95,
        )
        ax.annotate(
            "",
            xy=(float(refs["mean_augmented_correlation"]), 0.84),
            xytext=(float(refs["baseline_correlation"]), 0.84),
            xycoords=("data", "axes fraction"),
            textcoords=("data", "axes fraction"),
            annotation_clip=False,
            zorder=5,
            arrowprops={
                "arrowstyle": "-|>",
                "lw": 1.15,
                "color": MODEL_COLORS[model],
                "alpha": 0.9,
                "mutation_scale": 10,
                "shrinkA": 0,
                "shrinkB": 0,
            },
        )
        ax.axvline(
            float(refs["baseline_correlation"]),
            color=MODEL_COLORS[model],
            linewidth=1.1,
            linestyle="--",
            alpha=0.95,
        )
        ax.axvline(
            float(refs["benchmark_correlation"]),
            color=MODEL_COLORS[model],
            linewidth=1.1,
            linestyle=":",
            alpha=0.95,
        )
        ax.axvline(
            noise_ceiling,
            color="#111827",
            linewidth=1.0,
            linestyle="-.",
            alpha=0.85,
        )
        ax.text(
            0.01,
            0.82,
            model,
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=11.0,
            color=MODEL_COLORS[model],
        )
        ax.set_yticks([])
        ax.set_ylabel("")
        ax.grid(False)
        ax.spines["right"].set_visible(False)
        ax.spines["top"].set_visible(False)

    axes[-1].set_xlim(x_min, x_max)
    axes[-1].set_xticks(np.arange(0.0, 0.91, 0.1))
    axes[-1].set_xlabel("Correlation with true treatment outcome")
    fig.text(0.03, 0.5, "Probability density", rotation=90, va="center", ha="center")

    legend_items = [
        Line2D([0], [0], color="#4b5563", linewidth=1.4, label="Average augmented paper"),
        Line2D([0], [0], color="#4b5563", linewidth=1.1, linestyle="--", label="No augmentation"),
        Line2D([0], [0], color="#4b5563", linewidth=1.1, linestyle=":", label="Benchmark paper augmented"),
        Line2D([0], [0], color="#111827", linewidth=1.0, linestyle="-.", label="Noise ceiling"),
    ]
    fig.legend(
        handles=legend_items,
        loc="upper center",
        bbox_to_anchor=(0.54, 0.995),
        ncol=2,
        frameon=False,
        columnspacing=1.6,
        handlelength=2.6,
        borderaxespad=0.0,
    )
    fig.subplots_adjust(bottom=0.09, left=0.08, top=0.93, right=0.98)

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure3_individual_paper_augmentation_density_correlation.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_figure4_density(plot_df: pd.DataFrame, summary_df: pd.DataFrame) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, axes = plt.subplots(
        len(FIGURE3_MODEL_ORDER),
        1,
        figsize=(8.8, 7.6),
        sharex=True,
        gridspec_kw={"hspace": 0.08},
    )

    x_min, x_max = 0.0, 0.90
    noise_ceiling = load_noise_ceiling()
    for ax, model in zip(axes, FIGURE3_MODEL_ORDER):
        sub = plot_df.loc[plot_df["model"] == model]
        refs = summary_df.loc[summary_df["model"] == model].iloc[0]
        vals = sub["correlation"].to_numpy(dtype=float)

        sns.kdeplot(
            x=vals,
            ax=ax,
            color=MODEL_COLORS[model],
            fill=True,
            alpha=0.18,
            linewidth=1.8,
            bw_adjust=0.9,
            cut=0,
            clip=(x_min, x_max),
        )
        ax.axvline(
            float(refs["mean_augmented_correlation"]),
            color=MODEL_COLORS[model],
            linewidth=1.4,
            alpha=0.95,
        )
        ax.annotate(
            "",
            xy=(float(refs["mean_augmented_correlation"]), 0.84),
            xytext=(float(refs["baseline_correlation"]), 0.84),
            xycoords=("data", "axes fraction"),
            textcoords=("data", "axes fraction"),
            annotation_clip=False,
            zorder=5,
            arrowprops={
                "arrowstyle": "-|>",
                "lw": 1.15,
                "color": MODEL_COLORS[model],
                "alpha": 0.9,
                "mutation_scale": 10,
                "shrinkA": 0,
                "shrinkB": 0,
            },
        )
        ax.axvline(
            float(refs["baseline_correlation"]),
            color=MODEL_COLORS[model],
            linewidth=1.1,
            linestyle="--",
            alpha=0.95,
        )
        ax.axvline(
            float(refs["benchmark_correlation"]),
            color=MODEL_COLORS[model],
            linewidth=1.1,
            linestyle=":",
            alpha=0.95,
        )
        ax.axvline(
            noise_ceiling,
            color="#111827",
            linewidth=1.0,
            linestyle="-.",
            alpha=0.85,
        )
        ax.text(
            0.01,
            0.82,
            model,
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=11.0,
            color=MODEL_COLORS[model],
        )
        ax.set_yticks([])
        ax.set_ylabel("")
        ax.grid(False)
        ax.spines["right"].set_visible(False)
        ax.spines["top"].set_visible(False)

    axes[-1].set_xlim(x_min, x_max)
    axes[-1].set_xticks(np.arange(0.0, 0.91, 0.1))
    axes[-1].set_xlabel("Correlation with true treatment outcome")
    fig.text(0.03, 0.5, "Probability density", rotation=90, va="center", ha="center")

    legend_items = [
        Line2D([0], [0], color="#4b5563", linewidth=1.4, label="Average augmented collection"),
        Line2D([0], [0], color="#4b5563", linewidth=1.1, linestyle="--", label="No augmentation"),
        Line2D([0], [0], color="#4b5563", linewidth=1.1, linestyle=":", label="Benchmark paper augmented"),
        Line2D([0], [0], color="#111827", linewidth=1.0, linestyle="-.", label="Noise ceiling"),
    ]
    fig.legend(
        handles=legend_items,
        loc="upper center",
        bbox_to_anchor=(0.54, 0.995),
        ncol=2,
        frameon=False,
        columnspacing=1.6,
        handlelength=2.6,
        borderaxespad=0.0,
    )
    fig.subplots_adjust(bottom=0.09, left=0.08, top=0.93, right=0.98)

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure4_collection_augmentation_density_correlation.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    figure1_rows, figure1_refs = build_figure1_data()
    figure2_plot_rows, figure2_delta, figure2_ceiling = build_figure2_data()
    figure3_plot_rows, figure3_baseline = build_figure3_data()
    figure4_plot_rows, figure4_summary = build_figure4_data()

    figure1_rows.to_csv(RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_rows.csv", index=False)
    figure1_refs.to_csv(RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_reference_lines.csv", index=False)
    figure2_plot_rows.to_csv(RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_plot_rows.csv", index=False)
    figure2_delta.to_csv(RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_summary.csv", index=False)
    figure2_delta.to_csv(RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_deltas.csv", index=False)
    figure3_plot_rows.to_csv(RESULTS_DIR / "figure3_individual_paper_augmentation_cdf_rows.csv", index=False)
    figure3_baseline.to_csv(RESULTS_DIR / "figure3_individual_paper_augmentation_cdf_baselines.csv", index=False)
    figure4_plot_rows.to_csv(RESULTS_DIR / "figure4_collection_augmentation_density_rows.csv", index=False)
    figure4_summary.to_csv(RESULTS_DIR / "figure4_collection_augmentation_density_summary.csv", index=False)

    plot_figure1_panel_b(figure1_rows, figure1_refs)
    figure1_cdf_percentiles = plot_figure1_panel_b_cdf(figure1_rows, figure1_refs)
    figure1_cdf_percentiles.to_csv(
        RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_percentiles.csv",
        index=False,
    )
    plot_figure2(figure2_plot_rows, figure2_delta, figure2_ceiling)
    plot_figure3(figure3_plot_rows, figure3_baseline)
    plot_figure3_density(figure3_plot_rows, figure3_baseline)
    plot_figure4_density(figure4_plot_rows, figure4_summary)


if __name__ == "__main__":
    main()
