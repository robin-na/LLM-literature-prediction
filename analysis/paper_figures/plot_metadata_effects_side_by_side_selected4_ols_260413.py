from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2] / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.ticker import FormatStrFormatter, MaxNLocator
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


ROOT = Path(__file__).resolve().parents[2]
ANALYSIS_ROOT = ROOT / "analysis"
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

import plot_figure7_metadata_effect_robustness as fig7_module
from paper_figures.plot_collection_linear_metadata_effect_260409 import build_collection_df


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"

PAPER_METRICS_CSV = RESULTS_DIR / "paper_repeat_correlation_metrics.csv"
ROWS_CSV = RESULTS_DIR / "figure7_8_metadata_effect_side_by_side_selected4_ols_rows.csv"
OUT_PNG = PLOTS_DIR / "figure7_8_metadata_effect_side_by_side_selected4_ols.png"
OUT_PDF = PLOTS_DIR / "figure7_8_metadata_effect_side_by_side_selected4_ols.pdf"

MODELS = ["Claude Sonnet 4.6", "GPT-5.1", "GPT-4.1", "Gemini 2.5 Pro"]
MODEL_COLORS = {
    "Claude Sonnet 4.6": "#9c755f",
    "GPT-5.1": "#d95f02",
    "GPT-4.1": "#2b8cbe",
    "Gemini 2.5 Pro": "#17becf",
}
N_BOOT = 400
RNG = np.random.default_rng(42)


def build_individual_df() -> pd.DataFrame:
    current_df = fig7_module.load_paper_df().drop(columns=["delta_correlation", "correlation"])
    base_feature_df = (
        current_df.loc[current_df["model"] == "GPT-4.1"]
        .drop(columns=["model"])
        .drop_duplicates("source_id", keep="first")
    )
    metrics = pd.read_csv(PAPER_METRICS_CSV)
    return metrics.loc[:, ["model", "source_id", "correlation", "delta_correlation"]].merge(
        base_feature_df,
        on="source_id",
        how="left",
        validate="many_to_one",
    )


def fit_ols_bootstrap(df: pd.DataFrame, feature_cols: list[str], *, y_col: str = "correlation") -> pd.DataFrame:
    part = df[feature_cols + [y_col]].copy()
    y = pd.to_numeric(part[y_col], errors="coerce")
    X = part[feature_cols].apply(pd.to_numeric, errors="coerce")
    valid = y.notna()
    X = X.loc[valid].reset_index(drop=True)
    y = y.loc[valid].to_numpy(dtype=float)
    n = len(y)

    pipe = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("model", LinearRegression()),
        ]
    )
    pipe.fit(X, y)
    point = pipe.named_steps["model"].coef_.astype(float)

    boot = np.empty((N_BOOT, len(feature_cols)), dtype=float)
    for b in range(N_BOOT):
        idx = RNG.integers(0, n, size=n)
        X_b = X.iloc[idx].reset_index(drop=True)
        y_b = y[idx]
        pipe.fit(X_b, y_b)
        boot[b] = pipe.named_steps["model"].coef_.astype(float)

    low = np.percentile(boot, 2.5, axis=0)
    high = np.percentile(boot, 97.5, axis=0)
    return pd.DataFrame(
        {
            "feature_key": feature_cols,
            "coef": point,
            "ci_low": low,
            "ci_high": high,
            "n": n,
        }
    )


def build_rows(df: pd.DataFrame, *, panel: str, feature_cols: list[str]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for model in MODELS:
        part = df.loc[df["model"] == model].copy()
        coef_df = fit_ols_bootstrap(part, feature_cols)
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


def draw_panel(
    ax: plt.Axes,
    df: pd.DataFrame,
    features: list[str],
    title: str,
    *,
    show_ylabels: bool,
) -> None:
    base_y = np.arange(len(features))[::-1].astype(float) * 1.22
    y_map = dict(zip(features, base_y))
    offsets = np.linspace(0.20, -0.20, len(MODELS))

    xabs = float(np.nanmax(np.abs(df[["coef", "ci_low", "ci_high"]].to_numpy(dtype=float))))
    xlim = max(0.01, xabs * 1.18)

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
            elinewidth=1.12,
            capsize=2.4,
            color=MODEL_COLORS[model],
            ecolor=MODEL_COLORS[model],
            alpha=0.96,
            zorder=3,
        )

    ax.set_title(title, fontsize=13, pad=8)
    ax.set_yticks(base_y)
    if show_ylabels:
        ax.set_yticklabels(features)
    else:
        ax.tick_params(axis="y", labelleft=False)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="x", color="#e6e6e6", lw=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#cfcfcf")
    ax.set_xlim(-xlim, xlim)
    ax.xaxis.set_major_locator(MaxNLocator(nbins=5))
    ax.xaxis.set_major_formatter(FormatStrFormatter("%.2f"))
    ax.tick_params(axis="x", labelsize=9.5, rotation=0, pad=2)
    ax.set_xlabel("")


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    individual = build_rows(
        build_individual_df().loc[lambda df: df["model"].isin(MODELS)].copy(),
        panel="Individual papers",
        feature_cols=fig7_module.PAPER_FEATURES,
    )
    collection = build_rows(
        build_collection_df().loc[lambda df: df["model"].isin(MODELS)].copy(),
        panel="Collections",
        feature_cols=fig7_module.COLLECTION_FEATURES,
    )
    rows = pd.concat([individual, collection], ignore_index=True)
    rows.to_csv(ROWS_CSV, index=False)

    features = ordered_features_from_individual(individual)

    fig, axes = plt.subplots(1, 2, figsize=(12.9, 6.7), sharey=True)
    draw_panel(axes[0], individual, features, "Individual Papers", show_ylabels=True)
    draw_panel(axes[1], collection, features, "Collections", show_ylabels=False)

    handles = [
        Line2D([0], [0], marker="o", linestyle="none", markersize=6, color=MODEL_COLORS[model], label=model)
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
    )
    fig.supxlabel("Coefficient on correlation gain", fontsize=11, y=0.06)
    fig.subplots_adjust(left=0.37, right=0.985, top=0.84, bottom=0.14, wspace=0.20)
    fig.savefig(OUT_PNG, dpi=300)
    fig.savefig(OUT_PDF)
    plt.close(fig)


if __name__ == "__main__":
    main()
