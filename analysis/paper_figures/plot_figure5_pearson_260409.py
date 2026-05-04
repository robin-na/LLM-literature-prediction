from __future__ import annotations

import os
from itertools import combinations
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2] / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"

PAPER_METRICS_CSV = RESULTS_DIR / "paper_repeat_correlation_metrics.csv"
COLLECTION_METRICS_CSV = RESULTS_DIR / "collection_repeat_correlation_metrics.csv"

FIGURE5_MODEL_ORDER = ["GPT-5.1", "GPT-4.1 Mini", "GPT-4.1", "GPT-5 Nano", "GPT-5 Mini", "Claude Sonnet 4.6", "Gemini 2.5 Pro"]


def build_pairwise_rows(metric_df: pd.DataFrame, *, kind: str, item_id_col: str) -> pd.DataFrame:
    wide = (
        metric_df.pivot(index=item_id_col, columns="model", values="correlation")
        .dropna()
        .reindex(columns=FIGURE5_MODEL_ORDER)
    )

    rows: list[dict[str, float | str | int]] = []
    for model_a, model_b in combinations(FIGURE5_MODEL_ORDER, 2):
        scores_a = wide[model_a].to_numpy(dtype=float)
        scores_b = wide[model_b].to_numpy(dtype=float)
        rows.append(
            {
                "kind": kind,
                "model_a": model_a,
                "model_b": model_b,
                "n_items": int(len(wide)),
                "pearson_r": float(np.corrcoef(scores_a, scores_b)[0, 1]),
                "spearman_rho": float(pd.Series(scores_a).corr(pd.Series(scores_b), method="spearman")),
            }
        )
    return pd.DataFrame(rows)


def build_matrix(df: pd.DataFrame, value_col: str) -> pd.DataFrame:
    matrix = pd.DataFrame(np.eye(len(FIGURE5_MODEL_ORDER)), index=FIGURE5_MODEL_ORDER, columns=FIGURE5_MODEL_ORDER)
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
    sns.set_theme(style="white", context="talk")
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    pairwise = pd.concat(
        [
            build_pairwise_rows(pd.read_csv(PAPER_METRICS_CSV), kind="papers", item_id_col="source_id"),
            build_pairwise_rows(pd.read_csv(COLLECTION_METRICS_CSV), kind="collections", item_id_col="variant_id"),
        ],
        ignore_index=True,
    )
    summary = (
        pairwise.groupby("kind", as_index=False)[["pearson_r", "spearman_rho"]]
        .mean()
        .rename(columns={"pearson_r": "mean_pearson_r", "spearman_rho": "mean_spearman_rho"})
    )

    pairwise.to_csv(RESULTS_DIR / "figure5_cross_model_rank_robustness_pearson_pairwise.csv", index=False)
    summary.to_csv(RESULTS_DIR / "figure5_cross_model_rank_robustness_pearson_summary.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.0))
    specs = [
        ("papers", "Individual papers"),
        ("collections", "Collections"),
    ]
    for ax, (kind, ylabel) in zip(axes, specs):
        sub = pairwise.loc[pairwise["kind"] == kind]
        draw_heatmap(ax, build_matrix(sub, "pearson_r"), "Pearson r", ylabel)

    fig.text(
        0.5,
        0.02,
        "Pearson is computed on the item-level correlation vectors over pairwise shared items for each model pair.",
        ha="center",
        fontsize=10,
    )
    fig.tight_layout(rect=[0, 0.06, 1, 1])
    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure5_cross_model_rank_robustness_pearson.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
