from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260427" / "exploratory"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260427" / "exploratory"
SOURCE_RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"

PAPER_METRICS_CSV = SOURCE_RESULTS_DIR / "paper_repeat_correlation_metrics.csv"
BASELINE30_CSV = SOURCE_RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_llm_mean30_model_summary.csv"
NO_AUG_BENCHMARKS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "no_augmentation_model_comparison"
    / "validation_no_augmentation_model_comparison_benchmarks.csv"
)

OUT_STEM = "figure3_paper_heterogeneity_agreement_cdf"
FIG_PNG = PLOTS_DIR / f"{OUT_STEM}.png"
ROWS_CSV = RESULTS_DIR / f"{OUT_STEM}_rows.csv"
SUMMARY_CSV = RESULTS_DIR / f"{OUT_STEM}_summary.csv"
PAIRWISE_CSV = RESULTS_DIR / f"{OUT_STEM}_pairwise.csv"
DOC_MD = RESULTS_DIR / f"{OUT_STEM}_documentation.md"

MODEL_ORDER = ["Claude Sonnet 4.6", "GPT-4.1", "Gemini 2.5 Pro"]
MODEL_COLORS = {
    "Claude Sonnet 4.6": "#9c755f",
    "GPT-4.1": "#2b8cbe",
    "Gemini 2.5 Pro": "#17becf",
}
HEATMAP_LABELS = {
    "Claude Sonnet 4.6": "Claude\nSonnet 4.6",
    "GPT-4.1": "GPT-4.1",
    "Gemini 2.5 Pro": "Gemini\n2.5 Pro",
}


def load_noise_ceiling() -> float:
    benchmarks = pd.read_csv(NO_AUG_BENCHMARKS_CSV)
    return float(benchmarks.loc[benchmarks["benchmark"] == "Noise ceiling", "correlation"].iloc[0])


def load_baseline30() -> dict[str, float]:
    df = pd.read_csv(BASELINE30_CSV)
    df = df.loc[df["model"].isin(MODEL_ORDER), ["model", "correlation_mean_prediction"]].copy()
    return {str(row["model"]): float(row["correlation_mean_prediction"]) for _, row in df.iterrows()}


def build_rows() -> pd.DataFrame:
    baseline_map = load_baseline30()
    rows = pd.read_csv(PAPER_METRICS_CSV)
    rows = rows.loc[
        rows["model"].isin(MODEL_ORDER),
        ["model", "source_id", "n_aug_runs", "correlation", "delta_correlation"],
    ].copy()
    rows = rows.rename(columns={"source_id": "item_id"})
    rows["baseline_correlation_mean30"] = rows["model"].map(baseline_map)
    rows["above_baseline"] = rows["correlation"] > rows["baseline_correlation_mean30"]
    return rows.sort_values(["model", "item_id"]).reset_index(drop=True)


def build_summary(rows: pd.DataFrame) -> pd.DataFrame:
    out_rows: list[dict[str, object]] = []
    for model in MODEL_ORDER:
        part = rows.loc[rows["model"] == model, "correlation"].dropna()
        baseline_value = float(rows.loc[rows["model"] == model, "baseline_correlation_mean30"].iloc[0])
        out_rows.append(
            {
                "model": model,
                "n_items": int(part.shape[0]),
                "mean_correlation": float(part.mean()),
                "median_correlation": float(part.median()),
                "p05_correlation": float(part.quantile(0.05)),
                "p25_correlation": float(part.quantile(0.25)),
                "p75_correlation": float(part.quantile(0.75)),
                "p95_correlation": float(part.quantile(0.95)),
                "min_correlation": float(part.min()),
                "max_correlation": float(part.max()),
                "baseline_correlation_mean30": baseline_value,
                "n_above_baseline": int((part > baseline_value).sum()),
                "share_above_baseline": float((part > baseline_value).mean()),
            }
        )
    return pd.DataFrame(out_rows)


