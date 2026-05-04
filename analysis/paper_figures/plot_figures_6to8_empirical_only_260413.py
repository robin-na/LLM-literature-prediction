from __future__ import annotations

import os
import re
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
from matplotlib.offsetbox import AnnotationBbox, HPacker, TextArea, VPacker
from matplotlib.ticker import FormatStrFormatter, MaxNLocator
from scipy.stats import spearmanr
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from analyze_literature_metadata_supervised_benchmarks import (
    COLLECTION_FEATURES as BENCH_COLLECTION_FEATURES,
    COLLECTION_NUMERIC,
    PAPER_FEATURES as BENCH_PAPER_FEATURES,
    PAPER_NUMERIC,
    evaluate_models,
    summarize_best,
)
import plot_figure7_metadata_effect_robustness as fig7_module
from paper_figures.plot_collection_linear_metadata_effect_260409 import build_collection_df
from plot_figure8_collection_feature_importance_gpt41 import (
    FEATURE_KEYS,
    NONLINEAR_MODELS,
    build_model,
    compute_permutation_importance,
    compute_shap_tables,
    draw_figure as draw_feature_importance_figure,
)


SOURCE_RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409_empirical_only"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409_empirical_only"

SOURCE_PAPER_METRICS_CSV = SOURCE_RESULTS_DIR / "paper_repeat_correlation_metrics.csv"
SOURCE_COLLECTION_METRICS_CSV = SOURCE_RESULTS_DIR / "collection_repeat_correlation_metrics.csv"
SOURCE_FIG6_PAPER_DATASET_CSV = SOURCE_RESULTS_DIR / "figure6_paper_metadata_benchmark_dataset.csv"
SOURCE_FIG6_COLLECTION_DATASET_CSV = SOURCE_RESULTS_DIR / "figure6_collection_metadata_benchmark_dataset.csv"

MODELS = ["Claude Sonnet 4.6", "GPT-5.1", "GPT-4.1", "Gemini 2.5 Pro"]
MODEL_COLORS = {
    "Claude Sonnet 4.6": "#9c755f",
    "GPT-5.1": "#d95f02",
    "GPT-4.1": "#2b8cbe",
    "Gemini 2.5 Pro": "#17becf",
}
DATASET_LABELS = {
    "individual_papers": "Individual papers",
    "metadata_filter_collections": "Collections",
}
DATASET_COLORS = {
    "individual_papers": "#73808f",
    "metadata_filter_collections": "#e59a3a",
}
N_BOOT = 400
RNG = np.random.default_rng(42)

BENCH_PAPER_FEATURES_EMP = [feature for feature in BENCH_PAPER_FEATURES if feature != "empirical"]
BENCH_COLLECTION_FEATURES_EMP = [feature for feature in BENCH_COLLECTION_FEATURES if feature != "type_value"]
PAPER_COEF_FEATURES = [feature for feature in fig7_module.PAPER_FEATURES if feature != "empirical_share"]
COLLECTION_COEF_FEATURES = [feature for feature in fig7_module.COLLECTION_FEATURES if feature != "empirical_share"]
FEATURE_IMPORTANCE_KEYS = [feature for feature in FEATURE_KEYS if feature != "empirical_share"]

SUBSET_SUMMARY_CSV = RESULTS_DIR / "empirical_only_subset_summary.csv"

FIG6_RESULTS_CSV = RESULTS_DIR / "literature_metadata_supervised_model_benchmark.csv"
FIG6_BEST_CSV = RESULTS_DIR / "literature_metadata_supervised_model_best.csv"
FIG6_ROWS_CSV = RESULTS_DIR / "figure6_metadata_predictability_correlation_rows.csv"
FIG6_PNG = PLOTS_DIR / "figure6_metadata_predictability_correlation.png"
FIG6_PDF = PLOTS_DIR / "figure6_metadata_predictability_correlation.pdf"

FIG7_ROWS_CSV = RESULTS_DIR / "figure7_individual_metadata_effect_robustness_rows.csv"
FIG7_PNG = PLOTS_DIR / "figure7_individual_metadata_effect_robustness.png"
FIG7_PDF = PLOTS_DIR / "figure7_individual_metadata_effect_robustness.pdf"

FIG8_ROWS_CSV = RESULTS_DIR / "figure8_collection_metadata_effect_robustness_rows.csv"
FIG8_PNG = PLOTS_DIR / "figure8_collection_metadata_effect_robustness.png"
FIG8_PDF = PLOTS_DIR / "figure8_collection_metadata_effect_robustness.pdf"

