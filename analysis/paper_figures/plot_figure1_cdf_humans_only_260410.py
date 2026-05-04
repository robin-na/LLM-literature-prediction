from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2] / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D


ROOT = Path(__file__).resolve().parents[2]
ANALYSIS_ROOT = ROOT / "analysis"
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from paper_figures.plot_figure1_cdf_llm_mean30_260410 import load_human_plot_rows, load_truth_vectors


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"

OUT_PNG = PLOTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_humans_only.png"
OUT_PDF = PLOTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_humans_only.pdf"
ROWS_CSV = RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_humans_only_rows.csv"
REFERENCE_CSV = RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_humans_only_reference.csv"
PERCENTILES_CSV = RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_humans_only_percentiles.csv"

GROUP_ORDER = ["Laypeople", "Experts"]
GROUP_COLORS = {
    "Laypeople": "#caa27e",
    "Experts": "#8d6748",
}


def build_percentile_rows(plot_df: pd.DataFrame, null_value: float, ceiling_value: float) -> pd.DataFrame:
    percentile_rows: list[dict[str, object]] = []
    for label, value, kind in [
        ("No treatment effect", float(null_value), "null_baseline"),
        ("Estimated ceiling", float(ceiling_value), "noise_ceiling"),
    ]:
        row: dict[str, object] = {"label": label, "value": value, "kind": kind}
        for group in GROUP_ORDER:
            vals = plot_df.loc[plot_df["group"] == group, "value"].to_numpy(dtype=float)
            row[f"share_{group.lower()}_below"] = float(np.mean(vals <= value))
        percentile_rows.append(row)

    out = pd.DataFrame(percentile_rows)
    out["pct_laypeople_below"] = out["share_laypeople_below"] * 100.0
    out["pct_experts_below"] = out["share_experts_below"] * 100.0
    return out.sort_values("value").reset_index(drop=True)


def plot_cdf(plot_df: pd.DataFrame, null_value: float, ceiling_value: float) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(8.2, 6.6), layout="constrained")
    counts = {
        group: int(plot_df.loc[plot_df["group"] == group].shape[0])
        for group in GROUP_ORDER
    }

    for group in GROUP_ORDER:
        vals = plot_df.loc[plot_df["group"] == group, "value"].to_numpy(dtype=float)
        sns.ecdfplot(
            x=vals,
            stat="proportion",
            linewidth=2.5,
            color=GROUP_COLORS[group],
            label=group,
            ax=ax,
        )

    ax.axvline(null_value, color="#111111", linewidth=1.8, linestyle="-", alpha=0.95, zorder=2)
    ax.axvline(ceiling_value, color="#111111", linewidth=1.6, linestyle=":", alpha=0.95, zorder=2)

    ax.set_xlim(-0.7, 0.86)
    ax.set_ylim(0.0, 1.02)
    ax.set_xticks(np.arange(-0.7, 0.81, 0.1))
    ax.set_yticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel("Correlation with true treatment outcome")
    ax.set_ylabel("Cumulative share of forecasters")
    ax.grid(axis="y", color="#dddddd", linewidth=0.8)
    ax.grid(axis="x", visible=False)

    legend_items = [
        Line2D([0], [0], color=GROUP_COLORS["Laypeople"], linewidth=2.5, label=f"Laypeople (n={counts['Laypeople']})"),
        Line2D([0], [0], color=GROUP_COLORS["Experts"], linewidth=2.5, label=f"Experts (n={counts['Experts']})"),
        Line2D([0], [0], color="#111111", linewidth=1.8, linestyle="-", label="No-treatment-effect baseline"),
        Line2D([0], [0], color="#111111", linewidth=1.6, linestyle=":", label="Estimated ceiling"),
    ]
    ax.legend(handles=legend_items, frameon=False, loc="upper left")

    fig.savefig(OUT_PNG, dpi=300, bbox_inches="tight")
    fig.savefig(OUT_PDF, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    truth_vec, null_value, ceiling_value = load_truth_vectors()
    plot_df = load_human_plot_rows(truth_vec)
    plot_df = plot_df.loc[plot_df["group"].isin(GROUP_ORDER)].copy()
    plot_df["group"] = pd.Categorical(plot_df["group"], categories=GROUP_ORDER, ordered=True)
    plot_df = plot_df.sort_values(["group", "value"]).reset_index(drop=True)

    reference_df = pd.DataFrame(
        [
            {"label": "No treatment effect", "value": float(null_value), "kind": "null_baseline"},
            {"label": "Estimated ceiling", "value": float(ceiling_value), "kind": "noise_ceiling"},
        ]
    )
    percentile_df = build_percentile_rows(plot_df, null_value, ceiling_value)

    plot_df.to_csv(ROWS_CSV, index=False)
    reference_df.to_csv(REFERENCE_CSV, index=False)
    percentile_df.to_csv(PERCENTILES_CSV, index=False)
    plot_cdf(plot_df, null_value, ceiling_value)


if __name__ == "__main__":
    main()
