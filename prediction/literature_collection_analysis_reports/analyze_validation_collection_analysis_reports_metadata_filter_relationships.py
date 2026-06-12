from __future__ import annotations

import re
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf


ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_metadata_filters"
ROWS_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_rows.csv"
META_CSV = (
    ROOT
    / "literature"
    / "output"
    / "evidence_cards"
    / "literature_evidence_cards_cleaned"
    / "collection_metadata_sets"
    / "collection_metadata_summary.csv"
)

MODEL_ORDER = ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
METRIC_SPECS = [
    ("delta_correlation", "correlation_gain", "Correlation gain"),
    ("delta_r2", "r2_gain", "R2 gain"),
    ("rmse_improvement", "rmse_improvement", "RMSE improvement"),
]
VALUE_COLUMNS = ["type_value", "citation_value", "jcr_value", "year_value", "discipline_value"]
VALUE_ORDER = {
    "type_value": ["empirical", "theoretical"],
    "citation_value": ["Q1_lowest", "Q2", "Q3", "Q4_highest"],
    "jcr_value": ["Q1", "Q2", "Q3", "Q4"],
    "year_value": ["Q1_oldest", "Q2", "Q3", "Q4_newest"],
    "discipline_value": ["bio_evo", "economics", "math_phys_cs", "multidisciplinary", "other", "psych_social"],
}
FEATURE_RANK = {
    "n_filters": 0,
    "size_quintile": 1,
    "type_value": 2,
    "citation_value": 3,
    "jcr_value": 4,
    "year_value": 5,
    "discipline_value": 6,
}


def load_dataset() -> pd.DataFrame:
    rows = pd.read_csv(ROWS_CSV)
    rows = rows.loc[rows["variant_group"] == "metadata_filter"].copy()

    meta = pd.read_csv(META_CSV).rename(columns={"collection_id": "variant_id", "count": "metadata_count"})
    df = rows.merge(meta, on="variant_id", how="left", validate="many_to_one")

    df["count"] = pd.to_numeric(df["count"], errors="coerce")
    df["metadata_count"] = pd.to_numeric(df["metadata_count"], errors="coerce")
    fill_count = df["count"].isna() & df["metadata_count"].notna()
    df.loc[fill_count, "count"] = df.loc[fill_count, "metadata_count"]

    for column in VALUE_COLUMNS:
        df[column] = df[column].fillna("ANY")

    df["n_filters"] = pd.to_numeric(df["n_filters"], errors="coerce").astype(int)
    df["log_count"] = np.log(df["count"])
    df["rmse_improvement"] = -pd.to_numeric(df["delta_rmse"], errors="coerce")
    df["model"] = pd.Categorical(df["model"], categories=MODEL_ORDER, ordered=True)

    variant_counts = df.loc[:, ["variant_id", "count"]].drop_duplicates().sort_values(["count", "variant_id"]).reset_index(drop=True)
    labels = [
        "Size Q1 (smallest)",
        "Size Q2",
        "Size Q3",
        "Size Q4",
        "Size Q5 (largest)",
    ]
    variant_counts["size_quintile"] = pd.qcut(variant_counts["count"], q=5, labels=labels, duplicates="drop").astype(str)
    df = df.merge(variant_counts, on=["variant_id", "count"], how="left", validate="many_to_one")
    return df.sort_values(["model", "variant_id"]).reset_index(drop=True)


def build_variant_means(df: pd.DataFrame) -> pd.DataFrame:
    group_cols = ["variant_id", "count", "n_filters", "size_quintile", *VALUE_COLUMNS]
    agg = {
        "delta_correlation": "mean",
        "delta_r2": "mean",
        "rmse_improvement": "mean",
    }
    return df.groupby(group_cols, dropna=False, observed=True).agg(agg).reset_index()


def _value_label(feature: str, value: object) -> str:
    if feature == "n_filters":
        return f"{int(value)} filter" if int(value) == 1 else f"{int(value)} filters"
    if feature == "size_quintile":
        return str(value)
    return f"{feature.replace('_value', '')}={value}"


def _value_rank(feature: str, value: object) -> int:
    if feature == "n_filters":
        return int(value)
    if feature == "size_quintile":
        labels = [
            "Size Q1 (smallest)",
            "Size Q2",
            "Size Q3",
            "Size Q4",
            "Size Q5 (largest)",
        ]
        return labels.index(str(value))
    return VALUE_ORDER[feature].index(str(value))


