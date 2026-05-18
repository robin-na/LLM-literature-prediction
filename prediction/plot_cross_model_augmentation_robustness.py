from __future__ import annotations

from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PAPER_CSV = (
    PROJECT_ROOT
    / "results"
    / "validation"
    / "literature_analysis_report_sources_overview"
    / "single_paper_overview_dataset.csv"
)
COLLECTION_CSV = (
    PROJECT_ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_metadata_filters"
    / "validation_literature_collection_analysis_report_metadata_filters_rows.csv"
)
RESULTS_DIR = PROJECT_ROOT / "results" / "paper" / "robustness"
PLOTS_DIR = PROJECT_ROOT / "plots" / "paper" / "exploratory"

MODELS = ["GPT-5 Mini", "GPT-5 Nano", "GPT-4.1", "GPT-4.1 Mini", "GPT-5.1"]
MODEL_SUBSETS = {
    "all_5_models": MODELS,
    "without_gpt_5_1": ["GPT-5 Mini", "GPT-5 Nano", "GPT-4.1", "GPT-4.1 Mini"],
}
EPSILON = 0.02


def load_paper_wide(models: list[str]) -> pd.DataFrame:
    df = pd.read_csv(PAPER_CSV)
    wide = (
        df.loc[df["model"].isin(models), ["source_id", "model", "delta_correlation"]]
        .pivot(index="source_id", columns="model", values="delta_correlation")
        .dropna()
        .reindex(columns=models)
    )
    return wide


def load_collection_wide(models: list[str]) -> pd.DataFrame:
    df = pd.read_csv(COLLECTION_CSV)
    wide = (
        df.loc[
            (df["variant_group"] == "metadata_filter") & df["model"].isin(models),
            ["variant_id", "model", "delta_correlation"],
        ]
        .pivot(index="variant_id", columns="model", values="delta_correlation")
        .dropna()
        .reindex(columns=models)
    )
    return wide


def classify_effect(series: pd.Series, epsilon: float) -> pd.Series:
    return pd.cut(
        series,
        bins=[-np.inf, -epsilon, epsilon, np.inf],
        labels=["hurt", "neutral", "help"],
    )


def pairwise_metric_rows(
    wide: pd.DataFrame,
    *,
    kind: str,
    model_subset: str,
    epsilon: float,
) -> pd.DataFrame:
    rows: list[dict[str, float | str | int]] = []
    n_items = len(wide)
    upper_idx = np.triu_indices(n_items, k=1)
    values = {model: wide[model].to_numpy() for model in wide.columns}
    categories = {
        model: classify_effect(wide[model], epsilon) for model in wide.columns
    }
    top_10_k = max(1, round(n_items * 0.10))
    bottom_10_k = max(1, round(n_items * 0.10))

    for model_a, model_b in combinations(wide.columns, 2):
        series_a = wide[model_a]
        series_b = wide[model_b]
        diff_a = values[model_a][upper_idx[0]] - values[model_a][upper_idx[1]]
        diff_b = values[model_b][upper_idx[0]] - values[model_b][upper_idx[1]]
        informative_mask = (np.abs(diff_a) > epsilon) & (np.abs(diff_b) > epsilon)

        top_a = set(series_a.nlargest(top_10_k).index)
        top_b = set(series_b.nlargest(top_10_k).index)
        bottom_a = set(series_a.nsmallest(bottom_10_k).index)
        bottom_b = set(series_b.nsmallest(bottom_10_k).index)

        rows.append(
            {
                "kind": kind,
                "model_subset": model_subset,
                "model_a": model_a,
                "model_b": model_b,
                "n_items": n_items,
                "epsilon": epsilon,
                "spearman_rank_corr": float(
                    spearmanr(series_a, series_b).statistic
                ),
                "pearson_value_corr": float(series_a.corr(series_b)),
                "sign_agreement": float(((series_a > 0) == (series_b > 0)).mean()),
                "effect_band_agreement": float(
                    (categories[model_a] == categories[model_b]).mean()
                ),
                "informative_order_agreement": float(
                    np.mean(np.sign(diff_a[informative_mask]) == np.sign(diff_b[informative_mask]))
                ),
                "informative_pair_coverage": float(informative_mask.mean()),
                "top_10_pct_jaccard": float(len(top_a & top_b) / len(top_a | top_b)),
                "bottom_10_pct_jaccard": float(
                    len(bottom_a & bottom_b) / len(bottom_a | bottom_b)
                ),
            }
        )
    return pd.DataFrame(rows)


