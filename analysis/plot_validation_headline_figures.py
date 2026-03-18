from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from analyze_validation_interaction_alignment import parse_variation


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
PLOTS = ROOT / "plots"
DATA = ROOT / "science-data_and_code" / "data" / "processed_data"

MODE_BASELINE = {
    "single": "baseline",
    "reasoning": "baseline_reasoning",
    "joint": "baseline_joint",
    "joint_reasoning": "baseline_joint_reasoning",
}

COLORS = {"both": "#1f77b4", "paper_only": "#ff7f0e", "data_only": "#2ca02c"}
MARKERS = {"single": "o", "reasoning": "s", "joint": "^", "joint_reasoning": "D"}


def load_variant_summary() -> tuple[pd.DataFrame, pd.DataFrame]:
    metrics = pd.read_csv(RESULTS / "prediction_positive_case_variations_41_metrics.csv")
    val = pd.read_csv(DATA / "df_paired_val.csv").sort_values("CONFIG_configId").reset_index(drop=True)
    y_true = 100 * val["treatment_itt_efficiency"].to_numpy()
    y_control = 100 * val["control_itt_efficiency"].to_numpy()
    null_mse = float(np.mean((y_true - y_control) ** 2))

    def r2_from_rmse(rmse: float) -> float:
        return 1.0 - (rmse**2) / null_mse

    metrics["r2"] = metrics["rmse"].map(r2_from_rmse)
    metrics[["input_group", "family", "mode"]] = metrics["variation"].apply(lambda v: pd.Series(parse_variation(v)))
    metrics["baseline_variation"] = metrics["mode"].map(MODE_BASELINE)

    baseline_lookup = metrics.set_index("variation")[["rmse", "correlation", "r2"]]
    aug = metrics.loc[metrics["input_group"] != "baseline"].copy()
    aug["baseline_rmse"] = aug["baseline_variation"].map(baseline_lookup["rmse"])
    aug["baseline_correlation"] = aug["baseline_variation"].map(baseline_lookup["correlation"])
    aug["baseline_r2"] = aug["baseline_variation"].map(baseline_lookup["r2"])
    aug["delta_rmse_vs_matched_baseline"] = aug["rmse"] - aug["baseline_rmse"]
    aug["delta_correlation_vs_matched_baseline"] = aug["correlation"] - aug["baseline_correlation"]
    aug["delta_r2_vs_matched_baseline"] = aug["r2"] - aug["baseline_r2"]

    extraction = pd.read_csv(RESULTS / "validation_extraction_gap_decomposition.csv")
    aug = aug.merge(
        extraction[["variation", "delta_extraction_gap_vs_matched_baseline"]],
        on="variation",
        how="left",
    )

    ewoa_cfg = pd.read_csv(RESULTS / "validation_matched_ewoa_by_config.csv")
    ewoa_cfg = ewoa_cfg.merge(
        aug[["variation", "delta_r2_vs_matched_baseline", "delta_correlation_vs_matched_baseline", "input_group", "mode"]],
        on=["variation", "input_group", "mode"],
        how="left",
    )
    aug.to_csv(RESULTS / "validation_headline_variant_summary.csv", index=False)
    return aug, ewoa_cfg


