from __future__ import annotations

from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from scipy.stats import ConstantInputWarning, spearmanr
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import ExtraTreesRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import RidgeCV
from sklearn.metrics import r2_score
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results" / "validation" / "literature_metadata_supervised_benchmarks"

PAPER_DATA_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_analysis_report_sources_repeat5"
    / "paper_feature_analysis_dataset_repeat5.csv"
)
PAPER_SIGNIFICANCE_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_analysis_report_sources_repeat5"
    / "validation_literature_analysis_report_source_significance.csv"
)
COLLECTION_DATA_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_metadata_filters"
    / "validation_literature_collection_analysis_report_metadata_filters_relationship_dataset.csv"
)

PAPER_FEATURES = [
    "empirical",
    "exactclose_domain",
    "payoff_relevance_exactclose",
    "payoff_outcome_primary",
    "pub_year_z",
    "log_citations_z",
    "n_pages_z",
    "dimension_informative_direct_count_z",
    "broad_only_count_z",
    "chat_discussed",
    "show_other_summaries_discussed",
    "show_punishment_id_discussed",
]
PAPER_NUMERIC = [
    "pub_year_z",
    "log_citations_z",
    "n_pages_z",
    "dimension_informative_direct_count_z",
    "broad_only_count_z",
]
COLLECTION_FEATURES = [
    "count",
    "log_count",
    "n_filters",
    "type_value",
    "citation_value",
    "jcr_value",
    "year_value",
    "discipline_value",
]
COLLECTION_NUMERIC = ["count", "log_count", "n_filters"]
TARGET_SPECS = [
    ("correlation", "Correlation"),
    ("delta_correlation", "Correlation gain"),
    ("rmse_improvement", "RMSE improvement"),
    ("delta_r2", "R2 gain"),
]


def load_paper_df() -> pd.DataFrame:
    df = pd.read_csv(PAPER_DATA_CSV).copy()
    raw_metrics = pd.read_csv(PAPER_SIGNIFICANCE_CSV)[
        ["model", "mode", "source_id", "correlation", "baseline_correlation", "rmse", "baseline_rmse", "r2", "baseline_r2"]
    ].copy()
    df = df.merge(raw_metrics, on=["model", "mode", "source_id"], how="left", validate="one_to_one")
    df = df.loc[~df[PAPER_FEATURES].isna().all(axis=1)].copy()
    df["rmse_improvement"] = -pd.to_numeric(df["delta_rmse"], errors="coerce")
    return df


def load_collection_df() -> pd.DataFrame:
    df = pd.read_csv(COLLECTION_DATA_CSV).copy()
    df["rmse_improvement"] = pd.to_numeric(df["rmse_improvement"], errors="coerce")
    return df


def build_preprocessor(features: list[str], numeric_cols: list[str]) -> ColumnTransformer:
    categorical_cols = [col for col in features if col not in numeric_cols]
    return ColumnTransformer(
        [
            (
                "num",
                Pipeline(
                    [
                        ("imputer", SimpleImputer(strategy="median")),
                        ("scaler", StandardScaler()),
                    ]
                ),
                numeric_cols,
            ),
            (
                "cat",
                Pipeline(
                    [
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
                    ]
                ),
                categorical_cols,
            ),
        ]
    )


def build_models(features: list[str], numeric_cols: list[str]) -> dict[str, Pipeline]:
    pre = build_preprocessor(features, numeric_cols)
    return {
        "dummy_mean": Pipeline([("preprocess", pre), ("model", DummyRegressor(strategy="mean"))]),
        "ridge": Pipeline(
            [("preprocess", pre), ("model", RidgeCV(alphas=np.logspace(-3, 3, 13)))]
        ),
        "random_forest": Pipeline(
            [
                ("preprocess", pre),
                (
                    "model",
                    RandomForestRegressor(
                        n_estimators=200,
                        min_samples_leaf=5,
                        random_state=42,
                        n_jobs=-1,
                    ),
                ),
            ]
        ),
        "extra_trees": Pipeline(
            [
                ("preprocess", pre),
                (
                    "model",
                    ExtraTreesRegressor(
                        n_estimators=250,
                        min_samples_leaf=3,
                        random_state=42,
                        n_jobs=-1,
                    ),
                ),
            ]
        ),
        "gradient_boosting": Pipeline(
            [
                ("preprocess", pre),
                (
                    "model",
                    GradientBoostingRegressor(
                        n_estimators=200,
                        learning_rate=0.05,
                        max_depth=3,
                        random_state=42,
                    ),
                ),
            ]
        ),
    }


def safe_spearman(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    if len(y_true) < 2 or np.std(y_true) == 0 or np.std(y_pred) == 0:
        return float("nan")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=ConstantInputWarning)
        return float(spearmanr(y_true, y_pred).statistic)


def safe_nanmean(values: list[float]) -> float:
    arr = np.asarray(values, dtype=float)
    finite = arr[np.isfinite(arr)]
    if finite.size == 0:
        return float("nan")
    return float(finite.mean())


def safe_nanstd(values: list[float]) -> float:
    arr = np.asarray(values, dtype=float)
    finite = arr[np.isfinite(arr)]
    if finite.size < 2:
        return 0.0
    return float(finite.std(ddof=1))


