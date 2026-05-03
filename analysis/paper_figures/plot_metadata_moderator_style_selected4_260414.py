from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from matplotlib.lines import Line2D
from matplotlib.ticker import FormatStrFormatter, MaxNLocator

ROOT = Path(__file__).resolve().parents[2]
ANALYSIS_ROOT = ROOT / "analysis"
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import plot_figure7_metadata_effect_robustness as fig7_module
from paper_figures.plot_collection_linear_metadata_effect_260409 import build_collection_df


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"

PAPER_METRICS_CSV = RESULTS_DIR / "paper_repeat_correlation_metrics.csv"
ROWS_CSV = RESULTS_DIR / "metadata_moderator_style_selected4_rows.csv"
PNG = PLOTS_DIR / "metadata_moderator_style_selected4.png"
PDF = PLOTS_DIR / "metadata_moderator_style_selected4.pdf"

MODELS = ["Claude Sonnet 4.6", "GPT-5.1", "GPT-4.1", "Gemini 2.5 Pro"]
MODEL_COLORS = {
    "Claude Sonnet 4.6": "#9c755f",
    "GPT-5.1": "#d95f02",
    "GPT-4.1": "#2b8cbe",
    "Gemini 2.5 Pro": "#17becf",
}


@dataclass(frozen=True)
class ModeratorSpec:
    key: str
    title: str
    levels: list[str]


INDIVIDUAL_MODERATORS = [
    ModeratorSpec("paper_type_group", "Paper type", ["Theoretical", "Empirical"]),
    ModeratorSpec("citation_quartile", "Citation", ["Q1 lowest", "Q2", "Q3", "Q4 highest"]),
    ModeratorSpec("journal_impact_quartile", "Journal impact factor", ["Q1 lowest", "Q2", "Q3", "Q4 highest"]),
    ModeratorSpec("year_quartile", "Publication year", ["Q1 earliest", "Q2", "Q3", "Q4 latest"]),
    ModeratorSpec(
        "discipline_group",
        "Journal discipline",
        ["Biology", "Economics", "Psychology", "Math/Physics", "Multidisciplinary", "Mixed/Other"],
    ),
]

COLLECTION_MODERATORS = [
    ModeratorSpec("empirical_quartile", "Empirical share", ["Q1 lowest", "Q2", "Q3", "Q4 highest"]),
    ModeratorSpec("citation_quartile", "Citation", ["Q1 lowest", "Q2", "Q3", "Q4 highest"]),
    ModeratorSpec("journal_impact_quartile", "Journal impact factor", ["Q1 lowest", "Q2", "Q3", "Q4 highest"]),
    ModeratorSpec("year_quartile", "Publication year", ["Q1 earliest", "Q2", "Q3", "Q4 latest"]),
    ModeratorSpec(
        "discipline_group",
        "Dominant discipline",
        ["Biology", "Economics", "Psychology", "Math/Physics", "Multidisciplinary", "Mixed/Other"],
    ),
]


def build_individual_df() -> pd.DataFrame:
    current_df = fig7_module.load_paper_df().drop(columns=["delta_correlation", "correlation"])
    base_feature_df = (
        current_df.loc[current_df["model"] == "GPT-4.1"]
        .drop(columns=["model"])
        .drop_duplicates("source_id", keep="first")
    )
    metrics = pd.read_csv(PAPER_METRICS_CSV)
    df = metrics.loc[:, ["model", "source_id", "correlation"]].merge(
        base_feature_df,
        on="source_id",
        how="left",
        validate="many_to_one",
    )
    df = df.loc[df["model"].isin(MODELS)].copy()
    df["paper_type_group"] = df["empirical_share"].map({0.0: "Theoretical", 1.0: "Empirical"})
    df["citation_quartile"] = pd.qcut(df["citation"], 4, labels=["Q1 lowest", "Q2", "Q3", "Q4 highest"], duplicates="drop")
    df["journal_impact_quartile"] = pd.qcut(
        df["journal_impact"], 4, labels=["Q1 lowest", "Q2", "Q3", "Q4 highest"], duplicates="drop"
    )
    df["year_quartile"] = pd.qcut(df["recent"], 4, labels=["Q1 earliest", "Q2", "Q3", "Q4 latest"], duplicates="drop")
    df["discipline_group"] = df["discipline_coarse"].map(_map_individual_discipline)
    return df


