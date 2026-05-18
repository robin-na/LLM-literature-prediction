from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D


ROOT = Path(__file__).resolve().parents[2]
RESULTS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_stage1"
    / "validation_literature_collection_analysis_report_rows.csv"
)
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_collection_analysis_reports_stage1"

METRIC_ORDER = ["correlation", "rmse", "r2", "directional_accuracy"]
METRIC_LABELS = {
    "correlation": "Correlation",
    "rmse": "RMSE",
    "r2": r"$R^2$ vs learning-set treatment mean baseline",
    "directional_accuracy": "Directional Accuracy",
}
MODEL_COLORS = {
    "GPT-4.1": "#2b8cbe",
    "GPT-4.1 Mini": "#1b9e77",
    "GPT-4.1 Nano": "#8c564b",
}
MODEL_OFFSETS = {
    "GPT-4.1": -0.22,
    "GPT-4.1 Mini": 0.0,
    "GPT-4.1 Nano": 0.22,
}
VARIANT_ORDER = [
    "broad_all_2011",
    "leaf_a0_b0_c0",
    "leaf_a0_b0_c1",
    "leaf_a0_b1_c0",
    "leaf_a0_b1_c1",
    "leaf_a1_b0_c0",
    "leaf_a1_b0_c1",
    "leaf_a1_b1_c0",
    "leaf_a1_b1_c1",
]


def variant_label(variant_id: str, count: float | int | None) -> str:
    if variant_id == "broad_all_2011":
        return f"All papers\n(n={int(count)})"
    parts = variant_id.replace("leaf_", "").split("_")
    pretty = " | ".join(part.replace("a", "A=").replace("b", "B=").replace("c", "C=") for part in parts)
    return f"{pretty}\n(n={int(count)})"


