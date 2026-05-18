from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_metadata_filters"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_collection_analysis_reports_metadata_filters"
RELATIONSHIP_DATASET_CSV = (
    RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_relationship_dataset.csv"
)
SIZE_SUMMARY_CSV = (
    RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_relationship_model_size_summary.csv"
)
FEATURE_VALUE_SUMMARY_CSV = (
    RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_relationship_model_feature_value_summary.csv"
)

MODEL_ORDER = ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
N_FILTER_COLORS = {
    "1": "#f28e2b",
    "2": "#59a14f",
    "3": "#4e79a7",
}
METRIC_SPECS = [
    ("delta_correlation", "correlation_gain", "Correlation gain"),
    ("delta_r2", "r2_gain", "R2 gain"),
    ("rmse_improvement", "rmse_improvement", "RMSE improvement"),
]
RAW_METRIC_SPECS = [
    ("correlation", "Raw correlation", "YlGnBu", None),
    ("r2", "Raw R2", "RdBu_r", 0.0),
    ("rmse", "Raw RMSE", "YlOrRd_r", None),
]
FEATURE_ORDER = ["n_filters", "type_value", "citation_value", "jcr_value", "year_value", "discipline_value"]


def _available_models(df: pd.DataFrame) -> list[str]:
    return [model for model in MODEL_ORDER if model in set(df["model"].astype(str))]


