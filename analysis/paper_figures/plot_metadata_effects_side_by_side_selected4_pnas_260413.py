from __future__ import annotations

import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from matplotlib.lines import Line2D
from matplotlib.ticker import FormatStrFormatter, MaxNLocator
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

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
ROWS_CSV = RESULTS_DIR / "figure7_8_metadata_effect_side_by_side_selected4_pnas_ols_rows.csv"
PNG = PLOTS_DIR / "figure7_8_metadata_effect_side_by_side_selected4_pnas_ols.png"
PDF = PLOTS_DIR / "figure7_8_metadata_effect_side_by_side_selected4_pnas_ols.pdf"

MODELS = ["Claude Sonnet 4.6", "GPT-5.1", "GPT-4.1", "Gemini 2.5 Pro"]
MODEL_COLORS = {
    "Claude Sonnet 4.6": "#9c755f",
    "GPT-5.1": "#d95f02",
    "GPT-4.1": "#2b8cbe",
    "Gemini 2.5 Pro": "#17becf",
}


def build_individual_df() -> pd.DataFrame:
    current_df = fig7_module.load_paper_df().drop(columns=["delta_correlation", "correlation"])
    base_feature_df = (
        current_df.loc[current_df["model"] == "GPT-4.1"]
        .drop(columns=["model"])
        .drop_duplicates("source_id", keep="first")
    )
    metrics = pd.read_csv(PAPER_METRICS_CSV)
    return metrics.loc[:, ["model", "source_id", "correlation"]].merge(
        base_feature_df,
        on="source_id",
        how="left",
        validate="many_to_one",
    )


def fit_standardized_ols_hc3(df: pd.DataFrame, feature_cols: list[str], *, y_col: str = "correlation") -> pd.DataFrame:
    part = df[feature_cols + [y_col]].copy()
    y = pd.to_numeric(part[y_col], errors="coerce")
    X = part[feature_cols].apply(pd.to_numeric, errors="coerce")
    valid = y.notna()
    X = X.loc[valid].reset_index(drop=True)
    y = y.loc[valid].to_numpy(dtype=float)

    imputer = SimpleImputer(strategy="median")
    scaler = StandardScaler()
    X_imp = imputer.fit_transform(X)
    X_std = scaler.fit_transform(X_imp)
    X_design = sm.add_constant(X_std, has_constant="add")
    fit = sm.OLS(y, X_design).fit(cov_type="HC3")
    conf = fit.conf_int(alpha=0.05)

    return pd.DataFrame(
        {
            "feature_key": feature_cols,
            "coef": fit.params[1:].astype(float),
            "ci_low": conf[1:, 0].astype(float),
            "ci_high": conf[1:, 1].astype(float),
            "p_value": fit.pvalues[1:].astype(float),
            "n": len(y),
        }
    )


def build_rows(df: pd.DataFrame, *, panel: str, feature_cols: list[str]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for model in MODELS:
        part = df.loc[df["model"] == model].copy()
        coef_df = fit_standardized_ols_hc3(part, feature_cols)
        for row in coef_df.itertuples(index=False):
            rows.append(
                {
                    "panel": panel,
                    "model": model,
                    "feature_key": row.feature_key,
                    "feature_label": fig7_module.FEATURE_LABELS[row.feature_key],
                    "coef": float(row.coef),
                    "ci_low": float(row.ci_low),
                    "ci_high": float(row.ci_high),
                    "p_value": float(row.p_value),
                    "n": int(row.n),
                }
            )
    return pd.DataFrame(rows)


def ordered_features_from_individual(df: pd.DataFrame) -> list[str]:
    ordered = (
        df.groupby("feature_label", as_index=False)
        .agg(mean_coef=("coef", "mean"))
        .sort_values("mean_coef", ascending=False)
    )
    features = ordered["feature_label"].tolist()
    if "Number of Papers" in features:
        features = [f for f in features if f != "Number of Papers"]
    return features + ["Number of Papers"]


def draw_panel(ax: plt.Axes, df: pd.DataFrame, features: list[str], title: str, *, show_ylabels: bool) -> None:
    base_y = np.arange(len(features))[::-1].astype(float) * 1.35
    y_map = dict(zip(features, base_y))
    offsets = np.linspace(0.28, -0.28, len(MODELS))

    xvals = df[["coef", "ci_low", "ci_high"]].to_numpy(dtype=float)
    xabs = float(np.nanmax(np.abs(xvals)))
    xlim = max(0.012, xabs * 1.10)

    for y in base_y:
        ax.axhline(y, color="#f1f1f1", lw=0.8, zorder=0)
    ax.axvline(0.0, color="black", lw=1.0, ls=(0, (1.2, 2.2)), zorder=1)

    for offset, model in zip(offsets, MODELS):
        part = df.loc[df["model"] == model].copy()
        ys = [y_map[label] + offset for label in part["feature_label"]]
        ax.errorbar(
            part["coef"],
            ys,
            xerr=[part["coef"] - part["ci_low"], part["ci_high"] - part["coef"]],
            fmt="o",
            ms=4.8,
            lw=0,
            elinewidth=1.15,
            capsize=2.2,
            color=MODEL_COLORS[model],
            ecolor=MODEL_COLORS[model],
            alpha=0.98,
            zorder=3,
        )

    ax.set_title(title, fontsize=12.5, pad=8)
    ax.set_xlim(-xlim, xlim)
    ax.set_yticks(base_y)
    if show_ylabels:
        ax.set_yticklabels(features, fontsize=10)
    else:
        ax.tick_params(axis="y", labelleft=False)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="x", color="#e5e5e5", lw=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#d0d0d0")
    ax.xaxis.set_major_locator(MaxNLocator(nbins=5))
    ax.xaxis.set_major_formatter(FormatStrFormatter("%.2f"))
    ax.tick_params(axis="x", labelsize=9)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    individual = build_rows(
        build_individual_df().loc[lambda df: df["model"].isin(MODELS)].copy(),
        panel="Individual papers",
        feature_cols=fig7_module.PAPER_FEATURES,
    )
    collections = build_rows(
        build_collection_df().loc[lambda df: df["model"].isin(MODELS)].copy(),
        panel="Collections",
        feature_cols=fig7_module.COLLECTION_FEATURES,
    )
    rows = pd.concat([individual, collections], ignore_index=True)
    rows.to_csv(ROWS_CSV, index=False)

    features = ordered_features_from_individual(individual)

    fig, axes = plt.subplots(1, 2, figsize=(11.9, 6.6), sharey=True)
    draw_panel(axes[0], individual, features, "Individual Papers", show_ylabels=True)
    draw_panel(axes[1], collections, features, "Collections", show_ylabels=False)

    handles = [
        Line2D([0], [0], marker="o", linestyle="none", markersize=5.8, color=MODEL_COLORS[model], label=model)
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
    fig.supxlabel("Standardized OLS coefficient (95% HC3 CI)", fontsize=11, y=0.06)
    fig.subplots_adjust(left=0.34, right=0.985, top=0.84, bottom=0.14, wspace=0.12)
    fig.savefig(PNG, dpi=300)
    fig.savefig(PDF)
    plt.close(fig)


if __name__ == "__main__":
    main()
