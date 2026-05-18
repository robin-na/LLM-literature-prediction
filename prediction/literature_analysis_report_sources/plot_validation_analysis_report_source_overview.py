from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import RidgeCV
from sklearn.metrics import r2_score
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


ROOT = Path(__file__).resolve().parents[2]
SIGNIFICANCE_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_analysis_report_sources_repeat5"
    / "validation_literature_analysis_report_source_significance.csv"
)
FEATURE_DATASET_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_analysis_report_sources_repeat5"
    / "paper_feature_analysis_dataset_repeat5.csv"
)
VAL_PROCESSED_CSV = ROOT / "science_data" / "data" / "processed_data" / "df_paired_val.csv"
BENCHMARK_REPEAT5_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5"
    / "validation_literature_collection_analysis_report_repeat5_rows.csv"
)
BASELINE_REPEAT5_SUMMARY_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5"
    / "validation_literature_collection_analysis_report_repeat5_summary.csv"
)

RESULTS_DIR = ROOT / "results" / "validation" / "literature_analysis_report_sources_overview"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_analysis_report_sources_overview"

MODEL_ORDER = ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
MODEL_GRID = [
    ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano"],
    ["GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"],
]
PAIR_ORDER = [
    ("GPT-4.1", "GPT-4.1 Mini"),
    ("GPT-4.1", "GPT-4.1 Nano"),
    ("GPT-4.1 Mini", "GPT-4.1 Nano"),
]
CATEGORY_COLORS = {
    "Significant improvement": "#2ca25f",
    "Not significant": "#9ca3af",
    "Significant worsening": "#d62728",
}
FEATURE_SET_COLORS = {
    "model_only": "#6b7280",
    "paper_only": "#2b8cbe",
    "model_plus_paper": "#ff7f0e",
}
TARGET_LABELS = {
    "delta_correlation": "Correlation delta",
    "delta_rmse": "RMSE delta",
}
METRIC_LABELS = {
    "correlation": "Raw correlation",
    "rmse": "Raw RMSE",
    "r2": r"Raw $R^2$",
}
GAP_CLOSED_LABELS = {
    "correlation": "Correlation gap closed\ntoward E-Net",
    "rmse": "RMSE gap closed\ntoward E-Net",
    "r2": r"$R^2$ gap closed" + "\ntoward E-Net",
}
MODEL_PALETTE = {
    "GPT-4.1": "#2b8cbe",
    "GPT-4.1 Mini": "#7bccc4",
    "GPT-4.1 Nano": "#8c564b",
    "GPT-5.1": "#17becf",
    "GPT-5 Mini": "#e377c2",
    "GPT-5 Nano": "#9467bd",
}


def load_single_paper_results() -> pd.DataFrame:
    df = pd.read_csv(SIGNIFICANCE_CSV)
    if "mode" in df.columns:
        df = df.loc[df["mode"] == "joint_reasoning"].copy()

    for metric in ["correlation", "rmse", "r2"]:
        improve = df[f"sig_improve_{metric}"]
        worsen = df[f"sig_worsen_{metric}"]
        df[f"{metric}_sig_category"] = np.select(
            [improve, worsen],
            ["Significant improvement", "Significant worsening"],
            default="Not significant",
        )
        ascending = metric == "rmse"
        df[f"{metric}_rank"] = df.groupby("model", dropna=False)[metric].rank(
            method="first",
            ascending=ascending,
            na_option="keep",
        )
        max_rank = df.groupby("model", dropna=False)[f"{metric}_rank"].transform("max")
        df[f"{metric}_rank_pct"] = (df[f"{metric}_rank"] - 1) / (max_rank - 1).replace(0, 1)
    return df


