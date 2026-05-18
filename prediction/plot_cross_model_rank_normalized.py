from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


ROOT = Path(__file__).resolve().parents[1]
PAIRWISE_CSV = ROOT / "results" / "paper" / "robustness" / "cross_model_repeat_rank_ceiling_pairwise.csv"
PLOTS_DIR = ROOT / "plots" / "paper" / "exploratory"

MODELS = ["GPT-5 Mini", "GPT-5 Nano", "GPT-4.1", "GPT-4.1 Mini", "GPT-5.1"]


def build_matrix(df: pd.DataFrame, value_col: str) -> pd.DataFrame:
    matrix = pd.DataFrame(np.eye(len(MODELS)), index=MODELS, columns=MODELS)
    for row in df.itertuples(index=False):
        value = float(getattr(row, value_col))
        matrix.loc[row.model_a, row.model_b] = value
        matrix.loc[row.model_b, row.model_a] = value
    return matrix


def draw_heatmap(ax: plt.Axes, matrix: pd.DataFrame, title: str) -> None:
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
        annot_kws={"fontsize": 10},
    )
    ax.set_title(title, fontsize=13, pad=10)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.tick_params(axis="x", rotation=45, labelsize=10)
    ax.tick_params(axis="y", rotation=0, labelsize=10)


def main() -> None:
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    pairwise = pd.read_csv(PAIRWISE_CSV)

    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.8))
    for ax, kind, title in [
        (axes[0], "papers", "Individual papers"),
        (axes[1], "collections", "Collections"),
    ]:
        sub = pairwise.loc[pairwise["kind"] == kind].copy()
        draw_heatmap(ax, build_matrix(sub, "ceiling_fraction"), title)

    fig.text(
        0.5,
        0.02,
        "Values are exact rank correlations normalized by the repeat-based ceiling: observed Spearman / repeat-noise ceiling.",
        ha="center",
        fontsize=10,
    )
    fig.tight_layout(rect=[0, 0.06, 1, 1])
    fig.savefig(PLOTS_DIR / "cross_model_rank_normalized.png", dpi=300, bbox_inches="tight")
    fig.savefig(PLOTS_DIR / "cross_model_rank_normalized.pdf", dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    sns.set_theme(style="white", context="talk")
    main()
