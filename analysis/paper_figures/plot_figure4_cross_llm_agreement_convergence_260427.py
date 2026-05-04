from __future__ import annotations

import os
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats


SOURCE_ROWS_CSV = ROOT / "results" / "paper" / "main_text_figures_260427" / "figure3_paper_heterogeneity_agreement_rows.csv"
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260427" / "exploratory"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260427" / "exploratory"

OUT_STEM = "figure4_cross_llm_agreement_convergence"
FIG_PNG = PLOTS_DIR / f"{OUT_STEM}.png"
PAPER_ROWS_CSV = RESULTS_DIR / f"{OUT_STEM}_paper_rows.csv"
PAIRWISE_CSV = RESULTS_DIR / f"{OUT_STEM}_pairwise.csv"
SUMMARY_CSV = RESULTS_DIR / f"{OUT_STEM}_summary.csv"
DOC_MD = RESULTS_DIR / f"{OUT_STEM}_documentation.md"

MODEL_ORDER = ["Claude Sonnet 4.6", "GPT-4.1", "Gemini 2.5 Pro"]
POINT_COLORS = {"reduce": "#2f9e44", "increase": "#c64b41"}
SHADE_COLORS = {"reduce": "#e7f1e5", "increase": "#f4e0dd"}


def load_wide_rows() -> tuple[pd.DataFrame, pd.Series]:
    rows = pd.read_csv(SOURCE_ROWS_CSV)
    rows = rows.loc[rows["model"].isin(MODEL_ORDER)].copy()
    wide = rows.pivot_table(index="item_id", columns="model", values="correlation", aggfunc="mean").reindex(columns=MODEL_ORDER)
    baselines = rows.groupby("model")["baseline_correlation_mean30"].first().reindex(MODEL_ORDER)
    return wide, baselines


def build_pairwise(shared: pd.DataFrame) -> pd.DataFrame:
    out_rows: list[dict[str, object]] = []
    for model_a, model_b in combinations(MODEL_ORDER, 2):
        pair = shared[[model_a, model_b]].dropna()
        pearson_r, pearson_p = stats.pearsonr(pair[model_a].to_numpy(), pair[model_b].to_numpy())
        out_rows.append(
            {
                "model_a": model_a,
                "model_b": model_b,
                "n_shared_papers": int(pair.shape[0]),
                "pearson_r": float(pearson_r),
                "pearson_p_two_sided": float(pearson_p),
            }
        )
    return pd.DataFrame(out_rows)


def build_convergence_rows(shared: pd.DataFrame, baselines: pd.Series) -> tuple[pd.DataFrame, pd.DataFrame]:
    pairs = list(combinations(MODEL_ORDER, 2))
    baseline_gap = float(np.mean([abs(float(baselines[a]) - float(baselines[b])) for a, b in pairs]))
    baseline_sd = float(np.std(baselines.to_numpy(dtype=float), ddof=1))
    baseline_range = float(baselines.max() - baselines.min())

    out_rows: list[dict[str, object]] = []
    for item_id, row in shared.iterrows():
        pairwise_gaps = [abs(float(row[a]) - float(row[b])) for a, b in pairs]
        mean_pairwise_gap = float(np.mean(pairwise_gaps))
        out_rows.append(
            {
                "item_id": item_id,
                "claude_sonnet_46_corr": float(row["Claude Sonnet 4.6"]),
                "gpt41_corr": float(row["GPT-4.1"]),
                "gemini25pro_corr": float(row["Gemini 2.5 Pro"]),
                "mean_pairwise_abs_gap": mean_pairwise_gap,
                "cross_model_sd": float(np.std(row.to_numpy(dtype=float), ddof=1)),
                "cross_model_range": float(row.max() - row.min()),
                "reduces_gap_vs_unaugmented": bool(mean_pairwise_gap < baseline_gap),
            }
        )
    convergence = pd.DataFrame(out_rows).sort_values("mean_pairwise_abs_gap").reset_index(drop=True)
    convergence["paper_percentile"] = np.linspace(0.0, 100.0, num=convergence.shape[0], endpoint=True)

    summary = pd.DataFrame(
        [
            {
                "n_shared_papers": int(convergence.shape[0]),
                "baseline_mean_pairwise_abs_gap": baseline_gap,
                "baseline_cross_model_sd": baseline_sd,
                "baseline_cross_model_range": baseline_range,
                "n_reduce_gap": int(convergence["reduces_gap_vs_unaugmented"].sum()),
                "share_reduce_gap": float(convergence["reduces_gap_vs_unaugmented"].mean()),
                "n_increase_gap": int((~convergence["reduces_gap_vs_unaugmented"]).sum()),
                "share_increase_gap": float((~convergence["reduces_gap_vs_unaugmented"]).mean()),
                "mean_augmented_mean_pairwise_abs_gap": float(convergence["mean_pairwise_abs_gap"].mean()),
                "median_augmented_mean_pairwise_abs_gap": float(convergence["mean_pairwise_abs_gap"].median()),
                "p05_augmented_mean_pairwise_abs_gap": float(convergence["mean_pairwise_abs_gap"].quantile(0.05)),
                "p95_augmented_mean_pairwise_abs_gap": float(convergence["mean_pairwise_abs_gap"].quantile(0.95)),
            }
        ]
    )
    return convergence, summary


