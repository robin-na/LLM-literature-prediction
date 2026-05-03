from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shap
from sklearn.ensemble import ExtraTreesRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GroupKFold


ROOT = Path(__file__).resolve().parents[1]
COLLECTION_REL_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_metadata_filters"
    / "validation_literature_collection_analysis_report_metadata_filters_relationship_dataset.csv"
)
PAPER_META_CSV = (
    ROOT
    / "literature"
    / "output"
    / "evidence_cards"
    / "literature_evidence_cards_cleaned"
    / "collection_metadata_sets"
    / "collection_metadata_catalog.csv"
)
BENCHMARK_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_metadata_supervised_benchmarks"
    / "literature_metadata_supervised_model_benchmark.csv"
)

RESULTS_DIR = ROOT / "results" / "paper" / "robustness"
PLOTS_DIR = ROOT / "plots" / "paper" / "exploratory"
PLOT_PNG = PLOTS_DIR / "collection_nonlinear_feature_importance.png"
PLOT_PDF = PLOTS_DIR / "collection_nonlinear_feature_importance.pdf"
PERM_CSV = RESULTS_DIR / "collection_nonlinear_feature_importance_permutation.csv"
SHAP_CSV = RESULTS_DIR / "collection_nonlinear_feature_importance_shap.csv"
GROUP_CSV = RESULTS_DIR / "collection_nonlinear_feature_importance_grouped.csv"
BEST_MODEL_CSV = RESULTS_DIR / "collection_nonlinear_feature_importance_best_models.csv"

