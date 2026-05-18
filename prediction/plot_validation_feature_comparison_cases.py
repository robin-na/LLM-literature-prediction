from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from analyze_validation_interaction_alignment import (
    compute_enet_validation_permutation_importance,
    load_or_compute_enet_validation_shap,
)


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
from plot_paths import VALIDATION_PLOTS as PLOTS, ensure_plot_dir
DATA = ROOT / "science_data" / "data" / "processed_data"

FEATURES = [
    "CONFIG_chat",
    "CONFIG_defaultContribProp",
    "CONFIG_allOrNothing",
    "CONFIG_numRounds",
    "CONFIG_showOtherSummaries",
    "CONFIG_rewardExists",
    "CONFIG_showNRounds",
    "CONFIG_MPCR",
    "CONFIG_punishmentCost",
    "CONFIG_showPunishmentId",
    "CONFIG_playerCount",
    "CONFIG_punishmentTech",
]

FEATURE_LABELS = {
    "CONFIG_chat": "Communication",
    "CONFIG_defaultContribProp": "Contribution Framing",
    "CONFIG_allOrNothing": "Contribution Type",
    "CONFIG_numRounds": "Game Length",
    "CONFIG_showOtherSummaries": "Peer Outcome Visibility",
    "CONFIG_rewardExists": "Reward",
    "CONFIG_showNRounds": "Horizon Knowledge",
    "CONFIG_MPCR": "Return Rate (MPCR)",
    "CONFIG_punishmentCost": "Peer Incentive Cost",
    "CONFIG_showPunishmentId": "Actor Anonymity",
    "CONFIG_playerCount": "Group Size",
    "CONFIG_punishmentTech": "Punishment Technology",
}

CASE_SPECS = [
    ("baseline_joint", "Baseline joint", "#4c78a8"),
    ("both_uncertainty_joint", "Best augmented", "#59a14f"),
    ("both_ensemble_joint", "Degraded augmented", "#e15759"),
]


def compute_r2_from_rmse(rmse: float, val_df: pd.DataFrame) -> float:
    control = 100 * val_df["control_itt_efficiency"].to_numpy()
    treatment = 100 * val_df["treatment_itt_efficiency"].to_numpy()
    null_mse = float(np.mean((control - treatment) ** 2))
    return 1.0 - (rmse**2) / null_mse


def signed_effect(x: pd.Series, y: pd.Series) -> float:
    x = x.astype(float)
    y = y.astype(float)
    uniq = sorted(pd.unique(x))
    if set(uniq).issubset({0, 1}):
        g1 = y[x == 1]
        g0 = y[x == 0]
        if len(g1) == 0 or len(g0) == 0:
            return np.nan
        return float(g1.mean() - g0.mean())
    if len(x) < 2 or np.allclose(x.std(ddof=0), 0):
        return np.nan
    slope = np.polyfit(x, y, 1)[0]
    return float(slope * x.std(ddof=0))


def load_variant_effects(val_df: pd.DataFrame) -> pd.DataFrame:
    pred = pd.read_csv(RESULTS / "prediction_positive_case_variations_41.csv").rename(columns={"Unnamed: 0": "variation"})
    q_cols = [c for c in pred.columns if c.startswith("Q")]
    control = 100 * val_df["control_itt_efficiency"].reset_index(drop=True)
    rows = []
    for _, row in pred.iterrows():
        temp = val_df.copy()
        temp["variation"] = row["variation"]
        temp["pred_effect"] = row[q_cols].astype(float).reset_index(drop=True).values - control.values
        rows.append(temp)
    return pd.concat(rows, ignore_index=True)


def build_feature_table() -> tuple[pd.DataFrame, pd.DataFrame]:
    val_df = pd.read_csv(DATA / "df_paired_val.csv").reset_index(drop=True)
    shap_df = load_or_compute_enet_validation_shap().copy()
    imp_df = compute_enet_validation_permutation_importance().copy()
    llm_df = load_variant_effects(val_df)
    metrics = pd.read_csv(RESULTS / "prediction_positive_case_variations_41_metrics.csv")

    shap_effects = []
    for feature in FEATURES:
        shap_effects.append(
            {
                "feature": feature,
                "target_signed_effect": signed_effect(val_df[feature], 100 * shap_df[f"shap_{feature}"]),
            }
        )
    target_df = pd.DataFrame(shap_effects)

    rows = []
    for variation, _, _ in CASE_SPECS:
        sub = llm_df[llm_df["variation"] == variation].copy()
        row = {"variation": variation}
        for feature in FEATURES:
            row[f"{feature}_signed_effect"] = signed_effect(sub[feature], sub["pred_effect"])
        rows.append(row)
    case_df = pd.DataFrame(rows)

    feature_df = (
        target_df.merge(
            imp_df.loc[:, ["feature", "pct_increase_in_error"]].rename(
                columns={"pct_increase_in_error": "enet_pct_increase_rmse"}
            ),
            on="feature",
            how="left",
        )
        .merge(case_df, how="cross")
    )

    # reshape case-specific effects to one row per feature
    wide_rows = []
    for feature in FEATURES:
        entry = {
            "feature": feature,
            "feature_label": FEATURE_LABELS[feature],
            "target_signed_effect": float(target_df.loc[target_df["feature"] == feature, "target_signed_effect"].iloc[0]),
            "enet_pct_increase_rmse": float(
                imp_df.loc[imp_df["feature"] == feature, "pct_increase_in_error"].iloc[0]
            ),
        }
        for variation, _, _ in CASE_SPECS:
            entry[variation] = float(case_df.loc[case_df["variation"] == variation, f"{feature}_signed_effect"].iloc[0])
        wide_rows.append(entry)
    wide = pd.DataFrame(wide_rows)
    for variation, _, _ in CASE_SPECS:
        wide[f"{variation}_abs_gap"] = (wide[variation] - wide["target_signed_effect"]).abs()
    wide["best_vs_baseline_gap_change"] = wide["baseline_joint_abs_gap"] - wide["both_uncertainty_joint_abs_gap"]
    wide["bad_vs_baseline_gap_change"] = wide["baseline_joint_abs_gap"] - wide["both_ensemble_joint_abs_gap"]
    weight = wide["enet_pct_increase_rmse"].clip(lower=0) / wide["enet_pct_increase_rmse"].clip(lower=0).max()
    wide["best_vs_baseline_gap_change_weighted"] = wide["best_vs_baseline_gap_change"] * weight
    wide["bad_vs_baseline_gap_change_weighted"] = wide["bad_vs_baseline_gap_change"] * weight
    wide = wide.sort_values("enet_pct_increase_rmse", ascending=False).reset_index(drop=True)

    metrics_rows = []
    for variation, label, _ in CASE_SPECS:
        metric_row = metrics.loc[metrics["variation"] == variation].iloc[0]
        metrics_rows.append(
            {
                "variation": variation,
                "label": label,
                "rmse": float(metric_row["rmse"]),
                "correlation": float(metric_row["correlation"]),
                "directional_accuracy": float(metric_row["directional_accuracy"]),
                "r2": compute_r2_from_rmse(float(metric_row["rmse"]), val_df),
            }
        )
    metrics_df = pd.DataFrame(metrics_rows)
    return wide, metrics_df