def build_heatmap_matrix(pairwise: pd.DataFrame) -> pd.DataFrame:
    matrix = pd.DataFrame(np.eye(len(MODEL_ORDER)), index=MODEL_ORDER, columns=MODEL_ORDER)
    for row in pairwise.itertuples(index=False):
        matrix.loc[row.model_a, row.model_b] = float(row.pearson_r)
        matrix.loc[row.model_b, row.model_a] = float(row.pearson_r)
    return matrix


def write_documentation(pairwise: pd.DataFrame, convergence: pd.DataFrame, summary: pd.DataFrame) -> None:
    pairwise_display = pairwise.copy()
    for col in ["pearson_r", "pearson_p_two_sided"]:
        pairwise_display[col] = pairwise_display[col].map(lambda x: f"{float(x):.6f}")

    summary_display = summary.copy()
    for col in summary_display.columns:
        if col.startswith("n_"):
            continue
        summary_display[col] = summary_display[col].map(lambda x: f"{float(x):.6f}")

    doc = f"""# {OUT_STEM}

## Purpose
Exploratory two-panel candidate for a possible `main_text_260427` Figure 4 focused on cross-LLM agreement across individual papers. This variant does not replace the current canonical Figure 4 mapping in `figure_manifest.csv`.

## Output files
- Plot PNG: `{FIG_PNG.relative_to(ROOT)}`
- Paper-level convergence rows: `{PAPER_ROWS_CSV.relative_to(ROOT)}`
- Pairwise agreement table: `{PAIRWISE_CSV.relative_to(ROOT)}`
- Summary table: `{SUMMARY_CSV.relative_to(ROOT)}`
- Documentation: `{DOC_MD.relative_to(ROOT)}`
- Script: `{Path(__file__).resolve().relative_to(ROOT)}`

## Input files
- Canonical Figure 3 rows: `{SOURCE_ROWS_CSV.relative_to(ROOT)}`

## Construction
1. Start from the canonical `260427` Figure 3 paper-level rows for the three main-text models.
2. Restrict to papers shared by all three models, yielding 2,010 papers.
3. Panel A computes pairwise Pearson correlations between the three model-specific paper-level augmented performance vectors.
4. Panel B computes, for each shared paper, the mean pairwise absolute gap in augmented correlation across the three models.
5. The Panel B reference line is the corresponding mean pairwise absolute gap across the three unaugmented model baselines.
6. Papers below that line are labeled as reducing cross-model performance gaps; papers above it are labeled as increasing them.

## Estimands
- Panel A: `corr(paper-level augmented correlation vector for model a, paper-level augmented correlation vector for model b)` across shared papers.
- Panel B: `mean(|r_a - r_b|, |r_a - r_c|, |r_b - r_c|)` across the three displayed LLMs for a given paper.

## Summary values
{summary_display.to_markdown(index=False)}

## Pairwise agreement values
{pairwise_display.to_markdown(index=False)}
"""
    DOC_MD.write_text(doc)


def draw_panel_a(ax: plt.Axes, pairwise: pd.DataFrame) -> None:
    matrix = build_heatmap_matrix(pairwise)
    cmap = sns.light_palette("#2f9e44", as_cmap=True)
    sns.heatmap(
        matrix,
        ax=ax,
        cmap=cmap,
        vmin=0.0,
        vmax=1.0,
        cbar=False,
        square=True,
        linewidths=1.1,
        linecolor="white",
        annot=True,
        fmt=".2f",
        annot_kws={"fontsize": 8.2, "color": "#111827"},
    )
    ax.set_title("Agreement across papers", fontsize=11.1, color="#111827", pad=10)
    ax.tick_params(axis="x", labelrotation=24, labelsize=7.4, colors="#374151")
    ax.tick_params(axis="y", labelrotation=0, labelsize=7.4, colors="#374151")
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.text(-0.14, 1.02, "A", transform=ax.transAxes, ha="left", va="bottom", fontsize=11.6, fontweight="bold", color="#111827")
    ax.text(0.5, -0.18, "Pearson r across 2,010 shared papers", transform=ax.transAxes, ha="center", va="top", fontsize=7.0, color="#4b5563")


