from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


RESULTS_DIR = ROOT / "results" / "validation" / "literature_incremental_pgg_science_repeat30"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_incremental_pgg_science_repeat30"
CURVE_CSV = RESULTS_DIR / "incremental_pgg_science_ensemble_size_curve.csv"

CONDITION_ORDER = ["baseline", "science_gpt41", "science_gpt51"]
CONDITION_LABELS = {
    "baseline": "No augmentation",
    "science_gpt41": "PGG Science report (GPT-4.1)",
    "science_gpt51": "PGG Science report (GPT-5.1)",
}
CONDITION_COLORS = {
    "baseline": "#9ca3af",
    "science_gpt41": "#2563eb",
    "science_gpt51": "#f28e2b",
}


def load_curve() -> pd.DataFrame:
    df = pd.read_csv(CURVE_CSV)
    df["condition"] = pd.Categorical(df["condition"], categories=CONDITION_ORDER, ordered=True)
    df["corr_interval90_width"] = df["p95"] - df["p05"]
    baseline_width = (
        df.loc[df["k_runs"] == 1, ["model", "condition", "corr_interval90_width"]]
        .rename(columns={"corr_interval90_width": "corr_interval90_width_k1"})
    )
    df = df.merge(baseline_width, on=["model", "condition"], how="left")
    df["corr_interval90_width_pct_of_k1"] = 100.0 * df["corr_interval90_width"] / df["corr_interval90_width_k1"]
    return df.sort_values(["condition", "model", "k_runs"]).reset_index(drop=True)


def build_condition_summary(curve: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for (condition, k_runs), part in curve.groupby(["condition", "k_runs"], observed=True):
        rows.append(
            {
                "condition": condition,
                "k_runs": int(k_runs),
                "median_corr_interval90_width": float(part["corr_interval90_width"].median()),
                "p25_corr_interval90_width": float(part["corr_interval90_width"].quantile(0.25)),
                "p75_corr_interval90_width": float(part["corr_interval90_width"].quantile(0.75)),
                "median_corr_interval90_width_pct_of_k1": float(part["corr_interval90_width_pct_of_k1"].median()),
                "p25_corr_interval90_width_pct_of_k1": float(part["corr_interval90_width_pct_of_k1"].quantile(0.25)),
                "p75_corr_interval90_width_pct_of_k1": float(part["corr_interval90_width_pct_of_k1"].quantile(0.75)),
            }
        )
    out = pd.DataFrame(rows)
    out["condition"] = pd.Categorical(out["condition"], categories=CONDITION_ORDER, ordered=True)
    return out.sort_values(["condition", "k_runs"]).reset_index(drop=True)


def plot_ci_vs_k(curve: pd.DataFrame, summary: pd.DataFrame) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, axes = plt.subplots(1, 2, figsize=(13.8, 4.8), sharex=True)

    for ax, y_col, y_label, band_lo, band_hi in [
        (
            axes[0],
            "median_corr_interval90_width",
            "90% interval width of correlation",
            "p25_corr_interval90_width",
            "p75_corr_interval90_width",
        ),
        (
            axes[1],
            "median_corr_interval90_width_pct_of_k1",
            "90% interval width (% of k=1)",
            "p25_corr_interval90_width_pct_of_k1",
            "p75_corr_interval90_width_pct_of_k1",
        ),
    ]:
        for condition in CONDITION_ORDER:
            part = curve.loc[curve["condition"] == condition]
            for _, sub in part.groupby("model", observed=True):
                ax.plot(
                    sub["k_runs"],
                    sub["corr_interval90_width"] if "pct_of_k1" not in y_col else sub["corr_interval90_width_pct_of_k1"],
                    color=CONDITION_COLORS[condition],
                    alpha=0.18,
                    linewidth=1.0,
                    zorder=1,
                )

            sub = summary.loc[summary["condition"] == condition]
            ax.fill_between(
                sub["k_runs"],
                sub[band_lo],
                sub[band_hi],
                color=CONDITION_COLORS[condition],
                alpha=0.14,
                linewidth=0,
                zorder=2,
            )
            ax.plot(
                sub["k_runs"],
                sub[y_col],
                color=CONDITION_COLORS[condition],
                linewidth=2.3,
                zorder=3,
                label=CONDITION_LABELS[condition],
            )

        ax.set_xlabel("Number of runs averaged (k out of 30)")
        ax.set_ylabel(y_label)
        ax.grid(False)

    axes[0].set_title("Absolute uncertainty")
    axes[1].set_title("Uncertainty relative to single-run")

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, frameon=False, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.03))
    fig.tight_layout(rect=(0, 0.08, 1, 1))

    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(PLOTS_DIR / "incremental_pgg_science_ci_width_vs_k.png", dpi=240, bbox_inches="tight")
    fig.savefig(PLOTS_DIR / "incremental_pgg_science_ci_width_vs_k.pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    curve = load_curve()
    summary = build_condition_summary(curve)
    summary.to_csv(RESULTS_DIR / "incremental_pgg_science_ci_width_vs_k_summary.csv", index=False)
    plot_ci_vs_k(curve, summary)


if __name__ == "__main__":
    main()
