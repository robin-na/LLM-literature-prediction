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
from matplotlib import transforms
from scipy import stats


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260427"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260427"
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

OUT_STEM = "figure3_paper_heterogeneity_agreement"
FIG_PNG = PLOTS_DIR / f"{OUT_STEM}.png"
ROWS_CSV = RESULTS_DIR / f"{OUT_STEM}_rows.csv"
SUMMARY_CSV = RESULTS_DIR / f"{OUT_STEM}_summary.csv"
PAIRWISE_CSV = RESULTS_DIR / f"{OUT_STEM}_pairwise.csv"
DOC_MD = RESULTS_DIR / f"{OUT_STEM}_documentation.md"

MODEL_ORDER = ["Claude Sonnet 4.6", "GPT-4.1", "Gemini 2.5 Pro"]
PANEL_LETTERS = {
    "Claude Sonnet 4.6": "A",
    "GPT-4.1": "B",
    "Gemini 2.5 Pro": "C",
}
POINT_COLORS = {
    "below": "#c64b41",
    "above": "#2f9e44",
}
SHADE_COLORS = {
    "below_active": "#deb0ac",
    "below_inactive": "#f3dfdc",
    "above_inactive": "#e8f1e0",
    "above_active": "#bfd5ba",
}
BASELINE_COLOR = "#111111"
def load_baseline30() -> dict[str, float]:
    df = pd.read_csv(BASELINE30_CSV)
    df = df.loc[df["model"].isin(MODEL_ORDER), ["model", "correlation_mean_prediction"]].copy()
    return {str(row["model"]): float(row["correlation_mean_prediction"]) for _, row in df.iterrows()}


def load_noise_ceiling() -> float:
    benchmarks = pd.read_csv(NO_AUG_BENCHMARKS_CSV)
    return float(benchmarks.loc[benchmarks["benchmark"] == "Noise ceiling", "correlation"].iloc[0])


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
    rows["model_display"] = pd.Categorical(rows["model"], categories=MODEL_ORDER, ordered=True)
    return rows.sort_values(["model_display", "item_id"]).reset_index(drop=True)


