from __future__ import annotations

import os
import sys
import warnings
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ANALYSIS_ROOT = ROOT / "analysis"
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import numpy as np
import pandas as pd
from scipy.stats import ConstantInputWarning, spearmanr
from sklearn.ensemble import ExtraTreesRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import ElasticNetCV, LinearRegression, RidgeCV
from sklearn.metrics import r2_score
from sklearn.model_selection import GroupKFold
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

import plot_figure7_metadata_effect_robustness as fig7_module
from paper_figures.plot_figure3_metadata_coefficients_260415 import build_individual_df


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260427"
BENCHMARK_CSV = RESULTS_DIR / "figure4_predictive_model_benchmark.csv"
BEST_CSV = RESULTS_DIR / "figure4_predictive_model_best.csv"
DOC_MD = RESULTS_DIR / "figure4_predictive_model_benchmark_documentation.md"

MODELS = ["Claude Sonnet 4.6", "GPT-4.1", "Gemini 2.5 Pro"]
MODEL_DISPLAY = {
    "Claude Sonnet 4.6": "Claude Sonnet 4.6",
    "GPT-4.1": "GPT-4.1",
    "Gemini 2.5 Pro": "Gemini 2.5 Pro",
}
FEATURES = fig7_module.PAPER_FEATURES


def safe_pearson(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    valid = np.isfinite(y_true) & np.isfinite(y_pred)
    if valid.sum() < 2 or np.std(y_true[valid]) == 0 or np.std(y_pred[valid]) == 0:
        return float("nan")
    return float(np.corrcoef(y_true[valid], y_pred[valid])[0, 1])


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


def build_models() -> dict[str, Pipeline]:
    return {
        "ols": Pipeline(
            [
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler()),
                ("model", LinearRegression()),
            ]
        ),
        "ridge": Pipeline(
            [
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler()),
                ("model", RidgeCV(alphas=np.logspace(-3, 3, 13))),
            ]
        ),
        "elastic_net": Pipeline(
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
        ),
        "random_forest": Pipeline(
            [
                ("imputer", SimpleImputer(strategy="median")),
                (
                    "model",
                    RandomForestRegressor(
                        n_estimators=300,
                        min_samples_leaf=5,
                        random_state=42,
                        n_jobs=-1,
                    ),
                ),
            ]
        ),
        "extra_trees": Pipeline(
            [
                ("imputer", SimpleImputer(strategy="median")),
                (
                    "model",
                    ExtraTreesRegressor(
                        n_estimators=350,
                        min_samples_leaf=3,
                        random_state=42,
                        n_jobs=-1,
                    ),
                ),
            ]
        ),
        "gradient_boosting": Pipeline(
            [
                ("imputer", SimpleImputer(strategy="median")),
                (
                    "model",
                    GradientBoostingRegressor(
                        n_estimators=250,
                        learning_rate=0.05,
                        max_depth=3,
                        random_state=42,
                    ),
                ),
            ]
        ),
        "mlp": Pipeline(
            [
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler()),
                (
                    "model",
                    MLPRegressor(
                        hidden_layer_sizes=(16, 8),
                        activation="relu",
                        alpha=1e-3,
                        learning_rate_init=1e-3,
                        early_stopping=True,
                        max_iter=4000,
                        random_state=42,
                    ),
                ),
            ]
        ),
    }