def build_pairwise(rows: pd.DataFrame) -> pd.DataFrame:
    wide = rows.pivot_table(index="item_id", columns="model", values="correlation", aggfunc="mean")
    wide = wide.reindex(columns=MODEL_ORDER)

    out_rows: list[dict[str, object]] = []
    for i, model_a in enumerate(MODEL_ORDER):
        for model_b in MODEL_ORDER[i + 1 :]:
            pair = wide[[model_a, model_b]].dropna()
            a = pair[model_a].to_numpy(dtype=float)
            b = pair[model_b].to_numpy(dtype=float)
            pearson_r, pearson_p = stats.pearsonr(a, b)
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


def build_heatmap_matrix(pairwise: pd.DataFrame) -> pd.DataFrame:
    labels = [HEATMAP_LABELS[model] for model in MODEL_ORDER]
    matrix = pd.DataFrame(np.nan, index=labels, columns=labels)
    for label in labels:
        matrix.loc[label, label] = 1.0
    for row in pairwise.itertuples(index=False):
        a = HEATMAP_LABELS[row.model_a]
        b = HEATMAP_LABELS[row.model_b]
        matrix.loc[b, a] = float(row.pearson_r)
        matrix.loc[a, b] = float(row.pearson_r)
    return matrix


def write_documentation(summary: pd.DataFrame, pairwise: pd.DataFrame) -> None:
    summary_display = summary.copy()
    for col in [
        "mean_correlation",
        "median_correlation",
        "p05_correlation",
        "p25_correlation",
        "p75_correlation",
        "p95_correlation",
        "min_correlation",
        "max_correlation",
        "baseline_correlation_mean30",
        "share_above_baseline",
    ]:
        summary_display[col] = summary_display[col].map(lambda x: f"{float(x):.6f}")

    pairwise_display = pairwise.copy()
    for col in ["pearson_r", "pearson_p_two_sided"]:
        pairwise_display[col] = pairwise_display[col].map(lambda x: f"{float(x):.6f}")

    doc = f"""# {OUT_STEM}

## Purpose
Exploratory CDF variant for `main_text_260427` Figure 3. This version keeps the raw correlation scale on the x-axis and shows the cumulative share of papers on the y-axis.

## Output files
- Plot PNG: `{FIG_PNG.relative_to(ROOT)}`
- Paper-level rows: `{ROWS_CSV.relative_to(ROOT)}`
- Summary table: `{SUMMARY_CSV.relative_to(ROOT)}`
- Pairwise agreement table: `{PAIRWISE_CSV.relative_to(ROOT)}`
- Documentation: `{DOC_MD.relative_to(ROOT)}`
- Script: `{Path(__file__).resolve().relative_to(ROOT)}`

## Notes
- Panel A is a raw-correlation CDF: x-axis = augmented paper performance, y-axis = share of papers at or below that performance.
- The no-augmentation baseline is shown as a vertical dashed line, so the share above baseline can be read directly as `1 - F(baseline)`.
- This variant is exploratory and is not the canonical Figure 3 unless promoted later.

## Summary values
{summary_display.to_markdown(index=False)}

## Pairwise agreement values
{pairwise_display.to_markdown(index=False)}
"""
    DOC_MD.write_text(doc)


