from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import RidgeCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


ROOT = Path(__file__).resolve().parents[1]
PAPER_PERF_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_analysis_report_sources_repeat5"
    / "validation_literature_analysis_report_source_significance.csv"
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
COLLECTION_REL_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_metadata_filters"
    / "validation_literature_collection_analysis_report_metadata_filters_relationship_dataset.csv"
)

RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text"
FIGURE7_PNG = PLOTS_DIR / "figure7_individual_metadata_effect_robustness.png"
FIGURE7_PDF = PLOTS_DIR / "figure7_individual_metadata_effect_robustness.pdf"
FIGURE8_PNG = PLOTS_DIR / "figure8_collection_metadata_effect_robustness.png"
FIGURE8_PDF = PLOTS_DIR / "figure8_collection_metadata_effect_robustness.pdf"
FIGURE7_CSV = RESULTS_DIR / "figure7_individual_metadata_effect_robustness_rows.csv"
FIGURE8_CSV = RESULTS_DIR / "figure8_collection_metadata_effect_robustness_rows.csv"

MODELS = ["GPT-4.1", "GPT-4.1 Mini", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
MODEL_COLORS = {
    "GPT-4.1": "#4c78a8",
    "GPT-4.1 Mini": "#72b7b2",
    "GPT-5.1": "#e45756",
    "GPT-5 Mini": "#f2cf5b",
    "GPT-5 Nano": "#b279a2",
}
FEATURE_LABELS = {
    "journal_impact": "Journal Impact Factor",
    "citation": "Citation",
    "empirical_share": "Empirical papers",
    "recent": "Publication Year",
    "biology_share": "Biology Journals",
    "economics_share": "Economics Journals",
    "psychology_share": "Psychology Journals",
    "mathphysics_share": "Math/Physics Journals",
    "multidisciplinary_share": "Multidisciplinary Journals",
    "collection_size": "Number of Papers",
}
PAPER_FEATURES = [
    "journal_impact",
    "citation",
    "empirical_share",
    "recent",
    "biology_share",
    "economics_share",
    "psychology_share",
    "mathphysics_share",
    "multidisciplinary_share",
]
COLLECTION_FEATURES = PAPER_FEATURES + ["collection_size"]
N_BOOT = 400
RNG = np.random.default_rng(42)


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


def load_paper_df() -> pd.DataFrame:
    perf = pd.read_csv(PAPER_PERF_CSV)
    perf = perf.loc[(perf["model"].isin(MODELS)) & perf["delta_correlation"].notna()].copy()

    meta = pd.read_csv(PAPER_META_CSV).copy()
    meta["source_id"] = meta["custom_id"].astype(str).str.removesuffix(".md")
    meta = meta.drop_duplicates("source_id", keep="first")

    df = perf.merge(
        meta[
            [
                "source_id",
                "paper_type_primary",
                "Publication Year",
                "Times Cited, All Databases",
                "jif_value",
                "discipline_coarse",
            ]
        ],
        on="source_id",
        how="left",
        validate="many_to_one",
    )
    df["journal_impact"] = np.log1p(pd.to_numeric(df["jif_value"], errors="coerce"))
    df["citation"] = np.log1p(pd.to_numeric(df["Times Cited, All Databases"], errors="coerce").clip(lower=0))
    df["empirical_share"] = df["paper_type_primary"].map({"theory": 0.0, "empirical": 1.0})
    df["recent"] = pd.to_numeric(df["Publication Year"], errors="coerce")
    df = pd.concat([df, _discipline_indicators(df["discipline_coarse"])], axis=1)
    return df


def build_collection_feature_frame() -> pd.DataFrame:
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

    comp_rows: list[dict[str, object]] = []
    cache: dict[str, dict[str, float]] = {}
    for row in rel[["variant_id", "set_path", "count", "log_count"]].drop_duplicates("variant_id").itertuples(index=False):
        variant_id = str(row.variant_id)
        set_path = ROOT / str(row.set_path)
        if variant_id in cache:
            stats = cache[variant_id]
        else:
            set_df = pd.read_csv(set_path)
            members = catalog.reindex(set_df["custom_id"].astype(str))
            stats = {
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
            cache[variant_id] = stats
        comp_rows.append({"variant_id": variant_id, **stats})

    comp = pd.DataFrame(comp_rows)
    return rel.merge(comp, on="variant_id", how="left", validate="many_to_one")


def fit_ridge_bootstrap(df: pd.DataFrame, feature_cols: list[str], *, y_col: str = "delta_correlation") -> pd.DataFrame:
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
            ("model", RidgeCV(alphas=np.logspace(-3, 3, 13))),
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


def build_rows(df: pd.DataFrame, *, item_type: str, feature_cols: list[str]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for model in MODELS:
        part = df.loc[df["model"] == model].copy()
        coef_df = fit_ridge_bootstrap(part, feature_cols)
        for row in coef_df.itertuples(index=False):
            rows.append(
                {
                    "item_type": item_type,
                    "model": model,
                    "feature_key": row.feature_key,
                    "feature_label": FEATURE_LABELS[row.feature_key],
                    "coef": float(row.coef),
                    "ci_low": float(row.ci_low),
                    "ci_high": float(row.ci_high),
                    "n": int(row.n),
                }
            )
    return pd.DataFrame(rows)


def ordered_features(df: pd.DataFrame) -> list[str]:
    order = (
        df.groupby("feature_label", as_index=False)
        .agg(mean_coef=("coef", "mean"))
        .sort_values("mean_coef", ascending=False)
    )
    return order["feature_label"].tolist()


def draw_figure(df: pd.DataFrame, title: str | None, out_png: Path, out_pdf: Path) -> None:
    features = ordered_features(df)
    base_y = np.arange(len(features))[::-1].astype(float)
    y_map = dict(zip(features, base_y))
    offsets = np.linspace(-0.24, 0.24, len(MODELS))
    xlim = 0.02

    fig, ax = plt.subplots(1, 1, figsize=(7.0, 5.3))
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
            elinewidth=1.15,
            capsize=2.4,
            color=MODEL_COLORS[model],
            ecolor=MODEL_COLORS[model],
            alpha=0.95,
            zorder=3,
        )

    if title:
        ax.set_title(title, fontsize=13, pad=8)
    ax.set_yticks(base_y)
    ax.set_yticklabels(features)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="x", color="#e6e6e6", lw=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#cfcfcf")
    ax.set_xlim(-xlim, xlim)
    ax.set_xlabel("Standardized ridge coefficient on correlation gain")

    handles = [
        plt.Line2D([0], [0], marker="o", linestyle="none", markersize=6, color=MODEL_COLORS[model], label=model)
        for model in MODELS
    ]
    legend_y = 0.935 if not title else 0.955
    top_margin = 0.86 if not title else 0.83
    fig.legend(
        handles=handles,
        loc="upper center",
        ncol=5,
        frameon=False,
        bbox_to_anchor=(0.5, legend_y),
        columnspacing=1.1,
        handletextpad=0.3,
    )
    fig.subplots_adjust(left=0.46, right=0.98, top=top_margin, bottom=0.11)
    fig.savefig(out_png, dpi=300)
    fig.savefig(out_pdf)
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    paper_rows = build_rows(load_paper_df(), item_type="Individual papers", feature_cols=PAPER_FEATURES)
    collection_rows = build_rows(
        build_collection_feature_frame(),
        item_type="Collections",
        feature_cols=COLLECTION_FEATURES,
    )

    paper_rows.to_csv(FIGURE7_CSV, index=False)
    collection_rows.to_csv(FIGURE8_CSV, index=False)

    draw_figure(paper_rows, None, FIGURE7_PNG, FIGURE7_PDF)
    draw_figure(collection_rows, "Collections", FIGURE8_PNG, FIGURE8_PDF)


if __name__ == "__main__":
    main()
