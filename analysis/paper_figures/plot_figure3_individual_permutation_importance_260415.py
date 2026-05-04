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
from matplotlib.lines import Line2D
from matplotlib.ticker import PercentFormatter
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

import plot_figure7_metadata_effect_robustness as fig7_module
from paper_figures.plot_figure2_combined_heterogeneity_agreement_260415 import MODEL_DISPLAY
from paper_figures.plot_figure2_main_text_260415 import MODEL_COLORS, MODELS
from paper_figures.plot_figure3_metadata_coefficients_260415 import (
    DISPLAY_FEATURE_LABELS,
    FEATURE_GROUPS,
    build_individual_df,
)


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260415"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260415"

N_PERM_REPEATS = 100
RNG_SEED = 20260421

ESTIMATORS = {
    "ols": "OLS / linear regression",
    "ridge": "Ridge regression",
}

OUT_PNG = {
    "ols": PLOTS_DIR / "figure3_individual_permutation_importance_ols.png",
    "ridge": PLOTS_DIR / "figure3_individual_permutation_importance_ridge.png",
}
OUT_CSV = {
    "ols": RESULTS_DIR / "figure3_individual_permutation_importance_ols_rows.csv",
    "ridge": RESULTS_DIR / "figure3_individual_permutation_importance_ridge_rows.csv",
}
DOC_MD = RESULTS_DIR / "figure3_individual_permutation_importance_documentation.md"


def build_estimator(estimator_key: str) -> Pipeline:
    if estimator_key == "ols":
        model = LinearRegression()
    elif estimator_key == "ridge":
        model = RidgeCV(alphas=np.logspace(-3, 3, 13))
    else:
        raise ValueError(estimator_key)
    return Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("model", model),
        ]
    )


def feature_label(feature_key: str) -> str:
    raw = fig7_module.FEATURE_LABELS[feature_key]
    return DISPLAY_FEATURE_LABELS.get(raw, raw)


def feature_group(feature_label_: str) -> str:
    for group, labels in FEATURE_GROUPS:
        if feature_label_ in labels:
            return group
    return "Other"


def compute_cv_permutation_importance(
    df: pd.DataFrame,
    *,
    estimator_key: str,
    model_name: str,
    feature_cols: list[str],
    y_col: str = "correlation",
) -> pd.DataFrame:
    part = df.loc[df["model"] == model_name].dropna(subset=["source_id"]).copy()
    X = part[feature_cols].apply(pd.to_numeric, errors="coerce").reset_index(drop=True)
    y = pd.to_numeric(part[y_col], errors="coerce").to_numpy(dtype=float)
    groups = part["source_id"].astype(str).to_numpy()
    valid = np.isfinite(y)
    X = X.loc[valid].reset_index(drop=True)
    y = y[valid]
    groups = groups[valid]

    rng = np.random.default_rng(RNG_SEED + 1009 * MODELS.index(model_name) + (0 if estimator_key == "ols" else 503))
    splitter = GroupKFold(n_splits=5)
    rows: list[dict[str, object]] = []

    for fold, (train_idx, test_idx) in enumerate(splitter.split(X, y, groups), start=1):
        pipe = build_estimator(estimator_key)
        X_train = X.iloc[train_idx].reset_index(drop=True)
        X_test = X.iloc[test_idx].reset_index(drop=True)
        y_train = y[train_idx]
        y_test = y[test_idx]
        pipe.fit(X_train, y_train)
        baseline_pred = pipe.predict(X_test)
        baseline_rmse = float(np.sqrt(mean_squared_error(y_test, baseline_pred)))

        for feature in feature_cols:
            deltas = np.empty(N_PERM_REPEATS, dtype=float)
            for repeat in range(N_PERM_REPEATS):
                permuted = X_test.copy()
                permuted[feature] = rng.permutation(permuted[feature].to_numpy())
                pred = pipe.predict(permuted)
                permuted_rmse = float(np.sqrt(mean_squared_error(y_test, pred)))
                deltas[repeat] = 100.0 * (permuted_rmse - baseline_rmse) / baseline_rmse
            rows.append(
                {
                    "estimator": estimator_key,
                    "estimator_label": ESTIMATORS[estimator_key],
                    "model": model_name,
                    "model_display": MODEL_DISPLAY[model_name],
                    "fold": fold,
                    "feature_key": feature,
                    "feature_label": feature_label(feature),
                    "feature_group": feature_group(feature_label(feature)),
                    "baseline_rmse": baseline_rmse,
                    "importance_pct_rmse_increase": float(np.mean(deltas)),
                    "n_permutation_repeats": N_PERM_REPEATS,
                    "n_test": int(len(test_idx)),
                    "n_total": int(len(y)),
                }
            )

    fold_rows = pd.DataFrame(rows)
    summary = (
        fold_rows.groupby(
            ["estimator", "estimator_label", "model", "model_display", "feature_key", "feature_label", "feature_group"],
            as_index=False,
        )
        .agg(
            mean_importance=("importance_pct_rmse_increase", "mean"),
            sd_importance=("importance_pct_rmse_increase", "std"),
            n_folds=("importance_pct_rmse_increase", "size"),
            n_total=("n_total", "max"),
        )
    )
    summary["se_importance"] = summary["sd_importance"] / np.sqrt(summary["n_folds"])
    return summary