def draw_panel_a(axes: list[plt.Axes], rows: pd.DataFrame, summary: pd.DataFrame, noise_ceiling: float) -> None:
    for idx, (ax, model) in enumerate(zip(axes, MODEL_ORDER)):
        part = rows.loc[rows["model"] == model, "correlation"].dropna().sort_values().to_numpy(dtype=float)
        cdf = np.arange(1, len(part) + 1, dtype=float) / len(part)
        baseline_value = float(summary.loc[summary["model"] == model, "baseline_correlation_mean30"].iloc[0])
        n_items = int(summary.loc[summary["model"] == model, "n_items"].iloc[0])
        n_above = int(summary.loc[summary["model"] == model, "n_above_baseline"].iloc[0])
        share_above = float(summary.loc[summary["model"] == model, "share_above_baseline"].iloc[0])

        ax.axvspan(0.0, baseline_value, color="#e9caca", alpha=0.72, zorder=0)
        ax.axvspan(baseline_value, 0.86, color="#d8e7d1", alpha=0.78, zorder=0)
        ax.plot(part, cdf, color=MODEL_COLORS[model], linewidth=2.25, zorder=4)
        ax.axvline(baseline_value, color=MODEL_COLORS[model], linestyle="--", linewidth=1.3, zorder=3)
        ax.axvline(noise_ceiling, color="#111827", linestyle=":", linewidth=1.15, zorder=2)

        ax.text(
            0.5,
            1.04,
            model,
            transform=ax.transAxes,
            ha="center",
            va="bottom",
            fontsize=10.8,
            color=MODEL_COLORS[model],
            fontweight="bold",
        )
        ax.text(
            0.98,
            0.08,
            f"{n_above:,} above baseline\n({100.0 * share_above:.0f}%)",
            transform=ax.transAxes,
            ha="right",
            va="bottom",
            fontsize=8.2,
            color="#1f2937",
            bbox={"boxstyle": "round,pad=0.14", "facecolor": "white", "edgecolor": "none", "alpha": 0.82},
        )
        ax.text(
            0.02,
            0.90,
            f"{n_items - n_above:,} at/below baseline",
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=8.2,
            color="#1f2937",
            bbox={"boxstyle": "round,pad=0.14", "facecolor": "white", "edgecolor": "none", "alpha": 0.82},
        )

        if idx == 0:
            ax.text(
                noise_ceiling + 0.008,
                0.98,
                "Noise ceiling",
                transform=ax.get_xaxis_transform(),
                ha="left",
                va="top",
                fontsize=8.4,
                color="#111827",
            )

        ax.set_xlim(0.0, 0.86)
        ax.set_ylim(0.0, 1.0)
        ax.set_xticks(np.arange(0.0, 0.81, 0.2))
        ax.set_yticks(np.arange(0.0, 1.01, 0.25))
        ax.grid(axis="both", color="#dbe3ea", linewidth=0.85)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_xlabel("")
        ax.tick_params(axis="x", labelsize=8.8)
        if idx != 0:
            ax.tick_params(axis="y", labelleft=False)


def draw_panel_b(ax: plt.Axes, pairwise: pd.DataFrame) -> None:
    matrix = build_heatmap_matrix(pairwise)
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
        linewidths=1.0,
        linecolor="white",
        annot_kws={"fontsize": 10.2},
    )
    ax.set_title("B   Cross-LLM Agreement\n(Pearson $r$)", loc="left", fontsize=12.4, pad=12)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.tick_params(axis="x", labelrotation=0, labelsize=9.0)
    ax.tick_params(axis="y", labelrotation=0, labelsize=9.0)
    ax.text(
        0.02,
        -0.16,
        "Shared papers: n = 2,010",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=8.9,
        color="#374151",
    )


def draw_figure(rows: pd.DataFrame, summary: pd.DataFrame, pairwise: pd.DataFrame) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig = plt.figure(figsize=(12.8, 4.25))
    gs = fig.add_gridspec(1, 4, width_ratios=[1.0, 1.0, 1.0, 1.18], wspace=0.24)
    ax_a = [fig.add_subplot(gs[0, 0])]
    ax_a.append(fig.add_subplot(gs[0, 1], sharey=ax_a[0]))
    ax_a.append(fig.add_subplot(gs[0, 2], sharey=ax_a[0]))
    ax_b = fig.add_subplot(gs[0, 3])

    draw_panel_a(ax_a, rows, summary, load_noise_ceiling())
    draw_panel_b(ax_b, pairwise)

    fig.text(0.065, 0.96, "A   Heterogeneity Across Augmented Papers", ha="left", va="top", fontsize=12.4)
    fig.text(0.065, 0.92, "2,011 papers shown as cumulative distributions", ha="left", va="top", fontsize=9.0, color="#374151")
    fig.supxlabel(r"Correlation coefficient with the true outcome ($r$)", y=0.045, fontsize=10.3)
    fig.supylabel("Cumulative share of papers", x=0.012, fontsize=10.3)
    fig.subplots_adjust(left=0.07, right=0.985, top=0.84, bottom=0.16)
    fig.savefig(FIG_PNG, dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    rows = build_rows()
    summary = build_summary(rows)
    pairwise = build_pairwise(rows)

    rows.to_csv(ROWS_CSV, index=False)
    summary.to_csv(SUMMARY_CSV, index=False)
    pairwise.to_csv(PAIRWISE_CSV, index=False)
    write_documentation(summary, pairwise)
    draw_figure(rows, summary, pairwise)


if __name__ == "__main__":
    main()
