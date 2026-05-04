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
from matplotlib.ticker import FormatStrFormatter, MaxNLocator, PercentFormatter
from sklearn.impute import SimpleImputer
from sklearn.linear_model import ElasticNetCV
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

import plot_figure7_metadata_effect_robustness as fig7_module
from paper_figures.plot_figure2_main_text_260415 import MODEL_COLORS
from paper_figures.plot_figure3_metadata_coefficients_260415 import (
    DISPLAY_FEATURE_LABELS,
    FEATURE_GROUPS,
    build_individual_df,
)


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260427"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260427"

OUT_STEM = "figure4_metadata_coefficients"
FIG_PNG = PLOTS_DIR / f"{OUT_STEM}.png"
ROWS_CSV = RESULTS_DIR / f"{OUT_STEM}_rows.csv"
COEF_ROWS_CSV = RESULTS_DIR / f"{OUT_STEM}_elastic_net_rows.csv"
PERM_ROWS_CSV = RESULTS_DIR / f"{OUT_STEM}_elastic_net_permutation_rows.csv"
DOC_MD = RESULTS_DIR / f"{OUT_STEM}_documentation.md"

MODELS = ["Claude Sonnet 4.6", "GPT-4.1", "Gemini 2.5 Pro"]
MODEL_DISPLAY = {
    "Claude Sonnet 4.6": "Claude Sonnet 4.6",
    "GPT-4.1": "GPT-4.1",
    "Gemini 2.5 Pro": "Gemini 2.5 Pro",
}

N_BOOT = 400
N_PERM_REPEATS = 100
BOOTSTRAP_SEED = 20260427


def feature_label(feature_key: str) -> str:
    raw = fig7_module.FEATURE_LABELS[feature_key]
    label = DISPLAY_FEATURE_LABELS.get(raw, raw)
    return normalize_feature_label(label)


def normalize_feature_label(label: str) -> str:
    if label == "Empirical papers":
        return "Empirical"
    return label


def feature_group(label: str) -> str:
    for group, labels in FEATURE_GROUPS:
        if label in [normalize_feature_label(v) for v in labels]:
            return group
    return "Other"


def grouped_feature_layout(rows: pd.DataFrame) -> tuple[list[str], dict[str, float], list[dict[str, object]], list[float], list[str], list[bool]]:
    available = set(rows["feature_label"].dropna().unique())
    features: list[str] = []
    group_spans: list[dict[str, object]] = []
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
        present = [normalize_feature_label(feature) for feature in group_features if normalize_feature_label(feature) in available]
        if not present:
            continue

        group_positions: list[float] = []
        for feature in reversed(present):
            y_map[feature] = current_y
            group_positions.append(current_y)
            features.append(feature)
            tick_positions.append(current_y)
            tick_labels.append(f"  {feature}")
            tick_is_header.append(False)
            current_y += row_step

        header_y = current_y
        tick_positions.append(header_y)
        tick_labels.append(group_name.upper())
        tick_is_header.append(True)
        group_spans.append(
            {
                "name": group_name,
                "y_min": min(group_positions) - 0.42,
                "y_max": header_y + 0.42,
            }
        )
        current_y += row_step + group_gap

    features = list(reversed(features))
    group_spans = list(reversed(group_spans))
    tick_positions = list(reversed(tick_positions))
    tick_labels = list(reversed(tick_labels))
    tick_is_header = list(reversed(tick_is_header))
    return features, y_map, group_spans, tick_positions, tick_labels, tick_is_header


def build_enet_estimator() -> Pipeline:
    return Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            (
                "model",
                ElasticNetCV(
                    l1_ratio=[0.05, 0.2, 0.5, 0.8, 0.95, 1.0],
                    alphas=np.logspace(-4, 2, 25),
                    max_iter=20000,
                    cv=5,
                    random_state=42,
                ),
            ),
        ]
    )


def fit_elastic_net_bootstrap(df: pd.DataFrame, feature_cols: list[str], *, y_col: str = "correlation", seed_offset: int = 0) -> pd.DataFrame:
    part = df[feature_cols + [y_col]].copy()
    y = pd.to_numeric(part[y_col], errors="coerce")
    X = part[feature_cols].apply(pd.to_numeric, errors="coerce")
    valid = y.notna()
    X = X.loc[valid].reset_index(drop=True)
    y = y.loc[valid].to_numpy(dtype=float)
    n = len(y)

    pipe = build_enet_estimator()
    pipe.fit(X, y)
    point = pipe.named_steps["model"].coef_.astype(float)

    rng = np.random.default_rng(BOOTSTRAP_SEED + seed_offset)
    boot = np.empty((N_BOOT, len(feature_cols)), dtype=float)
    for b in range(N_BOOT):
        idx = rng.integers(0, n, size=n)
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


