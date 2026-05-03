from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ANALYSIS_ROOT = ROOT / "analysis"
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from sklearn.metrics import r2_score
from sklearn.model_selection import GroupKFold

from plot_figure7_metadata_effect_robustness import (
    COLLECTION_FEATURES,
    PAPER_FEATURES,
    build_collection_feature_frame,
    build_rows,
    draw_figure,
    load_paper_df,
)
from plot_figure8_collection_feature_importance_gpt41 import (
    FEATURE_KEYS,
    NONLINEAR_MODELS,
    build_model,
    compute_permutation_importance,
    compute_shap_tables,
    draw_figure as draw_feature_importance_figure,
)


SOURCE_RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_mean_repeat_correlation"
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_mean_repeat_correlation_empirical_only"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_mean_repeat_correlation_empirical_only"

PAPER_METRICS_CSV = SOURCE_RESULTS_DIR / "paper_mean_repeat_correlation_metrics.csv"
COLLECTION_METRICS_CSV = SOURCE_RESULTS_DIR / "collection_mean_repeat_correlation_metrics.csv"

PAPER_ROWS_CSV = RESULTS_DIR / "individual_empirical_only_metadata_effect_robustness_rows.csv"
COLLECTION_ROWS_CSV = RESULTS_DIR / "collection_empirical_filter_metadata_effect_robustness_rows.csv"
SUBSET_SUMMARY_CSV = RESULTS_DIR / "empirical_only_subset_summary.csv"
COLLECTION_SURROGATE_BENCHMARK_CSV = RESULTS_DIR / "collection_empirical_filter_surrogate_benchmark.csv"
COLLECTION_SURROGATE_BEST_CSV = RESULTS_DIR / "collection_empirical_filter_best_nonlinear_model_by_model.csv"
COLLECTION_GPT41_PERM_CSV = RESULTS_DIR / "figure8_collection_empirical_filter_feature_importance_gpt41_permutation.csv"
COLLECTION_GPT41_SHAP_POINTS_CSV = RESULTS_DIR / "figure8_collection_empirical_filter_feature_importance_gpt41_shap_points.csv"
COLLECTION_GPT41_SHAP_SUMMARY_CSV = RESULTS_DIR / "figure8_collection_empirical_filter_feature_importance_gpt41_shap_summary.csv"

PAPER_PNG = PLOTS_DIR / "individual_empirical_only_metadata_effect_robustness.png"
PAPER_PDF = PLOTS_DIR / "individual_empirical_only_metadata_effect_robustness.pdf"
COLLECTION_PNG = PLOTS_DIR / "collection_empirical_filter_metadata_effect_robustness.png"
COLLECTION_PDF = PLOTS_DIR / "collection_empirical_filter_metadata_effect_robustness.pdf"
COLLECTION_GPT41_PNG = PLOTS_DIR / "figure8_collection_empirical_filter_feature_importance_gpt41.png"
COLLECTION_GPT41_PDF = PLOTS_DIR / "figure8_collection_empirical_filter_feature_importance_gpt41.pdf"


def build_alt_paper_df() -> pd.DataFrame:
    current_df = load_paper_df().drop(columns=["delta_correlation"])
    alt_metrics = pd.read_csv(PAPER_METRICS_CSV).loc[:, ["model", "source_id", "delta_correlation"]]
    merged = current_df.merge(
        alt_metrics,
        on=["model", "source_id"],
        how="inner",
        validate="many_to_one",
    )
    return merged


def build_alt_collection_df() -> pd.DataFrame:
    current_df = build_collection_feature_frame().drop(columns=["delta_correlation"])
    alt_metrics = pd.read_csv(COLLECTION_METRICS_CSV).loc[:, ["model", "variant_id", "delta_correlation"]]
    merged = current_df.merge(
        alt_metrics,
        on=["model", "variant_id"],
        how="inner",
        validate="many_to_one",
    )
    return merged