def summarize_pairwise_metrics(pairwise_df: pd.DataFrame) -> pd.DataFrame:
    metric_cols = [
        "spearman_rank_corr",
        "pearson_value_corr",
        "sign_agreement",
        "effect_band_agreement",
        "informative_order_agreement",
        "informative_pair_coverage",
        "top_10_pct_jaccard",
        "bottom_10_pct_jaccard",
    ]
    summary = (
        pairwise_df.groupby(["kind", "model_subset"], as_index=False)[metric_cols]
        .mean()
        .sort_values(["kind", "model_subset"])
    )
    return summary


def build_matrix(pairwise_df: pd.DataFrame, metric: str, models: list[str]) -> pd.DataFrame:
    matrix = pd.DataFrame(
        np.eye(len(models)),
        index=models,
        columns=models,
    )
    for row in pairwise_df.itertuples(index=False):
        value = getattr(row, metric)
        matrix.loc[row.model_a, row.model_b] = value
        matrix.loc[row.model_b, row.model_a] = value
    return matrix


def draw_heatmap(
    ax: plt.Axes,
    matrix: pd.DataFrame,
    title: str,
    *,
    ylabel: str = "",
) -> None:
    sns.heatmap(
        matrix,
        ax=ax,
        cmap="YlGnBu",
        vmin=0,
        vmax=1,
        annot=True,
        fmt=".2f",
        cbar=False,
        square=True,
        linewidths=0.6,
        linecolor="white",
        annot_kws={"fontsize": 9},
    )
    ax.set_title(title, fontsize=11, pad=8)
    ax.set_xlabel("")
    ax.set_ylabel(ylabel, fontsize=12 if ylabel else 10)
    ax.tick_params(axis="x", rotation=45, labelsize=9)
    ax.tick_params(axis="y", rotation=0, labelsize=9)


def plot_pairwise_heatmaps(pairwise_df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(2, 3, figsize=(14, 8.6))
    plot_specs = [
        ("papers", "spearman_rank_corr", "Exact rank\n(Spearman ρ)"),
        ("papers", "informative_order_agreement", "Tie-aware order\n(ε = 0.02)"),
        ("papers", "effect_band_agreement", "Help / neutral / hurt\n(ε = 0.02)"),
        ("collections", "spearman_rank_corr", "Exact rank\n(Spearman ρ)"),
        ("collections", "informative_order_agreement", "Tie-aware order\n(ε = 0.02)"),
        ("collections", "effect_band_agreement", "Help / neutral / hurt\n(ε = 0.02)"),
    ]

    all_5 = pairwise_df.loc[pairwise_df["model_subset"] == "all_5_models"].copy()

    for ax, (kind, metric, title) in zip(axes.flatten(), plot_specs):
        subset = all_5.loc[all_5["kind"] == kind]
        matrix = build_matrix(subset, metric, MODELS)
        ylabel = "Individual papers" if kind == "papers" and ax in axes[:, 0] else ""
        if kind == "collections" and ax in axes[:, 0]:
            ylabel = "Collections"
        draw_heatmap(ax, matrix, title, ylabel=ylabel)

    fig.text(
        0.5,
        0.02,
        "Tie-aware order agreement only counts item pairs separated by more than 0.02 in both models.",
        ha="center",
        fontsize=10,
    )
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig(
        PLOTS_DIR / "cross_model_augmentation_robustness_correlation.png",
        dpi=300,
        bbox_inches="tight",
    )
    fig.savefig(
        PLOTS_DIR / "cross_model_augmentation_robustness_correlation.pdf",
        dpi=300,
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    pairwise_frames: list[pd.DataFrame] = []
    for subset_name, models in MODEL_SUBSETS.items():
        pairwise_frames.append(
            pairwise_metric_rows(
                load_paper_wide(models),
                kind="papers",
                model_subset=subset_name,
                epsilon=EPSILON,
            )
        )
        pairwise_frames.append(
            pairwise_metric_rows(
                load_collection_wide(models),
                kind="collections",
                model_subset=subset_name,
                epsilon=EPSILON,
            )
        )

    pairwise_df = pd.concat(pairwise_frames, ignore_index=True)
    summary_df = summarize_pairwise_metrics(pairwise_df)

    pairwise_df.to_csv(
        RESULTS_DIR / "cross_model_augmentation_robustness_pairwise_metrics.csv",
        index=False,
    )
    summary_df.to_csv(
        RESULTS_DIR / "cross_model_augmentation_robustness_summary.csv",
        index=False,
    )
    plot_pairwise_heatmaps(pairwise_df)


if __name__ == "__main__":
    sns.set_theme(style="white", context="talk")
    main()
