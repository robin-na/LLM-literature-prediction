from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2] / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D


ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"
NO_AUG_BENCHMARKS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "no_augmentation_model_comparison"
    / "validation_no_augmentation_model_comparison_benchmarks.csv"
)
LLM_BASELINE_SUMMARY_CSV = RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_llm_mean30_model_summary.csv"
PAPER_METRICS_CSV = RESULTS_DIR / "paper_repeat_correlation_metrics.csv"
COLLECTION_METRICS_CSV = RESULTS_DIR / "collection_repeat_correlation_metrics.csv"

FIG3_ROWS_CSV = RESULTS_DIR / "figure3_individual_paper_augmentation_cdf_rows.csv"
FIG3_SUMMARY_CSV = RESULTS_DIR / "figure3_individual_paper_augmentation_cdf_baselines.csv"
FIG4_ROWS_CSV = RESULTS_DIR / "figure4_collection_augmentation_density_rows.csv"
FIG4_SUMMARY_CSV = RESULTS_DIR / "figure4_collection_augmentation_density_summary.csv"

MODEL_COLORS = {
    "Claude Sonnet 4.6": "#9c755f",
    "Gemini 2.5 Pro": "#17becf",
    "GPT-4.1": "#2b8cbe",
    "GPT-4.1 Mini": "#1b9e77",
    "GPT-5.1": "#d95f02",
    "GPT-5 Mini": "#7570b3",
    "GPT-5 Nano": "#e7298a",
}


def load_noise_ceiling() -> float:
    benchmarks = pd.read_csv(NO_AUG_BENCHMARKS_CSV)
    return float(benchmarks.loc[benchmarks["benchmark"] == "Noise ceiling", "correlation"].iloc[0])


def load_model_order(available_models: list[str]) -> list[str]:
    baseline_summary = pd.read_csv(LLM_BASELINE_SUMMARY_CSV)
    ranked = baseline_summary.loc[baseline_summary["model"].isin(available_models), "model"].astype(str).tolist()
    return [model for model in ranked if model in available_models]


def load_baseline_override_map(available_models: list[str]) -> dict[str, float]:
    baseline_summary = pd.read_csv(LLM_BASELINE_SUMMARY_CSV)
    baseline_summary = baseline_summary.loc[baseline_summary["model"].isin(available_models)].copy()
    return {
        str(row["model"]): float(row["correlation_mean_prediction"])
        for _, row in baseline_summary.iterrows()
    }