def build_subset_summary(
    paper_df: pd.DataFrame,
    collection_df: pd.DataFrame,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for model, part in paper_df.groupby("model", sort=False):
        rows.append(
            {
                "subset": "individual_empirical_only",
                "model": model,
                "n_rows": int(len(part)),
                "n_unique_items": int(part["source_id"].nunique()),
            }
        )
    for model, part in collection_df.groupby("model", sort=False):
        rows.append(
            {
                "subset": "collection_empirical_filter_only",
                "model": model,
                "n_rows": int(len(part)),
                "n_unique_items": int(part["variant_id"].nunique()),
            }
        )
    return pd.DataFrame(rows)


def safe_spearman(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    if len(y_true) < 2 or np.std(y_true) == 0 or np.std(y_pred) == 0:
        return float("nan")
    return float(spearmanr(y_true, y_pred).statistic)


def select_best_collection_surrogates(collection_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    feature_keys = [feature for feature in FEATURE_KEYS if feature != "empirical_share"]
    estimator_names = sorted(NONLINEAR_MODELS)
    rows: list[dict[str, object]] = []

    for model_name, part in collection_df.groupby("model", sort=False):
        part = part.sort_values("variant_id").reset_index(drop=True)
        X = part[feature_keys].apply(pd.to_numeric, errors="coerce")
        y = pd.to_numeric(part["delta_correlation"], errors="coerce").to_numpy(dtype=float)
        groups = part["variant_id"].astype(str).to_numpy()
        splitter = GroupKFold(n_splits=5)

        for estimator_name in estimator_names:
            preds = np.empty_like(y, dtype=float)
            fold_r2: list[float] = []
            fold_spearman: list[float] = []
            for fold_idx, (train_idx, test_idx) in enumerate(splitter.split(X, y, groups), start=1):
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


def write_empirical_collection_feature_importance(collection_df: pd.DataFrame) -> None:
    benchmark_df, best_df = select_best_collection_surrogates(collection_df)
    benchmark_df.to_csv(COLLECTION_SURROGATE_BENCHMARK_CSV, index=False)
    best_df.to_csv(COLLECTION_SURROGATE_BEST_CSV, index=False)

    estimator_name = str(best_df.loc[best_df["model"] == "GPT-4.1", "estimator_name"].iloc[0])
    feature_keys = [feature for feature in FEATURE_KEYS if feature != "empirical_share"]
    df = collection_df.loc[collection_df["model"] == "GPT-4.1"].sort_values("variant_id").reset_index(drop=True)
    X = df[feature_keys].apply(pd.to_numeric, errors="coerce")
    y = pd.to_numeric(df["delta_correlation"], errors="coerce").to_numpy(dtype=float)
    groups = df["variant_id"].astype(str).to_numpy()

    perm_df = compute_permutation_importance(X, y, groups, estimator_name)
    shap_points, shap_summary = compute_shap_tables(X, y, perm_df["feature_key"].tolist(), estimator_name)

    perm_df.to_csv(COLLECTION_GPT41_PERM_CSV, index=False)
    shap_points.to_csv(COLLECTION_GPT41_SHAP_POINTS_CSV, index=False)
    shap_summary.to_csv(COLLECTION_GPT41_SHAP_SUMMARY_CSV, index=False)
    draw_feature_importance_figure(
        "GPT-4.1 empirical-only",
        estimator_name,
        perm_df,
        shap_points,
        COLLECTION_GPT41_PNG,
        COLLECTION_GPT41_PDF,
    )


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    paper_df = build_alt_paper_df()
    paper_empirical = paper_df.loc[paper_df["empirical_share"] == 1.0].copy()
    paper_feature_cols = [feature for feature in PAPER_FEATURES if feature != "empirical_share"]
    paper_rows = build_rows(
        paper_empirical,
        item_type="Empirical papers",
        feature_cols=paper_feature_cols,
    )
    paper_rows.to_csv(PAPER_ROWS_CSV, index=False)
    draw_figure(paper_rows, "Empirical papers only", PAPER_PNG, PAPER_PDF)

    collection_df = build_alt_collection_df()
    collection_empirical = collection_df.loc[collection_df["type_value"] == "empirical"].copy()
    collection_feature_cols = [feature for feature in COLLECTION_FEATURES if feature != "empirical_share"]
    collection_rows = build_rows(
        collection_empirical,
        item_type="Collections (Empirical = True)",
        feature_cols=collection_feature_cols,
    )
    collection_rows.to_csv(COLLECTION_ROWS_CSV, index=False)
    draw_figure(
        collection_rows,
        "Collections (Empirical = True)",
        COLLECTION_PNG,
        COLLECTION_PDF,
    )
    write_empirical_collection_feature_importance(collection_empirical)

    summary_df = build_subset_summary(paper_empirical, collection_empirical)
    summary_df.to_csv(SUBSET_SUMMARY_CSV, index=False)


if __name__ == "__main__":
    main()