def _map_individual_discipline(value: object) -> str:
    s = "" if pd.isna(value) else str(value)
    if s == "bio_evo":
        return "Biology"
    if s == "economics":
        return "Economics"
    if s == "psych_social":
        return "Psychology"
    if s == "math_phys_cs":
        return "Math/Physics"
    if s == "multidisciplinary":
        return "Multidisciplinary"
    return "Mixed/Other"


def _dominant_collection_discipline(row: pd.Series) -> str:
    vals = {
        "Biology": row["biology_share"],
        "Economics": row["economics_share"],
        "Psychology": row["psychology_share"],
        "Math/Physics": row["mathphysics_share"],
        "Multidisciplinary": row["multidisciplinary_share"],
    }
    label, value = max(vals.items(), key=lambda kv: kv[1])
    if pd.isna(value) or value < 0.5:
        return "Mixed/Other"
    return label


def build_collection_moderator_df() -> pd.DataFrame:
    df = build_collection_df().loc[lambda d: d["model"].isin(MODELS)].copy()
    df["empirical_quartile"] = pd.qcut(
        df["empirical_share"], 4, labels=["Q1 lowest", "Q2", "Q3", "Q4 highest"], duplicates="drop"
    )
    df["citation_quartile"] = pd.qcut(df["citation"], 4, labels=["Q1 lowest", "Q2", "Q3", "Q4 highest"], duplicates="drop")
    df["journal_impact_quartile"] = pd.qcut(
        df["journal_impact"], 4, labels=["Q1 lowest", "Q2", "Q3", "Q4 highest"], duplicates="drop"
    )
    df["year_quartile"] = pd.qcut(df["recent"], 4, labels=["Q1 earliest", "Q2", "Q3", "Q4 latest"], duplicates="drop")
    df["discipline_group"] = df.apply(_dominant_collection_discipline, axis=1)
    return df


def fit_group_means(part: pd.DataFrame, moderator: ModeratorSpec) -> pd.DataFrame:
    sub = part[[moderator.key, "correlation"]].dropna().copy()
    sub[moderator.key] = pd.Categorical(sub[moderator.key], categories=moderator.levels, ordered=True)
    fit = smf.ols(f"correlation ~ C({moderator.key})", data=sub).fit(cov_type="HC3")
    pred_df = pd.DataFrame({moderator.key: pd.Categorical(moderator.levels, categories=moderator.levels, ordered=True)})
    pred = fit.get_prediction(pred_df).summary_frame(alpha=0.05)

    counts = sub[moderator.key].value_counts().reindex(moderator.levels, fill_value=0)
    return pd.DataFrame(
        {
            "level": moderator.levels,
            "estimate": pred["mean"].astype(float).to_numpy(),
            "ci_low": pred["mean_ci_lower"].astype(float).to_numpy(),
            "ci_high": pred["mean_ci_upper"].astype(float).to_numpy(),
            "n_level": counts.to_numpy(dtype=int),
        }
    )