def build_summary(rows: pd.DataFrame) -> pd.DataFrame:
    out_rows: list[dict[str, object]] = []
    for model in MODEL_ORDER:
        part = rows.loc[rows["model"] == model, "correlation"].dropna()
        n_items = int(part.shape[0])
        mean_value = float(part.mean())
        sd_value = float(part.std(ddof=1))
        se_value = sd_value / np.sqrt(n_items)
        t_crit = float(stats.t.ppf(0.975, df=n_items - 1))
        baseline_value = float(rows.loc[rows["model"] == model, "baseline_correlation_mean30"].iloc[0])
        out_rows.append(
            {
                "model": model,
                "n_items": n_items,
                "mean_correlation": mean_value,
                "mean_correlation_ci_low": mean_value - t_crit * se_value,
                "mean_correlation_ci_high": mean_value + t_crit * se_value,
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
            spearman_rho, spearman_p = stats.spearmanr(a, b)
            kendall_tau, kendall_p = stats.kendalltau(a, b)

            out_rows.append(
                {
                    "model_a": model_a,
                    "model_b": model_b,
                    "n_shared_papers": int(pair.shape[0]),
                    "pearson_r": float(pearson_r),
                    "pearson_p_two_sided": float(pearson_p),
                    "spearman_rho": float(spearman_rho),
                    "spearman_p_two_sided": float(spearman_p),
                    "kendall_tau": float(kendall_tau),
                    "kendall_p_two_sided": float(kendall_p),
                }
            )
    return pd.DataFrame(out_rows)


def write_documentation(rows: pd.DataFrame, summary: pd.DataFrame, pairwise: pd.DataFrame) -> None:
    summary_display = summary.copy()
    for col in [
        "mean_correlation",
        "mean_correlation_ci_low",
        "mean_correlation_ci_high",
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
    for col in [
        "pearson_r",
        "pearson_p_two_sided",
        "spearman_rho",
        "spearman_p_two_sided",
        "kendall_tau",
        "kendall_p_two_sided",
    ]:
        pairwise_display[col] = pairwise_display[col].map(lambda x: f"{float(x):.6f}")

    doc = f"""# {OUT_STEM}

## Purpose
Figure 3 for `main_text_260427`. The current canonical version focuses on the 2,011 individual papers only and shows heterogeneity in absolute augmented prediction performance on the raw correlation scale with paper rank made explicit on the x-axis. Cross-LLM agreement is not rendered in the current main-text figure and can be handled separately in text or a companion figure.

## Inheritance
- Semantic figure intent: paper-level augmentation heterogeneity
- Adapted from `main_text_260415` Figure 2 variants:
  - `plots/paper/main_text_260415/figure2_individual_collection_density.png`
  - `plots/paper/main_text_260415/figure2_heterogeneity_and_cross_model_agreement.png`
- Collections are intentionally removed from the `260427` main-text version and can be handled in the supplement.

## Output files
- Plot PNG: `{FIG_PNG.relative_to(ROOT)}`
- Paper-level rows: `{ROWS_CSV.relative_to(ROOT)}`
- Summary table: `{SUMMARY_CSV.relative_to(ROOT)}`
- Pairwise agreement table: `{PAIRWISE_CSV.relative_to(ROOT)}`
- Documentation: `{DOC_MD.relative_to(ROOT)}`
- Script: `{Path(__file__).resolve().relative_to(ROOT)}`

## Input files
- Paper-level augmented performance rows: `{PAPER_METRICS_CSV.relative_to(ROOT)}`
- No-augmentation 30-run baseline summary: `{BASELINE30_CSV.relative_to(ROOT)}`
- Noise ceiling benchmark table: `{NO_AUG_BENCHMARKS_CSV.relative_to(ROOT)}`

## Estimand
- Paper-level augmented performance: `corr(mean prediction across augmentation repeats, true outcome)` for each of the 2,011 papers.
- No-augmentation baseline marker: `corr(mean prediction across 30 baseline runs, true outcome)`.

## Construction
1. Restrict to the three main-text models: `Claude Sonnet 4.6`, `GPT-4.1`, and `Gemini 2.5 Pro`.
2. Take the paper-level `correlation` column from `{PAPER_METRICS_CSV.name}` for each model across all available papers.
3. Within each model, sort papers from worst to best augmented performance.
4. Plot paper percentile on the x-axis and raw augmented correlation on the y-axis in three side-by-side small multiples.
5. Divide each panel into four background regions using the no-augmentation baseline and the within-model crossover percentile, with darker shades for the realized underperformance and outperformance quadrants and lighter shades for the two counterfactual quadrants.
6. Plot sorted paper-level points in matching red and green based on whether each paper falls below or above the no-augmentation baseline.
7. Overlay the no-augmentation 30-run baseline as a solid black horizontal line and the estimated noise ceiling as a dotted black horizontal line, described by a compact figure-level legend.
8. Add one lower-left annotation reporting the share of papers that worsen prediction when given to the LLM.
9. Add a far-right summary gutter separated by a light vertical line, containing a small average point with a vertical 95% t interval across papers and a rotated `Average: ...` label.
10. Pairwise cross-LLM agreement is still computed into `{PAIRWISE_CSV.name}` as a companion table, but it is intentionally omitted from the current canonical main-text figure.

## Notes
- The figure stays on the raw-correlation scale so improvements are not overstated for lower-baseline models.
- `Paper percentile` is used rather than raw rank so the x-axis remains directly comparable across the three panels despite the one-paper difference for `GPT-4.1`.
- The displayed mean interval is a descriptive 95% interval for the average correlation across papers within a model, not a CI for a single paper-level correlation.
- Confidence intervals are intentionally omitted from the main panel. Raw-correlation CIs across only 20 validation experiments are large enough to visually swamp the paper-to-paper heterogeneity signal, while delta-based paired CIs would mismatch the raw-correlation y-axis.
- `GPT-4.1` has one fewer source paper in the corrected table, so its panel contains `2010` papers while the other two panels contain `2011`.

## Summary values
{summary_display.to_markdown(index=False)}

## Companion pairwise agreement values
{pairwise_display.to_markdown(index=False)}
"""
    DOC_MD.write_text(doc)


def draw_panel_a(
    axes: list[plt.Axes],
    rows: pd.DataFrame,
    summary: pd.DataFrame,
    noise_ceiling: float,
) -> None:
    for idx, (ax, model) in enumerate(zip(axes, MODEL_ORDER)):
        part_df = rows.loc[rows["model"] == model, ["correlation", "above_baseline"]].dropna().sort_values("correlation")
        part = part_df["correlation"].to_numpy(dtype=float)
        above_baseline = part_df["above_baseline"].to_numpy(dtype=bool)
        percentiles = np.linspace(0.0, 100.0, num=len(part), endpoint=True)
        baseline_value = float(summary.loc[summary["model"] == model, "baseline_correlation_mean30"].iloc[0])
        share_above = float(summary.loc[summary["model"] == model, "share_above_baseline"].iloc[0])
        mean_value = float(summary.loc[summary["model"] == model, "mean_correlation"].iloc[0])
        mean_ci_low = float(summary.loc[summary["model"] == model, "mean_correlation_ci_low"].iloc[0])
        mean_ci_high = float(summary.loc[summary["model"] == model, "mean_correlation_ci_high"].iloc[0])
        n_items = int(summary.loc[summary["model"] == model, "n_items"].iloc[0])
        n_above = int(summary.loc[summary["model"] == model, "n_above_baseline"].iloc[0])
        n_below = n_items - n_above
        x_cut = 100.0 * n_below / n_items

        plot_xmax = 100.0
        gutter_sep = 100.65
        x_max = 105.45

        ax.axvspan(0.0, x_cut, ymin=0.0 / 0.86, ymax=baseline_value / 0.86, color=SHADE_COLORS["below_active"], zorder=0)
        ax.axvspan(0.0, x_cut, ymin=baseline_value / 0.86, ymax=1.0, color=SHADE_COLORS["above_inactive"], zorder=0)
        ax.axvspan(x_cut, x_max, ymin=0.0 / 0.86, ymax=baseline_value / 0.86, color=SHADE_COLORS["below_inactive"], zorder=0)
        ax.axvspan(x_cut, x_max, ymin=baseline_value / 0.86, ymax=1.0, color=SHADE_COLORS["above_active"], zorder=0)
        ax.scatter(
            percentiles[~above_baseline],
            part[~above_baseline],
            color=POINT_COLORS["below"],
            s=9,
            alpha=0.75,
            linewidths=0.0,
            zorder=3,
            rasterized=True,
        )
        ax.scatter(
            percentiles[above_baseline],
            part[above_baseline],
            color=POINT_COLORS["above"],
            s=9,
            alpha=0.75,
            linewidths=0.0,
            zorder=3,
            rasterized=True,
        )
        ax.axhline(baseline_value, color=BASELINE_COLOR, linestyle="-", linewidth=1.3, zorder=4)
        ax.axhline(noise_ceiling, color="#111111", linestyle=":", linewidth=1.15, zorder=4)

        ax.text(
            0.00,
            1.035,
            PANEL_LETTERS[model],
            transform=ax.transAxes,
            ha="left",
            va="bottom",
            fontsize=10.3,
            color="#111827",
            fontweight="bold",
        )
        ax.text(
            0.10,
            1.035,
            model,
            transform=ax.transAxes,
            ha="left",
            va="bottom",
            fontsize=10.5,
            color="#111827",
            fontweight="bold",
        )
        ax.text(
            8.5,
            0.135,
            f"{100.0 * (1.0 - share_above):.0f}% (n={n_below:,}) of papers\nworsen LLM prediction",
            transform=ax.transData,
            ha="left",
            va="center",
            fontsize=6.1,
            color="#111827",
        )
        ax.text(
            8.5,
            noise_ceiling - 0.055,
            f"{100.0 * share_above:.0f}% (n={n_above:,}) of papers\nimprove LLM prediction",
            transform=ax.transData,
            ha="left",
            va="center",
            fontsize=6.1,
            color="#111827",
        )

        ax.axvline(gutter_sep, color="#98a2ad", linewidth=1.0, zorder=1)
        ax.axvline(x_max, color="#98a2ad", linewidth=1.0, zorder=1)

        mean_x = 0.5 * (gutter_sep + x_max)
        mean_color = POINT_COLORS["above"] if mean_value > baseline_value else POINT_COLORS["below"]
        ax.errorbar(
            [mean_x],
            [mean_value],
            yerr=[[mean_value - mean_ci_low], [mean_ci_high - mean_value]],
            fmt="o",
            markersize=3.7,
            color=mean_color,
            ecolor=mean_color,
            elinewidth=1.0,
            capsize=2.2,
            capthick=1.0,
            zorder=6,
        )
        gutter_text_transform = transforms.blended_transform_factory(ax.transAxes, ax.transData)
        avg_label = (
            f"Average: {mean_value:.3f}"
            if model == "Gemini 2.5 Pro"
            else f"Average across papers: {mean_value:.3f}"
        )
        avg_label_y = mean_value - 0.014 if model != "Gemini 2.5 Pro" else mean_value + 0.010
        ax.text(
            0.996,
            avg_label_y,
            avg_label,
            transform=gutter_text_transform,
            rotation=90,
            ha="right",
            va="top" if model != "Gemini 2.5 Pro" else "bottom",
            fontsize=5.15,
            color="#111111",
        )

        ax.set_xlim(0.0, x_max)
        ax.set_ylim(0.0, 0.86)
        ax.set_yticks(np.arange(0.0, 0.81, 0.2))
        ax.set_xticks([0, 25, 50, 75, 100])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("#111827")
        ax.spines["bottom"].set_color("#111827")
        ax.spines["left"].set_linewidth(1.0)
        ax.spines["bottom"].set_linewidth(1.0)
        ax.tick_params(axis="both", labelsize=7.6, colors="#374151", length=3.0, width=0.8)
        ax.set_xlabel("")
        ax.set_ylabel("")
        if idx != 0:
            ax.tick_params(axis="y", labelleft=False)


def draw_figure(rows: pd.DataFrame, summary: pd.DataFrame, _pairwise: pd.DataFrame) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig = plt.figure(figsize=(9.35, 3.75))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.0, 1.0, 1.0], wspace=0.12)
    ax_a = [fig.add_subplot(gs[0, 0])]
    ax_a.append(fig.add_subplot(gs[0, 1], sharey=ax_a[0]))
    ax_a.append(fig.add_subplot(gs[0, 2], sharey=ax_a[0]))

    draw_panel_a(ax_a, rows, summary, load_noise_ceiling())

    legend_handles = [
        Line2D([0], [0], color="#111111", linewidth=1.3, linestyle="-", label="Unaugmented LLM"),
        Line2D([0], [0], color="#111111", linewidth=1.15, linestyle=":", label="Noise ceiling"),
    ]
    fig.legend(
        handles=legend_handles,
        loc="lower left",
        bbox_to_anchor=(0.085, 0.045),
        ncol=2,
        frameon=False,
        fontsize=7.2,
        handlelength=2.6,
        columnspacing=1.2,
    )

    fig.supxlabel("Paper percentile", y=0.027, fontsize=9.3, color="#111827")
    fig.supylabel(r"Correlation with the true outcome ($r$)", x=0.028, fontsize=9.2, color="#111827")
    fig.subplots_adjust(left=0.088, right=0.985, top=0.84, bottom=0.15)
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
    write_documentation(rows, summary, pairwise)
    draw_figure(rows, summary, pairwise)


if __name__ == "__main__":
    main()