def plot_correlation_by_model(rows: pd.DataFrame, variant_counts: pd.Series, y_base: np.ndarray, y_map: dict[str, int]) -> None:
    models = list(MODEL_COLORS.keys())
    fig, axes = plt.subplots(1, 3, figsize=(18, 8.5), sharey=True)

    corr_vals = rows["correlation"].to_numpy(dtype=float)
    base_vals = rows["baseline_correlation"].to_numpy(dtype=float)
    finite = np.isfinite(corr_vals) & np.isfinite(base_vals)
    x_min = min(corr_vals[finite].min(), base_vals[finite].min()) - 0.03
    x_max = max(corr_vals[finite].max(), base_vals[finite].max()) + 0.03

    label_text = [variant_label(v, variant_counts.loc[v]) for v in VARIANT_ORDER]

    for ax, model in zip(axes, models):
        color = MODEL_COLORS[model]
        part = rows[rows["model"] == model].set_index("variant_id").reindex(VARIANT_ORDER).reset_index()
        y = np.array([y_map[v] for v in part["variant_id"]], dtype=float)
        sig_mask = part["sig_improved_correlation"].fillna(False).to_numpy(dtype=bool)
        improved_mask = part["improved_correlation"].fillna(False).to_numpy(dtype=bool)

        baseline = float(part["baseline_correlation"].iloc[0])
        ax.axvline(
            baseline,
            color="black",
            linestyle="--",
            linewidth=1.1,
            alpha=0.85,
            zorder=0,
        )
        ax.scatter(
            part.loc[~improved_mask, "correlation"],
            y[~improved_mask],
            s=70,
            color="#b0b0b0",
            alpha=0.95,
            edgecolors=np.where(sig_mask[~improved_mask], "black", "white"),
            linewidths=np.where(sig_mask[~improved_mask], 1.2, 0.8),
            zorder=2,
        )
        ax.scatter(
            part.loc[improved_mask, "correlation"],
            y[improved_mask],
            s=70,
            color=color,
            alpha=0.95,
            edgecolors=np.where(sig_mask[improved_mask], "black", "white"),
            linewidths=np.where(sig_mask[improved_mask], 1.2, 0.8),
            zorder=3,
        )

        ax.set_title(model, loc="left")
        ax.set_xlim(x_min, x_max)
        ax.set_yticks(y_base)
        ax.set_yticklabels(label_text)
        ax.grid(axis="x", alpha=0.18)
        ax.set_axisbelow(True)
        ax.set_xlabel("Raw correlation")

    axes[0].set_ylabel("Collection variant")

    handles = [
        Line2D([], [], color=MODEL_COLORS["GPT-4.1"], marker="o", linestyle="None", markersize=7, label="Improves baseline"),
        Line2D([], [], color="#b0b0b0", marker="o", linestyle="None", markersize=7, label="Does not improve baseline"),
        Line2D([], [], color="black", marker="o", linestyle="None", markerfacecolor="white", markersize=7, label="Not significant"),
        Line2D([], [], color="black", marker="o", linestyle="None", markerfacecolor="black", markersize=7, label="Paired-bootstrap CI excludes 0"),
        Line2D([], [], color="black", linestyle="--", linewidth=1.1, label="No-augmentation baseline"),
    ]

    fig.legend(handles=handles, loc="lower center", ncol=5, frameon=False, bbox_to_anchor=(0.5, 0.01))
    fig.suptitle(
        "Correlation by collection variant and model\n"
        "A = exact/close on both PGG relevance and punishment relevance; "
        "B = reports payoff-like outcomes; C = empirical only",
        fontsize=15,
        y=0.98,
    )
    fig.text(
        0.5,
        0.045,
        "Rows are the 9 synthesized collection reports. Colored points improve the matched no-augmentation baseline. "
        "Black-edged points have paired-bootstrap 95% CIs that exclude 0.",
        ha="center",
        fontsize=9,
        color="0.3",
    )
    fig.tight_layout(rect=[0.12, 0.08, 1, 0.93])
    fig.savefig(
        PLOTS_DIR / "validation_literature_collection_analysis_report_correlation_by_model.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    rows = pd.read_csv(RESULTS_CSV)
    rows = rows.copy()
    rows["variant_id"] = pd.Categorical(rows["variant_id"], categories=VARIANT_ORDER, ordered=True)
    rows = rows.sort_values(["variant_id", "model"]).reset_index(drop=True)

    variant_counts = (
        rows.groupby("variant_id", dropna=False)["count"]
        .first()
        .reindex(VARIANT_ORDER)
    )
    y_base = np.arange(len(VARIANT_ORDER))[::-1]
    y_map = {variant_id: y for variant_id, y in zip(VARIANT_ORDER, y_base)}

    plt.rcParams["font.family"] = "Arial"
    plt.rcParams["font.size"] = 12

    fig, axes = plt.subplots(2, 2, figsize=(16, 10), sharey=True)
    axes = axes.flatten()

    for ax, metric in zip(axes, METRIC_ORDER):
        for model, color in MODEL_COLORS.items():
            part = rows[rows["model"] == model].set_index("variant_id").reindex(VARIANT_ORDER).reset_index()
            y = np.array([y_map[v] for v in part["variant_id"]], dtype=float) + MODEL_OFFSETS[model]

            # model-specific raw baseline reference
            baseline = float(part[f"baseline_{metric}"].iloc[0])
            ax.axvline(
                baseline,
                color=color,
                linestyle="--",
                linewidth=1.1,
                alpha=0.8,
                zorder=0,
            )

            sig_mask = part[f"sig_improved_{metric}"].fillna(False).to_numpy(dtype=bool)
            ax.scatter(
                part[metric],
                y,
                s=70,
                color=color,
                alpha=0.95,
                edgecolors=np.where(sig_mask, "black", "white"),
                linewidths=np.where(sig_mask, 1.2, 0.8),
                zorder=3,
            )

        ax.set_title(METRIC_LABELS[metric], loc="left")
        ax.grid(axis="x", alpha=0.18)
        ax.set_axisbelow(True)

    label_text = [variant_label(v, variant_counts.loc[v]) for v in VARIANT_ORDER]
    for ax in axes:
        ax.set_yticks(y_base)
        ax.set_yticklabels(label_text)

    axes[0].set_ylabel("Collection variant")
    axes[2].set_ylabel("Collection variant")
    axes[2].set_xlabel("Raw metric value")
    axes[3].set_xlabel("Raw metric value")

    handles = [
        Line2D([], [], color=color, marker="o", linestyle="None", markersize=7, label=model)
        for model, color in MODEL_COLORS.items()
    ]
    handles += [
        Line2D([], [], color="black", marker="o", linestyle="None", markerfacecolor="white", markersize=7, label="Not significant"),
        Line2D([], [], color="black", marker="o", linestyle="None", markerfacecolor="black", markersize=7, label="Paired-bootstrap CI excludes 0"),
        Line2D([], [], color="black", linestyle="--", linewidth=1.1, label="No-augmentation baseline"),
    ]

    fig.legend(handles=handles, loc="lower center", ncol=6, frameon=False, bbox_to_anchor=(0.5, 0.01))
    fig.suptitle(
        "Collection-level augmentation by paper-set definition\n"
        "A = exact/close on both PGG relevance and punishment relevance; "
        "B = reports payoff-like outcomes; C = empirical only",
        fontsize=15,
        y=0.98,
    )
    fig.text(
        0.5,
        0.045,
        "Rows are the 9 synthesized collection reports used as augmentation sources. "
        "Points show raw performance for each model. Dashed vertical lines show each model's matched no-augmentation baseline.",
        ha="center",
        fontsize=9,
        color="0.3",
    )
    fig.tight_layout(rect=[0.12, 0.08, 1, 0.93])
    fig.savefig(
        PLOTS_DIR / "validation_literature_collection_analysis_report_raw_levels.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)
    plot_correlation_by_model(rows, variant_counts, y_base, y_map)


if __name__ == "__main__":
    main()