def grouped_feature_layout(rows: pd.DataFrame) -> tuple[list[str], dict[str, float], list[float], list[str], list[bool]]:
    available = set(rows["feature_label"].dropna().unique())
    features: list[str] = []
    y_map: dict[str, float] = {}
    tick_positions: list[float] = []
    tick_labels: list[str] = []
    tick_is_header: list[bool] = []
    current_y = 0.0
    row_step = 1.0
    group_gap = 0.48

    for group_name, group_features in reversed(FEATURE_GROUPS):
        if group_name == "Collection scale":
            continue
        present = [feature for feature in group_features if feature in available]
        if not present:
            continue
        for feature in reversed(present):
            y_map[feature] = current_y
            features.append(feature)
            tick_positions.append(current_y)
            tick_labels.append(f"  {feature}")
            tick_is_header.append(False)
            current_y += row_step
        tick_positions.append(current_y)
        tick_labels.append(group_name.upper())
        tick_is_header.append(True)
        current_y += row_step + group_gap

    features = list(reversed(features))
    tick_positions = list(reversed(tick_positions))
    tick_labels = list(reversed(tick_labels))
    tick_is_header = list(reversed(tick_is_header))
    return features, y_map, tick_positions, tick_labels, tick_is_header


def draw_figure(rows: pd.DataFrame, estimator_key: str) -> None:
    features, y_map, tick_positions, tick_labels, tick_is_header = grouped_feature_layout(rows)
    base_y = np.array([y_map[feature] for feature in features], dtype=float)
    offsets = np.linspace(0.22, -0.22, len(MODELS))
    height = 0.16

    xmax = max(0.5, float(rows["mean_importance"].max() + rows["se_importance"].fillna(0).max()) * 1.22)
    xmin = min(0.0, float(rows["mean_importance"].min() - rows["se_importance"].fillna(0).max()) * 1.20)
    if xmin > -0.15:
        xmin = -0.15

    fig, ax = plt.subplots(1, 1, figsize=(8.7, 6.55))
    for y in base_y:
        ax.axhline(y, color="#e8edf3", lw=0.75, zorder=0)
    ax.axvline(0.0, color="#111827", lw=1.0, ls=(0, (1.2, 2.2)), zorder=1)

    for offset, model in zip(offsets, MODELS):
        part = rows.loc[rows["model"] == model].copy()
        part["_y"] = part["feature_label"].map(y_map) + offset
        ax.barh(
            part["_y"],
            part["mean_importance"],
            height=height,
            color=MODEL_COLORS[model],
            edgecolor="none",
            alpha=0.82,
            zorder=2,
        )
        ax.errorbar(
            part["mean_importance"],
            part["_y"],
            xerr=part["se_importance"].fillna(0.0),
            fmt="none",
            ecolor="#4b5563",
            elinewidth=0.9,
            capsize=2.0,
            alpha=0.55,
            zorder=3,
        )

    ax.set_yticks(tick_positions)
    ax.set_yticklabels(tick_labels, fontsize=9.6)
    for tick, is_header in zip(ax.get_yticklabels(), tick_is_header):
        if is_header:
            tick.set_fontsize(8.1)
            tick.set_fontweight("bold")
            tick.set_color("#64748b")
        else:
            tick.set_color("#111827")
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", labelsize=9.1)
    ax.set_ylim(min(tick_positions) - 0.62, max(tick_positions) + 0.62)
    ax.set_xlim(xmin, xmax)
    ax.xaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=1))
    ax.grid(axis="x", color="#e5e7eb", lw=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#cfd4dc")
    ax.set_title(f"Individual papers: permutation importance ({ESTIMATORS[estimator_key]})", fontsize=12.7, pad=10)
    ax.set_xlabel("Increase in held-out RMSE when permuted", fontsize=10.8, labelpad=10)

    handles = [
        Line2D([0], [0], marker="s", linestyle="none", markersize=7.5, color=MODEL_COLORS[model], label=MODEL_DISPLAY[model])
        for model in MODELS
    ]
    fig.legend(
        handles=handles,
        loc="upper center",
        ncol=3,
        frameon=False,
        bbox_to_anchor=(0.57, 0.965),
        columnspacing=1.25,
        handletextpad=0.42,
        fontsize=9.2,
    )
    fig.subplots_adjust(left=0.255, right=0.985, top=0.855, bottom=0.125)
    fig.savefig(OUT_PNG[estimator_key], dpi=300)
    plt.close(fig)


def write_documentation(all_rows: dict[str, pd.DataFrame]) -> None:
    n_values = sorted({int(v) for rows in all_rows.values() for v in rows["n_total"].unique()})
    doc = f"""# Figure 3 Individual-Paper Permutation Importance

Outputs:
- OLS plot: `{OUT_PNG["ols"]}`
- Ridge plot: `{OUT_PNG["ridge"]}`
- OLS rows: `{OUT_CSV["ols"]}`
- Ridge rows: `{OUT_CSV["ridge"]}`

Purpose:
- Exploratory companion to Figure 3 showing which individual-paper metadata variables matter most for predicting augmented performance.
- Target is raw augmented performance, `Corr(y_true, y_pred)`, matching Figure 3.

Construction:
- LLMs: `Claude Sonnet 4.6`, `GPT-4.1`, and `Gemini 2.5 Pro`.
- Rows: individual papers only (`n = {', '.join(f'{n:,}' for n in n_values)}` depending on model availability).
- Features: same individual-paper metadata as Figure 3: empirical-paper indicator, log citation count, log journal impact factor, publication year, and journal-discipline indicators.
- Preprocessing: median imputation and standardization inside each training fold.
- Estimators:
  - OLS / linear regression: same unregularized linear estimator used for Figure 3 predictive-performance documentation.
  - Ridge regression: `RidgeCV` over `np.logspace(-3, 3, 13)`, included because ridge was the best predictive model for individual papers in the Figure 3 benchmark table.
- Importance: 5-fold grouped cross-validation by paper ID. Within each held-out fold, each feature is permuted {N_PERM_REPEATS} times and importance is the percent increase in held-out RMSE relative to the unpermuted held-out prediction.
- Error bars: standard error across the 5 held-out folds.

Interpretation:
- Larger positive values mean predictions get worse when that feature is broken, so the model relies more on that feature for held-out prediction.
- Values near zero mean little held-out predictive contribution.
- Negative values can occur when a feature adds noise in held-out data.
- Because predictors are correlated, permutation importance is a predictive-utility measure, not a causal or uniquely attributable effect size.
"""
    DOC_MD.write_text(doc, encoding="utf-8")


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    df = build_individual_df().loc[lambda frame: frame["model"].isin(MODELS)].copy()

    all_rows: dict[str, pd.DataFrame] = {}
    for estimator_key in ESTIMATORS:
        rows = pd.concat(
            [
                compute_cv_permutation_importance(
                    df,
                    estimator_key=estimator_key,
                    model_name=model,
                    feature_cols=fig7_module.PAPER_FEATURES,
                )
                for model in MODELS
            ],
            ignore_index=True,
        )
        rows.to_csv(OUT_CSV[estimator_key], index=False)
        draw_figure(rows, estimator_key)
        all_rows[estimator_key] = rows

    write_documentation(all_rows)


if __name__ == "__main__":
    main()