def build_rows(df: pd.DataFrame, *, panel: str, moderators: list[ModeratorSpec]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for moderator in moderators:
        for model in MODELS:
            part = df.loc[df["model"] == model].copy()
            est = fit_group_means(part, moderator)
            for row in est.itertuples(index=False):
                rows.append(
                    {
                        "panel": panel,
                        "moderator_key": moderator.key,
                        "moderator_title": moderator.title,
                        "model": model,
                        "level": row.level,
                        "estimate": float(row.estimate),
                        "ci_low": float(row.ci_low),
                        "ci_high": float(row.ci_high),
                        "n_level": int(row.n_level),
                    }
                )
    return pd.DataFrame(rows)


def layout_rows(moderators: list[ModeratorSpec]) -> tuple[list[tuple[str, str | None]], dict[tuple[str, str], float], list[float]]:
    rows: list[tuple[str, str | None]] = []
    y_positions: dict[tuple[str, str], float] = {}
    header_positions: list[float] = []

    y = 0.0
    for i, moderator in enumerate(moderators):
        rows.append((moderator.title, None))
        header_positions.append(y)
        y -= 0.95
        for level in moderator.levels:
            rows.append((moderator.title, level))
            y_positions[(moderator.title, level)] = y
            y -= 0.86
        if i < len(moderators) - 1:
            y -= 0.30
    return rows, y_positions, header_positions


def draw_panel(ax: plt.Axes, rows_df: pd.DataFrame, moderators: list[ModeratorSpec], title: str) -> None:
    layout, y_map, _ = layout_rows(moderators)
    offsets = np.linspace(0.24, -0.24, len(MODELS))

    xvals = rows_df[["estimate", "ci_low", "ci_high"]].to_numpy(dtype=float)
    xmin = float(np.nanmin(xvals))
    xmax = float(np.nanmax(xvals))
    pad = max(0.01, (xmax - xmin) * 0.08)
    ax.set_xlim(xmin - pad, xmax + pad)

    for moderator in moderators[:-1]:
        last_y = y_map[(moderator.title, moderator.levels[-1])]
        ax.axhline(last_y - 0.52, color="#e7e7e7", lw=0.8, zorder=0)

    for moderator_title, level in layout:
        if level is None:
            y = max(v for (mt, _), v in y_map.items() if mt == moderator_title) + 0.74
            ax.text(
                -0.02,
                y,
                moderator_title,
                transform=ax.get_yaxis_transform(),
                ha="right",
                va="center",
                fontsize=10.2,
                fontweight="bold",
                color="#222222",
            )
        else:
            y = y_map[(moderator_title, level)]
            n_level = int(
                rows_df.loc[
                    (rows_df["moderator_title"] == moderator_title) & (rows_df["level"] == level),
                    "n_level",
                ].iloc[0]
            )
            ax.text(
                -0.02,
                y,
                f"{level} (n={n_level})",
                transform=ax.get_yaxis_transform(),
                ha="right",
                va="center",
                fontsize=9.1,
                color="#444444",
            )

    for offset, model in zip(offsets, MODELS):
        part = rows_df.loc[rows_df["model"] == model].copy()
        ys = [y_map[(r.moderator_title, r.level)] + offset for r in part.itertuples(index=False)]
        ax.errorbar(
            part["estimate"],
            ys,
            xerr=[part["estimate"] - part["ci_low"], part["ci_high"] - part["estimate"]],
            fmt="o",
            ms=4.4,
            lw=0,
            elinewidth=1.05,
            capsize=2.0,
            color=MODEL_COLORS[model],
            ecolor=MODEL_COLORS[model],
            alpha=0.98,
            zorder=3,
        )

    ax.set_title(title, fontsize=12.5, pad=8)
    ax.grid(axis="x", color="#e8e8e8", lw=0.8)
    ax.set_axisbelow(True)
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#d0d0d0")
    ax.xaxis.set_major_locator(MaxNLocator(nbins=5))
    ax.xaxis.set_major_formatter(FormatStrFormatter("%.2f"))
    ymin = min(y_map.values()) - 0.8
    ymax = max(y_map.values()) + 1.1
    ax.set_ylim(ymin, ymax)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    individual_df = build_individual_df()
    collection_df = build_collection_moderator_df()

    individual_rows = build_rows(individual_df, panel="Individual papers", moderators=INDIVIDUAL_MODERATORS)
    collection_rows = build_rows(collection_df, panel="Collections", moderators=COLLECTION_MODERATORS)
    rows = pd.concat([individual_rows, collection_rows], ignore_index=True)
    rows.to_csv(ROWS_CSV, index=False)

    fig, axes = plt.subplots(1, 2, figsize=(13.2, 10.2))
    draw_panel(axes[0], individual_rows, INDIVIDUAL_MODERATORS, "Individual Papers")
    draw_panel(axes[1], collection_rows, COLLECTION_MODERATORS, "Collections")

    handles = [
        Line2D([0], [0], marker="o", linestyle="none", markersize=5.4, color=MODEL_COLORS[model], label=model)
        for model in MODELS
    ]
    fig.legend(
        handles=handles,
        loc="upper center",
        ncol=4,
        frameon=False,
        bbox_to_anchor=(0.5, 0.985),
        columnspacing=1.2,
        handletextpad=0.4,
        fontsize=9.5,
    )
    fig.supxlabel("Estimated correlation by subgroup (95% HC3 CI)", fontsize=11, y=0.05)
    fig.subplots_adjust(left=0.34, right=0.985, top=0.90, bottom=0.10, wspace=0.18)
    fig.savefig(PNG, dpi=300)
    fig.savefig(PDF)
    plt.close(fig)


if __name__ == "__main__":
    main()
