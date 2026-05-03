from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


ROOT = Path(__file__).resolve().parents[1]
PAIRWISE_CSV = ROOT / "results" / "paper" / "robustness" / "cross_model_repeat_rank_ceiling_pairwise.csv"
RELIABILITY_CSV = ROOT / "results" / "paper" / "robustness" / "cross_model_repeat_rank_ceiling_reliability.csv"
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text"

MODEL_ORDER = ["GPT-5 Mini", "GPT-5 Nano", "GPT-4.1", "GPT-4.1 Mini", "GPT-5.1"]


def build_matrix(df: pd.DataFrame, value_col: str) -> pd.DataFrame:
    matrix = pd.DataFrame(np.eye(len(MODEL_ORDER)), index=MODEL_ORDER, columns=MODEL_ORDER)
    for row in df.itertuples(index=False):
        value = float(getattr(row, value_col))
        matrix.loc[row.model_a, row.model_b] = value
        matrix.loc[row.model_b, row.model_a] = value
    return matrix


def draw_heatmap(ax: plt.Axes, matrix: pd.DataFrame, title: str, ylabel: str = "") -> None:
    sns.heatmap(
        matrix,
        ax=ax,
        cmap="YlGnBu",
        vmin=0.0,
        vmax=1.0,
        annot=True,
        fmt=".2f",
        cbar=False,
        square=True,
        linewidths=0.6,
        linecolor="white",
        annot_kws={"fontsize": 9},
    )
    ax.set_title(title, fontsize=12, pad=8)
    ax.set_xlabel("")
    ax.set_ylabel(ylabel, fontsize=12 if ylabel else 10)
    ax.tick_params(axis="x", rotation=45, labelsize=9)
    ax.tick_params(axis="y", rotation=0, labelsize=9)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    pairwise = pd.read_csv(PAIRWISE_CSV)
    reliability = pd.read_csv(RELIABILITY_CSV)

    plot_pairwise = pairwise.copy()
    plot_pairwise["normalized_spearman"] = plot_pairwise["ceiling_fraction"]

    summary = (
        plot_pairwise.groupby("kind", as_index=False)[["observed_spearman", "normalized_spearman", "repeat_rank_ceiling_avg5"]]
        .mean()
        .rename(
            columns={
                "observed_spearman": "mean_spearman_rho",
                "normalized_spearman": "mean_normalized_rho",
                "repeat_rank_ceiling_avg5": "mean_repeat_based_ceiling",
            }
        )
    )

    plot_pairwise.to_csv(RESULTS_DIR / "figure5_cross_model_rank_robustness_pairwise.csv", index=False)
    summary.to_csv(RESULTS_DIR / "figure5_cross_model_rank_robustness_summary.csv", index=False)
    reliability.to_csv(RESULTS_DIR / "figure5_cross_model_rank_robustness_reliability.csv", index=False)

    fig, axes = plt.subplots(2, 2, figsize=(10.6, 8.1))
    specs = [
        ("papers", "observed_spearman", "Spearman ρ", "Individual papers"),
        ("papers", "normalized_spearman", "Normalized ρ", ""),
        ("collections", "observed_spearman", "Spearman ρ", "Collections"),
        ("collections", "normalized_spearman", "Normalized ρ", ""),
    ]
    for ax, (kind, value_col, title, ylabel) in zip(axes.flatten(), specs):
        sub = plot_pairwise.loc[plot_pairwise["kind"] == kind]
        draw_heatmap(ax, build_matrix(sub, value_col), title, ylabel)

    fig.text(
        0.5,
        0.02,
        "Normalized ρ = observed Spearman ρ divided by the repeat-based ceiling derived from within-model repeat-to-repeat ranking agreement.",
        ha="center",
        fontsize=10,
    )
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig(PLOTS_DIR / "figure5_cross_model_rank_robustness.png", dpi=300, bbox_inches="tight")
    fig.savefig(PLOTS_DIR / "figure5_cross_model_rank_robustness.pdf", dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    sns.set_theme(style="white", context="talk")
    main()
