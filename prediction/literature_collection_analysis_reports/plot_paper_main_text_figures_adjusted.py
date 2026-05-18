from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))
if str(ROOT / "analysis") not in sys.path:
    sys.path.insert(0, str(ROOT / "analysis"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D

from adjusted_correlation import (
    compare_adjusted_corr_conditions,
    fit_adjusted_corr,
    load_truth_and_sem,
    profile_likelihood_ci_adjusted_corr,
)


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_adjusted_correlation"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_adjusted_correlation"
HUMAN_PREDICTIONS_CSV = ROOT / "science_data" / "data" / "processed_data" / "prediction_survey.csv"
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
GROUP_COLORS = {"Laypeople": "#caa27e", "Experts": "#8d6748"}
MODEL_COLORS = {
    "GPT-4.1": "#2b8cbe",
    "GPT-4.1 Mini": "#1b9e77",
    "GPT-4.1 Nano": "#8c564b",
    "GPT-5.1": "#d95f02",
    "GPT-5 Mini": "#7570b3",
    "GPT-5 Nano": "#e7298a",
}
Q_COLS = [f"Q{i}" for i in range(1, 21)]


def load_human_predictions() -> tuple[pd.DataFrame, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    rows = pd.read_csv(HUMAN_PREDICTIONS_CSV)
    rows = rows.query("prediction.between(-0.2, 1.2) and n_predictions_made == 20").copy()
    truth, control, sem_y = load_truth_and_sem()
    config_ids = (
        pd.read_csv(ROOT / "science_data" / "data" / "processed_data" / "df_paired_val.csv")
        .sort_values("CONFIG_configId")["CONFIG_configId"]
        .to_numpy(dtype=int)
    )
    return rows, truth, control, sem_y, config_ids


def build_human_matrix(rows: pd.DataFrame, source: str, config_ids: np.ndarray) -> pd.DataFrame:
    wide = (
        rows.loc[rows["source"] == source, ["CONFIG_configId", "playerID", "prediction"]]
        .pivot_table(index="CONFIG_configId", columns="playerID", values="prediction", aggfunc="mean")
        .reindex(config_ids)
    )
    return wide.loc[:, wide.notna().all(axis=0)]


def compute_adjusted_many(mat: np.ndarray, truth: np.ndarray, sem_y: np.ndarray) -> np.ndarray:
    values = np.empty(mat.shape[0], dtype=float)
    init = None
    for i in range(mat.shape[0]):
        res = fit_adjusted_corr(mat[i], truth, sem_y, init_params=init)
        values[i] = float(res["r_adj"])
        init = np.asarray(res["params"], dtype=float)
    return values


def build_figure1_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    human_rows, truth_vec, control_vec, sem_y, config_ids = load_human_predictions()
    plot_rows: list[dict[str, object]] = []
    reference_rows: list[dict[str, object]] = []

    for source in SOURCE_ORDER:
        group = SOURCE_LABELS[source]
        mat = build_human_matrix(human_rows, source, config_ids).to_numpy(dtype=float).T * 100.0
        adjusted = compute_adjusted_many(mat, truth_vec, sem_y)
        plot_rows.extend(
            {"group": group, "value": float(value)}
            for value in adjusted
            if np.isfinite(value)
        )

    baseline_df = pd.read_csv(REPEAT5_BASELINE_AVG_PRED_CSV)
    for model in MODEL_ORDER:
        part = baseline_df.loc[baseline_df["model"] == model]
        if part.empty:
            continue
        res = fit_adjusted_corr(part.iloc[0][Q_COLS].to_numpy(dtype=float), truth_vec, sem_y)
        reference_rows.append({"label": model, "value": float(res["r_adj"]), "kind": "llm_model"})

    null_res = fit_adjusted_corr(control_vec, truth_vec, sem_y)
    reference_rows.append({"label": "No treatment effect", "value": float(null_res["r_adj"]), "kind": "null_baseline"})

    plot_df = pd.DataFrame(plot_rows)
    reference_df = pd.DataFrame(reference_rows)
    return plot_df, reference_df.sort_values(["kind", "value"]).reset_index(drop=True)


def build_figure2_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    truth, _, sem_y = load_truth_and_sem()
    avg_pred = pd.read_csv(REPEAT5_AVG_PRED_CSV)
    baseline_avg = pd.read_csv(REPEAT5_BASELINE_AVG_PRED_CSV)

    plot_rows: list[dict[str, object]] = []
    delta_rows: list[dict[str, object]] = []

    for model in MODEL_ORDER:
        baseline_row = baseline_avg.loc[baseline_avg["model"] == model]
        benchmark_row = avg_pred.loc[(avg_pred["model"] == model) & (avg_pred["variant_id"] == "benchmark_pgg_ms")]
        if baseline_row.empty or benchmark_row.empty:
            continue
        baseline_vec = baseline_row.iloc[0][Q_COLS].to_numpy(dtype=float)
        benchmark_vec = benchmark_row.iloc[0][Q_COLS].to_numpy(dtype=float)
        baseline_fit = profile_likelihood_ci_adjusted_corr(
            baseline_vec,
            truth,
            sem_y,
            level=0.95,
        )
        benchmark_fit = profile_likelihood_ci_adjusted_corr(
            benchmark_vec,
            truth,
            sem_y,
            level=0.95,
        )
        comparison = compare_adjusted_corr_conditions(
            baseline_vec,
            benchmark_vec,
            truth,
            sem_y,
        )
        plot_rows.extend(
            [
                {
                    "model": model,
                    "condition": "baseline",
                    "correlation": float(baseline_fit["r_adj"]),
                    "ci_low": float(baseline_fit["ci_low"]),
                    "ci_high": float(baseline_fit["ci_high"]),
                },
                {
                    "model": model,
                    "condition": "benchmark",
                    "correlation": float(benchmark_fit["r_adj"]),
                    "ci_low": float(benchmark_fit["ci_low"]),
                    "ci_high": float(benchmark_fit["ci_high"]),
                },
            ]
        )
        delta_rows.append(
            {
                "model": model,
                "baseline_correlation": float(baseline_fit["r_adj"]),
                "correlation": float(benchmark_fit["r_adj"]),
                "delta_correlation": float(benchmark_fit["r_adj"]) - float(baseline_fit["r_adj"]),
                "p_value": float(comparison["p_value"]),
                "lr_stat": float(comparison["lr_stat"]),
                "paired_sig_label": str(comparison["sig_label"]),
            }
        )

    plot_df = pd.DataFrame(plot_rows)
    baseline_order = (
        plot_df.loc[plot_df["condition"] == "baseline", ["model", "correlation"]]
        .sort_values("correlation", ascending=False)["model"].tolist()
    )
    plot_df["model"] = pd.Categorical(plot_df["model"], categories=baseline_order, ordered=True)
    delta_df = pd.DataFrame(delta_rows)
    delta_df["model"] = pd.Categorical(delta_df["model"], categories=baseline_order, ordered=True)
    return (
        plot_df.sort_values(["model", "condition"]).reset_index(drop=True),
        delta_df.sort_values("model").reset_index(drop=True),
    )


def _fit_condition_reference_map() -> dict[tuple[str, str], float]:
    truth, _, sem_y = load_truth_and_sem()
    base_df = pd.read_csv(REPEAT5_BASELINE_AVG_PRED_CSV)
    aug_df = pd.read_csv(REPEAT5_AVG_PRED_CSV)
    out: dict[tuple[str, str], float] = {}
    for model in set(FIGURE3_MODEL_ORDER):
        part = base_df.loc[base_df["model"] == model]
        if not part.empty:
            out[(model, "baseline")] = float(
                fit_adjusted_corr(part.iloc[0][Q_COLS].to_numpy(dtype=float), truth, sem_y)["r_adj"]
            )
        bench = aug_df.loc[(aug_df["model"] == model) & (aug_df["variant_id"] == "benchmark_pgg_ms")]
        if not bench.empty:
            out[(model, "benchmark")] = float(
                fit_adjusted_corr(bench.iloc[0][Q_COLS].to_numpy(dtype=float), truth, sem_y)["r_adj"]
            )
    return out


def build_figure3_data(ref_map: dict[tuple[str, str], float]) -> tuple[pd.DataFrame, pd.DataFrame]:
    truth, _, sem_y = load_truth_and_sem()
    df = pd.read_csv(SINGLE_PAPER_SIGNIFICANCE_CSV)
    df = df.loc[df["model"].isin(FIGURE3_MODEL_ORDER), ["model", "source_id", *Q_COLS]].copy() if set(Q_COLS).issubset(df.columns) else None
    if df is None:
        # Recover vectors from the saved average-prediction table.
        avg = pd.read_csv(
            ROOT
            / "results"
            / "validation"
            / "literature_analysis_report_sources_repeat5"
            / "validation_literature_analysis_report_source_avg_predictions.csv"
        )
        df = avg.loc[avg["model"].isin(FIGURE3_MODEL_ORDER), ["model", "source_id", *Q_COLS]].copy()

    rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []
    for model in FIGURE3_MODEL_ORDER:
        sub = df.loc[df["model"] == model].sort_values("source_id").reset_index(drop=True)
        if sub.empty:
            continue
        adjusted = compute_adjusted_many(sub[Q_COLS].to_numpy(dtype=float), truth, sem_y)
        model_rows = pd.DataFrame({"model": model, "source_id": sub["source_id"], "correlation": adjusted})
        rows.append(model_rows)
        summary_rows.append(
            {
                "model": model,
                "baseline_correlation": ref_map[(model, "baseline")],
                "benchmark_correlation": ref_map[(model, "benchmark")],
                "mean_augmented_correlation": float(np.nanmean(adjusted)),
                "n_papers": int(len(adjusted)),
            }
        )

    plot_df = pd.concat(rows, ignore_index=True)
    plot_df["model"] = pd.Categorical(plot_df["model"], categories=FIGURE3_MODEL_ORDER, ordered=True)
    plot_df = plot_df.sort_values(["model", "correlation"]).reset_index(drop=True)
    summary_df = pd.DataFrame(summary_rows)
    summary_df["model"] = pd.Categorical(summary_df["model"], categories=FIGURE3_MODEL_ORDER, ordered=True)
    summary_df = summary_df.sort_values("model").reset_index(drop=True)
    return plot_df, summary_df


def build_figure4_data(ref_map: dict[tuple[str, str], float]) -> tuple[pd.DataFrame, pd.DataFrame]:
    truth, _, sem_y = load_truth_and_sem()
    avg = pd.read_csv(
        ROOT
        / "results"
        / "validation"
        / "literature_collection_analysis_reports_metadata_filters"
        / "validation_literature_collection_analysis_report_metadata_filters_avg_predictions.csv"
    )
    avg = avg.loc[(avg["variant_group"] == "metadata_filter") & (avg["model"].isin(FIGURE3_MODEL_ORDER))].copy()

    rows: list[pd.DataFrame] = []
    summary_rows: list[dict[str, object]] = []
    for model in FIGURE3_MODEL_ORDER:
        sub = avg.loc[avg["model"] == model].sort_values("variant_id").reset_index(drop=True)
        if sub.empty:
            continue
        adjusted = compute_adjusted_many(sub[Q_COLS].to_numpy(dtype=float), truth, sem_y)
        rows.append(pd.DataFrame({"model": model, "variant_id": sub["variant_id"], "correlation": adjusted}))
        summary_rows.append(
            {
                "model": model,
                "baseline_correlation": ref_map[(model, "baseline")],
                "benchmark_correlation": ref_map[(model, "benchmark")],
                "mean_augmented_correlation": float(np.nanmean(adjusted)),
                "n_collections": int(len(adjusted)),
            }
        )

    plot_df = pd.concat(rows, ignore_index=True)
    plot_df["model"] = pd.Categorical(plot_df["model"], categories=FIGURE3_MODEL_ORDER, ordered=True)
    plot_df = plot_df.sort_values(["model", "correlation"]).reset_index(drop=True)
    summary_df = pd.DataFrame(summary_rows)
    summary_df["model"] = pd.Categorical(summary_df["model"], categories=FIGURE3_MODEL_ORDER, ordered=True)
    summary_df = summary_df.sort_values("model").reset_index(drop=True)
    return plot_df, summary_df


def plot_figure1_cdf(plot_df: pd.DataFrame, reference_df: pd.DataFrame) -> pd.DataFrame:
    fig, ax = plt.subplots(figsize=(9.4, 6.2))
    human_counts = {group: int(plot_df.loc[plot_df["group"] == group].shape[0]) for group in ["Laypeople", "Experts"]}
    for group in ["Laypeople", "Experts"]:
        vals = plot_df.loc[plot_df["group"] == group, "value"].to_numpy(dtype=float)
        sns.ecdfplot(x=vals, stat="proportion", linewidth=2.4, color=GROUP_COLORS[group], label=group, ax=ax)

    x_min, x_max = 0.65, 1.0
    llm_refs = reference_df.loc[reference_df["kind"] == "llm_model"].sort_values("value")
    null_ref = reference_df.loc[reference_df["kind"] == "null_baseline"]
    percentile_rows: list[dict[str, object]] = []

    for _, row in llm_refs.iterrows():
        value = float(row["value"])
        label = str(row["label"])
        ax.axvline(value, color=MODEL_COLORS[label], linewidth=1.4, alpha=0.95, zorder=3)
        percentile_row = {"label": label, "value": value, "kind": "llm_model"}
        for group in ["Laypeople", "Experts"]:
            group_vals = plot_df.loc[plot_df["group"] == group, "value"].to_numpy(dtype=float)
            percentile_row[f"share_{group.lower()}_below"] = float(np.mean(group_vals <= value))
        percentile_rows.append(percentile_row)

    if not null_ref.empty:
        value = float(null_ref["value"].iloc[0])
        ax.axvline(value, color="#111827", linewidth=1.8, linestyle="--", alpha=0.9, zorder=2)
        percentile_row = {"label": "No treatment effect", "value": value, "kind": "null_baseline"}
        for group in ["Laypeople", "Experts"]:
            group_vals = plot_df.loc[plot_df["group"] == group, "value"].to_numpy(dtype=float)
            percentile_row[f"share_{group.lower()}_below"] = float(np.mean(group_vals <= value))
        percentile_rows.append(percentile_row)

    for row in percentile_rows:
        if row["kind"] != "llm_model":
            continue
        for group, share_col, color in [
            ("Laypeople", "share_laypeople_below", GROUP_COLORS["Laypeople"]),
            ("Experts", "share_experts_below", GROUP_COLORS["Experts"]),
        ]:
            ax.hlines(
                y=float(row[share_col]),
                xmin=x_min,
                xmax=float(row["value"]),
                color=color,
                linewidth=0.9,
                alpha=0.7,
                linestyle="--",
                zorder=1,
            )

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(0.0, 1.02)
    ax.set_xticks(np.arange(0.65, 1.01, 0.05))
    ax.set_yticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel("Adjusted correlation with true treatment outcome")
    ax.set_ylabel("Cumulative share")
    ax.grid(False)

    legend_items = [
        Line2D([0], [0], color=GROUP_COLORS["Laypeople"], linewidth=2.4, label=f"Laypeople (n={human_counts['Laypeople']})"),
        Line2D([0], [0], color=GROUP_COLORS["Experts"], linewidth=2.4, label=f"Experts (n={human_counts['Experts']})"),
        Line2D([0], [0], color="#111827", linewidth=1.8, linestyle="--", label="No-treatment-effect baseline"),
    ]
    for model in llm_refs["label"].tolist():
        legend_items.append(Line2D([0], [0], color=MODEL_COLORS[model], linewidth=1.4, label=model))
    ax.legend(handles=legend_items, loc="upper left", bbox_to_anchor=(0.0, -0.17), ncol=3, frameon=False, columnspacing=1.0, handlelength=2.0, borderaxespad=0.0)
    fig.subplots_adjust(bottom=0.25, left=0.1, right=0.98, top=0.98)

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure1_panel_b_baseline_vs_humans_adjusted_correlation_cdf.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)
    percentile_df = pd.DataFrame(percentile_rows)
    percentile_df["pct_laypeople_below"] = percentile_df["share_laypeople_below"] * 100.0
    percentile_df["pct_experts_below"] = percentile_df["share_experts_below"] * 100.0
    return percentile_df


def plot_figure2(plot_df: pd.DataFrame, delta_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(10.0, 5.7))
    model_order = plot_df["model"].cat.categories.tolist()
    y_positions = np.arange(len(model_order))
    offsets = {"baseline": -0.18, "benchmark": 0.18}
    colors = {"baseline": "#c9ced6", "benchmark": "#f2a65a"}
    labels = {"baseline": "No augmentation", "benchmark": "Benchmark paper augmented"}
    delta_lookup = delta_df.set_index("model")
    bracket_color = "#6b7280"

    for condition in ["baseline", "benchmark"]:
        part = plot_df.loc[plot_df["condition"] == condition].set_index("model").reindex(model_order).reset_index()
        y = y_positions + offsets[condition]
        ax.barh(y, part["correlation"].to_numpy(dtype=float), color=colors[condition], edgecolor="#4b5563", linewidth=0.8, height=0.32, zorder=2, label=labels[condition])
        xerr = np.vstack([
            part["correlation"].to_numpy(dtype=float) - part["ci_low"].to_numpy(dtype=float),
            part["ci_high"].to_numpy(dtype=float) - part["correlation"].to_numpy(dtype=float),
        ])
        ax.errorbar(part["correlation"].to_numpy(dtype=float), y, xerr=xerr, fmt="none", ecolor=(17 / 255, 24 / 255, 39 / 255, 0.22), elinewidth=0.9, capsize=2.5, zorder=3)

    bracket_x = 0.95
    bracket_left = 0.935
    for idx, model in enumerate(model_order):
        row = delta_lookup.loc[model]
        y0 = y_positions[idx] + offsets["baseline"]
        y1 = y_positions[idx] + offsets["benchmark"]
        ax.plot([bracket_left, bracket_x, bracket_x, bracket_left], [y0, y0, y1, y1], color=bracket_color, linewidth=1.2, zorder=4, clip_on=True)
        sig_label = str(row["paired_sig_label"])
        ax.text(bracket_x + 0.008, (y0 + y1) / 2.0, sig_label, ha="left", va="center", fontsize=11.2, fontstyle="italic" if sig_label == "n.s." else "normal", fontweight="semibold" if sig_label != "n.s." else "normal", color=bracket_color, zorder=5, clip_on=True, bbox={"boxstyle": "round,pad=0.08", "facecolor": "white", "edgecolor": "none"})

    ax.set_xlim(0.0, 1.0)
    ax.set_xticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel("Adjusted correlation with true treatment outcome")
    ax.set_yticks(y_positions, model_order)
    ax.invert_yaxis()
    ax.grid(False)
    legend_items = [
        Line2D([0], [0], color=colors["baseline"], linewidth=8, label=labels["baseline"]),
        Line2D([0], [0], color=colors["benchmark"], linewidth=8, label=labels["benchmark"]),
    ]
    ax.legend(handles=legend_items, frameon=False, loc="upper left", bbox_to_anchor=(0.0, -0.14), ncol=2, columnspacing=1.2, handlelength=2.4, borderaxespad=0.0)
    fig.text(0.99, 0.02, "Bars show 95% profile-likelihood CI for adjusted correlation.  * p < 0.05   ** p < 0.01   n.s. otherwise", ha="right", va="bottom", fontsize=9.0, color="#4b5563")
    fig.subplots_adjust(bottom=0.22, right=0.95)
    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure2_benchmark_report_vs_baseline_adjusted_correlation.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_figure3_cdf(plot_df: pd.DataFrame, summary_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(9.8, 6.2))
    x_min, x_max = 0.0, 1.0
    baseline_min = float(summary_df["baseline_correlation"].min())
    baseline_max = float(summary_df["baseline_correlation"].max())
    benchmark_min = float(summary_df["benchmark_correlation"].min())
    benchmark_max = float(summary_df["benchmark_correlation"].max())

    for model in FIGURE3_MODEL_ORDER:
        sub = plot_df.loc[plot_df["model"] == model]
        vals = sub["correlation"].to_numpy(dtype=float)
        sns.ecdfplot(x=vals, stat="proportion", linewidth=2.0, color=MODEL_COLORS[model], alpha=0.78, ax=ax)
        refs = summary_df.loc[summary_df["model"] == model].iloc[0]
        ax.axvline(float(refs["baseline_correlation"]), color=MODEL_COLORS[model], linewidth=1.0, linestyle="--", alpha=0.95, zorder=3)
        ax.axvline(float(refs["benchmark_correlation"]), color=MODEL_COLORS[model], linewidth=1.0, linestyle=":", alpha=0.95, zorder=3)

    def add_range_marker(x0: float, x1: float, y_axes: float, color: str, label: str) -> None:
        transform = ax.get_xaxis_transform()
        ax.plot([x0, x1], [y_axes, y_axes], color=color, linewidth=1.5, zorder=4, clip_on=False, transform=transform)
        ax.plot([x0, x0], [y_axes - 0.02, y_axes + 0.02], color=color, linewidth=1.5, zorder=4, clip_on=False, transform=transform)
        ax.plot([x1, x1], [y_axes - 0.02, y_axes + 0.02], color=color, linewidth=1.5, zorder=4, clip_on=False, transform=transform)
        ax.text((x0 + x1) / 2.0, y_axes + 0.01, label, ha="center", va="bottom", fontsize=9.2, color=color, transform=transform, bbox={"boxstyle": "round,pad=0.08", "facecolor": "white", "edgecolor": "none"}, clip_on=False)

    add_range_marker(baseline_min, baseline_max, 1.01, "#6b7280", "No augmentation")
    add_range_marker(benchmark_min, benchmark_max, 1.065, "#b45309", "Benchmark paper augmented")

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(0.0, 1.02)
    ax.set_xticks(np.arange(0.0, 1.01, 0.1))
    ax.set_yticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel("Adjusted correlation with true treatment outcome")
    ax.set_ylabel("Cumulative share")
    ax.grid(False)
    legend_items = [Line2D([0], [0], color=MODEL_COLORS[m], linewidth=2.0, alpha=0.78, label=m) for m in FIGURE3_MODEL_ORDER]
    legend_items += [
        Line2D([0], [0], color="#4b5563", linewidth=1.15, linestyle="--", label="No augmentation"),
        Line2D([0], [0], color="#4b5563", linewidth=1.15, linestyle=":", label="Benchmark paper augmented"),
    ]
    ax.legend(handles=legend_items, loc="upper left", bbox_to_anchor=(0.0, -0.18), ncol=3, frameon=False, columnspacing=1.1, handlelength=2.2, borderaxespad=0.0)
    fig.subplots_adjust(bottom=0.24, top=0.84)
    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure3_individual_paper_augmentation_adjusted_correlation_cdf.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def _plot_density(plot_df: pd.DataFrame, summary_df: pd.DataFrame, *, item_label: str, out_stem: str) -> None:
    fig, axes = plt.subplots(len(FIGURE3_MODEL_ORDER), 1, figsize=(8.8, 7.6), sharex=True, gridspec_kw={"hspace": 0.08})
    x_min, x_max = 0.0, 1.0
    for ax, model in zip(axes, FIGURE3_MODEL_ORDER):
        sub = plot_df.loc[plot_df["model"] == model]
        refs = summary_df.loc[summary_df["model"] == model].iloc[0]
        vals = sub["correlation"].to_numpy(dtype=float)
        sns.kdeplot(x=vals, ax=ax, color=MODEL_COLORS[model], fill=True, alpha=0.18, linewidth=1.8, bw_adjust=0.9, cut=0, clip=(x_min, x_max))
        ax.axvline(float(refs["mean_augmented_correlation"]), color=MODEL_COLORS[model], linewidth=1.4, alpha=0.95)
        ax.annotate("", xy=(float(refs["mean_augmented_correlation"]), 0.84), xytext=(float(refs["baseline_correlation"]), 0.84), xycoords=("data", "axes fraction"), textcoords=("data", "axes fraction"), annotation_clip=False, zorder=5, arrowprops={"arrowstyle": "-|>", "lw": 1.15, "color": MODEL_COLORS[model], "alpha": 0.9, "mutation_scale": 10, "shrinkA": 0, "shrinkB": 0})
        ax.axvline(float(refs["baseline_correlation"]), color=MODEL_COLORS[model], linewidth=1.1, linestyle="--", alpha=0.95)
        ax.axvline(float(refs["benchmark_correlation"]), color=MODEL_COLORS[model], linewidth=1.1, linestyle=":", alpha=0.95)
        ax.text(0.01, 0.82, model, transform=ax.transAxes, ha="left", va="center", fontsize=11.0, color=MODEL_COLORS[model])
        ax.set_yticks([])
        ax.grid(False)
        ax.spines["right"].set_visible(False)
        ax.spines["top"].set_visible(False)

    axes[-1].set_xlim(x_min, x_max)
    axes[-1].set_xticks(np.arange(0.0, 1.01, 0.1))
    axes[-1].set_xlabel("Adjusted correlation with true treatment outcome")
    fig.text(0.03, 0.5, "Probability density", rotation=90, va="center", ha="center")
    legend_items = [
        Line2D([0], [0], color="#4b5563", linewidth=1.4, label=f"Average augmented {item_label}"),
        Line2D([0], [0], color="#4b5563", linewidth=1.1, linestyle="--", label="No augmentation"),
        Line2D([0], [0], color="#4b5563", linewidth=1.1, linestyle=":", label="Benchmark paper augmented"),
    ]
    fig.legend(handles=legend_items, loc="upper center", bbox_to_anchor=(0.54, 0.995), ncol=2, frameon=False, columnspacing=1.6, handlelength=2.6, borderaxespad=0.0)
    fig.subplots_adjust(bottom=0.09, left=0.08, top=0.93, right=0.98)
    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"{out_stem}.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    fig1_rows, fig1_refs = build_figure1_data()
    fig2_plot, fig2_delta = build_figure2_data()
    ref_map = _fit_condition_reference_map()
    fig3_plot, fig3_summary = build_figure3_data(ref_map)
    fig4_plot, fig4_summary = build_figure4_data(ref_map)

    fig1_rows.to_csv(RESULTS_DIR / "figure1_adjusted_correlation_rows.csv", index=False)
    fig1_refs.to_csv(RESULTS_DIR / "figure1_adjusted_correlation_reference_lines.csv", index=False)
    fig2_plot.to_csv(RESULTS_DIR / "figure2_adjusted_correlation_plot_rows.csv", index=False)
    fig2_delta.to_csv(RESULTS_DIR / "figure2_adjusted_correlation_summary.csv", index=False)
    fig3_plot.to_csv(RESULTS_DIR / "figure3_individual_paper_adjusted_correlation_rows.csv", index=False)
    fig3_summary.to_csv(RESULTS_DIR / "figure3_individual_paper_adjusted_correlation_summary.csv", index=False)
    fig4_plot.to_csv(RESULTS_DIR / "figure4_collection_adjusted_correlation_rows.csv", index=False)
    fig4_summary.to_csv(RESULTS_DIR / "figure4_collection_adjusted_correlation_summary.csv", index=False)

    percentiles = plot_figure1_cdf(fig1_rows, fig1_refs)
    percentiles.to_csv(RESULTS_DIR / "figure1_adjusted_correlation_cdf_percentiles.csv", index=False)
    plot_figure2(fig2_plot, fig2_delta)
    plot_figure3_cdf(fig3_plot, fig3_summary)
    _plot_density(fig3_plot, fig3_summary, item_label="paper", out_stem="figure3_individual_paper_augmentation_adjusted_correlation_density")
    _plot_density(fig4_plot, fig4_summary, item_label="collection", out_stem="figure4_collection_augmentation_adjusted_correlation_density")


if __name__ == "__main__":
    sns.set_theme(style="white", context="talk")
    main()