def plot_feature_comparison(feature_df: pd.DataFrame, metrics_df: pd.DataFrame) -> None:
    fig = plt.figure(figsize=(17.0, 10.5), constrained_layout=True)
    gs = fig.add_gridspec(1, 3, width_ratios=[1.0, 1.45, 1.1])
    ax_imp = fig.add_subplot(gs[0, 0])
    ax_signed = fig.add_subplot(gs[0, 1])
    ax_gap = fig.add_subplot(gs[0, 2])

    y = np.arange(len(feature_df))
    labels = feature_df["feature_label"]

    # Panel A: permutation importance
    ax_imp.barh(y, feature_df["enet_pct_increase_rmse"], color="#9c755f", alpha=0.85)
    ax_imp.set_yticks(y, labels)
    ax_imp.invert_yaxis()
    ax_imp.set_title("A. Validation E-net permutation importance")
    ax_imp.set_xlabel("% increase in validation RMSE when permuted")
    ax_imp.grid(axis="x", alpha=0.2)

    # Panel B: signed feature effects
    ax_signed.axvline(0, color="#999999", linewidth=1)
    ax_signed.scatter(feature_df["target_signed_effect"], y, color="#111111", marker="|", s=450, linewidths=2.5, label="E-net target")
    for variation, label, color in CASE_SPECS:
        ax_signed.scatter(feature_df[variation], y, color=color, s=60, label=label, alpha=0.9)
    ax_signed.set_yticks(y, [])
    ax_signed.invert_yaxis()
    ax_signed.set_title("B. Signed feature effect on validation predictions")
    ax_signed.set_xlabel("Standardized SHAP / predicted-effect contrast")
    ax_signed.grid(axis="x", alpha=0.2)
    ax_signed.legend(frameon=False, loc="lower right")

    # Panel C: change in alignment vs baseline
    ax_gap.axvline(0, color="#999999", linewidth=1)
    h = 0.35
    ax_gap.barh(y - h / 2, feature_df["best_vs_baseline_gap_change_weighted"], height=h, color="#59a14f", alpha=0.85, label="Best augmented vs baseline")
    ax_gap.barh(y + h / 2, feature_df["bad_vs_baseline_gap_change_weighted"], height=h, color="#e15759", alpha=0.85, label="Degraded augmented vs baseline")
    ax_gap.set_yticks(y, [])
    ax_gap.invert_yaxis()
    ax_gap.set_title("C. Alignment change vs baseline\n(weighted by E-net importance)")
    ax_gap.set_xlabel("Positive = moved closer to E-net target")
    ax_gap.grid(axis="x", alpha=0.2)
    ax_gap.legend(frameon=False, loc="lower right")

    metric_lines = [
        f"{row.label}: RMSE {row.rmse:.2f}, corr {row.correlation:.3f}, DA {row.directional_accuracy:.2f}, R^2 {row.r2:.3f}"
        for row in metrics_df.itertuples(index=False)
    ]
    fig.suptitle(
        "Validation feature-level comparison: no augmentation vs improved augmentation vs degraded augmentation",
        fontsize=16,
        y=1.02,
    )
    fig.text(0.52, 0.01, " | ".join(metric_lines), ha="center", fontsize=10, color="#444444")

    out_png = PLOTS / "validation_feature_comparison_cases.png"
    out_pdf = PLOTS / "validation_feature_comparison_cases.pdf"
    fig.savefig(out_png, dpi=220, bbox_inches="tight")
    fig.savefig(out_pdf, bbox_inches="tight")


def main() -> None:
    feature_df, metrics_df = build_feature_table()
    feature_df.to_csv(RESULTS / "validation_feature_comparison_cases_table.csv", index=False)
    metrics_df.to_csv(RESULTS / "validation_feature_comparison_cases_metrics.csv", index=False)
    plot_feature_comparison(feature_df, metrics_df)


if __name__ == "__main__":
    main()