def _prepare_X(df: pd.DataFrame, features: list[str], numeric_cols: list[str]) -> pd.DataFrame:
    X = df[features].copy()
    for col in X.columns:
        if col not in numeric_cols:
            X[col] = X[col].astype(str)
    return X


def evaluate_models(
    df: pd.DataFrame,
    *,
    dataset_name: str,
    features: list[str],
    numeric_cols: list[str],
    group_col: str,
    within_model: bool,
    min_groups: int = 5,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    model_pipelines = build_models(features, numeric_cols)

    scopes: list[tuple[str, pd.DataFrame]]
    if within_model:
        scopes = [(str(model), part.copy()) for model, part in df.groupby("model", dropna=False, observed=False)]
    else:
        scopes = [("All models pooled", df.copy())]

    for scope_name, part in scopes:
        part = part.dropna(subset=[group_col]).copy()
        n_groups = int(part[group_col].nunique())
        if n_groups < min_groups:
            continue

        X = _prepare_X(part, features, numeric_cols)
        groups = part[group_col].astype(str).to_numpy()
        splitter = GroupKFold(n_splits=5)

        for target_col, target_label in TARGET_SPECS:
            if target_col not in part.columns:
                continue
            y = pd.to_numeric(part[target_col], errors="coerce")
            valid = y.notna()
            if valid.sum() < min_groups:
                continue
            X_t = X.loc[valid].reset_index(drop=True)
            y_t = y.loc[valid].to_numpy(dtype=float)
            groups_t = part.loc[valid, group_col].astype(str).to_numpy()
            if len(np.unique(groups_t)) < min_groups:
                continue

            for model_name, pipe in model_pipelines.items():
                preds = np.empty_like(y_t, dtype=float)
                fold_rows: list[dict[str, object]] = []
                for fold_idx, (train_idx, test_idx) in enumerate(splitter.split(X_t, y_t, groups_t), start=1):
                    pipe.fit(X_t.iloc[train_idx], y_t[train_idx])
                    pred = pipe.predict(X_t.iloc[test_idx])
                    preds[test_idx] = pred
                    fold_rows.append(
                        {
                            "dataset": dataset_name,
                            "scope": "within_model" if within_model else "pooled",
                            "scope_name": scope_name,
                            "target": target_col,
                            "target_label": target_label,
                            "model_name": model_name,
                            "fold": fold_idx,
                            "n_test": int(len(test_idx)),
                            "r2": float(r2_score(y_t[test_idx], pred)),
                            "spearman": safe_spearman(y_t[test_idx], pred),
                        }
                    )

                rows.append(
                    {
                        "dataset": dataset_name,
                        "scope": "within_model" if within_model else "pooled",
                        "scope_name": scope_name,
                        "target": target_col,
                        "target_label": target_label,
                        "model_name": model_name,
                        "n_rows": int(len(y_t)),
                        "n_groups": int(len(np.unique(groups_t))),
                        "cv_r2": float(r2_score(y_t, preds)),
                        "cv_spearman": safe_spearman(y_t, preds),
                        "mean_fold_r2": float(np.mean([row["r2"] for row in fold_rows])),
                        "mean_fold_spearman": safe_nanmean([row["spearman"] for row in fold_rows]),
                        "sd_fold_r2": float(np.std([row["r2"] for row in fold_rows], ddof=1)),
                        "sd_fold_spearman": safe_nanstd([row["spearman"] for row in fold_rows]),
                    }
                )

    return pd.DataFrame(rows)


def summarize_best(results: pd.DataFrame) -> pd.DataFrame:
    sort_cols = ["dataset", "scope", "scope_name", "target", "cv_r2", "cv_spearman"]
    return (
        results.sort_values(sort_cols, ascending=[True, True, True, True, False, False])
        .groupby(["dataset", "scope", "scope_name", "target", "target_label"], dropna=False, as_index=False)
        .head(1)
        .reset_index(drop=True)
    )


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    paper_df = load_paper_df()
    collection_df = load_collection_df()

    results = pd.concat(
        [
            evaluate_models(
                paper_df,
                dataset_name="individual_papers",
                features=PAPER_FEATURES,
                numeric_cols=PAPER_NUMERIC,
                group_col="source_id",
                within_model=False,
            ),
            evaluate_models(
                paper_df,
                dataset_name="individual_papers",
                features=PAPER_FEATURES,
                numeric_cols=PAPER_NUMERIC,
                group_col="source_id",
                within_model=True,
            ),
            evaluate_models(
                collection_df,
                dataset_name="metadata_filter_collections",
                features=COLLECTION_FEATURES,
                numeric_cols=COLLECTION_NUMERIC,
                group_col="variant_id",
                within_model=False,
            ),
            evaluate_models(
                collection_df,
                dataset_name="metadata_filter_collections",
                features=COLLECTION_FEATURES,
                numeric_cols=COLLECTION_NUMERIC,
                group_col="variant_id",
                within_model=True,
            ),
        ],
        ignore_index=True,
        sort=False,
    )

    best = summarize_best(results)

    results.to_csv(RESULTS_DIR / "literature_metadata_supervised_model_benchmark.csv", index=False)
    best.to_csv(RESULTS_DIR / "literature_metadata_supervised_model_best.csv", index=False)


if __name__ == "__main__":
    main()
