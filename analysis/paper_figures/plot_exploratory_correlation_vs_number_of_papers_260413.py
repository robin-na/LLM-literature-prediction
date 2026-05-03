from __future__ import annotations

import math
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ANALYSIS_ROOT = ROOT / "analysis"
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from paper_figures.plot_collection_linear_metadata_effect_260409 import build_collection_df
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"

PAPER_METRICS_CSV = RESULTS_DIR / "paper_repeat_correlation_metrics.csv"
COLLECTION_METRICS_CSV = RESULTS_DIR / "collection_repeat_correlation_metrics.csv"

RAW_CSV = RESULTS_DIR / "exploratory_correlation_vs_number_of_papers_selected4_raw.csv"
BINNED_CSV = RESULTS_DIR / "exploratory_correlation_vs_number_of_papers_selected4_binned.csv"
FIGURE_PNG = PLOTS_DIR / "exploratory_correlation_vs_number_of_papers_selected4.png"
FIGURE_PDF = PLOTS_DIR / "exploratory_correlation_vs_number_of_papers_selected4.pdf"

MODELS = ["Claude Sonnet 4.6", "GPT-5.1", "GPT-4.1", "Gemini 2.5 Pro"]
MODEL_COLORS = {
    "Claude Sonnet 4.6": "#9c755f",
    "GPT-5.1": "#d95f02",
    "GPT-4.1": "#2b8cbe",
    "Gemini 2.5 Pro": "#17becf",
}


def load_raw_rows() -> pd.DataFrame:
    paper = pd.read_csv(PAPER_METRICS_CSV)
    paper = paper.loc[paper["model"].isin(MODELS), ["model", "source_id", "correlation"]].copy()
    paper["item_id"] = paper["source_id"].astype(str)
    paper["item_type"] = "Individual paper"
    paper["n_papers"] = 1
    paper = paper.drop(columns=["source_id"])

    collection_metrics = pd.read_csv(COLLECTION_METRICS_CSV)
    collection_meta = build_collection_df().loc[:, ["model", "variant_id", "count"]].drop_duplicates()
    collection = collection_metrics.merge(
        collection_meta,
        on=["model", "variant_id"],
        how="inner",
        validate="one_to_one",
    )
    collection = collection.loc[
        collection["model"].isin(MODELS), ["model", "variant_id", "correlation", "count"]
    ].copy()
    collection["item_id"] = collection["variant_id"].astype(str)
    collection["item_type"] = "Collection"
    collection["n_papers"] = pd.to_numeric(collection["count"], errors="coerce")
    collection = collection.loc[collection["n_papers"].notna()].copy()
    collection["n_papers"] = collection["n_papers"].round().astype(int)
    collection = collection.drop(columns=["variant_id", "count"])

    raw = pd.concat([paper, collection], ignore_index=True, sort=False)
    raw = raw.loc[raw["n_papers"].notna() & raw["correlation"].notna()].copy()
    raw["n_papers"] = raw["n_papers"].astype(int)
    raw = raw.sort_values(["model", "n_papers", "item_type", "item_id"]).reset_index(drop=True)
    return raw


def build_binned_summary(raw: pd.DataFrame) -> pd.DataFrame:
    edges = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048], dtype=float)

    rows: list[dict[str, object]] = []
    for model in MODELS:
        part = raw.loc[raw["model"] == model].copy()
        if part.empty:
            continue

        single = part.loc[part["n_papers"] == 1, "correlation"].to_numpy(dtype=float)
        if single.size:
            rows.append(
                {
                    "model": model,
                    "bin_label": "1",
                    "bin_left": 1.0,
                    "bin_right": 1.0,
                    "bin_center": 1.0,
                    "n_obs": int(single.size),
                    "mean_correlation": float(np.mean(single)),
                    "median_correlation": float(np.median(single)),
                    "q10_correlation": float(np.quantile(single, 0.10)),
                    "q90_correlation": float(np.quantile(single, 0.90)),
                }
            )

        multi = part.loc[part["n_papers"] > 1].copy()
        for left, right in zip(edges[1:-2], edges[2:-1]):
            mask = (multi["n_papers"] >= int(left)) & (multi["n_papers"] < int(right))
            vals = multi.loc[mask, "correlation"].to_numpy(dtype=float)
            if vals.size == 0:
                continue
            rows.append(
                {
                    "model": model,
                    "bin_label": f"{int(left)}-{int(right) - 1}",
                    "bin_left": float(left),
                    "bin_right": float(right),
                    "bin_center": float(math.sqrt(left * right)),
                    "n_obs": int(vals.size),
                    "mean_correlation": float(np.mean(vals)),
                    "median_correlation": float(np.median(vals)),
                    "q10_correlation": float(np.quantile(vals, 0.10)),
                    "q90_correlation": float(np.quantile(vals, 0.90)),
                }
            )

        tail = multi.loc[multi["n_papers"] >= int(edges[-2]), "correlation"].to_numpy(dtype=float)
        if tail.size:
            rows.append(
                {
                    "model": model,
                    "bin_label": f"{int(edges[-2])}+",
                    "bin_left": float(edges[-2]),
                    "bin_right": float(edges[-1]),
                    "bin_center": float(math.sqrt(edges[-2] * edges[-1])),
                    "n_obs": int(tail.size),
                    "mean_correlation": float(np.mean(tail)),
                    "median_correlation": float(np.median(tail)),
                    "q10_correlation": float(np.quantile(tail, 0.10)),
                    "q90_correlation": float(np.quantile(tail, 0.90)),
                }
            )

    return pd.DataFrame(rows)


