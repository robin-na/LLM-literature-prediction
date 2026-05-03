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
import statsmodels.api as sm
from matplotlib.lines import Line2D
from matplotlib.ticker import FormatStrFormatter, MaxNLocator
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import Pipeline

import plot_figure7_metadata_effect_robustness as fig7_module
from paper_figures.plot_collection_linear_metadata_effect_260409 import build_collection_df
from paper_figures.plot_figure2_combined_heterogeneity_agreement_260415 import MODEL_DISPLAY
from paper_figures.plot_figure2_main_text_260415 import MODEL_COLORS, MODELS, compute_everything_collection_rows


SOURCE_RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260415"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260415"

PAPER_METRICS_CSV = SOURCE_RESULTS_DIR / "paper_repeat_correlation_metrics.csv"
FIG_PNG = PLOTS_DIR / "figure3_metadata_coefficients.png"
ROWS_CSV = RESULTS_DIR / "figure3_metadata_coefficients_rows.csv"
PREDICTIVE_PERFORMANCE_CSV = RESULTS_DIR / "figure3_ols_predictive_performance.csv"
DOC_MD = RESULTS_DIR / "figure3_metadata_coefficients_documentation.md"

FEATURE_GROUPS = [
    ("Study type", ["Empirical papers"]),
    ("Prestige / visibility", ["Citation", "Journal Impact Factor"]),
    ("Publication timing", ["Publication Year"]),
    (
        "Journal discipline",
        [
            "Biology",
            "Psychology",
            "Multidisciplinary",
            "Economics",
            "Math/Physics",
        ],
    ),
    ("Collection scale", ["Number of Papers"]),
]

