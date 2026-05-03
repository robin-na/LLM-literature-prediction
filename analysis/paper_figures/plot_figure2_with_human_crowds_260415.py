from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"

K5_BOOTSTRAP_PLOT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_incremental_pgg_science_repeat30"
    / "incremental_pgg_science_k5_bootstrap_figure2_style_plot_rows.csv"
)
HUMAN_PREDICTIONS_CSV = ROOT / "science-data_and_code" / "data" / "processed_data" / "prediction_survey.csv"
VALIDATION_CSV = ROOT / "input" / "pgg_CONFIGmerged_validation.csv"
NO_AUG_BENCHMARKS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "no_augmentation_model_comparison"
    / "validation_no_augmentation_model_comparison_benchmarks.csv"
)

OUT_STEM = "figure2_benchmark_report_vs_baseline_correlation_with_human_crowds"
PLOT_ROWS_OUT_CSV = RESULTS_DIR / f"{OUT_STEM}_plot_rows.csv"
SUMMARY_OUT_CSV = RESULTS_DIR / f"{OUT_STEM}_summary.csv"
REFERENCE_OUT_CSV = RESULTS_DIR / f"{OUT_STEM}_reference_lines.csv"

CONDITION_ORDER = ["baseline", "science_gpt41"]
CONDITION_COLORS = {"baseline": "#c9ced6", "science_gpt41": "#f2a65a"}
CONDITION_LABELS = {"baseline": "No augmentation", "science_gpt41": "Benchmark paper augmented"}

CROWD_SPECS = [
    {
        "source": "prolific",
        "label": "Laypeople crowd",
        "color": "#caa27e",
        "linestyle": (0, (5, 2)),
    },
    {
        "source": "sspp",
        "label": "Experts crowd",
        "color": "#8d6748",
        "linestyle": (0, (1, 1)),
    },
]


def load_noise_ceiling() -> float:
    benchmarks = pd.read_csv(NO_AUG_BENCHMARKS_CSV)
    return float(benchmarks.loc[benchmarks["benchmark"] == "Noise ceiling", "correlation"].iloc[0])


def load_llm_plot_rows() -> pd.DataFrame:
    df = pd.read_csv(K5_BOOTSTRAP_PLOT_ROWS_CSV)
    df = df.loc[df["condition"].isin(CONDITION_ORDER)].copy()
    df["model"] = pd.Categorical(
        df["model"],
        categories=df.loc[df["condition"] == "baseline", "model"].tolist(),
        ordered=True,
    )
    df["condition"] = pd.Categorical(df["condition"], categories=CONDITION_ORDER, ordered=True)
    return df.sort_values(["model", "condition"]).reset_index(drop=True)


def load_human_crowd_reference() -> pd.DataFrame:
    pred = pd.read_csv(HUMAN_PREDICTIONS_CSV)
    pred = pred.query("prediction.between(-0.2, 1.2) and n_predictions_made == 20").copy()

    truth = (
        pd.read_csv(VALIDATION_CSV)
        .sort_values("CONFIG_configId")
        .set_index("CONFIG_configId")["efficiency_p"]
    )

    rows: list[dict[str, object]] = []
    for spec in CROWD_SPECS:
        wide = (
            pred.loc[pred["source"] == spec["source"], ["CONFIG_configId", "playerID", "prediction"]]
            .pivot_table(index="CONFIG_configId", columns="playerID", values="prediction", aggfunc="mean")
            .sort_index()
        )
        wide = wide.loc[:, wide.notna().all(axis=0)]
        crowd_pred = wide.mean(axis=1).to_numpy(dtype=float) * 100.0
        aligned_truth = truth.loc[wide.index].to_numpy(dtype=float) * 100.0
        rows.append(
            {
                "kind": "human_crowd",
                "source": spec["source"],
                "label": spec["label"],
                "value": float(np.corrcoef(crowd_pred, aligned_truth)[0, 1]),
                "n_complete_participants": int(wide.shape[1]),
                "n_questions": int(wide.shape[0]),
                "color": spec["color"],
                "linestyle": str(spec["linestyle"]),
            }
        )

    rows.append(
        {
            "kind": "noise_ceiling",
            "source": "noise_ceiling",
            "label": "Estimated noise ceiling",
            "value": load_noise_ceiling(),
            "n_complete_participants": np.nan,
            "n_questions": 20,
            "color": "#0f766e",
            "linestyle": "--",
        }
    )
    return pd.DataFrame(rows)