def plot_size_by_model(dataset: pd.DataFrame, size_summary: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"

    available_models = _available_models(dataset)
    fig, axes = plt.subplots(len(available_models), len(METRIC_SPECS), figsize=(14.8, 10.5), sharex=True)
    if len(available_models) == 1:
        axes = np.asarray([axes])

    for row_idx, model in enumerate(available_models):
        model_df = dataset.loc[dataset["model"].astype(str) == model].copy()
        for col_idx, (source_col, _metric_name, title) in enumerate(METRIC_SPECS):
            ax = axes[row_idx, col_idx]
            for n_filters, color in N_FILTER_COLORS.items():
                part = model_df.loc[model_df["n_filters"].astype(str) == n_filters].copy()
                if part.empty:
                    continue
                ax.scatter(
                    part["count"],
                    part[source_col],
                    s=15,
                    alpha=0.45,
                    color=color,
                    edgecolor="none",
                )

            fit_part = model_df.loc[:, ["count", "log_count", source_col]].dropna()
            if len(fit_part) >= 2:
                coeffs = np.polyfit(fit_part["log_count"], fit_part[source_col], deg=1)
                x_vals = np.geomspace(float(fit_part["count"].min()), float(fit_part["count"].max()), 120)
                ax.plot(x_vals, coeffs[0] * np.log(x_vals) + coeffs[1], color="black", linewidth=1.4)

            summary_row = size_summary.loc[
                (size_summary["model"] == model) & (size_summary["metric"] == source_col)
            ].iloc[0]
            ax.text(
                0.04,
                0.93,
                f"rho={float(summary_row['spearman_count']):+.2f}",
                transform=ax.transAxes,
                ha="left",
                va="top",
                fontsize=8.5,
                color="#374151",
                bbox={"facecolor": "white", "alpha": 0.85, "edgecolor": "none", "pad": 1.6},
            )
            ax.axhline(0.0, color="#9ca3af", linewidth=0.9, linestyle="--")
            ax.set_xscale("log")
            if row_idx == 0:
                ax.set_title(title)
            if col_idx == 0:
                ax.set_ylabel(model)
            else:
                ax.set_ylabel("")
            if row_idx == len(available_models) - 1:
                ax.set_xlabel("Collection size (log scale)")
            else:
                ax.set_xlabel("")

    handles = [
        plt.Line2D([], [], linestyle="None", marker="o", color=color, markersize=6, label=label)
        for label, color in [("1 filter", N_FILTER_COLORS["1"]), ("2 filters", N_FILTER_COLORS["2"]), ("3 filters", N_FILTER_COLORS["3"])]
    ]
    handles.append(plt.Line2D([], [], color="black", linewidth=1.4, label="OLS fit on log(count)"))
    fig.legend(handles=handles, loc="lower center", ncol=4, frameon=False, bbox_to_anchor=(0.5, 0.01))
    fig.suptitle("Model-by-model relationship between metadata-filter collection size and augmentation gain", fontsize=15, y=0.995)
    fig.text(
        0.5,
        0.035,
        "Each point is one metadata-filter collection. Panels show per-model gains versus that model's no-augmentation baseline; annotations report Spearman rho with raw collection size.",
        ha="center",
        fontsize=9,
        color="#4b5563",
    )
    fig.tight_layout(rect=[0.03, 0.06, 1.0, 0.965])
    fig.savefig(
        PLOTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_gain_vs_size_by_model.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def plot_feature_heatmaps(summary_df: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"

    available_models = _available_models(summary_df)
    heatmap_df = summary_df.loc[summary_df["feature"].isin(FEATURE_ORDER)].copy()
    heatmap_df = heatmap_df.sort_values(["feature_rank", "value_rank", "model"]).reset_index(drop=True)
    row_labels = heatmap_df.loc[:, ["feature_rank", "value_rank", "label"]].drop_duplicates()["label"].tolist()

    fig, axes = plt.subplots(1, len(METRIC_SPECS), figsize=(16.5, 10.8), sharey=True)
    if len(METRIC_SPECS) == 1:
        axes = [axes]

    for ax, (_, metric_col, title) in zip(axes, METRIC_SPECS):
        pivot = (
            heatmap_df.pivot_table(index="label", columns="model", values=metric_col, aggfunc="first")
            .reindex(index=row_labels, columns=available_models)
        )
        vmax = float(np.nanquantile(np.abs(pivot.to_numpy(dtype=float)), 0.98))
        sns.heatmap(
            pivot,
            ax=ax,
            cmap="RdBu_r",
            center=0.0,
            vmin=-vmax,
            vmax=vmax,
            annot=True,
            fmt=".2f",
            linewidths=0.45,
            linecolor="white",
            cbar=True,
            cbar_kws={"shrink": 0.7},
        )
        ax.set_title(title)
        ax.set_xlabel("")
        if ax is axes[0]:
            ax.set_ylabel("Metadata value")
        else:
            ax.set_ylabel("")
        ax.tick_params(axis="x", rotation=20)
        ax.tick_params(axis="y", rotation=0, labelsize=8.6)

    fig.suptitle("Model-by-model augmentation gain by metadata value used to construct the collection", fontsize=15, y=0.995)
    fig.text(
        0.5,
        0.015,
        "Each cell is the mean augmentation gain for metadata-filter collections that include that value. Positive is better in all three panels because RMSE is converted to baseline RMSE minus augmented RMSE.",
        ha="center",
        fontsize=9,
        color="#4b5563",
    )
    fig.tight_layout(rect=[0.03, 0.045, 1.0, 0.965])
    fig.savefig(
        PLOTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_gain_by_metadata_value_by_model.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def build_raw_feature_summary(dataset: pd.DataFrame, template_summary: pd.DataFrame) -> pd.DataFrame:
    records: list[dict[str, object]] = []
    unique_rows = template_summary.loc[:, ["model", "feature", "value", "label", "feature_rank", "value_rank"]].drop_duplicates()

    for row in unique_rows.to_dict("records"):
        model = str(row["model"])
        feature = str(row["feature"])
        value = str(row["value"])
        part = dataset.loc[dataset["model"].astype(str) == model].copy()
        if feature == "n_filters":
            part = part.loc[part["n_filters"].astype(str) == value]
        else:
            part = part.loc[part[feature].astype(str) == value]
        if part.empty:
            continue
        records.append(
            {
                **row,
                "raw_correlation": float(part["correlation"].mean()),
                "raw_r2": float(part["r2"].mean()),
                "raw_rmse": float(part["rmse"].mean()),
            }
        )

    out = pd.DataFrame(records)
    out["model"] = pd.Categorical(out["model"], categories=MODEL_ORDER, ordered=True)
    return out.sort_values(["feature_rank", "value_rank", "model"]).reset_index(drop=True)


def plot_raw_feature_heatmaps(raw_summary_df: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"

    available_models = _available_models(raw_summary_df)
    raw_summary_df = raw_summary_df.sort_values(["feature_rank", "value_rank", "model"]).reset_index(drop=True)
    row_labels = raw_summary_df.loc[:, ["feature_rank", "value_rank", "label"]].drop_duplicates()["label"].tolist()

    fig, axes = plt.subplots(1, len(RAW_METRIC_SPECS), figsize=(16.5, 10.8), sharey=True)
    if len(RAW_METRIC_SPECS) == 1:
        axes = [axes]

    for ax, (metric_col, title, cmap, center) in zip(axes, RAW_METRIC_SPECS):
        pivot = (
            raw_summary_df.pivot_table(
                index="label",
                columns="model",
                values=f"raw_{metric_col}",
                aggfunc="first",
                observed=True,
            )
            .reindex(index=row_labels, columns=available_models)
        )
        heatmap_kwargs = {
            "data": pivot,
            "ax": ax,
            "cmap": cmap,
            "annot": True,
            "fmt": ".2f",
            "linewidths": 0.45,
            "linecolor": "white",
            "cbar": True,
            "cbar_kws": {"shrink": 0.7},
        }
        if center is not None:
            vmax = float(np.nanquantile(np.abs(pivot.to_numpy(dtype=float)), 0.98))
            heatmap_kwargs["center"] = center
            heatmap_kwargs["vmin"] = -vmax
            heatmap_kwargs["vmax"] = vmax
        sns.heatmap(**heatmap_kwargs)
        ax.set_title(title)
        ax.set_xlabel("")
        if ax is axes[0]:
            ax.set_ylabel("Metadata value")
        else:
            ax.set_ylabel("")
        ax.tick_params(axis="x", rotation=20)
        ax.tick_params(axis="y", rotation=0, labelsize=8.6)

    fig.suptitle("Model-by-model raw performance by metadata value used to construct the collection", fontsize=15, y=0.995)
    fig.text(
        0.5,
        0.015,
        "Each cell is the mean raw augmented metric for metadata-filter collections that include that value. Higher is better for correlation and R2; lower is better for RMSE.",
        ha="center",
        fontsize=9,
        color="#4b5563",
    )
    fig.tight_layout(rect=[0.03, 0.045, 1.0, 0.965])
    fig.savefig(
        PLOTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_raw_by_metadata_value_by_model.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    dataset = pd.read_csv(RELATIONSHIP_DATASET_CSV)
    size_summary = pd.read_csv(SIZE_SUMMARY_CSV)
    feature_value_summary = pd.read_csv(FEATURE_VALUE_SUMMARY_CSV)

    plot_size_by_model(dataset, size_summary)
    plot_feature_heatmaps(feature_value_summary)
    raw_feature_summary = build_raw_feature_summary(dataset, feature_value_summary)
    plot_raw_feature_heatmaps(raw_feature_summary)


if __name__ == "__main__":
    main()