MODELS = ["GPT-4.1", "GPT-4.1 Mini", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
MODEL_COLORS = {
    "GPT-4.1": "#4c78a8",
    "GPT-4.1 Mini": "#72b7b2",
    "GPT-5.1": "#e45756",
    "GPT-5 Mini": "#f2cf5b",
    "GPT-5 Nano": "#b279a2",
}
FEATURE_LABELS = {
    "journal_impact": "Higher journal impact factor",
    "citation": "Higher citation",
    "empirical_share": "Empirical papers",
    "recent": "More recent paper",
    "biology_share": "Biology Journals",
    "economics_share": "Economics Journals",
    "psychology_share": "Psychology Journals",
    "mathphysics_share": "Math/Physics Journals",
    "multidisciplinary_share": "Multidisciplinary Journals",
    "collection_size": "Larger collection size",
}
FEATURE_GROUPS = {
    "Higher journal impact factor": "Journal quality",
    "Higher citation": "Citation",
    "Empirical papers": "Paper type",
    "More recent paper": "Recency",
    "Larger collection size": "Collection size",
    "Biology Journals": "Journal discipline mix",
    "Economics Journals": "Journal discipline mix",
    "Psychology Journals": "Journal discipline mix",
    "Math/Physics Journals": "Journal discipline mix",
    "Multidisciplinary Journals": "Journal discipline mix",
}
FEATURE_ORDER_KEYS = [
    "journal_impact",
    "citation",
    "empirical_share",
    "recent",
    "biology_share",
    "economics_share",
    "psychology_share",
    "mathphysics_share",
    "multidisciplinary_share",
    "collection_size",
]
RNG = np.random.default_rng(42)
N_REPEATS = 60


def _discipline_indicators(series: pd.Series) -> pd.DataFrame:
    text = series.fillna("").astype(str)
    return pd.DataFrame(
        {
            "biology_share": text.str.contains("bio_evo", regex=False).astype(float),
            "economics_share": text.str.contains("economics", regex=False).astype(float),
            "psychology_share": text.str.contains("psych_social", regex=False).astype(float),
            "mathphysics_share": text.str.contains("math_phys_cs", regex=False).astype(float),
            "multidisciplinary_share": text.str.contains("multidisciplinary", regex=False).astype(float),
        }
    )


def load_collection_feature_frame() -> pd.DataFrame:
    catalog = pd.read_csv(PAPER_META_CSV).copy()
    catalog["custom_id"] = catalog["custom_id"].astype(str)
    catalog["journal_impact"] = np.log1p(pd.to_numeric(catalog["jif_value"], errors="coerce"))
    catalog["citation"] = np.log1p(pd.to_numeric(catalog["Times Cited, All Databases"], errors="coerce").clip(lower=0))
    catalog["empirical_share"] = catalog["paper_type_primary"].map({"theory": 0.0, "empirical": 1.0})
    catalog["recent"] = pd.to_numeric(catalog["Publication Year"], errors="coerce")
    catalog = pd.concat([catalog, _discipline_indicators(catalog["discipline_coarse"])], axis=1)
    catalog = catalog.set_index("custom_id")

    rel = pd.read_csv(COLLECTION_REL_CSV)
    rel = rel.loc[
        (rel["model"].isin(MODELS))
        & (rel["variant_group"] == "metadata_filter")
        & rel["delta_correlation"].notna()
    ].copy()

    rows: list[dict[str, object]] = []
    cache: dict[str, dict[str, float]] = {}
    for row in rel[["variant_id", "set_path", "log_count"]].drop_duplicates("variant_id").itertuples(index=False):
        variant_id = str(row.variant_id)
        set_path = ROOT / str(row.set_path)
        if variant_id not in cache:
            set_df = pd.read_csv(set_path)
            members = catalog.reindex(set_df["custom_id"].astype(str))
            cache[variant_id] = {
                "journal_impact": float(members["journal_impact"].mean()),
                "citation": float(members["citation"].mean()),
                "empirical_share": float(members["empirical_share"].mean()),
                "recent": float(members["recent"].mean()),
                "biology_share": float(members["biology_share"].mean()),
                "economics_share": float(members["economics_share"].mean()),
                "psychology_share": float(members["psychology_share"].mean()),
                "mathphysics_share": float(members["mathphysics_share"].mean()),
                "multidisciplinary_share": float(members["multidisciplinary_share"].mean()),
                "collection_size": float(row.log_count),
            }
        rows.append({"variant_id": variant_id, **cache[variant_id]})

    comp = pd.DataFrame(rows)
    return rel.merge(comp, on="variant_id", how="left", validate="many_to_one")


def build_model(model_name: str):
    if model_name == "gradient_boosting":
        return GradientBoostingRegressor(
            n_estimators=200,
            learning_rate=0.05,
            max_depth=3,
            random_state=42,
        )
    if model_name == "extra_trees":
        return ExtraTreesRegressor(
            n_estimators=250,
            min_samples_leaf=3,
            random_state=42,
            n_jobs=-1,
        )
    if model_name == "random_forest":
        return RandomForestRegressor(
            n_estimators=200,
            min_samples_leaf=5,
            random_state=42,
            n_jobs=-1,
        )
    raise ValueError(model_name)


def load_best_models() -> pd.DataFrame:
    bench = pd.read_csv(BENCHMARK_CSV)
    bench = bench.loc[
        (bench["dataset"] == "metadata_filter_collections")
        & (bench["target"] == "delta_correlation")
        & (bench["scope"] == "within_model")
        & (bench["scope_name"].isin(MODELS))
        & (bench["model_name"].isin(["gradient_boosting", "extra_trees", "random_forest"]))
    ].copy()
    best = (
        bench.sort_values(["scope_name", "cv_r2", "cv_spearman"], ascending=[True, False, False])
        .groupby("scope_name", as_index=False)
        .head(1)
        .rename(columns={"scope_name": "model"})
        .reset_index(drop=True)
    )
    return best[["model", "model_name", "cv_r2", "cv_spearman"]]


def permutation_importance_cv(
    X: pd.DataFrame,
    y: np.ndarray,
    groups: np.ndarray,
    estimator_name: str,
) -> pd.DataFrame:
    splitter = GroupKFold(n_splits=5)
    rows: list[dict[str, float]] = []

    for fold, (train_idx, test_idx) in enumerate(splitter.split(X, y, groups), start=1):
        model = build_model(estimator_name)
        X_train = X.iloc[train_idx].reset_index(drop=True)
        X_test = X.iloc[test_idx].reset_index(drop=True)
        y_train = y[train_idx]
        y_test = y[test_idx]
        model.fit(X_train, y_train)
        base_pred = model.predict(X_test)
        base_rmse = float(np.sqrt(mean_squared_error(y_test, base_pred)))
        for feature in X.columns:
            deltas = []
            for _ in range(N_REPEATS):
                perm = X_test.copy()
                perm[feature] = RNG.permutation(perm[feature].to_numpy())
                pred = model.predict(perm)
                perm_rmse = float(np.sqrt(mean_squared_error(y_test, pred)))
                deltas.append(100.0 * (perm_rmse - base_rmse) / base_rmse)
            rows.append(
                {
                    "fold": fold,
                    "feature_key": feature,
                    "importance_pct_rmse_increase": float(np.mean(deltas)),
                }
            )

    out = pd.DataFrame(rows)
    summary = (
        out.groupby("feature_key", as_index=False)
        .agg(
            mean_importance=("importance_pct_rmse_increase", "mean"),
            sd_importance=("importance_pct_rmse_increase", "std"),
            n_folds=("importance_pct_rmse_increase", "size"),
        )
    )
    summary["se_importance"] = summary["sd_importance"] / np.sqrt(summary["n_folds"])
    return summary


def shap_summary(X: pd.DataFrame, y: np.ndarray, estimator_name: str) -> pd.DataFrame:
    model = build_model(estimator_name)
    model.fit(X, y)
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)
    z = X.apply(lambda col: (col - col.mean()) / (col.std(ddof=0) if col.std(ddof=0) > 0 else 1.0))
    rows = []
    for j, feature in enumerate(X.columns):
        sv = np.asarray(shap_values[:, j], dtype=float)
        zv = z.iloc[:, j].to_numpy(dtype=float)
        rows.append(
            {
                "feature_key": feature,
                "mean_abs_shap": float(np.mean(np.abs(sv))),
                "signed_shap_effect": float(np.mean(sv * zv)),
            }
        )
    return pd.DataFrame(rows)