def build_feature_value_summary(df: pd.DataFrame) -> pd.DataFrame:
    records: list[dict[str, object]] = []
    available_models = [model for model in MODEL_ORDER if model in set(df["model"].astype(str))]
    for model in available_models:
        model_df = df.loc[df["model"].astype(str) == model].copy()

        for n_filters in sorted(model_df["n_filters"].dropna().unique()):
            part = model_df.loc[model_df["n_filters"] == n_filters]
            records.append(
                {
                    "model": model,
                    "feature": "n_filters",
                    "value": str(int(n_filters)),
                    "label": _value_label("n_filters", int(n_filters)),
                    "feature_rank": FEATURE_RANK["n_filters"],
                    "value_rank": _value_rank("n_filters", int(n_filters)),
                    "n_collections": int(len(part)),
                    "mean_count": float(part["count"].mean()),
                    "correlation_gain": float(part["delta_correlation"].mean()),
                    "r2_gain": float(part["delta_r2"].mean()),
                    "rmse_improvement": float(part["rmse_improvement"].mean()),
                }
            )

        for size_quintile in model_df["size_quintile"].dropna().unique():
            part = model_df.loc[model_df["size_quintile"] == size_quintile]
            records.append(
                {
                    "model": model,
                    "feature": "size_quintile",
                    "value": str(size_quintile),
                    "label": _value_label("size_quintile", size_quintile),
                    "feature_rank": FEATURE_RANK["size_quintile"],
                    "value_rank": _value_rank("size_quintile", size_quintile),
                    "n_collections": int(len(part)),
                    "mean_count": float(part["count"].mean()),
                    "correlation_gain": float(part["delta_correlation"].mean()),
                    "r2_gain": float(part["delta_r2"].mean()),
                    "rmse_improvement": float(part["rmse_improvement"].mean()),
                }
            )

        for feature in VALUE_COLUMNS:
            for value in VALUE_ORDER[feature]:
                part = model_df.loc[model_df[feature] == value]
                if part.empty:
                    continue
                records.append(
                    {
                        "model": model,
                        "feature": feature,
                        "value": value,
                        "label": _value_label(feature, value),
                        "feature_rank": FEATURE_RANK[feature],
                        "value_rank": _value_rank(feature, value),
                        "n_collections": int(len(part)),
                        "mean_count": float(part["count"].mean()),
                        "correlation_gain": float(part["delta_correlation"].mean()),
                        "r2_gain": float(part["delta_r2"].mean()),
                        "rmse_improvement": float(part["rmse_improvement"].mean()),
                    }
                )

    out = pd.DataFrame(records)
    out["model"] = pd.Categorical(out["model"], categories=MODEL_ORDER, ordered=True)
    return out.sort_values(["feature_rank", "value_rank", "model"]).reset_index(drop=True)


def build_model_size_summary(df: pd.DataFrame, variant_means: pd.DataFrame) -> pd.DataFrame:
    records: list[dict[str, object]] = []
    variant_metric_cols = {
        "delta_correlation": "delta_correlation",
        "delta_r2": "delta_r2",
        "rmse_improvement": "rmse_improvement",
    }
    available_models = [model for model in MODEL_ORDER if model in set(df["model"].astype(str))]

    for model in available_models:
        model_df = df.loc[df["model"].astype(str) == model].copy()
        for metric_col, summary_col in variant_metric_cols.items():
            part = model_df.loc[:, ["count", "log_count", metric_col]].dropna()
            records.append(
                {
                    "model": model,
                    "metric": summary_col,
                    "n_collections": int(len(part)),
                    "spearman_count": float(part["count"].corr(part[metric_col], method="spearman")),
                    "pearson_count": float(part["count"].corr(part[metric_col], method="pearson")),
                    "pearson_log_count": float(part["log_count"].corr(part[metric_col], method="pearson")),
                }
            )

    for metric_col, summary_col in variant_metric_cols.items():
        part = variant_means.loc[:, ["count", metric_col]].dropna().copy()
        part["log_count"] = np.log(part["count"])
        records.append(
            {
                "model": "All available models mean",
                "metric": summary_col,
                "n_collections": int(len(part)),
                "spearman_count": float(part["count"].corr(part[metric_col], method="spearman")),
                "pearson_count": float(part["count"].corr(part[metric_col], method="pearson")),
                "pearson_log_count": float(part["log_count"].corr(part[metric_col], method="pearson")),
            }
        )

    return pd.DataFrame(records)