def plot_figure2(plot_df: pd.DataFrame, ref_df: pd.DataFrame) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(11.0, 7.0))

    model_order = plot_df["model"].cat.categories.tolist()
    y_positions = np.arange(len(model_order))
    offsets = {"baseline": -0.16, "science_gpt41": 0.16}

    ceiling = float(ref_df.loc[ref_df["kind"] == "noise_ceiling", "value"].iloc[0])
    ax.axvline(ceiling, color="#0f766e", linestyle="--", linewidth=1.4, zorder=1)

    for spec in CROWD_SPECS:
        row = ref_df.loc[ref_df["source"] == spec["source"]].iloc[0]
        ax.axvline(
            float(row["value"]),
            color=spec["color"],
            linestyle=spec["linestyle"],
            linewidth=1.6,
            alpha=0.95,
            zorder=1,
        )

    for condition in CONDITION_ORDER:
        part = (
            plot_df.loc[plot_df["condition"] == condition]
            .set_index("model")
            .reindex(model_order)
            .reset_index()
        )
        y = y_positions + offsets[condition]
        ax.barh(
            y,
            part["correlation"].to_numpy(dtype=float),
            color=CONDITION_COLORS[condition],
            edgecolor="#4b5563",
            linewidth=0.8,
            height=0.28,
            zorder=2,
            label=CONDITION_LABELS[condition],
        )
        xerr = np.vstack(
            [
                part["correlation"].to_numpy(dtype=float) - part["ci_low"].to_numpy(dtype=float),
                part["ci_high"].to_numpy(dtype=float) - part["correlation"].to_numpy(dtype=float),
            ]
        )
        ax.errorbar(
            part["correlation"].to_numpy(dtype=float),
            y,
            xerr=xerr,
            fmt="none",
            ecolor=(17 / 255, 24 / 255, 39 / 255, 0.28),
            elinewidth=0.9,
            capsize=2.5,
            zorder=3,
        )

    ax.set_xlim(0.0, 1.0)
    ax.set_xticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel("Correlation with true treatment outcome")
    ax.set_yticks(y_positions, model_order)
    ax.invert_yaxis()
    ax.grid(False)

    lay = ref_df.loc[ref_df["source"] == "prolific"].iloc[0]
    exp = ref_df.loc[ref_df["source"] == "sspp"].iloc[0]
    legend_items = [
        Line2D([0], [0], color=CONDITION_COLORS["baseline"], linewidth=8, label=CONDITION_LABELS["baseline"]),
        Line2D([0], [0], color=CONDITION_COLORS["science_gpt41"], linewidth=8, label=CONDITION_LABELS["science_gpt41"]),
        Line2D([0], [0], color="#0f766e", linestyle="--", linewidth=1.4, label="Estimated noise ceiling"),
        Line2D(
            [0],
            [0],
            color=str(lay["color"]),
            linestyle=CROWD_SPECS[0]["linestyle"],
            linewidth=1.6,
            label=f"Laypeople crowd ({float(lay['value']):.3f})",
        ),
        Line2D(
            [0],
            [0],
            color=str(exp["color"]),
            linestyle=CROWD_SPECS[1]["linestyle"],
            linewidth=1.6,
            label=f"Experts crowd ({float(exp['value']):.3f})",
        ),
    ]
    ax.legend(
        handles=legend_items,
        frameon=False,
        loc="upper left",
        bbox_to_anchor=(0.0, -0.19),
        ncol=2,
        columnspacing=1.2,
        handlelength=2.8,
        borderaxespad=0.0,
    )

    fig.text(
        0.99,
        0.03,
        "Bars show the mean correlation over 50,000 bootstrap 5-of-30 ensembles; whiskers show the 5th-95th percentile.",
        ha="right",
        va="bottom",
        fontsize=9.2,
        color="#4b5563",
    )
    fig.text(
        0.01,
        0.02,
        "Human crowd baselines use the correlation between the mean human prediction and the true outcome across the 20 validation questions.",
        ha="left",
        va="bottom",
        fontsize=9.0,
        color="#4b5563",
    )
    fig.subplots_adjust(bottom=0.28, right=0.95)

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"{OUT_STEM}.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    plot_df = load_llm_plot_rows()
    ref_df = load_human_crowd_reference()

    plot_df.to_csv(PLOT_ROWS_OUT_CSV, index=False)
    plot_df.to_csv(SUMMARY_OUT_CSV, index=False)
    ref_df.to_csv(REFERENCE_OUT_CSV, index=False)

    plot_figure2(plot_df, ref_df)


if __name__ == "__main__":
    main()
