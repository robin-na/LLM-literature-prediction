from __future__ import annotations

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

import plot_figure7_metadata_effect_robustness as fig7_module


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"

PAPER_METRICS_CSV = RESULTS_DIR / "paper_repeat_correlation_metrics.csv"
VALUE_ROWS_CSV = RESULTS_DIR / "figure7_individual_metadata_effect_robustness_rows.csv"
RANK_ROWS_CSV = RESULTS_DIR / "figure7_individual_metadata_effect_rank_target_rows.csv"
COMPARISON_CSV = RESULTS_DIR / "figure7_individual_metadata_effect_rank_target_vs_value_comparison.csv"
MODEL_SUMMARY_CSV = RESULTS_DIR / "figure7_individual_metadata_effect_rank_target_model_summary.csv"
FEATURE_SUMMARY_CSV = RESULTS_DIR / "figure7_individual_metadata_effect_rank_target_feature_summary.csv"

RANK_PNG = PLOTS_DIR / "figure7_individual_metadata_effect_rank_target.png"
RANK_PDF = PLOTS_DIR / "figure7_individual_metadata_effect_rank_target.pdf"

MODELS = ["GPT-4.1", "GPT-4.1 Mini", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano", "Claude Sonnet 4.6", "Gemini 2.5 Pro"]
MODEL_COLORS = {
    "GPT-4.1": "#2b8cbe",
    "GPT-4.1 Mini": "#1b9e77",
    "GPT-5.1": "#d95f02",
    "GPT-5 Mini": "#7570b3",
    "GPT-5 Nano": "#e7298a",
    "Claude Sonnet 4.6": "#9c755f",
    "Gemini 2.5 Pro": "#a6761d",
}


def build_rank_target_frame() -> pd.DataFrame:
    current_df = fig7_module.load_paper_df().drop(columns=["delta_correlation"])
    base_feature_df = (
        current_df.loc[current_df["model"] == "GPT-4.1"]
        .drop(columns=["model"])
        .drop_duplicates("source_id", keep="first")
    )
    metrics = pd.read_csv(PAPER_METRICS_CSV)
    df = metrics.loc[:, ["model", "source_id", "delta_correlation"]].merge(
        base_feature_df,
        on="source_id",
        how="left",
        validate="many_to_one",
    )
    df = df.loc[df["model"].isin(MODELS)].copy()
    df["delta_rank_pct"] = df.groupby("model")["delta_correlation"].rank(method="average", pct=True)
    df["delta_rank_centered"] = df["delta_rank_pct"] - 0.5
    return df


def build_rank_rows(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for model in MODELS:
        part = df.loc[df["model"] == model].copy()
        coef_df = fig7_module.fit_ridge_bootstrap(part, fig7_module.PAPER_FEATURES, y_col="delta_rank_centered")
        for row in coef_df.itertuples(index=False):
            rows.append(
                {
                    "item_type": "Individual papers (rank target)",
                    "model": model,
                    "feature_key": row.feature_key,
                    "feature_label": fig7_module.FEATURE_LABELS[row.feature_key],
                    "coef": float(row.coef),
                    "ci_low": float(row.ci_low),
                    "ci_high": float(row.ci_high),
                    "n": int(row.n),
                }
            )
    return pd.DataFrame(rows)


def draw_rank_figure(df: pd.DataFrame) -> None:
    features = fig7_module.ordered_features(df)
    base_y = np.arange(len(features))[::-1].astype(float)
    y_map = dict(zip(features, base_y))
    offsets = np.linspace(-0.24, 0.24, len(MODELS))
    xlim = max(0.02, float(np.nanmax(np.abs(df[["coef", "ci_low", "ci_high"]].to_numpy(dtype=float)))) * 1.1)

    fig, ax = plt.subplots(1, 1, figsize=(7.0, 5.3))
    ax.axvline(0.0, color="#777777", lw=1.0, ls=(0, (4, 3)), zorder=1)

    for offset, model in zip(offsets, MODELS):
        part = df.loc[df["model"] == model].copy()
        ys = [y_map[label] + offset for label in part["feature_label"]]
        ax.errorbar(
            part["coef"],
            ys,
            xerr=[part["coef"] - part["ci_low"], part["ci_high"] - part["coef"]],
            fmt="o",
            ms=5.0,
            lw=0,
            elinewidth=1.15,
            capsize=2.4,
            color=MODEL_COLORS[model],
            ecolor=MODEL_COLORS[model],
            alpha=0.95,
            zorder=3,
        )

    ax.set_title("Figure 7 Variant: rank target", fontsize=13, pad=8)
    ax.set_yticks(base_y)
    ax.set_yticklabels(features)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="x", color="#e6e6e6", lw=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#cfcfcf")
    ax.set_xlim(-xlim, xlim)
    ax.set_xlabel("Standardized ridge coefficient on within-model rank percentile")

    handles = [
        plt.Line2D([0], [0], marker="o", linestyle="none", markersize=6, color=MODEL_COLORS[model], label=model)
        for model in MODELS
    ]
    fig.legend(
        handles=handles,
        loc="upper center",
        ncol=3,
        frameon=False,
        bbox_to_anchor=(0.5, 0.96),
        columnspacing=1.1,
        handletextpad=0.3,
    )
    fig.subplots_adjust(left=0.46, right=0.98, top=0.82, bottom=0.11)
    fig.savefig(RANK_PNG, dpi=300)
    fig.savefig(RANK_PDF)
    plt.close(fig)


def build_comparison(value_rows: pd.DataFrame, rank_rows: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    merged = value_rows.merge(
        rank_rows.loc[:, ["model", "feature_key", "coef", "ci_low", "ci_high"]],
        on=["model", "feature_key"],
        suffixes=("_value", "_rank"),
    )
    merged["sign_value"] = np.sign(merged["coef_value"]).astype(int)
    merged["sign_rank"] = np.sign(merged["coef_rank"]).astype(int)
    merged["sign_flip"] = merged["sign_value"] != merged["sign_rank"]

    model_rows: list[dict[str, object]] = []
    for model, part in merged.groupby("model", dropna=False):
        corr = float(np.corrcoef(part["coef_value"], part["coef_rank"])[0, 1])
        top_value = part.loc[part["coef_value"].abs().idxmax(), "feature_label"]
        top_rank = part.loc[part["coef_rank"].abs().idxmax(), "feature_label"]
        model_rows.append(
            {
                "model": model,
                "coef_vector_corr": corr,
                "n_sign_flips": int(part["sign_flip"].sum()),
                "top_feature_value_target": str(top_value),
                "top_feature_rank_target": str(top_rank),
            }
        )

    feature_summary = (
        merged.groupby("feature_label", as_index=False)
        .agg(
            mean_coef_value=("coef_value", "mean"),
            mean_coef_rank=("coef_rank", "mean"),
            sign_flips=("sign_flip", "sum"),
        )
        .sort_values("mean_coef_rank", ascending=False)
        .reset_index(drop=True)
    )
    return merged, pd.DataFrame(model_rows), feature_summary


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    fig7_module.MODELS = MODELS
    fig7_module.MODEL_COLORS = MODEL_COLORS

    rank_target_df = build_rank_target_frame()
    rank_rows = build_rank_rows(rank_target_df)
    rank_rows.to_csv(RANK_ROWS_CSV, index=False)
    draw_rank_figure(rank_rows)

    value_rows = pd.read_csv(VALUE_ROWS_CSV)
    comparison, model_summary, feature_summary = build_comparison(value_rows, rank_rows)
    comparison.to_csv(COMPARISON_CSV, index=False)
    model_summary.to_csv(MODEL_SUMMARY_CSV, index=False)
    feature_summary.to_csv(FEATURE_SUMMARY_CSV, index=False)


if __name__ == "__main__":
    main()