COMBINED_OLS_ROWS_CSV = RESULTS_DIR / "figure7_8_metadata_effect_side_by_side_selected4_ols_rows.csv"
COMBINED_OLS_PNG = PLOTS_DIR / "figure7_8_metadata_effect_side_by_side_selected4_ols.png"
COMBINED_OLS_PDF = PLOTS_DIR / "figure7_8_metadata_effect_side_by_side_selected4_ols.pdf"

FEATURE_IMPORTANCE_BENCH_CSV = RESULTS_DIR / "figure8_collection_best_nonlinear_model_by_model.csv"
FEATURE_IMPORTANCE_ALL_CSV = RESULTS_DIR / "figure8_collection_nonlinear_surrogate_benchmark.csv"


def pretty_estimator(name: str) -> str:
    return str(name).replace("_", " ").title()


def slugify_model_name(model_name: str) -> str:
    text = model_name.lower()
    text = text.replace("claude sonnet 4.6", "claude_sonnet46")
    text = text.replace("gpt-5.1", "gpt51")
    text = text.replace("gpt-4.1", "gpt41")
    text = text.replace("gemini 2.5 pro", "gemini_2_5_pro")
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")


def safe_spearman(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    if len(y_true) < 2 or np.std(y_true) == 0 or np.std(y_pred) == 0:
        return float("nan")
    return float(spearmanr(y_true, y_pred).statistic)


def build_alt_paper_df() -> pd.DataFrame:
    current_df = fig7_module.load_paper_df().drop(columns=["delta_correlation", "correlation"])
    base_feature_df = (
        current_df.loc[current_df["model"] == "GPT-4.1"]
        .drop(columns=["model"])
        .drop_duplicates("source_id", keep="first")
    )
    metrics = pd.read_csv(SOURCE_PAPER_METRICS_CSV)
    df = metrics.loc[:, ["model", "source_id", "correlation", "delta_correlation"]].merge(
        base_feature_df,
        on="source_id",
        how="left",
        validate="many_to_one",
    )
    return df.loc[df["model"].isin(MODELS)].copy()


def build_empirical_paper_df() -> pd.DataFrame:
    df = build_alt_paper_df()
    return df.loc[df["empirical_share"] == 1.0].copy()


def build_empirical_collection_df() -> pd.DataFrame:
    df = build_collection_df().loc[lambda x: x["model"].isin(MODELS)].copy()
    return df.loc[df["type_value"] == "empirical"].copy()


def build_figure6_datasets() -> tuple[pd.DataFrame, pd.DataFrame]:
    paper_df = pd.read_csv(SOURCE_FIG6_PAPER_DATASET_CSV)
    paper_df = paper_df.loc[paper_df["model"].isin(MODELS) & paper_df["empirical"].eq(True)].copy()

    collection_df = pd.read_csv(SOURCE_FIG6_COLLECTION_DATASET_CSV)
    collection_df = collection_df.loc[
        collection_df["model"].isin(MODELS) & collection_df["type_value"].eq("empirical")
    ].copy()
    return paper_df, collection_df


def build_subset_summary(
    paper_bench_df: pd.DataFrame,
    collection_bench_df: pd.DataFrame,
    paper_coef_df: pd.DataFrame,
    collection_coef_df: pd.DataFrame,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for model in MODELS:
        part = paper_bench_df.loc[paper_bench_df["model"] == model]
        rows.append(
            {
                "subset": "figure6_individual_empirical_only",
                "model": model,
                "n_rows": int(len(part)),
                "n_unique_items": int(part["source_id"].nunique()),
            }
        )
        part = collection_bench_df.loc[collection_bench_df["model"] == model]
        rows.append(
            {
                "subset": "figure6_collection_empirical_only",
                "model": model,
                "n_rows": int(len(part)),
                "n_unique_items": int(part["variant_id"].nunique()),
            }
        )
        part = paper_coef_df.loc[paper_coef_df["model"] == model]
        rows.append(
            {
                "subset": "figure7_individual_empirical_only",
                "model": model,
                "n_rows": int(len(part)),
                "n_unique_items": int(part["source_id"].nunique()),
            }
        )
        part = collection_coef_df.loc[collection_coef_df["model"] == model]
        rows.append(
            {
                "subset": "figure8_collection_empirical_only",
                "model": model,
                "n_rows": int(len(part)),
                "n_unique_items": int(part["variant_id"].nunique()),
            }
        )
    return pd.DataFrame(rows)


def write_figure6_outputs(benchmark_df: pd.DataFrame) -> None:
    rows = benchmark_df.loc[
        (benchmark_df["target"] == "correlation")
        & (benchmark_df["scope"] == "within_model")
        & (benchmark_df["model_name"] == "ridge")
    ].copy()
    rows = rows.loc[rows["scope_name"].isin(MODELS)].copy()
    rows["scope_order"] = rows["scope_name"].map({name: idx for idx, name in enumerate(MODELS)})
    rows["estimator_label"] = rows["model_name"].map(pretty_estimator)
    rows["dataset_label"] = rows["dataset"].map(DATASET_LABELS)
    rows["se_fold_r2"] = rows["sd_fold_r2"] / np.sqrt(5.0)
    rows["se_fold_spearman"] = rows["sd_fold_spearman"] / np.sqrt(5.0)
    rows = rows.sort_values(["scope_order", "dataset"]).reset_index(drop=True)
    rows.to_csv(FIG6_ROWS_CSV, index=False)

    def draw_panel(ax: plt.Axes, metric: str, err: str, xlabel: str, *, show_ylabels: bool) -> None:
        row_y = np.arange(len(MODELS))[::-1].astype(float) * 1.35
        y_map = dict(zip(MODELS, row_y))
        offsets = {"individual_papers": 0.23, "metadata_filter_collections": -0.23}
        height = 0.36

        for dataset in ["individual_papers", "metadata_filter_collections"]:
            part = rows.loc[rows["dataset"] == dataset].copy()
            ys = [y_map[name] + offsets[dataset] for name in part["scope_name"]]
            xs = part[metric].to_numpy(dtype=float)
            xerr = part[err].to_numpy(dtype=float)

            ax.barh(
                ys,
                xs,
                height=height,
                color=DATASET_COLORS[dataset],
                alpha=0.86,
                edgecolor="none",
                zorder=2,
            )
            ax.errorbar(
                xs,
                ys,
                xerr=xerr,
                fmt="none",
                ecolor="#46505d",
                elinewidth=1.0,
                alpha=0.45,
                capsize=2.3,
                zorder=3,
            )

        ax.axvline(0.0, color="#777777", lw=1.1, ls=(0, (4, 3)), zorder=1)
        ax.set_xlabel(xlabel)
        ax.set_yticks(row_y)
        ax.tick_params(axis="y", labelleft=False, length=0, pad=10)
        ax.grid(axis="x", color="#e6e6e6", lw=0.8)
        ax.set_axisbelow(True)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("#cfcfcf")
        ax.spines["bottom"].set_color("#cfcfcf")

        if show_ylabels:
            trans = ax.get_yaxis_transform()
            for model in MODELS:
                part = rows.loc[rows["scope_name"] == model].copy()
                ind = part.loc[part["dataset"] == "individual_papers", "estimator_label"].iloc[0]
                coll = part.loc[part["dataset"] == "metadata_filter_collections", "estimator_label"].iloc[0]
                label_box = VPacker(
                    children=[
                        TextArea(
                            model,
                            textprops={"fontsize": 12.0, "color": "#222222", "ha": "right", "va": "center"},
                        ),
                        HPacker(
                            children=[
                                TextArea(
                                    ind,
                                    textprops={
                                        "fontsize": 10.4,
                                        "color": DATASET_COLORS["individual_papers"],
                                        "ha": "right",
                                        "va": "center",
                                    },
                                ),
                                TextArea(
                                    " | ",
                                    textprops={"fontsize": 10.4, "color": "#555555", "ha": "center", "va": "center"},
                                ),
                                TextArea(
                                    coll,
                                    textprops={
                                        "fontsize": 10.4,
                                        "color": DATASET_COLORS["metadata_filter_collections"],
                                        "ha": "left",
                                        "va": "center",
                                    },
                                ),
                            ],
                            align="center",
                            pad=0,
                            sep=0,
                        ),
                    ],
                    align="right",
                    pad=0,
                    sep=2,
                )
                ax.add_artist(
                    AnnotationBbox(
                        label_box,
                        (-0.08, y_map[model]),
                        xycoords=trans,
                        frameon=False,
                        box_alignment=(1.0, 0.5),
                        pad=0.0,
                        annotation_clip=False,
                    )
                )

    fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.4), sharey=True)
    draw_panel(axes[0], "mean_fold_r2", "se_fold_r2", "Grouped-CV R^2", show_ylabels=True)
    draw_panel(axes[1], "mean_fold_spearman", "se_fold_spearman", "Grouped-CV Spearman", show_ylabels=False)
    axes[0].set_xlim(-0.02, max(0.26, rows["mean_fold_r2"].max() + rows["se_fold_r2"].max() + 0.02))
    axes[1].set_xlim(-0.02, max(0.54, rows["mean_fold_spearman"].max() + rows["se_fold_spearman"].max() + 0.03))

    handles = [
        Line2D([0], [0], color=DATASET_COLORS[key], lw=10, solid_capstyle="round", label=label)
        for key, label in DATASET_LABELS.items()
    ]
    handles.append(Line2D([0], [0], color="#777777", lw=1.1, ls=(0, (4, 3)), label="No signal"))
    fig.legend(
        handles=handles,
        loc="upper center",
        ncol=3,
        frameon=False,
        bbox_to_anchor=(0.5, 0.985),
        columnspacing=1.2,
        handlelength=2.0,
    )
    fig.subplots_adjust(top=0.78, left=0.43, right=0.985, bottom=0.18, wspace=0.18)
    fig.savefig(FIG6_PNG, dpi=300)
    fig.savefig(FIG6_PDF)
    plt.close(fig)


