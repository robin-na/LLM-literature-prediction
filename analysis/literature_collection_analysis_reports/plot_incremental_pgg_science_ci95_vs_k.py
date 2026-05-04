from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from analyze_validation_incremental_pgg_science_ensemble_size_curve import (
    CONDITION_LABELS,
    CONDITION_ORDER,
    MODEL_ORDER,
    N_MONTE_CARLO,
    load_repeat_rows,
    load_ensemble30,
    simulate_k_distribution,
    _truth_vector,
)


RESULTS_DIR = ROOT / "results" / "validation" / "literature_incremental_pgg_science_repeat30"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_incremental_pgg_science_repeat30"

CONDITION_COLORS = {
    "baseline": "#9ca3af",
    "science_gpt41": "#2563eb",
    "science_gpt51": "#f28e2b",
}


def build_curve_with_ci95() -> pd.DataFrame:
    repeat_rows = load_repeat_rows()
    ensemble30 = load_ensemble30().set_index(["model", "condition"])
    truth = _truth_vector()

    rows: list[dict[str, object]] = []
    for model_idx, model in enumerate(MODEL_ORDER):
        for condition_idx, condition in enumerate(CONDITION_ORDER):
            sub = repeat_rows.loc[
                (repeat_rows["model"] == model) & (repeat_rows["condition"] == condition),
                ["repeat", *[f"Q{i}" for i in range(1, 21)]],
            ].sort_values("repeat")
            if sub.empty:
                continue
            pred_mat = sub.loc[:, [f"Q{i}" for i in range(1, 21)]].to_numpy(dtype=float)
            if pred_mat.shape != (30, 20):
                raise ValueError(f"Expected 30x20 matrix for {model} / {condition}, got {pred_mat.shape}")

            for k in range(1, 31):
                if k == 30:
                    dist = pd.Series([float(ensemble30.loc[(model, condition), "correlation"])])
                else:
                    dist = pd.Series(
                        simulate_k_distribution(
                            pred_mat,
                            truth,
                            sample_size=k,
                            n_samples=N_MONTE_CARLO,
                            seed=100_000 + 1000 * model_idx + 100 * condition_idx + k,
                        )
                    )
                rows.append(
                    {
                        "model": model,
                        "condition": condition,
                        "k_runs": k,
                        "mean": float(dist.mean()),
                        "p025": float(dist.quantile(0.025)),
                        "p25": float(dist.quantile(0.25)),
                        "p50": float(dist.quantile(0.50)),
                        "p75": float(dist.quantile(0.75)),
                        "p975": float(dist.quantile(0.975)),
                    }
                )

    out = pd.DataFrame(rows)
    out["condition"] = pd.Categorical(out["condition"], categories=CONDITION_ORDER, ordered=True)
    out["model"] = pd.Categorical(out["model"], categories=MODEL_ORDER, ordered=True)
    out["corr_interval95_width"] = out["p975"] - out["p025"]
    baseline_width = (
        out.loc[out["k_runs"] == 1, ["model", "condition", "corr_interval95_width"]]
        .rename(columns={"corr_interval95_width": "corr_interval95_width_k1"})
    )
    out = out.merge(baseline_width, on=["model", "condition"], how="left")
    out["corr_interval95_width_pct_of_k1"] = 100.0 * out["corr_interval95_width"] / out["corr_interval95_width_k1"]
    return out.sort_values(["condition", "model", "k_runs"]).reset_index(drop=True)


def build_condition_summary(curve: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for (condition, k_runs), part in curve.groupby(["condition", "k_runs"], observed=True):
        rows.append(
            {
                "condition": condition,
                "k_runs": int(k_runs),
                "median_corr_interval95_width": float(part["corr_interval95_width"].median()),
                "p25_corr_interval95_width": float(part["corr_interval95_width"].quantile(0.25)),
                "p75_corr_interval95_width": float(part["corr_interval95_width"].quantile(0.75)),
                "median_corr_interval95_width_pct_of_k1": float(part["corr_interval95_width_pct_of_k1"].median()),
                "p25_corr_interval95_width_pct_of_k1": float(part["corr_interval95_width_pct_of_k1"].quantile(0.25)),
                "p75_corr_interval95_width_pct_of_k1": float(part["corr_interval95_width_pct_of_k1"].quantile(0.75)),
            }
        )
    out = pd.DataFrame(rows)
    out["condition"] = pd.Categorical(out["condition"], categories=CONDITION_ORDER, ordered=True)
    return out.sort_values(["condition", "k_runs"]).reset_index(drop=True)


def plot_ci95_vs_k(curve: pd.DataFrame, summary: pd.DataFrame) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, axes = plt.subplots(1, 2, figsize=(13.8, 4.8), sharex=True)

    panels = [
        (
            axes[0],
            "corr_interval95_width",
            "median_corr_interval95_width",
            "p25_corr_interval95_width",
            "p75_corr_interval95_width",
            "95% interval width of correlation",
            "Absolute uncertainty",
        ),
        (
            axes[1],
            "corr_interval95_width_pct_of_k1",
            "median_corr_interval95_width_pct_of_k1",
            "p25_corr_interval95_width_pct_of_k1",
            "p75_corr_interval95_width_pct_of_k1",
            "95% interval width (% of k=1)",
            "Uncertainty relative to single-run",
        ),
    ]

    for ax, model_col, median_col, lo_col, hi_col, ylabel, title in panels:
        for condition in CONDITION_ORDER:
            part = curve.loc[curve["condition"] == condition]
            for _, sub in part.groupby("model", observed=True):
                ax.plot(
                    sub["k_runs"],
                    sub[model_col],
                    color=CONDITION_COLORS[condition],
                    alpha=0.18,
                    linewidth=1.0,
                    zorder=1,
                )

            sub = summary.loc[summary["condition"] == condition]
            ax.fill_between(
                sub["k_runs"],
                sub[lo_col],
                sub[hi_col],
                color=CONDITION_COLORS[condition],
                alpha=0.14,
                linewidth=0,
                zorder=2,
            )
            ax.plot(
                sub["k_runs"],
                sub[median_col],
                color=CONDITION_COLORS[condition],
                linewidth=2.3,
                zorder=3,
                label=CONDITION_LABELS[condition],
            )

        ax.set_title(title)
        ax.set_xlabel("Number of runs averaged (k out of 30)")
        ax.set_ylabel(ylabel)
        ax.grid(False)

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, frameon=False, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.03))
    fig.tight_layout(rect=(0, 0.08, 1, 1))

    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(PLOTS_DIR / "incremental_pgg_science_ci95_width_vs_k.png", dpi=240, bbox_inches="tight")
    fig.savefig(PLOTS_DIR / "incremental_pgg_science_ci95_width_vs_k.pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    curve = build_curve_with_ci95()
    summary = build_condition_summary(curve)
    curve.to_csv(RESULTS_DIR / "incremental_pgg_science_ci95_width_vs_k_curve.csv", index=False)
    summary.to_csv(RESULTS_DIR / "incremental_pgg_science_ci95_width_vs_k_summary.csv", index=False)
    plot_ci95_vs_k(curve, summary)


if __name__ == "__main__":
    main()
