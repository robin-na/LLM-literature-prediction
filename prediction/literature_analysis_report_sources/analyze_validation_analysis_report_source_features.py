from __future__ import annotations

import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf


ROOT = Path(__file__).resolve().parents[2]
PERF_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_analysis_report_sources_repeat5"
    / "validation_literature_analysis_report_source_significance.csv"
)
PAPERS_CSV = (
    ROOT
    / "literature"
    / "output"
    / "evidence_cards"
    / "literature_evidence_cards_cleaned"
    / "papers.csv"
)
DIMENSIONS_CSV = (
    ROOT
    / "literature"
    / "output"
    / "evidence_cards"
    / "literature_evidence_cards_cleaned"
    / "dimensions.csv"
)
METADATA_CSV = ROOT / "paper_collection" / "WoS_251031_fileInfo.csv"
RESULTS_DIR = ROOT / "results" / "validation" / "literature_analysis_report_source_features"

FEATURES = [
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
METRICS = [
    "delta_correlation",
    "delta_rmse",
    "delta_r2",
    "delta_directional_accuracy",
]
MIXED_METRICS = ["delta_correlation", "delta_rmse"]
MODELS = ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]


def load_analysis_frame() -> pd.DataFrame:
    perf = pd.read_csv(PERF_CSV)
    papers = pd.read_csv(PAPERS_CSV).rename(columns={"custom_id": "source_id"})
    dims = pd.read_csv(DIMENSIONS_CSV)
    meta = pd.read_csv(METADATA_CSV)
    meta = meta.loc[meta["custom_id"].notna()].copy()
    meta["source_id"] = meta["custom_id"].astype(str).map(lambda value: Path(value).stem)
    meta = meta.drop_duplicates("source_id", keep="first")

    feat = papers[
        [
            "source_id",
            "paper_type_primary",
            "relevance_pgg_or_variant",
            "relevance_punishment_or_sanctions",
            "relevance_efficiency_or_related_payoff_outcome",
            "outcomes_primary_outcome_type",
            "dimension_contextual_or_better_count",
            "dimension_informative_direct_count",
        ]
    ].copy()
    feat["empirical"] = feat["paper_type_primary"].eq("empirical")
    feat["exactclose_domain"] = feat["relevance_pgg_or_variant"].isin(["exact", "close"]) & feat[
        "relevance_punishment_or_sanctions"
    ].isin(["exact", "close"])
    feat["payoff_relevance_exactclose"] = feat[
        "relevance_efficiency_or_related_payoff_outcome"
    ].isin(["exact", "close"])
    feat["payoff_outcome_primary"] = feat["outcomes_primary_outcome_type"].isin(
        ["efficiency_or_payoff", "mixed"]
    )
    feat["broad_only_count"] = (
        feat["dimension_contextual_or_better_count"]
        - feat["dimension_informative_direct_count"]
    )

    dim_pivot = dims.pivot(index="custom_id", columns="dimension", values="evidence_tier")
    discussed_levels = {"informative_direct", "informative_indirect", "contextual", "mention_only"}
    for dim in ["chat", "show_other_summaries", "show_punishment_id"]:
        feat[f"{dim}_discussed"] = (
            dim_pivot[dim]
            .reindex(feat["source_id"])
            .fillna("N/R")
            .isin(discussed_levels)
            .to_numpy()
        )

    meta2 = meta[
        ["source_id", "Publication Year", "Times Cited, WoS Core", "Number of Pages"]
    ].rename(
        columns={
            "Publication Year": "pub_year",
            "Times Cited, WoS Core": "times_cited_wos",
            "Number of Pages": "n_pages",
        }
    )

    df = perf.merge(feat, on="source_id", how="left").merge(meta2, on="source_id", how="left")

    numeric_cols = [
        "times_cited_wos",
        "n_pages",
        "pub_year",
        "dimension_informative_direct_count",
        "broad_only_count",
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())
        std = float(df[col].std())
        df[f"{col}_z"] = (df[col] - df[col].mean()) / (std if np.isfinite(std) and std > 0 else 1.0)

    log_citations = np.log1p(df["times_cited_wos"])
    log_std = float(log_citations.std())
    df["log_citations_z"] = (log_citations - log_citations.mean()) / (
        log_std if np.isfinite(log_std) and log_std > 0 else 1.0
    )

    use_cols = (
        ["model", "mode", "source_id", "title", "journal", "year"]
        + METRICS
        + FEATURES
    )
    return df[use_cols].dropna().reset_index(drop=True)


