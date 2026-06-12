from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch
from matplotlib.ticker import PercentFormatter
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

MAIN_RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures"
SI_RESULTS_DIR = ROOT / "results" / "paper" / "si_figures"
MAIN_PLOTS_DIR = ROOT / "plots" / "paper" / "main_text"
SI_PLOTS_DIR = ROOT / "plots" / "paper" / "si"

MAIN_MODEL = "GPT-4.1"
MODELS = ["GPT-4.1", "GPT-4.1 Mini", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
MODEL_SLUG = {
    "GPT-4.1": "gpt41",
    "GPT-4.1 Mini": "gpt41mini",
    "GPT-5.1": "gpt51",
    "GPT-5 Mini": "gpt5mini",
    "GPT-5 Nano": "gpt5nano",
}
FEATURE_LABELS = {
    "journal_impact": "Journal Impact Factor",
    "citation": "Citation",
    "empirical_share": "Empirical Papers",
    "recent": "Publication Year",
    "biology_share": "Biology Journals",
    "economics_share": "Economics Journals",
    "psychology_share": "Psychology Journals",
    "mathphysics_share": "Math/Physics Journals",
    "multidisciplinary_share": "Multidisciplinary Journals",
    "collection_size": "Number of Papers",
}
FEATURE_GROUPS = {
    "Journal Impact Factor": "Journal Quality / Attention",
    "Citation": "Journal Quality / Attention",
    "Publication Year": "Journal Quality / Attention",
    "Number of Papers": "Collection Characteristics",
    "Empirical Papers": "Paper Type",
    "Biology Journals": "Journal Discipline",
    "Economics Journals": "Journal Discipline",
    "Psychology Journals": "Journal Discipline",
    "Math/Physics Journals": "Journal Discipline",
    "Multidisciplinary Journals": "Journal Discipline",
}
GROUP_COLORS = {
    "Collection Characteristics": "#2166AC",
    "Journal Quality / Attention": "#92C5DE",
    "Journal Discipline": "#D6604D",
    "Paper Type": "#F4A582",
}
FEATURE_KEYS = [
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
NONLINEAR_MODELS = {"gradient_boosting", "extra_trees", "random_forest"}
RNG = np.random.default_rng(42)
N_PERM_REPEATS = 80
VALUE_CMAP = LinearSegmentedColormap.from_list("feature_value", ["#1e88e5", "#ff0d57"])


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
        if variant_id not in cache:
            set_df = pd.read_csv(ROOT / str(row.set_path))
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


def best_nonlinear_model_by_model() -> dict[str, str]:
    bench = pd.read_csv(BENCHMARK_CSV)
    bench = bench.loc[
        (bench["dataset"] == "metadata_filter_collections")
        & (bench["target"] == "delta_correlation")
        & (bench["scope"] == "within_model")
        & (bench["scope_name"].isin(MODELS))
        & (bench["model_name"].isin(NONLINEAR_MODELS))
    ].copy()
    best = (
        bench.sort_values(["scope_name", "cv_r2", "cv_spearman"], ascending=[True, False, False])
        .groupby("scope_name", as_index=False)
        .head(1)
    )
    return dict(zip(best["scope_name"], best["model_name"]))


def build_model(model_name: str):
    if model_name == "extra_trees":
        return ExtraTreesRegressor(
            n_estimators=250,
            min_samples_leaf=3,
            random_state=42,
            n_jobs=-1,
        )
    if model_name == "gradient_boosting":
        return GradientBoostingRegressor(
            n_estimators=200,
            learning_rate=0.05,
            max_depth=3,
            random_state=42,
        )
    if model_name == "random_forest":
        return RandomForestRegressor(
            n_estimators=200,
            min_samples_leaf=5,
            random_state=42,
            n_jobs=-1,
        )
    raise ValueError(model_name)


def compute_permutation_importance(X: pd.DataFrame, y: np.ndarray, groups: np.ndarray, estimator_name: str) -> pd.DataFrame:
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
            for _ in range(N_PERM_REPEATS):
                perm = X_test.copy()
                perm[feature] = RNG.permutation(perm[feature].to_numpy())
                pred = model.predict(perm)
                perm_rmse = float(np.sqrt(mean_squared_error(y_test, pred)))
                deltas.append(100.0 * (perm_rmse - base_rmse) / base_rmse)
            rows.append(
                {
                    "fold": fold,
                    "feature_key": feature,
                    "feature_label": FEATURE_LABELS[feature],
                    "importance_pct_rmse_increase": float(np.mean(deltas)),
                }
            )

    out = pd.DataFrame(rows)
    summary = (
        out.groupby(["feature_key", "feature_label"], as_index=False)
        .agg(
            mean_importance=("importance_pct_rmse_increase", "mean"),
            sd_importance=("importance_pct_rmse_increase", "std"),
            n_folds=("importance_pct_rmse_increase", "size"),
        )
    )
    summary["se_importance"] = summary["sd_importance"] / np.sqrt(summary["n_folds"])
    summary["feature_group"] = summary["feature_label"].map(FEATURE_GROUPS)
    return summary.sort_values("mean_importance", ascending=False).reset_index(drop=True)


def _normalized_feature_values(X: pd.DataFrame) -> pd.DataFrame:
    out = {}
    for col in X.columns:
        vals = X[col].to_numpy(dtype=float)
        lo = np.nanmin(vals)
        hi = np.nanmax(vals)
        if not np.isfinite(lo) or not np.isfinite(hi) or hi <= lo:
            out[col] = np.full_like(vals, 0.5, dtype=float)
        else:
            out[col] = (vals - lo) / (hi - lo)
    return pd.DataFrame(out)


def _beeswarm_offsets(values: np.ndarray, max_spread: float = 0.31, bins: int = 36) -> np.ndarray:
    if len(values) == 0:
        return np.array([])
    edges = np.linspace(values.min() - 1e-9, values.max() + 1e-9, bins + 1)
    bin_ids = np.digitize(values, edges) - 1
    offsets = np.zeros(len(values), dtype=float)
    for b in np.unique(bin_ids):
        idx = np.where(bin_ids == b)[0]
        if len(idx) <= 1:
            continue
        spread = np.linspace(-max_spread, max_spread, len(idx))
        order = np.argsort(values[idx])
        offsets[idx[order]] = spread
    return offsets


def compute_shap_tables(X: pd.DataFrame, y: np.ndarray, feature_order: list[str], estimator_name: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    model = build_model(estimator_name)
    model.fit(X, y)
    explainer = shap.TreeExplainer(model)
    shap_values = np.asarray(explainer.shap_values(X), dtype=float)
    norm_vals = _normalized_feature_values(X)

    points = []
    summary_rows = []
    for feature in feature_order:
        j = X.columns.get_loc(feature)
        sv = shap_values[:, j]
        color_val = norm_vals[feature].to_numpy(dtype=float)
        offsets = _beeswarm_offsets(sv)
        summary_rows.append(
            {
                "feature_key": feature,
                "feature_label": FEATURE_LABELS[feature],
                "mean_abs_shap": float(np.mean(np.abs(sv))),
                "mean_signed_shap": float(np.mean(sv)),
            }
        )
        for i in range(len(X)):
            points.append(
                {
                    "feature_key": feature,
                    "feature_label": FEATURE_LABELS[feature],
                    "shap_value": float(sv[i]),
                    "feature_value_raw": float(X.iloc[i, j]),
                    "feature_value_norm": float(color_val[i]),
                    "y_offset": float(offsets[i]),
                }
            )

    return pd.DataFrame(points), pd.DataFrame(summary_rows)


def draw_figure(
    model_name: str,
    estimator_name: str,
    perm_df: pd.DataFrame,
    shap_points: pd.DataFrame,
    out_png: Path,
    out_pdf: Path,
) -> None:
    order_labels = perm_df["feature_label"].tolist()
    base_y = np.arange(len(order_labels))[::-1].astype(float)
    y_map = dict(zip(order_labels, base_y))

    mpl.rcParams["pdf.fonttype"] = 42
    mpl.rcParams["ps.fonttype"] = 42
    mpl.rcParams["font.sans-serif"] = ["Arial"]
    mpl.rcParams["font.family"] = "sans-serif"

    fig = plt.figure(figsize=(12.2, 7.8), dpi=300)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.04, 1.0], wspace=0.12)
    ax_left = fig.add_subplot(gs[0, 0])
    ax_right = fig.add_subplot(gs[0, 1])

    y_positions = [y_map[label] for label in perm_df["feature_label"]]
    colors = [GROUP_COLORS[group] for group in perm_df["feature_group"]]
    ax_left.barh(
        y_positions,
        perm_df["mean_importance"],
        color=colors,
        edgecolor="none",
        height=0.72,
        zorder=2,
    )
    ax_left.errorbar(
        perm_df["mean_importance"],
        y_positions,
        xerr=perm_df["se_importance"],
        fmt="none",
        ecolor="#444444",
        elinewidth=1.05,
        capsize=3,
        zorder=3,
    )
    ax_left.axvline(0.0, linestyle="--", color="#8f8f8f", linewidth=1.0, zorder=1)
    ax_left.set_yticks(base_y)
    ax_left.set_yticklabels(order_labels)
    ax_left.set_xlabel("Permutation Feature Importance\n(% increase in prediction RMSE)", fontsize=14, labelpad=12)
    ax_left.xaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
    ax_left.tick_params(axis="both", which="major", labelsize=11, length=4, width=0.8)
    ax_left.spines["top"].set_visible(False)
    ax_left.spines["right"].set_visible(False)
    ax_left.spines["left"].set_linewidth(0.8)
    ax_left.spines["bottom"].set_linewidth(0.8)
    ax_left.set_title("A", loc="left", fontsize=20, fontweight="bold", pad=14)

    shap_min = float(shap_points["shap_value"].min())
    shap_max = float(shap_points["shap_value"].max())
    xleft = min(shap_min, -1e-4)
    xright = max(shap_max, 1e-4)
    for y in base_y:
        ax_right.hlines(y, xmin=xleft, xmax=xright, colors="#d8d8d8", linewidth=1.0, linestyles=(0, (1, 4)), zorder=0)
    for label in order_labels:
        part = shap_points.loc[shap_points["feature_label"] == label].copy()
        y = y_map[label] + part["y_offset"].to_numpy(dtype=float)
        ax_right.scatter(
            part["shap_value"],
            y,
            c=part["feature_value_norm"],
            cmap=VALUE_CMAP,
            s=28,
            alpha=0.60,
            edgecolors="none",
            rasterized=True,
        )

    shap_xlim = max(0.01, float(np.quantile(np.abs(shap_points["shap_value"]), 0.995)) * 1.05)
    ax_right.axvline(0.0, color="#9a9a9a", linewidth=2.0, zorder=1)
    ax_right.set_xlim(-shap_xlim, shap_xlim)
    ax_right.set_yticks(base_y)
    ax_right.set_yticklabels([])
    ax_right.tick_params(axis="y", length=0)
    ax_right.tick_params(axis="x", which="major", labelsize=11, length=4, width=0.8)
    ax_right.spines["top"].set_visible(False)
    ax_right.spines["right"].set_visible(False)
    ax_right.spines["left"].set_visible(False)
    ax_right.spines["bottom"].set_linewidth(0.8)
    ax_right.set_xlabel("SHAP Value\n(impact on prediction)", fontsize=14, labelpad=12)
    ax_right.set_title("B", loc="left", fontsize=20, fontweight="bold", pad=14)

    legend_elements = [
        Patch(facecolor=color, edgecolor="none", label=group)
        for group, color in GROUP_COLORS.items()
    ]
    ax_left.legend(
        handles=legend_elements,
        loc="lower right",
        frameon=False,
        fontsize=11,
        ncol=1,
    )

    norm = mpl.colors.Normalize(vmin=0, vmax=1)
    sm = plt.cm.ScalarMappable(cmap=VALUE_CMAP, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax_right, fraction=0.048, pad=0.06)
    cbar.set_label("Feature value", fontsize=14)
    cbar.set_ticks([0, 1])
    cbar.set_ticklabels(["Low", "High"])
    cbar.ax.tick_params(labelsize=11)
    cbar.outline.set_visible(False)

    fig.suptitle(f"{model_name} ({estimator_name.replace('_', ' ').title()})", x=0.53, y=0.985, fontsize=14)
    fig.subplots_adjust(left=0.29, right=0.95, top=0.93, bottom=0.13)
    fig.savefig(out_png, dpi=300)
    fig.savefig(out_pdf)
    plt.close(fig)


def output_paths(model_name: str) -> tuple[Path, Path, Path, Path, Path]:
    slug = MODEL_SLUG[model_name]
    if model_name == MAIN_MODEL:
        base = "figure8_collection_feature_importance_gpt41"
        return (
            MAIN_PLOTS_DIR / f"{base}.png",
            MAIN_PLOTS_DIR / f"{base}.pdf",
            MAIN_RESULTS_DIR / f"{base}_permutation.csv",
            MAIN_RESULTS_DIR / f"{base}_shap_points.csv",
            MAIN_RESULTS_DIR / f"{base}_shap_summary.csv",
        )
    base = f"figure8_collection_feature_importance_{slug}"
    return (
        SI_PLOTS_DIR / f"{base}.png",
        SI_PLOTS_DIR / f"{base}.pdf",
        SI_RESULTS_DIR / f"{base}_permutation.csv",
        SI_RESULTS_DIR / f"{base}_shap_points.csv",
        SI_RESULTS_DIR / f"{base}_shap_summary.csv",
    )


def main() -> None:
    MAIN_RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    SI_RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    MAIN_PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    SI_PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    best_models = best_nonlinear_model_by_model()
    df_all = load_collection_feature_frame()

    for model_name in MODELS:
        estimator_name = best_models[model_name]
        df = df_all.loc[df_all["model"] == model_name].sort_values("variant_id").reset_index(drop=True)
        X = df[FEATURE_KEYS].apply(pd.to_numeric, errors="coerce")
        y = pd.to_numeric(df["delta_correlation"], errors="coerce").to_numpy(dtype=float)
        groups = df["variant_id"].astype(str).to_numpy()

        perm_df = compute_permutation_importance(X, y, groups, estimator_name)
        shap_points, shap_summary = compute_shap_tables(X, y, perm_df["feature_key"].tolist(), estimator_name)
        out_png, out_pdf, perm_csv, shap_points_csv, shap_summary_csv = output_paths(model_name)
        perm_df.to_csv(perm_csv, index=False)
        shap_points.to_csv(shap_points_csv, index=False)
        shap_summary.to_csv(shap_summary_csv, index=False)
        draw_figure(model_name, estimator_name, perm_df, shap_points, out_png, out_pdf)


if __name__ == "__main__":
    main()