def build_n_filters_summary(df: pd.DataFrame, variant_means: pd.DataFrame) -> pd.DataFrame:
    records: list[dict[str, object]] = []
    available_models = [model for model in MODEL_ORDER if model in set(df["model"].astype(str))]
    for model in available_models:
        model_df = df.loc[df["model"].astype(str) == model].copy()
        for n_filters, part in model_df.groupby("n_filters", dropna=False, observed=True):
            records.append(
                {
                    "scope": "model",
                    "model": model,
                    "n_filters": int(n_filters),
                    "n_collections": int(len(part)),
                    "mean_count": float(part["count"].mean()),
                    "correlation_gain": float(part["delta_correlation"].mean()),
                    "r2_gain": float(part["delta_r2"].mean()),
                    "rmse_improvement": float(part["rmse_improvement"].mean()),
                }
            )

    for n_filters, part in variant_means.groupby("n_filters", dropna=False, observed=True):
        records.append(
            {
                "scope": "all_models_mean",
                "model": "All available models mean",
                "n_filters": int(n_filters),
                "n_collections": int(len(part)),
                "mean_count": float(part["count"].mean()),
                "correlation_gain": float(part["delta_correlation"].mean()),
                "r2_gain": float(part["delta_r2"].mean()),
                "rmse_improvement": float(part["rmse_improvement"].mean()),
            }
        )

    return pd.DataFrame(records).sort_values(["scope", "model", "n_filters"]).reset_index(drop=True)


def _formula_base(include_model: bool) -> str:
    terms = []
    if include_model:
        terms.append("C(model, Treatment(reference='GPT-4.1'))")
    terms.extend(
        [
            "log_count",
            "C(n_filters, Treatment(reference=1))",
            "C(type_value, Treatment(reference='ANY'))",
            "C(citation_value, Treatment(reference='ANY'))",
            "C(jcr_value, Treatment(reference='ANY'))",
            "C(year_value, Treatment(reference='ANY'))",
            "C(discipline_value, Treatment(reference='ANY'))",
        ]
    )
    return " + ".join(terms)


def fit_regression_terms(df: pd.DataFrame, *, scope: str, include_model: bool) -> pd.DataFrame:
    records: list[dict[str, object]] = []
    formula_tail = _formula_base(include_model=include_model)
    available_models = [model for model in MODEL_ORDER if model in set(df["model"].astype(str))]

    if scope == "pooled":
        scopes = [("All available models", df.copy())]
    else:
        scopes = [(model, df.loc[df["model"].astype(str) == model].copy()) for model in available_models]

    for scope_name, part in scopes:
        for source_col, metric_name, _ in METRIC_SPECS:
            outcome = source_col if source_col != "rmse_improvement" else "rmse_improvement"
            if scope == "pooled":
                with warnings.catch_warnings():
                    warnings.filterwarnings(
                        "ignore",
                        message="invalid value encountered in sqrt",
                        category=RuntimeWarning,
                    )
                    fitted = smf.ols(f"{outcome} ~ {formula_tail}", data=part).fit(
                        cov_type="cluster",
                        cov_kwds={"groups": part["variant_id"]},
                    )
            else:
                fitted = smf.ols(f"{outcome} ~ {formula_tail}", data=part).fit()

            for term, coef, stderr, pvalue in zip(fitted.params.index, fitted.params.values, fitted.bse.values, fitted.pvalues.values):
                parsed_group, parsed_value, parsed_label = parse_term(term)
                records.append(
                    {
                        "scope": scope,
                        "model": scope_name,
                        "metric": metric_name,
                        "term": term,
                        "term_group": parsed_group,
                        "term_value": parsed_value,
                        "term_label": parsed_label,
                        "coefficient": float(coef),
                        "stderr": float(stderr),
                        "pvalue": float(pvalue),
                        "nobs": int(fitted.nobs),
                        "r2": float(fitted.rsquared),
                        "adj_r2": float(fitted.rsquared_adj),
                    }
                )

    return pd.DataFrame(records)


