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

from analyze_validation_incremental_pgg_science_repeat30 import (
    CONDITION_COLORS,
    PLOTS_DIR,
    RESULTS_DIR,
    load_noise_ceiling,
)


EXACT_SUMMARY_CSV = RESULTS_DIR / "incremental_pgg_science_k5_exact_summary.csv"
BOOTSTRAP_SUMMARY_CSV = RESULTS_DIR / "incremental_pgg_science_k5_bootstrap_summary.csv"
FIGURE_CONDITION_ORDER = ["baseline", "science_gpt41"]
FIGURE_CONDITION_LABELS = {
    "baseline": "No augmentation",
    "science_gpt41": "Benchmark paper",
}


def load_plot_rows(summary_csv: Path, *, expected_distribution: str) -> pd.DataFrame:
    df = pd.read_csv(summary_csv)
    df = df.loc[df["distribution"] == expected_distribution].copy()
    df = df.loc[df["condition"].isin(FIGURE_CONDITION_ORDER)].copy()

    baseline_order = (
        df.loc[df["condition"] == "baseline", ["model", "mean"]]
        .sort_values("mean", ascending=False)["model"]
        .tolist()
    )
    df["model"] = pd.Categorical(df["model"], categories=baseline_order, ordered=True)
    df["condition"] = pd.Categorical(
        df["condition"], categories=FIGURE_CONDITION_ORDER, ordered=True
    )
    df = df.sort_values(["model", "condition"]).reset_index(drop=True)

    return df.rename(
        columns={
            "mean": "correlation",
            "p05": "ci_low",
            "p95": "ci_high",
        }
    )[
        [
            "model",
            "condition",
            "subset_k",
            "correlation",
            "ci_low",
            "ci_high",
            "sd",
            "single_run_corr_mean",
            "single_run_corr_sd",
            "count",
        ]
    ]


def plot_figure2_style(plot_df: pd.DataFrame, *, ceiling: float, output_stem: str, caption: str) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(12.0, 7.9))
    model_order = plot_df["model"].cat.categories.tolist()
    y_positions = np.arange(len(model_order))
    offsets = {"baseline": -0.16, "science_gpt41": 0.16}

    ax.axvline(ceiling, color="#0f766e", linestyle="--", linewidth=1.4, zorder=1)

    for condition in FIGURE_CONDITION_ORDER:
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
            height=0.28,
            zorder=2,
            label=FIGURE_CONDITION_LABELS[condition],
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

    ax.set_xlim(0.0, 1.0)
    ax.set_xticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel("Correlation with true treatment outcome")
    ax.set_yticks(y_positions, model_order)
    ax.invert_yaxis()
    ax.grid(False)

    legend_items = [
        Line2D(
            [0],
            [0],
            color=CONDITION_COLORS["baseline"],
            linewidth=8,
            label=FIGURE_CONDITION_LABELS["baseline"],
        ),
        Line2D(
            [0],
            [0],
            color=CONDITION_COLORS["science_gpt41"],
            linewidth=8,
            label=FIGURE_CONDITION_LABELS["science_gpt41"],
        ),
        Line2D([0], [0], color="#0f766e", linestyle="--", linewidth=1.4, label="Estimated ceiling"),
    ]
    ax.legend(
        handles=legend_items,
        frameon=False,
        loc="upper left",
        bbox_to_anchor=(0.0, -0.18),
        ncol=2,
        columnspacing=1.2,
        handlelength=2.4,
        borderaxespad=0.0,
    )

    fig.text(
        0.99,
        0.02,
        caption,
        ha="right",
        va="bottom",
        fontsize=9.4,
        color="#4b5563",
    )
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(PLOTS_DIR / f"{output_stem}.png", dpi=240, bbox_inches="tight")
    fig.savefig(PLOTS_DIR / f"{output_stem}.pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    exact_plot_rows = load_plot_rows(
        EXACT_SUMMARY_CSV,
        expected_distribution="exact_without_replacement",
    )
    exact_plot_rows.to_csv(
        RESULTS_DIR / "incremental_pgg_science_k5_exact_figure2_style_plot_rows.csv",
        index=False,
    )
    plot_figure2_style(
        exact_plot_rows,
        ceiling=load_noise_ceiling(),
        output_stem="incremental_pgg_science_k5_exact_figure2_style",
        caption="Bars show the mean correlation over all exact 5-of-30 subensembles; whiskers show the 5th-95th percentile.",
    )

    bootstrap_plot_rows = load_plot_rows(
        BOOTSTRAP_SUMMARY_CSV,
        expected_distribution="bootstrap_with_replacement",
    )
    bootstrap_plot_rows.to_csv(
        RESULTS_DIR / "incremental_pgg_science_k5_bootstrap_figure2_style_plot_rows.csv",
        index=False,
    )
    plot_figure2_style(
        bootstrap_plot_rows,
        ceiling=load_noise_ceiling(),
        output_stem="incremental_pgg_science_k5_bootstrap_figure2_style",
        caption="Bars show the mean correlation over 50,000 bootstrap 5-run ensembles with replacement; whiskers show the 5th-95th percentile.",
    )


if __name__ == "__main__":
    main()