def plot_updating(ewoa_cfg: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.8), constrained_layout=True)
    ax = axes[0]
    improved = ewoa_cfg["delta_r2_vs_matched_baseline"] > 0
    ax.scatter(
        ewoa_cfg.loc[~improved, "needed_correction"],
        ewoa_cfg.loc[~improved, "actual_update"],
        s=20,
        alpha=0.28,
        color="#b0b0b0",
        label="Variants that do not improve R²",
    )
    ax.scatter(
        ewoa_cfg.loc[improved, "needed_correction"],
        ewoa_cfg.loc[improved, "actual_update"],
        s=24,
        alpha=0.55,
        color="#1f77b4",
        label="Variants that improve R²",
    )
    lim = float(np.nanmax(np.abs(np.r_[ewoa_cfg["needed_correction"], ewoa_cfg["actual_update"]])))
    ax.plot([-lim, lim], [-lim, lim], linestyle="--", color="#444444", linewidth=1.5, label="Perfect update")
    ax.axhline(0, color="#777777", linewidth=1, linestyle=":")
    ax.axvline(0, color="#777777", linewidth=1, linestyle=":")
    ax.set_xlabel("Needed correction from matched baseline to E-net")
    ax.set_ylabel("Actual update after augmentation")
    ax.set_title("A. Augmentation causes real updating")
    ax.legend(frameon=False, fontsize=9)
    ax.grid(alpha=0.2)

    ax2 = axes[1]
    bins = np.linspace(-1.5, 1.5, 40)
    valid = ewoa_cfg["ewoa"].dropna()
    ax2.hist(valid, bins=bins, color="#4c78a8", alpha=0.85)
    ax2.axvline(0, color="#777777", linestyle=":", linewidth=1.5, label="No updating")
    ax2.axvline(1, color="#444444", linestyle="--", linewidth=1.5, label="Perfect extraction")
    ax2.set_title("B. Update efficiency is centered well below 1")
    ax2.set_xlabel("eWOA")
    ax2.set_ylabel("Count of config-variant pairs")
    ax2.legend(frameon=False, fontsize=9)
    ax2.grid(alpha=0.2)

    fig.suptitle("Validation updating relative to the matched no-augmentation baseline", fontsize=15)
    fig.savefig(PLOTS / "validation_headline_updating.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "validation_headline_updating.pdf", bbox_inches="tight")


def plot_performance(aug: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.8), constrained_layout=True)

    ax = axes[0]
    for mode, marker in MARKERS.items():
        for input_group, color in COLORS.items():
            sub = aug[(aug["mode"] == mode) & (aug["input_group"] == input_group)]
            ax.scatter(
                sub["delta_r2_vs_matched_baseline"],
                sub["delta_correlation_vs_matched_baseline"],
                color=color,
                marker=marker,
                s=58,
                alpha=0.85,
            )
    ax.axhline(0, color="#777777", linestyle=":", linewidth=1)
    ax.axvline(0, color="#777777", linestyle=":", linewidth=1)
    ax.set_xlabel("ΔR² vs matched baseline")
    ax.set_ylabel("ΔCorrelation vs matched baseline")
    ax.set_title("A. Most variants do not improve both metrics")
    ax.grid(alpha=0.2)

    both_better = int(((aug["delta_r2_vs_matched_baseline"] > 0) & (aug["delta_correlation_vs_matched_baseline"] > 0)).sum())
    ax.text(
        0.02,
        0.98,
        f"{both_better}/{len(aug)} improve both",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=10,
        bbox={"facecolor": "white", "edgecolor": "#dddddd", "pad": 3},
    )

    ax2 = axes[1]
    idx = np.arange(len(aug))
    aug_sorted = aug.sort_values("delta_r2_vs_matched_baseline").reset_index(drop=True)
    ax2.scatter(idx, aug_sorted["delta_rmse_vs_matched_baseline"], color="#8c564b", s=30, alpha=0.8, label="ΔRMSE")
    ax2.axhline(0, color="#777777", linestyle=":", linewidth=1)
    ax2.set_xlabel("Augmented variants (sorted by ΔR²)")
    ax2.set_ylabel("ΔRMSE vs matched baseline")
    ax2.set_title("B. RMSE usually worsens")
    ax2.grid(alpha=0.2)
    better_rmse = int((aug_sorted["delta_rmse_vs_matched_baseline"] < 0).sum())
    ax2.text(
        0.02,
        0.98,
        f"{better_rmse}/{len(aug)} improve RMSE",
        transform=ax2.transAxes,
        ha="left",
        va="top",
        fontsize=10,
        bbox={"facecolor": "white", "edgecolor": "#dddddd", "pad": 3},
    )

    fig.suptitle("Validation performance versus matched no-augmentation baselines", fontsize=15)
    fig.savefig(PLOTS / "validation_headline_performance.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "validation_headline_performance.pdf", bbox_inches="tight")


def plot_extraction_gap(aug: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.8), constrained_layout=True)
    specs = [
        ("delta_r2_vs_matched_baseline", "ΔR² vs matched baseline"),
        ("delta_correlation_vs_matched_baseline", "ΔCorrelation vs matched baseline"),
    ]
    for ax, (ycol, ylabel) in zip(axes, specs):
        for mode, marker in MARKERS.items():
            for input_group, color in COLORS.items():
                sub = aug[(aug["mode"] == mode) & (aug["input_group"] == input_group)]
                ax.scatter(
                    sub["delta_extraction_gap_vs_matched_baseline"],
                    sub[ycol],
                    color=color,
                    marker=marker,
                    s=58,
                    alpha=0.85,
                )
        x = aug["delta_extraction_gap_vs_matched_baseline"].to_numpy()
        y = aug[ycol].to_numpy()
        slope, intercept = np.polyfit(x, y, 1)
        xs = np.linspace(float(x.min()), float(x.max()), 100)
        ax.plot(xs, intercept + slope * xs, color="#222222", linewidth=1.7)
        corr = np.corrcoef(x, y)[0, 1]
        ax.axhline(0, color="#777777", linestyle=":", linewidth=1)
        ax.axvline(0, color="#777777", linestyle=":", linewidth=1)
        ax.set_xlabel("Δ extraction gap vs matched baseline")
        ax.set_ylabel(ylabel)
        ax.grid(alpha=0.2)
        ax.text(
            0.02,
            0.98,
            f"r = {corr:.3f}",
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=10,
            bbox={"facecolor": "white", "edgecolor": "#dddddd", "pad": 3},
        )
    axes[0].set_title("A. Strongest link with ΔR²")
    axes[1].set_title("B. Also visible for correlation")
    fig.suptitle("Extraction-gap change explains performance change", fontsize=15)
    fig.savefig(PLOTS / "validation_headline_extraction_gap.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "validation_headline_extraction_gap.pdf", bbox_inches="tight")


def main() -> None:
    aug, ewoa_cfg = load_variant_summary()
    plot_updating(ewoa_cfg)
    plot_performance(aug)
    plot_extraction_gap(aug)


if __name__ == "__main__":
    main()