def parse_term(term: str) -> tuple[str, str, str]:
    if term == "Intercept":
        return "intercept", "", "Intercept"
    if term == "log_count":
        return "log_count", "log_count", "log(count)"
    if term.startswith("C(model"):
        value = term.split("[T.", 1)[1].rstrip("]")
        return "model", value, value
    patterns = {
        "n_filters": re.compile(r"C\(n_filters.*\)\[T\.(?P<value>.+)\]"),
        "type_value": re.compile(r"C\(type_value.*\)\[T\.(?P<value>.+)\]"),
        "citation_value": re.compile(r"C\(citation_value.*\)\[T\.(?P<value>.+)\]"),
        "jcr_value": re.compile(r"C\(jcr_value.*\)\[T\.(?P<value>.+)\]"),
        "year_value": re.compile(r"C\(year_value.*\)\[T\.(?P<value>.+)\]"),
        "discipline_value": re.compile(r"C\(discipline_value.*\)\[T\.(?P<value>.+)\]"),
    }
    for group, pattern in patterns.items():
        match = pattern.match(term)
        if match is None:
            continue
        value = match.group("value")
        return group, value, _value_label(group, value)
    return "other", term, term


def build_robustness_summary(model_terms: pd.DataFrame) -> pd.DataFrame:
    terms = model_terms.loc[
        ~model_terms["term_group"].isin({"intercept", "model"})
        & (model_terms["term"] != "Intercept")
    ].copy()
    terms["direction"] = np.sign(terms["coefficient"]).astype(int)

    records: list[dict[str, object]] = []
    for (metric, term, term_group, term_value, term_label), part in terms.groupby(
        ["metric", "term", "term_group", "term_value", "term_label"],
        dropna=False,
        observed=True,
    ):
        positive = int((part["coefficient"] > 0).sum())
        negative = int((part["coefficient"] < 0).sum())
        significant = part.loc[part["pvalue"] < 0.05].copy()
        sig_positive = int((significant["coefficient"] > 0).sum())
        sig_negative = int((significant["coefficient"] < 0).sum())
        records.append(
            {
                "metric": metric,
                "term": term,
                "term_group": term_group,
                "term_value": term_value,
                "term_label": term_label,
                "n_models": int(len(part)),
                "n_positive": positive,
                "n_negative": negative,
                "same_sign_all_models": bool(positive == len(part) or negative == len(part)),
                "n_significant_p_lt_0_05": int(len(significant)),
                "n_significant_positive": sig_positive,
                "n_significant_negative": sig_negative,
                "same_sign_all_significant": bool(
                    len(significant) > 0 and (sig_positive == len(significant) or sig_negative == len(significant))
                ),
                "mean_coefficient": float(part["coefficient"].mean()),
                "max_abs_coefficient": float(part["coefficient"].abs().max()),
                "min_pvalue": float(part["pvalue"].min()),
                "models": ",".join(part["model"].astype(str)),
                "significant_models": ",".join(significant["model"].astype(str)),
            }
        )

    return pd.DataFrame(records).sort_values(
        ["metric", "same_sign_all_models", "n_significant_p_lt_0_05", "min_pvalue", "max_abs_coefficient"],
        ascending=[True, False, False, True, False],
    ).reset_index(drop=True)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    relationship_df = load_dataset()
    variant_means = build_variant_means(relationship_df)
    feature_value_summary = build_feature_value_summary(relationship_df)
    model_size_summary = build_model_size_summary(relationship_df, variant_means)
    n_filters_summary = build_n_filters_summary(relationship_df, variant_means)
    pooled_terms = fit_regression_terms(relationship_df, scope="pooled", include_model=True)
    model_terms = fit_regression_terms(relationship_df, scope="model", include_model=False)
    robustness_summary = build_robustness_summary(model_terms)

    relationship_df.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_relationship_dataset.csv",
        index=False,
    )
    variant_means.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_relationship_variant_means.csv",
        index=False,
    )
    feature_value_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_relationship_model_feature_value_summary.csv",
        index=False,
    )
    model_size_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_relationship_model_size_summary.csv",
        index=False,
    )
    n_filters_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_relationship_model_n_filters_summary.csv",
        index=False,
    )
    pooled_terms.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_relationship_pooled_regression_terms.csv",
        index=False,
    )
    model_terms.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_relationship_model_regression_terms.csv",
        index=False,
    )
    robustness_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_relationship_robustness_summary.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