def evaluate_models(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    model_pipelines = build_models()

    for model_name in MODELS:
        part = df.loc[df["model"] == model_name].dropna(subset=["source_id"]).copy()
        X = part[FEATURES].apply(pd.to_numeric, errors="coerce")
        y = pd.to_numeric(part["correlation"], errors="coerce")
        valid = y.notna()
        X = X.loc[valid].reset_index(drop=True)
        y_arr = y.loc[valid].to_numpy(dtype=float)
        groups = part.loc[valid, "source_id"].astype(str).to_numpy()
        splitter = GroupKFold(n_splits=5)

        for estimator_name, pipe in model_pipelines.items():
            preds = np.empty_like(y_arr, dtype=float)
            fold_r2: list[float] = []
            fold_pearson: list[float] = []
            fold_spearman: list[float] = []

            for train_idx, test_idx in splitter.split(X, y_arr, groups):
                pipe.fit(X.iloc[train_idx], y_arr[train_idx])
                pred = pipe.predict(X.iloc[test_idx])
                preds[test_idx] = pred
                fold_r2.append(float(r2_score(y_arr[test_idx], pred)))
                fold_pearson.append(safe_pearson(y_arr[test_idx], pred))
                fold_spearman.append(safe_spearman(y_arr[test_idx], pred))

            rows.append(
                {
                    "dataset": "individual_papers",
                    "model": model_name,
                    "model_display": MODEL_DISPLAY[model_name],
                    "predictive_model": estimator_name,
                    "n_rows": int(len(y_arr)),
                    "n_groups": int(len(np.unique(groups))),
                    "cv_r2": float(r2_score(y_arr, preds)),
                    "cv_pearson_r": safe_pearson(y_arr, preds),
                    "cv_spearman_rho": safe_spearman(y_arr, preds),
                    "mean_fold_r2": float(np.mean(fold_r2)),
                    "sd_fold_r2": float(np.std(fold_r2, ddof=1)),
                    "mean_fold_pearson_r": safe_nanmean(fold_pearson),
                    "sd_fold_pearson_r": safe_nanstd(fold_pearson),
                    "mean_fold_spearman_rho": safe_nanmean(fold_spearman),
                    "sd_fold_spearman_rho": safe_nanstd(fold_spearman),
                }
            )

    return pd.DataFrame(rows)


def summarize_best(results: pd.DataFrame) -> pd.DataFrame:
    return (
        results.sort_values(["model", "cv_r2", "cv_pearson_r", "cv_spearman_rho"], ascending=[True, False, False, False])
        .groupby("model", as_index=False)
        .head(1)
        .reset_index(drop=True)
    )


def write_documentation(results: pd.DataFrame, best: pd.DataFrame) -> None:
    doc = f"""# figure4_predictive_model_benchmark

## Purpose
Expanded predictive-model benchmark for the `260427` paper-only metadata task used alongside Figure 4.

## Task
- Dataset: individual papers only
- Models scored: `Claude Sonnet 4.6`, `GPT-4.1`, `Gemini 2.5 Pro`
- Target: raw augmented performance, `Corr(y_true, y_pred)`
- Features: same paper-level metadata features used in Figure 4

## Construction
1. Build the same individual-paper metadata dataset used by the Figure 4 coefficient and permutation panels.
2. Evaluate each estimator separately within each LLM.
3. Use grouped 5-fold cross-validation by paper ID.
4. Record overall cross-validated `R^2`, Pearson `r`, and Spearman `rho`, plus fold means and standard deviations.

## Estimators
- `ols`: unregularized linear regression
- `ridge`: `RidgeCV(alphas=np.logspace(-3, 3, 13))`
- `elastic_net`: `ElasticNetCV` with `l1_ratio` grid `[0.05, 0.2, 0.5, 0.8, 0.95, 1.0]`
- `random_forest`
- `extra_trees`
- `gradient_boosting`
- `mlp`: one hidden-layer neural-network baseline with early stopping

## Output files
- Full benchmark table: `{BENCHMARK_CSV.relative_to(ROOT)}`
- Best-by-model summary: `{BEST_CSV.relative_to(ROOT)}`
- Documentation: `{DOC_MD.relative_to(ROOT)}`
- Script: `{Path(__file__).resolve().relative_to(ROOT)}`

## Benchmark rows
{results.to_markdown(index=False)}

## Best estimator by model
{best.to_markdown(index=False)}
"""
    DOC_MD.write_text(doc, encoding="utf-8")


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    df = build_individual_df().loc[lambda frame: frame["model"].isin(MODELS)].copy()
    results = evaluate_models(df)
    best = summarize_best(results)
    results.to_csv(BENCHMARK_CSV, index=False)
    best.to_csv(BEST_CSV, index=False)
    write_documentation(results, best)
    print(f"Wrote {BENCHMARK_CSV.relative_to(ROOT)}")
    print(f"Wrote {BEST_CSV.relative_to(ROOT)}")
    print(f"Wrote {DOC_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