def compute_enet_metrics() -> dict[str, float]:
    df = pd.read_csv(VAL_PROCESSED_CSV).sort_values("CONFIG_configId")
    truth = df["treatment_itt_efficiency"].to_numpy(dtype=float) * 100.0
    control = df["control_itt_efficiency"].to_numpy(dtype=float) * 100.0
    pred = df["elastic_prereg_pred"].to_numpy(dtype=float) * 100.0
    rmse = float(np.sqrt(np.mean((pred - truth) ** 2)))
    corr = float(np.corrcoef(pred, truth)[0, 1])
    null_mse = float(np.mean((truth - control) ** 2))
    r2 = float(1.0 - np.mean((pred - truth) ** 2) / null_mse)
    return {"correlation": corr, "rmse": rmse, "r2": r2}


def load_benchmark_metrics() -> pd.DataFrame:
    df = pd.read_csv(BENCHMARK_REPEAT5_CSV)
    df = df.loc[df["variant_id"] == "benchmark_pgg_ms"].copy()
    return df[["model", "correlation", "rmse", "r2"]].reset_index(drop=True)


def load_repeat5_baselines() -> pd.DataFrame:
    df = pd.read_csv(BASELINE_REPEAT5_SUMMARY_CSV)
    return df[["model", "baseline_correlation", "baseline_rmse", "baseline_r2"]].drop_duplicates().reset_index(drop=True)