def build_figure3_tables(
    paper_metrics_df: pd.DataFrame,
    model_order: list[str],
    baseline_override_map: dict[str, float],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    plot_df = paper_metrics_df.loc[:, ["model", "source_id", "correlation", "baseline_correlation"]].copy()
    plot_df["model"] = pd.Categorical(plot_df["model"], categories=model_order, ordered=True)
    plot_df = plot_df.sort_values(["model", "correlation"]).reset_index(drop=True)

    summary_rows: list[dict[str, object]] = []
    for model in model_order:
        sub = plot_df.loc[plot_df["model"] == model].copy()
        original_baseline = float(sub["baseline_correlation"].iloc[0])
        baseline = float(baseline_override_map.get(model, original_baseline))
        mean_aug = float(sub["correlation"].mean())
        count_above = int((sub["correlation"] > baseline).sum())
        count_below_or_equal = int(sub.shape[0] - count_above)
        share_below = float(count_below_or_equal / sub.shape[0])
        summary_rows.append(
            {
                "model": model,
                "baseline_correlation": baseline,
                "baseline_correlation_previous_5run": original_baseline,
                "mean_augmented_correlation": mean_aug,
                "sd_augmented_correlation": float(sub["correlation"].std(ddof=1)),
                "n_above_baseline": count_above,
                "n_below_or_equal_baseline": count_below_or_equal,
                "share_augmented_papers_below_baseline": share_below,
                "share_augmented_papers_above_baseline": 1.0 - share_below,
                "n_papers": int(sub.shape[0]),
            }
        )
    summary_df = pd.DataFrame(summary_rows)
    summary_df["model"] = pd.Categorical(summary_df["model"], categories=model_order, ordered=True)
    summary_df = summary_df.sort_values("model").reset_index(drop=True)
    return plot_df, summary_df


def build_figure4_tables(
    collection_metrics_df: pd.DataFrame,
    model_order: list[str],
    baseline_override_map: dict[str, float],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    plot_df = collection_metrics_df.loc[:, ["model", "variant_id", "correlation", "baseline_correlation"]].copy()
    plot_df["model"] = pd.Categorical(plot_df["model"], categories=model_order, ordered=True)
    plot_df = plot_df.sort_values(["model", "correlation"]).reset_index(drop=True)

    summary_rows: list[dict[str, object]] = []
    for model in model_order:
        sub = plot_df.loc[plot_df["model"] == model].copy()
        original_baseline = float(sub["baseline_correlation"].iloc[0])
        baseline = float(baseline_override_map.get(model, original_baseline))
        count_above = int((sub["correlation"] > baseline).sum())
        count_below_or_equal = int(sub.shape[0] - count_above)
        summary_rows.append(
            {
                "model": model,
                "baseline_correlation": baseline,
                "baseline_correlation_previous_5run": original_baseline,
                "mean_augmented_correlation": float(sub["correlation"].mean()),
                "sd_augmented_correlation": float(sub["correlation"].std(ddof=1)),
                "n_above_baseline": count_above,
                "n_below_or_equal_baseline": count_below_or_equal,
                "share_augmented_collections_above_baseline": float(count_above / sub.shape[0]),
                "share_augmented_collections_below_or_equal_baseline": float(count_below_or_equal / sub.shape[0]),
                "n_collections": int(sub.shape[0]),
            }
        )
    summary_df = pd.DataFrame(summary_rows)
    summary_df["model"] = pd.Categorical(summary_df["model"], categories=model_order, ordered=True)
    summary_df = summary_df.sort_values("model").reset_index(drop=True)
    return plot_df, summary_df


def plot_density_figure(
    plot_df: pd.DataFrame,
    summary_df: pd.DataFrame,
    *,
    model_order: list[str],
    mean_label: str,
    out_stem: str,
    item_label: str,
) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, axes = plt.subplots(
        len(model_order),
        1,
        figsize=(8.8, 8.8),
        sharex=True,
        gridspec_kw={"hspace": 0.08},
    )

    x_min, x_max = 0.0, 0.90
    ceiling = load_noise_ceiling()
    for ax, model in zip(axes, model_order):
        sub = plot_df.loc[plot_df["model"] == model]
        refs = summary_df.loc[summary_df["model"] == model].iloc[0]
        vals = sub["correlation"].to_numpy(dtype=float)
        baseline_value = float(refs["baseline_correlation"])

        sns.kdeplot(
            x=vals,
            ax=ax,
            color=MODEL_COLORS[model],
            fill=False,
            linewidth=1.8,
            bw_adjust=0.9,
            cut=0,
            clip=(x_min, x_max),
        )
        kde_line = ax.lines[-1]
        x_kde = np.asarray(kde_line.get_xdata(), dtype=float)
        y_kde = np.asarray(kde_line.get_ydata(), dtype=float)
        mask = x_kde >= baseline_value
        if mask.any():
            ax.fill_between(
                x_kde[mask],
                y_kde[mask],
                0.0,
                color=MODEL_COLORS[model],
                alpha=0.18,
                zorder=1,
            )

        ax.axvline(
            float(refs["mean_augmented_correlation"]),
            color=MODEL_COLORS[model],
            linewidth=1.4,
            alpha=0.95,
            zorder=3,
        )
        ax.annotate(
            "",
            xy=(float(refs["mean_augmented_correlation"]), 0.84),
            xytext=(baseline_value, 0.84),
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
            baseline_value,
            color=MODEL_COLORS[model],
            linewidth=1.1,
            linestyle="--",
            alpha=0.95,
            zorder=3,
        )
        ax.axvline(
            ceiling,
            color="#111111",
            linewidth=1.0,
            linestyle=":",
            alpha=0.95,
            zorder=2,
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
        ax.text(
            0.01,
            0.66,
            f"mean={float(refs['mean_augmented_correlation']):.3f}, SD={float(refs['sd_augmented_correlation']):.3f}",
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=8.9,
            color="#4b5563",
        )
        ax.text(
            0.01,
            0.53,
            f"no augmentation={baseline_value:.3f}",
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=8.9,
            color="#4b5563",
        )
        total_inputs = int(refs["n_papers"]) if "n_papers" in refs.index else int(refs["n_collections"])
        count_above = int(refs["n_above_baseline"])
        pct_above = 100.0 * float(count_above / total_inputs)
        ax.text(
            0.985,
            0.88,
            f"{pct_above:.0f}% of augmentations\nsurpass the unaugmented",
            transform=ax.transAxes,
            ha="right",
            va="top",
            fontsize=8.8,
            fontweight="semibold",
            color=MODEL_COLORS[model],
            bbox={"boxstyle": "round,pad=0.18", "facecolor": "white", "edgecolor": "none", "alpha": 0.92},
        )
        ax.text(
            0.985,
            0.56,
            f"{count_above:,} / {total_inputs:,} {item_label}",
            transform=ax.transAxes,
            ha="right",
            va="center",
            fontsize=8.9,
            color="#4b5563",
            bbox={"boxstyle": "round,pad=0.12", "facecolor": "white", "edgecolor": "none", "alpha": 0.92},
        )
        ax.set_yticks([])
        ax.set_ylabel("")
        ax.set_xticks(np.arange(0.0, 0.91, 0.2))
        ax.set_xticks(np.arange(0.0, 0.91, 0.1), minor=True)
        ax.grid(axis="x", which="minor", color="#e5e7eb", linewidth=0.8)
        ax.grid(axis="x", which="major", color="#e5e7eb", linewidth=0.0)
        ax.grid(axis="y", visible=False)
        ax.spines["right"].set_visible(False)
        ax.spines["top"].set_visible(False)

    axes[-1].set_xlim(x_min, x_max)
    axes[-1].set_xticks(np.arange(0.0, 0.91, 0.2))
    axes[-1].set_xticks(np.arange(0.0, 0.91, 0.1), minor=True)
    axes[-1].set_xlabel(r"$\mathrm{Corr}(y_{\mathrm{true}}, y_{\mathrm{pred}})$")
    fig.text(0.03, 0.5, "Probability density", rotation=90, va="center", ha="center")

    legend_items = [
        Line2D([0], [0], color="#4b5563", linewidth=1.4, label=mean_label),
        Line2D([0], [0], color="#4b5563", linewidth=1.1, linestyle="--", label="No augmentation"),
        Line2D([0], [0], color="#111111", linewidth=1.0, linestyle=":", label="Estimated ceiling"),
    ]
    fig.legend(
        handles=legend_items,
        loc="upper center",
        bbox_to_anchor=(0.47, 0.995),
        ncol=3,
        frameon=False,
        columnspacing=1.6,
        handlelength=2.6,
        borderaxespad=0.0,
    )
    fig.subplots_adjust(bottom=0.09, left=0.08, top=0.94, right=0.98)

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"{out_stem}.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    paper_metrics_df = pd.read_csv(PAPER_METRICS_CSV)
    collection_metrics_df = pd.read_csv(COLLECTION_METRICS_CSV)

    available_models = sorted(set(paper_metrics_df["model"]).intersection(collection_metrics_df["model"]))
    model_order = load_model_order(available_models)
    baseline_override_map = load_baseline_override_map(available_models)

    figure3_rows, figure3_summary = build_figure3_tables(paper_metrics_df, model_order, baseline_override_map)
    figure4_rows, figure4_summary = build_figure4_tables(collection_metrics_df, model_order, baseline_override_map)

    figure3_rows.to_csv(FIG3_ROWS_CSV, index=False)
    figure3_summary.to_csv(FIG3_SUMMARY_CSV, index=False)
    figure4_rows.to_csv(FIG4_ROWS_CSV, index=False)
    figure4_summary.to_csv(FIG4_SUMMARY_CSV, index=False)

    plot_density_figure(
        figure3_rows,
        figure3_summary,
        model_order=model_order,
        mean_label="Average augmented paper",
        out_stem="figure3_individual_paper_augmentation_density_correlation",
        item_label="papers",
    )
    plot_density_figure(
        figure4_rows,
        figure4_summary,
        model_order=model_order,
        mean_label="Average augmented collection",
        out_stem="figure4_collection_augmentation_density_correlation",
        item_label="collections",
    )


if __name__ == "__main__":
    main()