def build_outputs() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    df = load_collection_feature_frame()
    best_models = load_best_models()
    perm_rows = []
    shap_rows = []
    for model in MODELS:
        estimator_name = best_models.loc[best_models["model"] == model, "model_name"].iloc[0]
        part = df.loc[df["model"] == model].copy().sort_values("variant_id").reset_index(drop=True)
        X = part[FEATURE_ORDER_KEYS].apply(pd.to_numeric, errors="coerce")
        y = pd.to_numeric(part["delta_correlation"], errors="coerce").to_numpy(dtype=float)
        groups = part["variant_id"].astype(str).to_numpy()

        perm = permutation_importance_cv(X, y, groups, estimator_name)
        perm["model"] = model
        perm["model_name"] = estimator_name
        perm_rows.append(perm)

        shap_df = shap_summary(X, y, estimator_name)
        shap_df["model"] = model
        shap_df["model_name"] = estimator_name
        shap_rows.append(shap_df)

    perm_df = pd.concat(perm_rows, ignore_index=True)
    shap_df = pd.concat(shap_rows, ignore_index=True)
    perm_df["feature_label"] = perm_df["feature_key"].map(FEATURE_LABELS)
    shap_df["feature_label"] = shap_df["feature_key"].map(FEATURE_LABELS)

    grouped = (
        perm_df.assign(feature_group=lambda d: d["feature_label"].map(FEATURE_GROUPS))
        .groupby(["model", "model_name", "feature_group"], as_index=False)
        .agg(group_mean_importance=("mean_importance", "sum"))
    )
    return perm_df, shap_df, grouped, best_models