def compute_gap_closed_dataset(df: pd.DataFrame, enet: dict[str, float], baseline_ref: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out = out.merge(baseline_ref, on="model", how="left", suffixes=("", "_repeat5"))
    for metric in ["correlation", "rmse", "r2"]:
        baseline_col = f"baseline_{metric}"
        baseline_ref_col = f"{baseline_col}_repeat5"
        baseline_anchor = out[baseline_ref_col].where(out[baseline_ref_col].notna(), out[baseline_col])
        out[f"gap_anchor_{metric}"] = baseline_anchor
        if metric == "rmse":
            denom = baseline_anchor - enet[metric]
            out[f"gap_closed_{metric}"] = (baseline_anchor - out[metric]) / denom
        else:
            denom = enet[metric] - baseline_anchor
            out[f"gap_closed_{metric}"] = (out[metric] - baseline_anchor) / denom
    return out


def summarize_gap_closed(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for model, part in df.groupby("model", dropna=False):
        row: dict[str, object] = {"model": model, "n_sources": int(len(part))}
        for metric in ["correlation", "rmse", "r2"]:
            values = pd.to_numeric(part[f"gap_closed_{metric}"], errors="coerce")
            row[f"mean_gap_closed_{metric}"] = float(values.mean())
            row[f"median_gap_closed_{metric}"] = float(values.median())
            row[f"share_gap_closed_positive_{metric}"] = float((values > 0).mean())
            row[f"share_gap_closed_ge_0_25_{metric}"] = float((values >= 0.25).mean())
            row[f"share_gap_closed_ge_0_50_{metric}"] = float((values >= 0.50).mean())
            row[f"share_gap_closed_ge_1_00_{metric}"] = float((values >= 1.00).mean())
        rows.append(row)
    return pd.DataFrame(rows).sort_values("model").reset_index(drop=True)


def compute_benchmark_gap_closed(
    benchmark: pd.DataFrame,
    baseline_ref: pd.DataFrame,
    enet: dict[str, float],
) -> pd.DataFrame:
    out = benchmark.merge(baseline_ref, on="model", how="left")
    for metric in ["correlation", "rmse", "r2"]:
        baseline_col = f"baseline_{metric}"
        if metric == "rmse":
            denom = out[baseline_col] - enet[metric]
            out[f"gap_closed_{metric}"] = (out[baseline_col] - out[metric]) / denom
        else:
            denom = enet[metric] - out[baseline_col]
            out[f"gap_closed_{metric}"] = (out[metric] - out[baseline_col]) / denom
    return out


def _gap_closed_ylims(df: pd.DataFrame, benchmark: pd.DataFrame, metric: str) -> tuple[float, float]:
    values = pd.to_numeric(df[f"gap_closed_{metric}"], errors="coerce").to_numpy(dtype=float)
    values = values[np.isfinite(values)]
    benchmark_vals = pd.to_numeric(
        benchmark.get(f"gap_closed_{metric}", pd.Series(dtype=float)),
        errors="coerce",
    ).to_numpy(dtype=float)
    benchmark_vals = benchmark_vals[np.isfinite(benchmark_vals)]
    lo = float(np.nanquantile(values, 0.01))
    hi = float(np.nanquantile(values, 0.99))
    if benchmark_vals.size:
        lo = min(lo, float(benchmark_vals.min()))
        hi = max(hi, float(benchmark_vals.max()))
    lo = min(lo, 0.0)
    hi = max(hi, 1.0)
    pad = 0.08 * (hi - lo + 1e-9)
    return lo - pad, hi + pad


def plot_gap_closed(df: pd.DataFrame, benchmark: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"

    available_models = [
        model
        for model in ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
        if model in set(df["model"])
    ]
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 4.9), sharex=False)

    for ax, metric in zip(axes, ["correlation", "rmse", "r2"]):
        sns.boxplot(
            data=df,
            x="model",
            y=f"gap_closed_{metric}",
            order=available_models,
            palette=MODEL_PALETTE,
            width=0.6,
            showfliers=False,
            ax=ax,
        )
        ax.axhline(0, color="black", linestyle="--", linewidth=1.2)
        ax.axhline(1, color="#6b7280", linestyle=":", linewidth=1.2)
        bench_part = benchmark.loc[benchmark["model"].isin(available_models)].copy()
        for idx, model in enumerate(available_models):
            sub = bench_part.loc[bench_part["model"] == model]
            if sub.empty:
                continue
            ax.scatter(
                idx,
                float(sub[f"gap_closed_{metric}"].iloc[0]),
                marker="D",
                s=56,
                color="#f28e2b",
                edgecolor="black",
                linewidth=0.6,
                zorder=4,
            )
        ax.set_xlabel("")
        ax.set_ylabel(GAP_CLOSED_LABELS[metric])
        ax.set_ylim(*_gap_closed_ylims(df, benchmark, metric))
        ax.tick_params(axis="x", rotation=25)

    handles = [
        plt.Line2D([0], [0], marker="D", color="#f28e2b", markeredgecolor="black", linestyle="None", markersize=7, label="Benchmark paper"),
        plt.Line2D([0], [0], color="black", linestyle="--", linewidth=1.2, label="No gain vs baseline"),
        plt.Line2D([0], [0], color="#6b7280", linestyle=":", linewidth=1.2, label="E-Net matched"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(0.5, -0.02))
    fig.suptitle(
        "Single-paper gains normalized by each model's baseline-to-E-Net gap\nRepeat-3 averaged paper augmentation vs 5-run baseline",
        fontsize=15,
    )
    fig.tight_layout(rect=[0, 0.05, 1, 0.92])
    fig.savefig(
        PLOTS_DIR / "validation_literature_analysis_report_source_gap_closed.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def _metric_ylims(df: pd.DataFrame, metric: str, extra_values: list[float]) -> tuple[float, float]:
    values = df[metric].to_numpy(dtype=float)
    values = values[np.isfinite(values)]
    extra = np.asarray([v for v in extra_values if np.isfinite(v)], dtype=float)
    q_low, q_high = {
        "correlation": (0.01, 0.99),
        "rmse": (0.01, 0.99),
        "r2": (0.02, 0.99),
    }[metric]
    lo = float(np.nanquantile(values, q_low))
    hi = float(np.nanquantile(values, q_high))
    if extra.size:
        lo = min(lo, float(extra.min()))
        hi = max(hi, float(extra.max()))
    pad = 0.08 * (hi - lo + 1e-9)
    if metric == "correlation":
        return max(-1.0, lo - pad), min(1.0, hi + pad)
    return lo - pad, hi + pad


def plot_metric_distributions(df: pd.DataFrame, enet: dict[str, float], benchmark: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"

    for metric in ["correlation", "rmse", "r2"]:
        higher_is_better = metric != "rmse"
        fig, axes = plt.subplots(2, 3, figsize=(16.5, 8.6), sharey=True)
        ylims = _metric_ylims(
            df,
            metric,
            list(df[f"baseline_{metric}"].unique())
            + list(benchmark[metric].dropna().to_numpy(dtype=float))
            + [enet[metric]],
        )
        max_papers = int(df.groupby("model").size().max())

        for ax, model in zip(axes.flat, sum(MODEL_GRID, [])):
            part = df.loc[df["model"] == model].copy()
            part = part.loc[np.isfinite(part[metric])].copy()
            benchmark_part = benchmark.loc[benchmark["model"] == model, metric]

            if part.empty:
                ax.set_title(f"{model}\nPending", fontsize=11)
                ax.set_xlim(-55, max_papers + 15)
                ax.set_ylim(*ylims)
                ax.set_xticks([])
                ax.set_xlabel("")
                ax.grid(False)
                ax.text(
                    0.5,
                    0.5,
                    "Pending",
                    transform=ax.transAxes,
                    ha="center",
                    va="center",
                    fontsize=12,
                    color="#6b7280",
                )
                continue

            part = part.sort_values(metric, ascending=not higher_is_better).reset_index(drop=True)
            part["x"] = np.arange(1, len(part) + 1)
            baseline_value = float(part[f"baseline_{metric}"].iloc[0])
            n_improve = int((part[f"{metric}_sig_category"] == "Significant improvement").sum())
            n_worsen = int((part[f"{metric}_sig_category"] == "Significant worsening").sum())
            benchmark_value = float(benchmark_part.iloc[0]) if not benchmark_part.empty else np.nan
            if np.isfinite(benchmark_value):
                if higher_is_better:
                    benchmark_rank = int((part[metric] > benchmark_value).sum()) + 1
                else:
                    benchmark_rank = int((part[metric] < benchmark_value).sum()) + 1
            else:
                benchmark_rank = None

            for category, color in CATEGORY_COLORS.items():
                sub = part.loc[part[f"{metric}_sig_category"] == category]
                ax.scatter(
                    sub["x"],
                    sub[metric],
                    s=9,
                    alpha=0.7,
                    color=color,
                    linewidths=0,
                    rasterized=True,
                    label=category,
                )

            ax.axhline(baseline_value, color="black", linestyle="--", linewidth=1.4)
            if benchmark_rank is not None:
                ax.axvline(benchmark_rank, color="#f28e2b", linestyle=":", linewidth=1.6)
            ax.scatter(
                0,
                enet[metric],
                marker="s",
                s=56,
                color="black",
                zorder=4,
            )
            if benchmark_rank is not None:
                ax.scatter(
                    benchmark_rank,
                    benchmark_value,
                    marker="D",
                    s=58,
                    color="#f28e2b",
                    edgecolor="black",
                    linewidth=0.6,
                    zorder=5,
                )
            ax.set_xlim(-55, max_papers + 15)
            ax.set_ylim(*ylims)
            ax.set_xticks([0])
            ax.set_xticklabels(["E-Net"], rotation=45, ha="right")
            ax.set_xlabel("Papers sorted best to worst")
            if benchmark_rank is not None:
                title = (
                    f"{model}\nbaseline={baseline_value:.3f}, benchmark={benchmark_value:.3f} "
                    f"(rank #{benchmark_rank}), sig +{n_improve} / -{n_worsen}"
                )
            else:
                title = f"{model}\nbaseline={baseline_value:.3f}, sig +{n_improve} / -{n_worsen}"
            ax.set_title(title, fontsize=11)

        axes[0, 0].set_ylabel(METRIC_LABELS[metric])
        axes[1, 0].set_ylabel(METRIC_LABELS[metric])
        fig.suptitle(
            f"Single-paper augmentation on validation {metric}\nPoints are repeat-5 averaged paper reports; dashed line is no augmentation",
            fontsize=15,
        )
        handles = [
            plt.Line2D([0], [0], marker="s", color="black", linestyle="None", markersize=7, label="E-Net"),
            plt.Line2D([0], [0], marker="D", color="#f28e2b", markeredgecolor="black", linestyle="None", markersize=7, label="Benchmark paper"),
            plt.Line2D([0], [0], color="black", linestyle="--", linewidth=1.4, label="No-augmentation baseline"),
            plt.Line2D([0], [0], color="#f28e2b", linestyle=":", linewidth=1.6, label="Benchmark rank"),
        ]
        handles.extend(
            plt.Line2D([0], [0], marker="o", color=color, linestyle="None", markersize=6, label=label)
            for label, color in CATEGORY_COLORS.items()
        )
        fig.legend(handles=handles, loc="lower center", ncol=4, frameon=False, bbox_to_anchor=(0.5, -0.02))
        fig.tight_layout(rect=[0, 0.05, 1, 0.95])
        fig.savefig(
            PLOTS_DIR / f"validation_literature_analysis_report_source_single_paper_{metric}.png",
            dpi=220,
            bbox_inches="tight",
        )
        plt.close(fig)


def plot_rank_robustness(df: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, axes = plt.subplots(2, 3, figsize=(13.5, 8.2), sharex=True, sharey=True)
    for row_idx, metric in enumerate(["correlation", "rmse"]):
        rank_col = f"{metric}_rank_pct"
        wide = df.pivot(index="source_id", columns="model", values=rank_col)
        for col_idx, (left, right) in enumerate(PAIR_ORDER):
            ax = axes[row_idx, col_idx]
            part = wide[[left, right]].dropna()
            rho = float(spearmanr(part[left], part[right]).statistic)
            ax.scatter(
                part[left],
                part[right],
                s=10,
                alpha=0.22,
                color="#2b8cbe" if metric == "correlation" else "#8c564b",
                linewidths=0,
                rasterized=True,
            )
            ax.plot([0, 1], [0, 1], color="black", linestyle="--", linewidth=1)
            ax.set_title(f"{left} vs {right}\nSpearman ρ={rho:.2f}", fontsize=11)
            if col_idx == 0:
                ax.set_ylabel(f"{metric.capitalize()} rank percentile\n0=best, 1=worst")
            if row_idx == 1:
                ax.set_xlabel(f"{left} rank percentile\n0=best, 1=worst")

    fig.suptitle("Single-paper rank robustness across models\nRepeat-3 averaged paper augmentation", fontsize=15)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(
        PLOTS_DIR / "validation_literature_analysis_report_source_rank_robustness.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def plot_metric_tradeoff(df: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, axes = plt.subplots(1, 3, figsize=(14.5, 4.6), sharex=True, sharey=True)
    for ax, model in zip(axes, MODEL_ORDER):
        part = df.loc[df["model"] == model].copy()
        part = part.dropna(subset=["correlation_rank_pct", "rmse_rank_pct"]).copy()
        rho = float(spearmanr(part["correlation_rank_pct"], part["rmse_rank_pct"]).statistic)
        ax.scatter(
            part["correlation_rank_pct"],
            part["rmse_rank_pct"],
            s=11,
            alpha=0.24,
            color="#4c78a8",
            linewidths=0,
            rasterized=True,
        )
        ax.plot([0, 1], [0, 1], color="black", linestyle="--", linewidth=1)
        ax.set_title(f"{model}\nSpearman ρ={rho:.2f}", fontsize=11)
        ax.set_xlabel("Correlation rank percentile\n0=best, 1=worst")

    axes[0].set_ylabel("RMSE rank percentile\n0=best, 1=worst")
    fig.suptitle("What helps correlation is not always what helps RMSE\nRepeat-3 averaged paper augmentation", fontsize=15)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(
        PLOTS_DIR / "validation_literature_analysis_report_source_metric_tradeoff.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def compute_feature_cv(df: pd.DataFrame) -> pd.DataFrame:
    feature_sets = {
        "model_only": ["model"],
        "paper_only": [
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
        ],
    }
    feature_sets["model_plus_paper"] = feature_sets["model_only"] + feature_sets["paper_only"]
    df = df.loc[~df[feature_sets["paper_only"]].isna().all(axis=1)].copy()

    numeric_cols = {
        "pub_year_z",
        "log_citations_z",
        "n_pages_z",
        "dimension_informative_direct_count_z",
        "broad_only_count_z",
    }
    targets = ["delta_correlation", "delta_rmse"]
    results: list[dict[str, object]] = []

    def build_pipeline(cols: list[str]) -> Pipeline:
        cat = [col for col in cols if col not in numeric_cols]
        num = [col for col in cols if col in numeric_cols]
        pre = ColumnTransformer(
            [
                (
                    "num",
                    Pipeline(
                        [
                            ("imputer", SimpleImputer(strategy="median")),
                            ("scaler", StandardScaler()),
                        ]
                    ),
                    num,
                ),
                (
                    "cat",
                    Pipeline(
                        [
                            ("imputer", SimpleImputer(strategy="most_frequent")),
                            ("onehot", OneHotEncoder(handle_unknown="ignore")),
                        ]
                    ),
                    cat,
                ),
            ]
        )
        return Pipeline(
            [
                ("preprocess", pre),
                ("ridge", RidgeCV(alphas=np.logspace(-3, 3, 13))),
            ]
        )

    groups = df["source_id"]
    for feature_set, cols in feature_sets.items():
        X = df[cols].copy()
        for col in X.columns:
            if col not in numeric_cols:
                X[col] = X[col].astype(str)
        for target in targets:
            y = df[target].to_numpy(dtype=float)
            preds = np.empty_like(y, dtype=float)
            splitter = GroupKFold(n_splits=5)
            for train_idx, test_idx in splitter.split(X, y, groups):
                pipe = build_pipeline(cols)
                pipe.fit(X.iloc[train_idx], y[train_idx])
                preds[test_idx] = pipe.predict(X.iloc[test_idx])
            results.append(
                {
                    "scope": "pooled",
                    "feature_set": feature_set,
                    "target": target,
                    "cv_r2": float(r2_score(y, preds)),
                    "cv_spearman": float(spearmanr(y, preds).statistic),
                }
            )

    paper_cols = feature_sets["paper_only"]
    for model in MODEL_ORDER:
        part = df.loc[df["model"] == model].copy()
        if part.empty:
            continue
        X = part[paper_cols].copy()
        if X.isna().all(axis=1).all():
            continue
        for col in X.columns:
            if col not in numeric_cols:
                X[col] = X[col].astype(str)
        splitter = GroupKFold(n_splits=5)
        groups = part["source_id"]
        for target in targets:
            y = part[target].to_numpy(dtype=float)
            preds = np.empty_like(y, dtype=float)
            for train_idx, test_idx in splitter.split(X, y, groups):
                pipe = build_pipeline(paper_cols)
                pipe.fit(X.iloc[train_idx], y[train_idx])
                preds[test_idx] = pipe.predict(X.iloc[test_idx])
            results.append(
                {
                    "scope": "within_model_paper_only",
                    "model": model,
                    "feature_set": "paper_only",
                    "target": target,
                    "cv_r2": float(r2_score(y, preds)),
                    "cv_spearman": float(spearmanr(y, preds).statistic),
                }
            )

    return pd.DataFrame(results)


def plot_feature_brittleness(cv_results: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, axes = plt.subplots(1, 2, figsize=(13.5, 4.8))

    pooled = cv_results.loc[cv_results["scope"] == "pooled"].copy()
    pooled["target_label"] = pooled["target"].map(TARGET_LABELS)
    sns.barplot(
        data=pooled,
        x="target_label",
        y="cv_r2",
        hue="feature_set",
        palette=FEATURE_SET_COLORS,
        ax=axes[0],
    )
    axes[0].axhline(0, color="black", linestyle="--", linewidth=1)
    axes[0].set_xlabel("")
    axes[0].set_ylabel("Grouped 5-fold CV $R^2$")
    axes[0].set_title("Pooled prediction of paper usefulness")
    axes[0].legend(title="", frameon=False, loc="upper left")

    within = cv_results.loc[cv_results["scope"] == "within_model_paper_only"].copy()
    within["target_label"] = within["target"].map(TARGET_LABELS)
    sns.barplot(
        data=within,
        x="model",
        y="cv_r2",
        hue="target_label",
        palette={"Correlation delta": "#2b8cbe", "RMSE delta": "#8c564b"},
        ax=axes[1],
    )
    axes[1].axhline(0, color="black", linestyle="--", linewidth=1)
    axes[1].set_xlabel("")
    axes[1].set_ylabel("Grouped 5-fold CV $R^2$")
    axes[1].set_title("Within-model prediction from paper features only")
    axes[1].legend(title="", frameon=False, loc="upper right")

    fig.suptitle("Paper-level metadata is brittle for predicting augmentation gains\nRepeat-3 averaged paper augmentation", fontsize=15)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(
        PLOTS_DIR / "validation_literature_analysis_report_source_feature_brittleness.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    single = load_single_paper_results()
    single.to_csv(RESULTS_DIR / "single_paper_overview_dataset.csv", index=False)

    enet = compute_enet_metrics()
    pd.DataFrame([enet]).to_csv(RESULTS_DIR / "single_paper_enet_metrics.csv", index=False)
    benchmark = load_benchmark_metrics()
    benchmark.to_csv(RESULTS_DIR / "single_paper_benchmark_metrics.csv", index=False)
    baseline_ref = load_repeat5_baselines()
    gap_closed = compute_gap_closed_dataset(single, enet, baseline_ref)
    gap_closed.to_csv(RESULTS_DIR / "single_paper_gap_closed_dataset.csv", index=False)
    gap_summary = summarize_gap_closed(gap_closed)
    gap_summary.to_csv(RESULTS_DIR / "single_paper_gap_closed_summary.csv", index=False)
    benchmark_gap = compute_benchmark_gap_closed(benchmark, baseline_ref, enet)
    benchmark_gap.to_csv(RESULTS_DIR / "single_paper_benchmark_gap_closed.csv", index=False)

    plot_metric_distributions(single, enet, benchmark)
    plot_gap_closed(gap_closed, benchmark_gap)
    plot_rank_robustness(single)
    plot_metric_tradeoff(single)

    feature_df = pd.read_csv(FEATURE_DATASET_CSV)
    cv_results = compute_feature_cv(feature_df)
    cv_results.to_csv(RESULTS_DIR / "paper_feature_grouped_cv.csv", index=False)
    plot_feature_brittleness(cv_results)

    print(RESULTS_DIR / "single_paper_overview_dataset.csv")
    print(RESULTS_DIR / "single_paper_enet_metrics.csv")
    print(RESULTS_DIR / "single_paper_benchmark_metrics.csv")
    print(RESULTS_DIR / "single_paper_gap_closed_dataset.csv")
    print(RESULTS_DIR / "single_paper_gap_closed_summary.csv")
    print(RESULTS_DIR / "single_paper_benchmark_gap_closed.csv")
    print(RESULTS_DIR / "paper_feature_grouped_cv.csv")
    print(PLOTS_DIR / "validation_literature_analysis_report_source_single_paper_correlation.png")
    print(PLOTS_DIR / "validation_literature_analysis_report_source_single_paper_rmse.png")
    print(PLOTS_DIR / "validation_literature_analysis_report_source_single_paper_r2.png")
    print(PLOTS_DIR / "validation_literature_analysis_report_source_gap_closed.png")
    print(PLOTS_DIR / "validation_literature_analysis_report_source_rank_robustness.png")
    print(PLOTS_DIR / "validation_literature_analysis_report_source_metric_tradeoff.png")
    print(PLOTS_DIR / "validation_literature_analysis_report_source_feature_brittleness.png")


if __name__ == "__main__":
    main()
