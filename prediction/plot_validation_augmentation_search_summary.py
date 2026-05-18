from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
from plot_paths import VALIDATION_PLOTS as PLOTS, ensure_plot_dir

BASELINE_RMSE = 6.704339
NULL_MSE = 50.847465


def r2_from_rmse(rmse: float) -> float:
    return 1.0 - (rmse ** 2) / NULL_MSE


def load_family(path: Path, family: str, include_baselines: bool = False) -> pd.DataFrame:
    df = pd.read_csv(path).copy()
    if "variation" not in df.columns:
        raise ValueError(f"{path} is missing a variation column")

    if not include_baselines:
        df = df.loc[~df["variation"].str.startswith("baseline")].copy()

    df["family"] = family
    df["rmse"] = BASELINE_RMSE + df["delta_rmse"]
    df["r2"] = df["rmse"].map(r2_from_rmse)
    df["baseline_r2"] = r2_from_rmse(BASELINE_RMSE)
    df["delta_r2"] = df["r2"] - df["baseline_r2"]
    return df


def build_summary(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for family, part in df.groupby("family", sort=False):
        rows.append(
            {
                "family": family,
                "n_variants": len(part),
                "median_delta_rmse": part["delta_rmse"].median(),
                "best_delta_rmse": part["delta_rmse"].min(),
                "share_delta_rmse_better": (part["delta_rmse"] < 0).mean(),
                "median_delta_r2": part["delta_r2"].median(),
                "best_delta_r2": part["delta_r2"].max(),
                "share_delta_r2_better": (part["delta_r2"] > 0).mean(),
                "median_delta_correlation": part["delta_correlation"].median(),
                "best_delta_correlation": part["delta_correlation"].max(),
                "share_delta_correlation_better": (part["delta_correlation"] > 0).mean(),
                "median_delta_directional_accuracy": part["delta_directional_accuracy"].median(),
                "best_delta_directional_accuracy": part["delta_directional_accuracy"].max(),
                "share_delta_directional_accuracy_better": (
                    part["delta_directional_accuracy"] > 0
                ).mean(),
            }
        )
    return pd.DataFrame(rows)


def add_box_strip(ax, df: pd.DataFrame, metric: str, family_order: list[str], colors: dict[str, str]) -> None:
    positions = np.arange(len(family_order))
    data = [df.loc[df["family"] == family, metric].values for family in family_order]
    bp = ax.boxplot(
        data,
        vert=False,
        patch_artist=True,
        positions=positions,
        widths=0.55,
        showfliers=False,
        medianprops={"color": "black", "linewidth": 1.2},
        boxprops={"linewidth": 1.0},
        whiskerprops={"linewidth": 1.0},
        capprops={"linewidth": 1.0},
    )
    for patch, family in zip(bp["boxes"], family_order):
        patch.set_facecolor(colors[family])
        patch.set_alpha(0.55)

    rng = np.random.default_rng(41)
    for pos, family in zip(positions, family_order):
        values = df.loc[df["family"] == family, metric].to_numpy()
        jitter = rng.normal(loc=0.0, scale=0.065, size=len(values))
        ax.scatter(
            values,
            np.full(len(values), pos) + jitter,
            s=10,
            alpha=0.18,
            color=colors[family],
            edgecolors="none",
        )

    ax.axvline(0.0, color="#666666", linestyle="--", linewidth=1.0)
    ax.grid(axis="x", alpha=0.25)
    ax.set_yticks(positions, family_order)


def main() -> None:
    family_specs = [
        ("Report filters", RESULTS / "prediction_251110_report_41_metrics_delta.csv", True),
        ("RAG filters", RESULTS / "prediction_251110_RAG_41_metrics_delta.csv", True),
        ("Abstract filters", RESULTS / "prediction_251110_abstracts_41_metrics_delta.csv", True),
        ("Positive-case prompt variants", RESULTS / "prediction_positive_case_variations_41_metrics_delta.csv", False),
    ]

    frames = [load_family(path, family, include_baselines) for family, path, include_baselines in family_specs]
    df = pd.concat(frames, ignore_index=True)
    summary = build_summary(df)

    colors = {
        "Report filters": "#4e79a7",
        "RAG filters": "#59a14f",
        "Abstract filters": "#f28e2b",
        "Positive-case prompt variants": "#e15759",
    }
    family_order = [spec[0] for spec in family_specs]
    labels = [
        f"{family}\n(n={int(summary.loc[summary['family'] == family, 'n_variants'].iloc[0])})"
        for family in family_order
    ]
    rename_map = dict(zip(family_order, labels))
    df["family_label"] = df["family"].map(rename_map)
    family_order_labels = [rename_map[family] for family in family_order]
    colors_labeled = {rename_map[k]: v for k, v in colors.items()}

    summary["family_label"] = summary["family"].map(rename_map)
    summary = summary[
        [
            "family",
            "family_label",
            "n_variants",
            "median_delta_rmse",
            "best_delta_rmse",
            "share_delta_rmse_better",
            "median_delta_r2",
            "best_delta_r2",
            "share_delta_r2_better",
            "median_delta_correlation",
            "best_delta_correlation",
            "share_delta_correlation_better",
            "median_delta_directional_accuracy",
            "best_delta_directional_accuracy",
            "share_delta_directional_accuracy_better",
        ]
    ]

    plot_df = df[
        [
            "family_label",
            "delta_rmse",
            "delta_r2",
            "delta_correlation",
            "delta_directional_accuracy",
        ]
    ].rename(
        columns={"family_label": "family"}
    )

    fig, axes = plt.subplots(1, 2, figsize=(14.5, 7.4), sharey=True)
    add_box_strip(axes[0], plot_df, "delta_rmse", family_order_labels, colors_labeled)
    axes[0].set_title(r"Validation Search Space: $\Delta$RMSE vs GPT-4.1 baseline")
    axes[0].set_xlabel(r"$\Delta$RMSE (lower is better)")
    axes[0].set_xlim(-1.5, 6.5)

    add_box_strip(axes[1], plot_df, "delta_r2", family_order_labels, colors_labeled)
    axes[1].set_title(r"Validation Search Space: $\Delta R^2$ vs GPT-4.1 baseline")
    axes[1].set_xlabel(r"$\Delta R^2$ (higher is better)")
    axes[1].set_xlim(-2.5, 0.45)

    fig.suptitle("Most validation augmentation variants do not improve on the canonical baseline", fontsize=16, y=0.98)
    fig.text(
        0.5,
        0.01,
        "Axes clipped to show the central mass; several extreme worse-than-baseline outliers fall beyond the plotted range.",
        ha="center",
        fontsize=9,
        color="#555555",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.96))

    out_csv = RESULTS / "validation_augmentation_search_summary_table.csv"
    out_png = PLOTS / "validation_augmentation_search_summary.png"
    out_pdf = PLOTS / "validation_augmentation_search_summary.pdf"
    summary.to_csv(out_csv, index=False)
    fig.savefig(out_png, dpi=220, bbox_inches="tight")
    fig.savefig(out_pdf, bbox_inches="tight")

    fig2, axes2 = plt.subplots(1, 2, figsize=(14.5, 7.4), sharey=True)
    add_box_strip(
        axes2[0],
        plot_df,
        "delta_correlation",
        family_order_labels,
        colors_labeled,
    )
    axes2[0].set_title("Validation Search Space: ΔCorrelation vs GPT-4.1 baseline")
    axes2[0].set_xlabel("ΔCorrelation (higher is better)")
    axes2[0].set_xlim(-0.5, 0.22)

    add_box_strip(
        axes2[1],
        plot_df,
        "delta_directional_accuracy",
        family_order_labels,
        colors_labeled,
    )
    axes2[1].set_title("Validation Search Space: ΔDirectional Accuracy vs GPT-4.1 baseline")
    axes2[1].set_xlabel("ΔDirectional Accuracy (higher is better)")
    axes2[1].set_xlim(-0.32, 0.22)

    fig2.suptitle(
        "Validation augmentation can improve correlation in pockets, but directional accuracy gains are sparse",
        fontsize=16,
        y=0.98,
    )
    fig2.text(
        0.5,
        0.01,
        "Axes clipped to show the central mass; a few worse-than-baseline outliers fall beyond the plotted range.",
        ha="center",
        fontsize=9,
        color="#555555",
    )
    fig2.tight_layout(rect=(0, 0, 1, 0.96))

    out_png2 = PLOTS / "validation_augmentation_search_summary_corr_da.png"
    out_pdf2 = PLOTS / "validation_augmentation_search_summary_corr_da.pdf"
    fig2.savefig(out_png2, dpi=220, bbox_inches="tight")
    fig2.savefig(out_pdf2, bbox_inches="tight")


if __name__ == "__main__":
    main()