def build_coefficient_rows(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for idx, model in enumerate(MODELS):
        part = df.loc[df["model"] == model].copy()
        coef_df = fit_elastic_net_bootstrap(
            part,
            fig7_module.PAPER_FEATURES,
            seed_offset=1000 + idx * 100,
        )
        for row in coef_df.itertuples(index=False):
            rows.append(
                {
                    "model": model,
                    "model_display": MODEL_DISPLAY[model],
                    "feature_key": row.feature_key,
                    "feature_label": feature_label(row.feature_key),
                    "feature_group": feature_group(feature_label(row.feature_key)),
                    "coef": float(row.coef),
                    "ci_low": float(row.ci_low),
                    "ci_high": float(row.ci_high),
                    "n": int(row.n),
                    "panel_key": "elastic_net_coefficients",
                    "panel_display": "Elastic net coefficients",
                }
            )
    return pd.DataFrame(rows)


def build_permutation_rows(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for model_idx, model_name in enumerate(MODELS):
        part = df.loc[df["model"] == model_name].dropna(subset=["source_id"]).copy()
        X = part[fig7_module.PAPER_FEATURES].apply(pd.to_numeric, errors="coerce").reset_index(drop=True)
        y = pd.to_numeric(part["correlation"], errors="coerce").to_numpy(dtype=float)
        groups = part["source_id"].astype(str).to_numpy()
        valid = np.isfinite(y)
        X = X.loc[valid].reset_index(drop=True)
        y = y[valid]
        groups = groups[valid]

        rng = np.random.default_rng(BOOTSTRAP_SEED + 5000 + model_idx * 1000)
        splitter = GroupKFold(n_splits=5)
        fold_rows: list[dict[str, object]] = []

        for fold, (train_idx, test_idx) in enumerate(splitter.split(X, y, groups), start=1):
            pipe = build_enet_estimator()
            X_train = X.iloc[train_idx].reset_index(drop=True)
            X_test = X.iloc[test_idx].reset_index(drop=True)
            y_train = y[train_idx]
            y_test = y[test_idx]
            pipe.fit(X_train, y_train)
            baseline_pred = pipe.predict(X_test)
            baseline_rmse = float(np.sqrt(mean_squared_error(y_test, baseline_pred)))

            for feature in fig7_module.PAPER_FEATURES:
                deltas = np.empty(N_PERM_REPEATS, dtype=float)
                for repeat in range(N_PERM_REPEATS):
                    permuted = X_test.copy()
                    permuted[feature] = rng.permutation(permuted[feature].to_numpy())
                    pred = pipe.predict(permuted)
                    permuted_rmse = float(np.sqrt(mean_squared_error(y_test, pred)))
                    deltas[repeat] = 100.0 * (permuted_rmse - baseline_rmse) / baseline_rmse
                fold_rows.append(
                    {
                        "estimator": "elastic_net",
                        "estimator_label": "Elastic net",
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

        fold_df = pd.DataFrame(fold_rows)
        summary = (
            fold_df.groupby(
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
        summary["panel_key"] = "elastic_net_permutation_importance"
        summary["panel_display"] = "Elastic net permutation importance"
        rows.append(summary)

    return pd.concat(rows, ignore_index=True)


def draw_coefficient_panel(
    ax: plt.Axes,
    rows: pd.DataFrame,
    *,
    y_map: dict[str, float],
    group_spans: list[dict[str, object]],
    tick_positions: list[float],
    tick_labels: list[str],
    tick_is_header: list[bool],
) -> None:
    base_y = np.array([y_map[feature] for feature in rows["feature_label"].drop_duplicates()], dtype=float)
    xvals = rows[["coef", "ci_low", "ci_high"]].to_numpy(dtype=float)
    xabs = float(np.nanmax(np.abs(xvals)))
    xlim = max(0.012, xabs * 1.16)
    offsets = np.linspace(0.20, -0.20, len(MODELS))

    for i, span in enumerate(group_spans):
        if i % 2 == 0:
            ax.axhspan(span["y_min"], span["y_max"], color="#f8fafc", zorder=0)
    for y in base_y:
        ax.axhline(y, color="#e8edf3", lw=0.75, zorder=1)
    ax.axvline(0.0, color="#111827", lw=1.0, ls=(0, (1.2, 2.2)), zorder=1)

    for offset, model in zip(offsets, MODELS):
        part = rows.loc[rows["model"] == model].copy()
        ys = [y_map[label] + offset for label in part["feature_label"]]
        ax.errorbar(
            part["coef"],
            ys,
            xerr=[part["coef"] - part["ci_low"], part["ci_high"] - part["coef"]],
            fmt="o",
            ms=5.2,
            lw=0,
            elinewidth=1.15,
            capsize=2.2,
            color=MODEL_COLORS[model],
            ecolor=MODEL_COLORS[model],
            alpha=0.98,
            zorder=3,
        )

    ax.set_xlim(-xlim, xlim)
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
    ax.tick_params(axis="x", labelsize=9.0)
    ax.set_ylim(min(tick_positions) - 0.62, max(tick_positions) + 0.62)
    ax.grid(axis="x", color="#e5e7eb", lw=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#cfd4dc")
    ax.xaxis.set_major_locator(MaxNLocator(nbins=5))
    ax.xaxis.set_major_formatter(FormatStrFormatter("%.2f"))
    ax.set_xlabel(r"Standardized Coefficient on $r$", fontsize=10.5, labelpad=7)


def draw_permutation_panel(
    ax: plt.Axes,
    rows: pd.DataFrame,
    *,
    y_map: dict[str, float],
    group_spans: list[dict[str, object]],
    tick_positions: list[float],
) -> None:
    base_y = np.array([y_map[feature] for feature in rows["feature_label"].drop_duplicates()], dtype=float)
    offsets = np.linspace(0.22, -0.22, len(MODELS))
    height = 0.16
    xmax = max(0.5, float(rows["mean_importance"].max() + rows["se_importance"].fillna(0).max()) * 1.18)
    xmin = min(0.0, float(rows["mean_importance"].min() - rows["se_importance"].fillna(0).max()) * 1.20)
    if xmin > -0.15:
        xmin = -0.15

    for i, span in enumerate(group_spans):
        if i % 2 == 0:
            ax.axhspan(span["y_min"], span["y_max"], color="#f8fafc", zorder=0)
    for y in base_y:
        ax.axhline(y, color="#e8edf3", lw=0.75, zorder=1)
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
            alpha=0.84,
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
    ax.tick_params(axis="y", labelleft=False, length=0)
    ax.tick_params(axis="x", labelsize=9.0)
    ax.set_ylim(min(tick_positions) - 0.62, max(tick_positions) + 0.62)
    ax.set_xlim(xmin, xmax)
    ax.xaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=1))
    ax.grid(axis="x", color="#e5e7eb", lw=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#cfd4dc")
    ax.set_xlabel("Permutation Importance\n(% increase in prediction error)", fontsize=10.5, labelpad=7)


def write_documentation(coef_rows: pd.DataFrame, perm_rows: pd.DataFrame) -> None:
    n_values = sorted(int(v) for v in perm_rows["n_total"].unique())
    doc = f"""# {OUT_STEM}

## Purpose
Figure 4 for `main_text_260427`. This is a paper-only metadata figure that pairs elastic-net coefficients with elastic-net predictive feature importance for augmented performance.

## Inheritance
- Semantic figure ID: `metadata_coefficients`
- Adapted from `main_text_260415` Figure 3 into the `main_text_260427` Figure 4 slot
- Parent coefficient figure: `plots/paper/main_text_260415/figure3_metadata_coefficients.png`
- Parent permutation companion: `plots/paper/main_text_260415/figure3_individual_permutation_importance_ridge.png`

## Output files
- Plot PNG: `{FIG_PNG.relative_to(ROOT)}`
- Canonical combined rows: `{ROWS_CSV.relative_to(ROOT)}`
- Elastic-net coefficient rows: `{COEF_ROWS_CSV.relative_to(ROOT)}`
- Elastic-net permutation rows: `{PERM_ROWS_CSV.relative_to(ROOT)}`
- Documentation: `{DOC_MD.relative_to(ROOT)}`
- Script: `{Path(__file__).resolve().relative_to(ROOT)}`

## Input files
- Individual-paper correlations: `results/paper/main_text_figures_260409/paper_repeat_correlation_metrics.csv`
- Individual-paper metadata catalog: `{fig7_module.PAPER_META_CSV.relative_to(ROOT)}`

## Construction
1. Restrict to the three displayed models: `Claude Sonnet 4.6`, `GPT-4.1`, and `Gemini 2.5 Pro`.
2. Build the individual-paper dataset by merging raw augmented correlation performance with paper metadata features.
3. Left panel:
   - fit a separate multivariable elastic-net model for each LLM
   - target = raw augmented performance, `Corr(y_true, y_pred)`
   - predictors = empirical-paper indicator, log citation count, log journal impact factor, publication year, and journal-discipline indicators
   - median-impute and standardize predictors before fitting
   - estimator = elastic net with `ElasticNetCV`
   - plot standardized coefficients with percentile bootstrap 95% intervals across paper rows
4. Right panel:
   - use the same individual-paper features and target
   - estimator = elastic net with `ElasticNetCV`
   - grouped 5-fold cross-validation by paper ID
   - within each held-out fold, permute one feature at a time `{N_PERM_REPEATS}` times
   - importance = percent increase in held-out prediction error (RMSE) relative to the unpermuted held-out prediction
   - plot mean importance with standard error across folds

## Interpretation
- Left panel: a positive coefficient means higher augmented correlation under the penalized elastic-net fit; coefficients may shrink to exactly zero.
- Right panel: a larger positive value means held-out prediction error rises more when that feature is broken, so the predictive model relies more on it.
- Both panels use the same elastic-net model family, so the coefficient and importance views are aligned to the same predictive estimator.

## Notes
- This `260427` figure intentionally drops the collection panel from the `260415` parent.
- The coefficient and permutation panels answer different questions and should not be numerically compared on the same x-scale.
- Individual-paper sample sizes are `{', '.join(f'{n:,}' for n in n_values)}` depending on model availability.
- The coefficient intervals are bootstrap intervals, not HC3 regression confidence intervals.

## Elastic-net coefficient rows
{coef_rows.to_markdown(index=False)}

## Elastic-net permutation-importance rows
{perm_rows.to_markdown(index=False)}
"""
    DOC_MD.write_text(doc, encoding="utf-8")


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    individual_df = build_individual_df().loc[lambda df: df["model"].isin(MODELS)].copy()
    coef_rows = build_coefficient_rows(individual_df)
    perm_rows = build_permutation_rows(individual_df)

    coef_rows.to_csv(COEF_ROWS_CSV, index=False)
    perm_rows.to_csv(PERM_ROWS_CSV, index=False)

    combined_rows = pd.concat(
        [
            coef_rows.assign(metric="coef", estimate=coef_rows["coef"], lower=coef_rows["ci_low"], upper=coef_rows["ci_high"]),
            perm_rows.assign(
                metric="importance_pct_rmse_increase",
                estimate=perm_rows["mean_importance"],
                lower=perm_rows["mean_importance"] - perm_rows["se_importance"],
                upper=perm_rows["mean_importance"] + perm_rows["se_importance"],
            ),
        ],
        ignore_index=True,
        sort=False,
    )
    combined_rows.to_csv(ROWS_CSV, index=False)

    features, y_map, group_spans, tick_positions, tick_labels, tick_is_header = grouped_feature_layout(coef_rows)
    fig, axes = plt.subplots(1, 2, figsize=(11.3, 6.6), sharey=True)
    draw_coefficient_panel(
        axes[0],
        coef_rows.copy(),
        y_map=y_map,
        group_spans=group_spans,
        tick_positions=tick_positions,
        tick_labels=tick_labels,
        tick_is_header=tick_is_header,
    )
    draw_permutation_panel(
        axes[1],
        perm_rows.copy(),
        y_map=y_map,
        group_spans=group_spans,
        tick_positions=tick_positions,
    )

    axes[0].text(
        0.01,
        0.99,
        "A",
        transform=axes[0].transAxes,
        fontsize=17,
        fontweight="bold",
        ha="left",
        va="top",
        color="#111827",
    )
    axes[1].text(
        0.01,
        0.99,
        "B",
        transform=axes[1].transAxes,
        fontsize=17,
        fontweight="bold",
        ha="left",
        va="top",
        color="#111827",
    )

    handles = [
        Line2D(
            [0],
            [0],
            marker="o",
            linestyle="none",
            markersize=5.8,
            color=MODEL_COLORS[model],
            label=MODEL_DISPLAY[model],
        )
        for model in MODELS
    ]
    axes[0].legend(
        handles=handles,
        loc="upper right",
        bbox_to_anchor=(0.99, 0.995),
        frameon=False,
        fontsize=9.0,
        handletextpad=0.35,
        borderaxespad=0.0,
        labelspacing=0.45,
    )
    fig.subplots_adjust(left=0.225, right=0.985, top=0.915, bottom=0.10, wspace=0.12)
    fig.savefig(FIG_PNG, dpi=300, bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)

    write_documentation(coef_rows, perm_rows)


if __name__ == "__main__":
    main()