def draw_panel_b(ax: plt.Axes, convergence: pd.DataFrame, summary: pd.DataFrame) -> None:
    baseline_gap = float(summary["baseline_mean_pairwise_abs_gap"].iloc[0])
    n_reduce = int(summary["n_reduce_gap"].iloc[0])
    n_increase = int(summary["n_increase_gap"].iloc[0])
    share_reduce = float(summary["share_reduce_gap"].iloc[0])
    share_increase = float(summary["share_increase_gap"].iloc[0])

    x = convergence["paper_percentile"].to_numpy(dtype=float)
    y = convergence["mean_pairwise_abs_gap"].to_numpy(dtype=float)
    reduce_mask = convergence["reduces_gap_vs_unaugmented"].to_numpy(dtype=bool)

    y_max = max(float(np.nanmax(y)) * 1.08, baseline_gap * 1.18)
    ax.axhspan(0.0, baseline_gap, color=SHADE_COLORS["reduce"], zorder=0)
    ax.axhspan(baseline_gap, y_max, color=SHADE_COLORS["increase"], zorder=0)
    ax.scatter(x[reduce_mask], y[reduce_mask], s=10, color=POINT_COLORS["reduce"], alpha=0.8, linewidths=0.0, rasterized=True, zorder=3)
    ax.scatter(x[~reduce_mask], y[~reduce_mask], s=10, color=POINT_COLORS["increase"], alpha=0.8, linewidths=0.0, rasterized=True, zorder=3)
    ax.axhline(baseline_gap, color="#111111", linewidth=1.2, zorder=4)

    ax.set_title("Most papers narrow performance gaps", fontsize=11.1, color="#111827", pad=10)
    ax.text(
        0.04,
        0.91,
        f"{100.0 * share_increase:.0f}% (n={n_increase:,}) of papers increase\nthe mean pairwise gap across LLMs",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=7.1,
        color="#111827",
    )
    ax.text(
        0.04,
        0.12,
        f"{100.0 * share_reduce:.0f}% (n={n_reduce:,}) of papers reduce\nthe mean pairwise gap across LLMs",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=7.1,
        color="#111827",
    )
    ax.text(
        0.02,
        baseline_gap + 0.006,
        "Unaugmented mean pairwise gap",
        transform=ax.get_yaxis_transform(),
        ha="left",
        va="bottom",
        fontsize=7.0,
        color="#111111",
    )

    ax.set_xlim(0.0, 100.0)
    ax.set_ylim(0.0, y_max)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xlabel("Paper percentile", fontsize=8.6, color="#111827", labelpad=4)
    ax.set_ylabel(r"Mean pairwise gap across LLMs ($|\Delta r|$)", fontsize=8.6, color="#111827", labelpad=5)
    ax.tick_params(axis="both", labelsize=7.6, colors="#374151", length=3.0, width=0.8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#111827")
    ax.spines["bottom"].set_color("#111827")
    ax.spines["left"].set_linewidth(1.0)
    ax.spines["bottom"].set_linewidth(1.0)
    ax.text(-0.14, 1.02, "B", transform=ax.transAxes, ha="left", va="bottom", fontsize=11.6, fontweight="bold", color="#111827")


def draw_figure(pairwise: pd.DataFrame, convergence: pd.DataFrame, summary: pd.DataFrame) -> None:
    sns.set_theme(style="white", context="paper")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig = plt.figure(figsize=(8.6, 3.45))
    gs = fig.add_gridspec(1, 2, width_ratios=[0.95, 1.65], wspace=0.3)
    ax_a = fig.add_subplot(gs[0, 0])
    ax_b = fig.add_subplot(gs[0, 1])

    draw_panel_a(ax_a, pairwise)
    draw_panel_b(ax_b, convergence, summary)

    fig.subplots_adjust(left=0.08, right=0.985, top=0.86, bottom=0.18)
    fig.savefig(FIG_PNG, dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    wide, baselines = load_wide_rows()
    shared = wide.dropna().copy()
    pairwise = build_pairwise(shared)
    convergence, summary = build_convergence_rows(shared, baselines)

    pairwise.to_csv(PAIRWISE_CSV, index=False)
    convergence.to_csv(PAPER_ROWS_CSV, index=False)
    summary.to_csv(SUMMARY_CSV, index=False)
    write_documentation(pairwise, convergence, summary)
    draw_figure(pairwise, convergence, summary)


if __name__ == "__main__":
    main()