def draw_figure(raw: pd.DataFrame, binned: pd.DataFrame) -> None:
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(2, 2, figsize=(10.8, 8.2), sharex=True, sharey=True)
    axes = axes.ravel()

    y_min = max(0.0, raw["correlation"].quantile(0.005) - 0.03)
    y_max = min(0.90, raw["correlation"].quantile(0.995) + 0.03)

    for ax, model in zip(axes, MODELS):
        color = MODEL_COLORS[model]
        part = raw.loc[raw["model"] == model].copy()
        trend = binned.loc[binned["model"] == model].sort_values("bin_center").copy()

        ax.scatter(
            part["n_papers"],
            part["correlation"],
            s=13,
            color=color,
            alpha=0.10,
            linewidths=0,
            rasterized=True,
        )
        ax.plot(
            trend["bin_center"],
            trend["mean_correlation"],
            color=color,
            lw=2.2,
            marker="o",
            ms=4.2,
            zorder=3,
        )
        ax.fill_between(
            trend["bin_center"],
            trend["q10_correlation"],
            trend["q90_correlation"],
            color=color,
            alpha=0.12,
            zorder=2,
        )

        ax.set_xscale("log")
        ax.set_title(model, color="#222222", fontsize=13, pad=8)
        ax.grid(axis="y", color="#e6e6e6", lw=0.8)
        ax.grid(axis="x", color="#f0f0f0", lw=0.6, which="major")
        ax.set_axisbelow(True)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("#cfcfcf")
        ax.spines["bottom"].set_color("#cfcfcf")
        ax.set_ylim(y_min, y_max)
        ax.set_xlim(0.9, 1600)
        ax.text(
            0.98,
            0.04,
            "Points: raw observations\nLine: log-binned mean",
            transform=ax.transAxes,
            ha="right",
            va="bottom",
            fontsize=9.2,
            color="#555555",
            bbox={"facecolor": "white", "alpha": 0.75, "edgecolor": "none", "pad": 2.5},
        )

    tick_values = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    for ax in axes:
        ax.set_xticks(tick_values)
        ax.set_xticklabels([str(v) for v in tick_values])

    axes[0].set_ylabel("Correlation performance")
    axes[2].set_ylabel("Correlation performance")
    axes[2].set_xlabel("Number of papers in report")
    axes[3].set_xlabel("Number of papers in report")

    fig.suptitle(
        "Correlation performance vs. report size",
        fontsize=15,
        y=0.98,
    )
    fig.text(
        0.5,
        0.935,
        "n=1 corresponds to the individual-paper augmentations; larger n are collection augmentations",
        ha="center",
        va="center",
        fontsize=10.2,
        color="#555555",
    )
    fig.subplots_adjust(top=0.87, left=0.10, right=0.985, bottom=0.10, wspace=0.14, hspace=0.23)
    fig.savefig(FIGURE_PNG, dpi=300)
    fig.savefig(FIGURE_PDF)
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    raw = load_raw_rows()
    binned = build_binned_summary(raw)
    raw.to_csv(RAW_CSV, index=False)
    binned.to_csv(BINNED_CSV, index=False)
    draw_figure(raw, binned)


if __name__ == "__main__":
    main()