DISPLAY_FEATURE_LABELS = {
    "Biology Journals": "Biology",
    "Psychology Journals": "Psychology",
    "Multidisciplinary Journals": "Multidisciplinary",
    "Economics Journals": "Economics",
    "Math/Physics Journals": "Math/Physics",
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


def build_all_papers_collection_feature_row() -> dict[str, float]:
    catalog = pd.read_csv(fig7_module.PAPER_META_CSV).copy()
    catalog["custom_id"] = catalog["custom_id"].astype(str)
    catalog = catalog.drop_duplicates("custom_id", keep="first")
    catalog["journal_impact"] = np.log1p(pd.to_numeric(catalog["jif_value"], errors="coerce"))
    catalog["citation"] = np.log1p(pd.to_numeric(catalog["Times Cited, All Databases"], errors="coerce").clip(lower=0))
    catalog["empirical_share"] = catalog["paper_type_primary"].map({"theory": 0.0, "empirical": 1.0})
    catalog["recent"] = pd.to_numeric(catalog["Publication Year"], errors="coerce")
    catalog = pd.concat([catalog, fig7_module._discipline_indicators(catalog["discipline_coarse"])], axis=1)
    values = {
        feature: float(catalog[feature].mean())
        for feature in fig7_module.PAPER_FEATURES
    }
    values["collection_size"] = float(np.log(len(catalog)))
    return values


def build_collection_df_with_everything() -> pd.DataFrame:
    base = build_collection_df().copy()
    everything_metrics = compute_everything_collection_rows()
    feature_values = build_all_papers_collection_feature_row()
    rows: list[dict[str, object]] = []
    for row in everything_metrics.itertuples(index=False):
        rows.append(
            {
                "model": row.model,
                "variant_id": "broad_all_2011",
                "correlation": float(row.correlation),
                "delta_correlation": np.nan,
                "count": 2011,
                "log_count": feature_values["collection_size"],
                "collection_size": feature_values["collection_size"],
                **feature_values,
            }
        )
    return pd.concat([base, pd.DataFrame(rows)], ignore_index=True, sort=False)


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


def safe_pearson(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    valid = np.isfinite(y_true) & np.isfinite(y_pred)
    if valid.sum() < 2 or np.std(y_true[valid]) == 0 or np.std(y_pred[valid]) == 0:
        return float("nan")
    return float(np.corrcoef(y_true[valid], y_pred[valid])[0, 1])


def evaluate_ols_predictive_performance(
    df: pd.DataFrame,
    *,
    panel: str,
    feature_cols: list[str],
    group_col: str,
    y_col: str = "correlation",
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for model in MODELS:
        part = df.loc[df["model"] == model].dropna(subset=[group_col]).copy()
        y = pd.to_numeric(part[y_col], errors="coerce")
        X = part[feature_cols].apply(pd.to_numeric, errors="coerce")
        valid = y.notna()
        X = X.loc[valid].reset_index(drop=True)
        y_arr = y.loc[valid].to_numpy(dtype=float)
        groups = part.loc[valid, group_col].astype(str).to_numpy()

        pipe = Pipeline(
            [
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler()),
                ("model", LinearRegression()),
            ]
        )
        pipe.fit(X, y_arr)
        in_sample_pred = pipe.predict(X)

        cv_pred = np.empty_like(y_arr, dtype=float)
        fold_r2: list[float] = []
        fold_pearson: list[float] = []
        splitter = GroupKFold(n_splits=5)
        for train_idx, test_idx in splitter.split(X, y_arr, groups):
            pipe.fit(X.iloc[train_idx], y_arr[train_idx])
            pred = pipe.predict(X.iloc[test_idx])
            cv_pred[test_idx] = pred
            fold_r2.append(float(r2_score(y_arr[test_idx], pred)))
            fold_pearson.append(safe_pearson(y_arr[test_idx], pred))

        rows.append(
            {
                "panel": panel,
                "model": model,
                "model_display": MODEL_DISPLAY[model],
                "n_rows": int(len(y_arr)),
                "n_groups": int(len(np.unique(groups))),
                "in_sample_r2": float(r2_score(y_arr, in_sample_pred)),
                "in_sample_pearson_r": safe_pearson(y_arr, in_sample_pred),
                "cv_r2": float(r2_score(y_arr, cv_pred)),
                "cv_pearson_r": safe_pearson(y_arr, cv_pred),
                "mean_fold_r2": float(np.mean(fold_r2)),
                "sd_fold_r2": float(np.std(fold_r2, ddof=1)),
                "mean_fold_pearson_r": float(np.nanmean(fold_pearson)),
                "sd_fold_pearson_r": float(np.nanstd(fold_pearson, ddof=1)),
            }
        )
    return pd.DataFrame(rows)


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
                    "model_display": MODEL_DISPLAY[model],
                    "feature_key": row.feature_key,
                    "feature_label": DISPLAY_FEATURE_LABELS.get(
                        fig7_module.FEATURE_LABELS[row.feature_key],
                        fig7_module.FEATURE_LABELS[row.feature_key],
                    ),
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
        features = [feature for feature in features if feature != "Number of Papers"]
    return features + ["Number of Papers"]


def grouped_feature_layout(
    rows: pd.DataFrame,
) -> tuple[list[str], dict[str, float], list[dict[str, object]], list[float], list[str], list[bool]]:
    available = set(rows["feature_label"].dropna().unique())
    features: list[str] = []
    group_spans: list[dict[str, object]] = []
    y_map: dict[str, float] = {}
    tick_positions: list[float] = []
    tick_labels: list[str] = []
    tick_is_header: list[bool] = []
    current_y = 0.0
    row_step = 1.0
    group_gap = 0.45

    for group_name, group_features in reversed(FEATURE_GROUPS):
        present = [feature for feature in group_features if feature in available]
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
                "y_mid": float(np.mean(group_positions)),
            }
        )
        current_y += row_step + group_gap

    features = list(reversed(features))
    group_spans = list(reversed(group_spans))
    tick_positions = list(reversed(tick_positions))
    tick_labels = list(reversed(tick_labels))
    tick_is_header = list(reversed(tick_is_header))
    return features, y_map, group_spans, tick_positions, tick_labels, tick_is_header