def write_linear_coefficient_outputs(paper_empirical: pd.DataFrame, collection_empirical: pd.DataFrame) -> None:
    fig7_module.MODELS = MODELS
    fig7_module.MODEL_COLORS = MODEL_COLORS

    paper_rows = fig7_module.build_rows(
        paper_empirical,
        item_type="Empirical papers",
        feature_cols=PAPER_COEF_FEATURES,
    )
    paper_rows.to_csv(FIG7_ROWS_CSV, index=False)
    fig7_module.draw_figure(
        paper_rows,
        "Empirical papers only",
        FIG7_PNG,
        FIG7_PDF,
    )

    collection_rows = fig7_module.build_rows(
        collection_empirical,
        item_type="Collections (Empirical = True)",
        feature_cols=COLLECTION_COEF_FEATURES,
    )
    collection_rows.to_csv(FIG8_ROWS_CSV, index=False)
    fig7_module.draw_figure(
        collection_rows,
        "Collections (Empirical = True)",
        FIG8_PNG,
        FIG8_PDF,
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


def build_ols_rows(df: pd.DataFrame, *, panel: str, feature_cols: list[str]) -> pd.DataFrame:
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
        features = [feature for feature in features if feature != "Number of Papers"]
    return features + ["Number of Papers"]


def write_combined_ols_output(paper_empirical: pd.DataFrame, collection_empirical: pd.DataFrame) -> None:
    individual = build_ols_rows(
        paper_empirical,
        panel="Individual papers",
        feature_cols=PAPER_COEF_FEATURES,
    )
    collection = build_ols_rows(
        collection_empirical,
        panel="Collections",
        feature_cols=COLLECTION_COEF_FEATURES,
    )
    rows = pd.concat([individual, collection], ignore_index=True)
    rows.to_csv(COMBINED_OLS_ROWS_CSV, index=False)

    features = ordered_features_from_individual(individual)

    def draw_panel(ax: plt.Axes, df: pd.DataFrame, title: str, *, show_ylabels: bool) -> None:
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

    fig, axes = plt.subplots(1, 2, figsize=(12.9, 6.7), sharey=True)
    draw_panel(axes[0], individual, "Individual Papers", show_ylabels=True)
    draw_panel(axes[1], collection, "Collections", show_ylabels=False)

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
    fig.savefig(COMBINED_OLS_PNG, dpi=300)
    fig.savefig(COMBINED_OLS_PDF)
    plt.close(fig)


def select_best_collection_surrogates(collection_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows: list[dict[str, object]] = []

    for model_name in MODELS:
        part = collection_df.loc[collection_df["model"] == model_name].sort_values("variant_id").reset_index(drop=True)
        X = part[FEATURE_IMPORTANCE_KEYS].apply(pd.to_numeric, errors="coerce")
        y = pd.to_numeric(part["delta_correlation"], errors="coerce").to_numpy(dtype=float)
        groups = part["variant_id"].astype(str).to_numpy()
        splitter = GroupKFold(n_splits=5)

        for estimator_name in sorted(NONLINEAR_MODELS):
            preds = np.empty_like(y, dtype=float)
            fold_r2: list[float] = []
            fold_spearman: list[float] = []
            for train_idx, test_idx in splitter.split(X, y, groups):
                estimator = build_model(estimator_name)
                estimator.fit(X.iloc[train_idx], y[train_idx])
                fold_pred = estimator.predict(X.iloc[test_idx])
                preds[test_idx] = fold_pred
                fold_r2.append(float(r2_score(y[test_idx], fold_pred)))
                fold_spearman.append(safe_spearman(y[test_idx], fold_pred))

            rows.append(
                {
                    "model": model_name,
                    "estimator_name": estimator_name,
                    "n_rows": int(len(part)),
                    "n_groups": int(part["variant_id"].nunique()),
                    "cv_r2": float(r2_score(y, preds)),
                    "cv_spearman": safe_spearman(y, preds),
                    "mean_fold_r2": float(np.mean(fold_r2)),
                    "mean_fold_spearman": float(np.nanmean(fold_spearman)),
                    "sd_fold_r2": float(np.std(fold_r2, ddof=1)),
                    "sd_fold_spearman": float(np.nanstd(fold_spearman, ddof=1)),
                }
            )

    benchmark_df = pd.DataFrame(rows).sort_values(
        ["model", "cv_r2", "cv_spearman"],
        ascending=[True, False, False],
    ).reset_index(drop=True)
    best_df = benchmark_df.groupby("model", as_index=False).head(1).reset_index(drop=True)
    return benchmark_df, best_df


def write_feature_importance_outputs(collection_empirical: pd.DataFrame) -> None:
    benchmark_df, best_df = select_best_collection_surrogates(collection_empirical)
    benchmark_df.to_csv(FEATURE_IMPORTANCE_ALL_CSV, index=False)
    best_df.to_csv(FEATURE_IMPORTANCE_BENCH_CSV, index=False)

    for model in MODELS:
        estimator_name = str(best_df.loc[best_df["model"] == model, "estimator_name"].iloc[0])
        df = collection_empirical.loc[collection_empirical["model"] == model].sort_values("variant_id").reset_index(drop=True)
        X = df[FEATURE_IMPORTANCE_KEYS].apply(pd.to_numeric, errors="coerce")
        y = pd.to_numeric(df["delta_correlation"], errors="coerce").to_numpy(dtype=float)
        groups = df["variant_id"].astype(str).to_numpy()

        perm_df = compute_permutation_importance(X, y, groups, estimator_name)
        shap_points, shap_summary = compute_shap_tables(X, y, perm_df["feature_key"].tolist(), estimator_name)

        stem = f"figure8_collection_feature_importance_{slugify_model_name(model)}"
        perm_df.to_csv(RESULTS_DIR / f"{stem}_permutation.csv", index=False)
        shap_points.to_csv(RESULTS_DIR / f"{stem}_shap_points.csv", index=False)
        shap_summary.to_csv(RESULTS_DIR / f"{stem}_shap_summary.csv", index=False)
        draw_feature_importance_figure(
            f"{model} empirical-only",
            estimator_name,
            perm_df,
            shap_points,
            PLOTS_DIR / f"{stem}.png",
            PLOTS_DIR / f"{stem}.pdf",
        )


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    paper_bench_df, collection_bench_df = build_figure6_datasets()
    benchmark_results = pd.concat(
        [
            evaluate_models(
                paper_bench_df,
                dataset_name="individual_papers",
                features=BENCH_PAPER_FEATURES_EMP,
                numeric_cols=PAPER_NUMERIC,
                group_col="source_id",
                within_model=True,
            ),
            evaluate_models(
                collection_bench_df,
                dataset_name="metadata_filter_collections",
                features=BENCH_COLLECTION_FEATURES_EMP,
                numeric_cols=COLLECTION_NUMERIC,
                group_col="variant_id",
                within_model=True,
            ),
        ],
        ignore_index=True,
        sort=False,
    )
    benchmark_best = summarize_best(benchmark_results)
    benchmark_results.to_csv(FIG6_RESULTS_CSV, index=False)
    benchmark_best.to_csv(FIG6_BEST_CSV, index=False)
    write_figure6_outputs(benchmark_results)

    paper_empirical = build_empirical_paper_df()
    collection_empirical = build_empirical_collection_df()

    write_linear_coefficient_outputs(paper_empirical, collection_empirical)
    write_combined_ols_output(paper_empirical, collection_empirical)
    write_feature_importance_outputs(collection_empirical)

    subset_summary = build_subset_summary(
        paper_bench_df,
        collection_bench_df,
        paper_empirical,
        collection_empirical,
    )
    subset_summary.to_csv(SUBSET_SUMMARY_CSV, index=False)


if __name__ == "__main__":
    main()