def feature_order(perm_df: pd.DataFrame) -> list[str]:
    order = (
        perm_df.groupby("feature_label", as_index=False)
        .agg(mean_importance=("mean_importance", "mean"))
        .sort_values("mean_importance", ascending=False)
    )
    return order["feature_label"].tolist()


def draw_figure(perm_df: pd.DataFrame, shap_df: pd.DataFrame) -> None:
    order = feature_order(perm_df)
    base_y = np.arange(len(order))[::-1].astype(float)
    y_map = dict(zip(order, base_y))
    offsets = np.linspace(-0.24, 0.24, len(MODELS))

    shap_map = shap_df.set_index(["model", "feature_label"])
    perm_finite = perm_df[["mean_importance", "se_importance"]].to_numpy(dtype=float).ravel()
    perm_xlim = float(np.nanmax(perm_df["mean_importance"] + perm_df["se_importance"])) * 1.15
    shap_xlim = max(0.002, float(np.nanmax(np.abs(shap_df["signed_shap_effect"]))) * 1.15)

    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(12.8, 5.8), gridspec_kw={"wspace": 0.28})

    for offset, model in zip(offsets, MODELS):
        p = perm_df.loc[perm_df["model"] == model].copy()
        ys = [y_map[label] + offset for label in p["feature_label"]]
        ax_left.errorbar(
            p["mean_importance"],
            ys,
            xerr=p["se_importance"],
            fmt="o",
            ms=5.0,
            lw=0,
            elinewidth=1.1,
            capsize=2.2,
            color=MODEL_COLORS[model],
            ecolor=MODEL_COLORS[model],
            alpha=0.95,
            zorder=3,
        )

        xs = [float(shap_map.loc[(model, label), "signed_shap_effect"]) for label in order]
        ax_right.scatter(xs, ys, s=28, color=MODEL_COLORS[model], alpha=0.95, zorder=3)

    ax_left.axvline(0.0, color="#777777", lw=1.0, ls=(0, (4, 3)), zorder=1)
    ax_right.axvline(0.0, color="#777777", lw=1.0, ls=(0, (4, 3)), zorder=1)

    for ax in (ax_left, ax_right):
        ax.set_yticks(base_y)
        ax.set_yticklabels(order)
        ax.tick_params(axis="y", length=0)
        ax.grid(axis="x", color="#e6e6e6", lw=0.8)
        ax.set_axisbelow(True)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_color("#cfcfcf")

    ax_left.set_xlim(-0.2, perm_xlim)
    ax_left.set_xlabel("Permutation importance\n(% increase in prediction RMSE)")
    ax_left.set_title("Permutation Importance", fontsize=13, pad=8)

    ax_right.set_xlim(-shap_xlim, shap_xlim)
    ax_right.set_xlabel("Signed SHAP summary\n(higher feature value -> predicted gain)")
    ax_right.set_title("SHAP Direction", fontsize=13, pad=8)
    ax_right.set_yticklabels([])

    handles = [
        plt.Line2D([0], [0], marker="o", linestyle="none", markersize=6, color=MODEL_COLORS[m], label=m)
        for m in MODELS
    ]
    fig.legend(
        handles=handles,
        loc="upper center",
        ncol=5,
        frameon=False,
        bbox_to_anchor=(0.5, 0.99),
        columnspacing=1.1,
        handletextpad=0.3,
    )
    fig.subplots_adjust(left=0.31, right=0.98, top=0.86, bottom=0.12)
    fig.savefig(PLOT_PNG, dpi=300)
    fig.savefig(PLOT_PDF)
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    perm_df, shap_df, grouped_df, best_models = build_outputs()
    perm_df.to_csv(PERM_CSV, index=False)
    shap_df.to_csv(SHAP_CSV, index=False)
    grouped_df.to_csv(GROUP_CSV, index=False)
    best_models.to_csv(BEST_MODEL_CSV, index=False)
    draw_figure(perm_df, shap_df)


if __name__ == "__main__":
    main()
