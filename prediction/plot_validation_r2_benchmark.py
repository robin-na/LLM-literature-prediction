from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
from plot_paths import VALIDATION_PLOTS as PLOTS, ensure_plot_dir

BASELINE_RMSE = 6.704339
NULL_MSE = 50.847465


def r2_from_rmse(rmse: float) -> float:
    return 1.0 - (rmse ** 2) / NULL_MSE


def load_rows() -> pd.DataFrame:
    baseline_comp = pd.read_csv(
        RESULTS / "prediction_positive_case_variations_baseline_comparison.csv"
    )
    nano_val = pd.read_csv(RESULTS / "prediction_crosswave_variations_41nano_validation_metrics.csv")
    r2_bench = pd.read_csv(RESULTS / "r2_vs_control_with_noise_ceiling.csv")

    rows = [
        {
            "label": "GPT-4.1 baseline",
            "group": "GPT-4.1",
            "r2": r2_from_rmse(BASELINE_RMSE),
        }
    ]

    for _, row in baseline_comp.iterrows():
        if row["variation"] == "baseline":
            continue
        rows.append(
            {
                "label": f"GPT-4.1 {row['variation']}",
                "group": "GPT-4.1",
                "r2": r2_from_rmse(float(row["rmse"])),
            }
        )

    for variation in [
        "baseline",
        "baseline_reasoning",
        "baseline_joint",
        "baseline_joint_reasoning",
    ]:
        row = nano_val.loc[nano_val["variation"] == variation].iloc[0]
        rows.append(
            {
                "label": f"GPT-4.1-nano {variation}",
                "group": "GPT-4.1-nano",
                "r2": r2_from_rmse(float(row["rmse"])),
            }
        )

    for model, label in [
        ("elastic_net", "Elastic net"),
        ("noise_ceiling", "Noise ceiling"),
    ]:
        row = r2_bench.loc[r2_bench["model"] == model].iloc[0]
        rows.append(
            {
                "label": label,
                "group": "Benchmarks",
                "r2": float(row["r2_vs_control_null"]),
            }
        )

    df = pd.DataFrame(rows)
    order = [
        "GPT-4.1 baseline",
        "GPT-4.1 baseline_reasoning",
        "GPT-4.1 baseline_joint",
        "GPT-4.1 baseline_joint_reasoning",
        "GPT-4.1-nano baseline",
        "GPT-4.1-nano baseline_reasoning",
        "GPT-4.1-nano baseline_joint",
        "GPT-4.1-nano baseline_joint_reasoning",
        "Elastic net",
        "Noise ceiling",
    ]
    return df.set_index("label").loc[order].reset_index()


def main() -> None:
    df = load_rows()
    colors = {
        "GPT-4.1": "#1f77b4",
        "GPT-4.1-nano": "#ff7f0e",
        "Benchmarks": "#2ca02c",
    }

    fig, ax = plt.subplots(figsize=(11.5, 7.2))
    y = list(range(len(df)))[::-1]

    for idx, (_, row) in enumerate(df.iterrows()):
        ypos = y[idx]
        ax.barh(ypos, row["r2"], color=colors[row["group"]], height=0.68)
        ax.text(
            row["r2"] + 0.012,
            ypos,
            f"{row['r2']:.3f}",
            va="center",
            ha="left",
            fontsize=10,
        )

    ax.set_yticks(y, df["label"])
    ax.set_xlabel(r"$R^2$ vs null predictor ($\hat{y}_{treatment}=control$)")
    ax.set_title("Validation Benchmark: Baselines, Elastic Net, And Noise Ceiling")
    ax.axvline(0.0, color="#666666", linewidth=1.0, linestyle="--")
    ax.grid(axis="x", alpha=0.25)
    ax.set_xlim(-1.15, 0.75)

    legend_handles = [
        plt.Rectangle((0, 0), 1, 1, color=colors[group], label=group)
        for group in ["GPT-4.1", "GPT-4.1-nano", "Benchmarks"]
    ]
    ax.legend(handles=legend_handles, loc="lower right", frameon=False)

    fig.tight_layout()

    out_csv = RESULTS / "validation_r2_benchmark_table.csv"
    out_png = PLOTS / "validation_r2_benchmark.png"
    out_pdf = PLOTS / "validation_r2_benchmark.pdf"
    df.to_csv(out_csv, index=False)
    fig.savefig(out_png, dpi=220, bbox_inches="tight")
    fig.savefig(out_pdf, bbox_inches="tight")


if __name__ == "__main__":
    main()