def fit_pooled_models(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    fit_rows: list[dict[str, object]] = []
    coef_rows: list[dict[str, object]] = []

    for metric in METRICS:
        model_only = smf.ols(f"{metric} ~ C(model)", data=df).fit()
        full = smf.ols(f"{metric} ~ C(model) + {' + '.join(FEATURES)}", data=df).fit(
            cov_type="cluster",
            cov_kwds={"groups": df["source_id"]},
        )
        fit_rows.append(
            {
                "metric": metric,
                "spec": "pooled_clustered",
                "n_obs": int(full.nobs),
                "r2_model_only": float(model_only.rsquared),
                "r2_full": float(full.rsquared),
                "r2_increment_from_features": float(full.rsquared - model_only.rsquared),
                "adj_r2_full": float(full.rsquared_adj),
            }
        )
        for term in full.params.index:
            coef_rows.append(
                {
                    "metric": metric,
                    "spec": "pooled_clustered",
                    "term": term,
                    "coef": float(full.params[term]),
                    "std_err": float(full.bse[term]),
                    "p_value": float(full.pvalues[term]),
                }
            )

    return pd.DataFrame(fit_rows), pd.DataFrame(coef_rows)


def fit_model_specific_ols(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    fit_rows: list[dict[str, object]] = []
    coef_rows: list[dict[str, object]] = []

    formula_rhs = " + ".join(FEATURES)
    for metric in METRICS:
        for model in MODELS:
            part = df.loc[df["model"] == model].copy()
            result = smf.ols(f"{metric} ~ {formula_rhs}", data=part).fit()
            fit_rows.append(
                {
                    "metric": metric,
                    "spec": "model_specific_ols",
                    "model": model,
                    "n_obs": int(result.nobs),
                    "r2_full": float(result.rsquared),
                    "adj_r2_full": float(result.rsquared_adj),
                }
            )
            for term in result.params.index:
                coef_rows.append(
                    {
                        "metric": metric,
                        "spec": "model_specific_ols",
                        "model": model,
                        "term": term,
                        "coef": float(result.params[term]),
                        "std_err": float(result.bse[term]),
                        "p_value": float(result.pvalues[term]),
                    }
                )

    return pd.DataFrame(fit_rows), pd.DataFrame(coef_rows)


def build_sign_consistency(model_coef: pd.DataFrame) -> pd.DataFrame:
    part = model_coef.loc[model_coef["term"] != "Intercept"].copy()
    pivot = part.pivot_table(
        index=["metric", "term"],
        columns="model",
        values="coef",
        aggfunc="first",
    )
    pval = part.pivot_table(
        index=["metric", "term"],
        columns="model",
        values="p_value",
        aggfunc="first",
    )
    sign_df = np.sign(pivot).rename(columns=lambda col: f"{col}_sign")
    out = pd.concat([pivot, sign_df, pval.rename(columns=lambda col: f"{col}_p")], axis=1).reset_index()

    sign_cols = [f"{model}_sign" for model in MODELS]
    p_cols = [f"{model}_p" for model in MODELS]
    out["all_same_sign"] = out[sign_cols].nunique(axis=1) == 1
    out["n_models_p_lt_0_05"] = (out[p_cols] < 0.05).sum(axis=1)
    out["all_same_sign_and_p_lt_0_05"] = out["all_same_sign"] & (out["n_models_p_lt_0_05"] == len(MODELS))
    return out.sort_values(["metric", "term"]).reset_index(drop=True)


def fit_mixedlm(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    fit_rows: list[dict[str, object]] = []
    coef_rows: list[dict[str, object]] = []
    formula_rhs = " + ".join(FEATURES)

    for metric in MIXED_METRICS:
        try:
            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter("always")
                model = smf.mixedlm(
                    f"{metric} ~ C(model) + {formula_rhs}",
                    data=df,
                    groups=df["source_id"],
                )
                result = model.fit(reml=False, method="lbfgs", maxiter=200, disp=False)
            fit_rows.append(
                {
                    "metric": metric,
                    "spec": "mixedlm_random_intercept",
                    "converged": bool(getattr(result, "converged", False)),
                    "n_obs": int(result.nobs),
                    "n_groups": int(df["source_id"].nunique()),
                    "group_var": float(result.cov_re.iloc[0, 0]),
                    "scale": float(result.scale),
                    "warning_count": len(caught),
                    "warnings": " | ".join(str(w.message) for w in caught),
                }
            )
            for term, coef in result.params.items():
                if term == "Group Var":
                    continue
                coef_rows.append(
                    {
                        "metric": metric,
                        "spec": "mixedlm_random_intercept",
                        "term": term,
                        "coef": float(coef),
                        "std_err": float(result.bse.get(term, np.nan)),
                        "p_value": float(result.pvalues.get(term, np.nan)),
                    }
                )
        except Exception as exc:  # pragma: no cover - exploratory fallback
            fit_rows.append(
                {
                    "metric": metric,
                    "spec": "mixedlm_random_intercept",
                    "converged": False,
                    "n_obs": int(len(df)),
                    "n_groups": int(df["source_id"].nunique()),
                    "group_var": np.nan,
                    "scale": np.nan,
                    "warning_count": np.nan,
                    "warnings": f"FAILED: {exc}",
                }
            )

    return pd.DataFrame(fit_rows), pd.DataFrame(coef_rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    df = load_analysis_frame()
    pooled_fit, pooled_coef = fit_pooled_models(df)
    model_fit, model_coef = fit_model_specific_ols(df)
    sign_consistency = build_sign_consistency(model_coef)
    mixed_fit, mixed_coef = fit_mixedlm(df)

    df.to_csv(RESULTS_DIR / "paper_feature_analysis_dataset.csv", index=False)
    pooled_fit.to_csv(RESULTS_DIR / "paper_feature_pooled_fit_summary.csv", index=False)
    pooled_coef.to_csv(RESULTS_DIR / "paper_feature_pooled_coefficients.csv", index=False)
    model_fit.to_csv(RESULTS_DIR / "paper_feature_model_specific_fit_summary.csv", index=False)
    model_coef.to_csv(RESULTS_DIR / "paper_feature_model_specific_coefficients.csv", index=False)
    sign_consistency.to_csv(RESULTS_DIR / "paper_feature_sign_consistency.csv", index=False)
    mixed_fit.to_csv(RESULTS_DIR / "paper_feature_mixedlm_fit_summary.csv", index=False)
    mixed_coef.to_csv(RESULTS_DIR / "paper_feature_mixedlm_coefficients.csv", index=False)

    print(RESULTS_DIR / "paper_feature_analysis_dataset.csv")
    print(RESULTS_DIR / "paper_feature_pooled_fit_summary.csv")
    print(RESULTS_DIR / "paper_feature_pooled_coefficients.csv")
    print(RESULTS_DIR / "paper_feature_model_specific_fit_summary.csv")
    print(RESULTS_DIR / "paper_feature_model_specific_coefficients.csv")
    print(RESULTS_DIR / "paper_feature_sign_consistency.csv")
    print(RESULTS_DIR / "paper_feature_mixedlm_fit_summary.csv")
    print(RESULTS_DIR / "paper_feature_mixedlm_coefficients.csv")


if __name__ == "__main__":
    main()