def draw_panel(
    ax: plt.Axes,
    df: pd.DataFrame,
    features: list[str],
    y_map: dict[str, float],
    group_spans: list[dict[str, object]],
    tick_positions: list[float],
    tick_labels: list[str],
    tick_is_header: list[bool],
    title: str,
    *,
    show_ylabels: bool,
    show_not_applicable: bool = False,
) -> None:
    base_y = np.array([y_map[feature] for feature in features], dtype=float)
    offsets = np.linspace(0.20, -0.20, len(MODELS))

    xvals = df[["coef", "ci_low", "ci_high"]].to_numpy(dtype=float)
    xabs = float(np.nanmax(np.abs(xvals)))
    xlim = max(0.012, xabs * 1.14)

    for i, span in enumerate(group_spans):
        if i % 2 == 0:
            ax.axhspan(span["y_min"], span["y_max"], color="#f8fafc", zorder=0)

    for y in base_y:
        ax.axhline(y, color="#e8edf3", lw=0.75, zorder=1)
    ax.axvline(0.0, color="#111827", lw=1.0, ls=(0, (1.2, 2.2)), zorder=1)

    for offset, model in zip(offsets, MODELS):
        part = df.loc[df["model"] == model].copy()
        ys = [y_map[label] + offset for label in part["feature_label"]]
        ax.errorbar(
            part["coef"],
            ys,
            xerr=[part["coef"] - part["ci_low"], part["ci_high"] - part["coef"]],
            fmt="o",
            ms=5.2,
            lw=0,
            elinewidth=1.2,
            capsize=2.3,
            color=MODEL_COLORS[model],
            ecolor=MODEL_COLORS[model],
            alpha=0.98,
            zorder=3,
        )

    if show_not_applicable and "Number of Papers" in y_map:
        ax.text(
            0.0,
            y_map["Number of Papers"],
            "Not applicable",
            ha="center",
            va="center",
            fontsize=8.8,
            fontstyle="italic",
            color="#8b95a1",
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.72, "pad": 1.4},
            zorder=4,
        )

    ax.set_title(title, fontsize=12.5, pad=8)
    ax.set_xlim(-xlim, xlim)
    ax.set_yticks(tick_positions)
    if show_ylabels:
        ax.set_yticklabels(tick_labels, fontsize=9.6)
        for tick, is_header in zip(ax.get_yticklabels(), tick_is_header):
            if is_header:
                tick.set_fontsize(8.1)
                tick.set_fontweight("bold")
                tick.set_color("#64748b")
            else:
                tick.set_color("#111827")
    else:
        ax.tick_params(axis="y", labelleft=False)
    ax.tick_params(axis="y", length=0)
    ax.set_ylim(min(tick_positions) - 0.62, max(tick_positions) + 0.62)
    ax.grid(axis="x", color="#e5e7eb", lw=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#cfd4dc")
    ax.xaxis.set_major_locator(MaxNLocator(nbins=5))
    ax.xaxis.set_major_formatter(FormatStrFormatter("%.2f"))
    ax.tick_params(axis="x", labelsize=9.0)


def draw_figure(rows: pd.DataFrame) -> None:
    features, y_map, group_spans, tick_positions, tick_labels, tick_is_header = grouped_feature_layout(rows)

    fig, axes = plt.subplots(1, 2, figsize=(11.7, 7.45), sharey=True)
    draw_panel(
        axes[0],
        rows.loc[rows["panel"] == "Individual papers"].copy(),
        features,
        y_map,
        group_spans,
        tick_positions,
        tick_labels,
        tick_is_header,
        "Individual papers",
        show_ylabels=True,
        show_not_applicable=True,
    )
    draw_panel(
        axes[1],
        rows.loc[rows["panel"] == "Collections"].copy(),
        features,
        y_map,
        group_spans,
        tick_positions,
        tick_labels,
        tick_is_header,
        "Collections",
        show_ylabels=False,
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
    fig.legend(
        handles=handles,
        loc="upper center",
        ncol=3,
        frameon=False,
        bbox_to_anchor=(0.58, 0.972),
        columnspacing=1.35,
        handletextpad=0.4,
        fontsize=9.3,
    )
    fig.subplots_adjust(left=0.215, right=0.985, top=0.865, bottom=0.125, wspace=0.13)
    plot_left = axes[0].get_position().x0
    plot_right = axes[1].get_position().x1
    fig.text(
        (plot_left + plot_right) / 2,
        0.052,
        r"Standardized regression coefficient for $\mathrm{Corr}(y_{\mathrm{true}}, y_{\mathrm{pred}})$",
        ha="center",
        va="center",
        fontsize=10.8,
    )
    fig.savefig(FIG_PNG, dpi=300)
    plt.close(fig)


def write_documentation(rows: pd.DataFrame) -> None:
    n_ind = int(rows.loc[rows["panel"] == "Individual papers", "n"].max())
    n_col = int(rows.loc[rows["panel"] == "Collections", "n"].max())
    doc = f"""# Figure 3: Metadata Coefficient Plot

Output:
- Figure: `{FIG_PNG}`
- Rows: `{ROWS_CSV}`
- OLS predictive performance: `{PREDICTIVE_PERFORMANCE_CSV}`

Purpose:
- Shows which paper or collection characteristics are positively or negatively associated with augmented prediction performance.
- The target is raw augmented performance, `Corr(y_true, y_pred)`, not correlation gain.

Construction:
- LLMs: `Claude Sonnet 4.6`, `GPT-4.1`, and `Gemini 2.5 Pro` (displayed as `Gemini Pro 2.5`).
- Panels: individual papers (n = {n_ind:,}) and collections (n = {n_col:,}).
- Model: separate multivariable OLS for each LLM and panel.
- Predictors: log journal impact factor, log citation count, empirical-paper indicator/share, publication year, journal-discipline indicators, and log number of papers for collections.
- Predictors are grouped visually as study type, prestige/visibility proxies, publication timing, journal discipline, and collection scale.
- Continuous and binary predictors are median-imputed and standardized before fitting, so coefficients are comparable within a panel.
- Intervals are 95% HC3 robust confidence intervals from the OLS model.
- The x-axis is labeled as the standardized regression coefficient for prediction accuracy; the plotted intervals are 95% HC3 confidence intervals.
- Predictive performance is evaluated separately with grouped 5-fold cross-validation using the same features, median imputation, standardization, and an unregularized linear regression estimator.
- A positive coefficient means higher `Corr(y_true, y_pred)` after augmentation, conditional on the other displayed metadata variables.

Data sources:
- Individual-paper correlations: `{PAPER_METRICS_CSV}`
- Individual-paper metadata: `{fig7_module.PAPER_META_CSV}`
- Collection correlations and metadata features: `build_collection_df()` from `{Path(build_collection_df.__code__.co_filename)}`

Notes:
- OLS is used here instead of ridge because this figure is about interpretable conditional associations and sign, not out-of-sample prediction.
- The discipline coefficients are relative to the omitted discipline category captured by the intercept and other covariates.
- `Number of Papers` is not applicable for individual papers and is annotated as such in the individual-paper panel.
"""
    DOC_MD.write_text(doc, encoding="utf-8")


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    individual_df = build_individual_df().loc[lambda df: df["model"].isin(MODELS)].copy()
    collection_df = build_collection_df_with_everything().loc[lambda df: df["model"].isin(MODELS)].copy()

    individual = build_rows(
        individual_df,
        panel="Individual papers",
        feature_cols=fig7_module.PAPER_FEATURES,
    )
    collections = build_rows(
        collection_df,
        panel="Collections",
        feature_cols=fig7_module.COLLECTION_FEATURES,
    )
    rows = pd.concat([individual, collections], ignore_index=True)
    rows.to_csv(ROWS_CSV, index=False)

    predictive_performance = pd.concat(
        [
            evaluate_ols_predictive_performance(
                individual_df,
                panel="Individual papers",
                feature_cols=fig7_module.PAPER_FEATURES,
                group_col="source_id",
            ),
            evaluate_ols_predictive_performance(
                collection_df,
                panel="Collections",
                feature_cols=fig7_module.COLLECTION_FEATURES,
                group_col="variant_id",
            ),
        ],
        ignore_index=True,
    )
    predictive_performance.to_csv(PREDICTIVE_PERFORMANCE_CSV, index=False)

    draw_figure(rows)
    write_documentation(rows)


if __name__ == "__main__":
    main()
