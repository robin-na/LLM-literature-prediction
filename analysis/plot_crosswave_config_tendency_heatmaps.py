from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


REPO_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = REPO_ROOT / "results"
PLOTS_DIR = REPO_ROOT / "plots"
DATA_DIR = REPO_ROOT / "science-data_and_code" / "data" / "processed_data"

VAL_PRED_PATH = RESULTS_DIR / "prediction_positive_case_variations_41.csv"
LEARN_BASELINE_PRED_PATH = RESULTS_DIR / "prediction_learning_wave_elicitation_41.csv"
LEARN_AUG_PRED_PATH = RESULTS_DIR / "prediction_crosswave_variations_41_learning.csv"

VAL_GT_PATH = REPO_ROOT / "input" / "pgg_CONFIGmerged_validation.csv"
LEARN_GT_PATH = DATA_DIR / "df_paired_learn.csv"

BINARY_FEATURES = [
    "CONFIG_chat",
    "CONFIG_allOrNothing",
    "CONFIG_defaultContribProp",
    "CONFIG_rewardExists",
    "CONFIG_showNRounds",
    "CONFIG_showOtherSummaries",
    "CONFIG_showPunishmentId",
]

CONTINUOUS_FEATURES = [
    "control_pct",
    "CONFIG_playerCount",
    "CONFIG_numRounds",
    "CONFIG_MPCR",
    "CONFIG_punishmentCost",
    "CONFIG_punishmentTech",
    "CONFIG_rewardTech",
]

MODE_ORDER = ["single", "reasoning", "joint", "joint_reasoning"]
INPUT_ORDER = ["baseline", "both", "paper_only", "data_only"]
WAVE_ORDER = ["validation", "learning"]

FEATURE_LABELS = {
    "CONFIG_chat": "chat",
    "CONFIG_allOrNothing": "all-or-nothing",
    "CONFIG_defaultContribProp": "default contribute",
    "CONFIG_rewardExists": "reward exists",
    "CONFIG_showNRounds": "rounds known",
    "CONFIG_showOtherSummaries": "peer outcomes shown",
    "CONFIG_showPunishmentId": "punisher ID shown",
    "control_pct": "control efficiency",
    "CONFIG_playerCount": "player count",
    "CONFIG_numRounds": "round count",
    "CONFIG_MPCR": "MPCR",
    "CONFIG_punishmentCost": "punishment cost",
    "CONFIG_punishmentTech": "punishment tech",
    "CONFIG_rewardTech": "reward tech",
}

COL_LABELS = {
    ("baseline", "single"): "baseline\nsingle",
    ("baseline", "reasoning"): "baseline\nreasoning",
    ("baseline", "joint"): "baseline\njoint",
    ("baseline", "joint_reasoning"): "baseline\njoint+reason",
    ("both", "single"): "both\nsingle",
    ("both", "reasoning"): "both\nreasoning",
    ("both", "joint"): "both\njoint",
    ("both", "joint_reasoning"): "both\njoint+reason",
    ("paper_only", "single"): "paper\nsingle",
    ("paper_only", "reasoning"): "paper\nreasoning",
    ("paper_only", "joint"): "paper\njoint",
    ("paper_only", "joint_reasoning"): "paper\njoint+reason",
    ("data_only", "single"): "data\nsingle",
    ("data_only", "reasoning"): "data\nreasoning",
    ("data_only", "joint"): "data\njoint",
    ("data_only", "joint_reasoning"): "data\njoint+reason",
}

DELTA_COL_LABELS = {
    ("both", "single"): "both\nsingle",
    ("both", "reasoning"): "both\nreasoning",
    ("both", "joint"): "both\njoint",
    ("both", "joint_reasoning"): "both\njoint+reason",
    ("paper_only", "single"): "paper\nsingle",
    ("paper_only", "reasoning"): "paper\nreasoning",
    ("paper_only", "joint"): "paper\njoint",
    ("paper_only", "joint_reasoning"): "paper\njoint+reason",
    ("data_only", "single"): "data\nsingle",
    ("data_only", "reasoning"): "data\nreasoning",
    ("data_only", "joint"): "data\njoint",
    ("data_only", "joint_reasoning"): "data\njoint+reason",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Plot CONFIG tendency heatmaps for validation/learning prediction outputs."
    )
    parser.add_argument(
        "--validation-pred",
        type=Path,
        default=VAL_PRED_PATH,
        help="Validation prediction CSV.",
    )
    parser.add_argument(
        "--learning-pred",
        type=Path,
        default=LEARN_AUG_PRED_PATH,
        help="Learning prediction CSV.",
    )
    parser.add_argument(
        "--learning-baseline-pred",
        type=Path,
        default=LEARN_BASELINE_PRED_PATH,
        help="Optional baseline learning prediction CSV used when the learning CSV lacks baseline rows.",
    )
    parser.add_argument(
        "--output-prefix",
        default="crosswave",
        help="Prefix for output files.",
    )
    return parser.parse_args()


def parse_variation_name(name: str) -> tuple[str, str]:
    if name.endswith("_joint_reasoning"):
        return name[: -len("_joint_reasoning")], "joint_reasoning"
    if name.endswith("_joint"):
        return name[: -len("_joint")], "joint"
    if name.endswith("_reasoning"):
        return name[: -len("_reasoning")], "reasoning"
    return name, "single"


def input_group_from_family(family: str) -> str:
    if family.startswith("both_"):
        return "both"
    if family.startswith("paper_only_"):
        return "paper_only"
    if family.startswith("data_only_"):
        return "data_only"
    return "baseline"


def matched_baseline_name(mode: str) -> str:
    return {
        "single": "baseline",
        "reasoning": "baseline_reasoning",
        "joint": "baseline_joint",
        "joint_reasoning": "baseline_joint_reasoning",
    }[mode]


def load_validation_predictions(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, index_col=0)


def load_learning_predictions(path: Path, baseline_path: Path | None) -> pd.DataFrame:
    pred = pd.read_csv(path, index_col=0)
    required = {"baseline", "baseline_reasoning", "baseline_joint", "baseline_joint_reasoning"}
    if required.issubset(set(pred.index)):
        return pred
    if baseline_path is None:
        raise ValueError("Learning predictions lack baselines and no baseline file was provided.")
    baseline = pd.read_csv(baseline_path, index_col=0).loc[sorted(required)]
    return pd.concat([baseline, pred], axis=0)


def build_wave_dataset(
    wave: str,
    validation_pred_path: Path,
    learning_pred_path: Path,
    learning_baseline_pred_path: Path | None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    if wave == "validation":
        pred = load_validation_predictions(validation_pred_path)
        gt = pd.read_csv(VAL_GT_PATH).reset_index(drop=True)
        labels = [f"Q{i}" for i in range(1, len(gt) + 1)]
        control = gt["efficiency_np"] * 100.0
        treatment = gt["efficiency_p"] * 100.0
    elif wave == "learning":
        pred = load_learning_predictions(learning_pred_path, learning_baseline_pred_path)
        gt = pd.read_csv(LEARN_GT_PATH).sort_values("CONFIG_configId").reset_index(drop=True)
        labels = [f"L{i}" for i in range(1, len(gt) + 1)]
        control = gt["control_itt_efficiency"] * 100.0
        treatment = gt["treatment_itt_efficiency"] * 100.0
    else:
        raise ValueError("wave must be validation or learning")

    config = pd.DataFrame(
        {
            "wave": wave,
            "label": labels,
            "CONFIG_configId": gt["CONFIG_configId"].astype(int),
            "control_pct": control.astype(float),
            "true_treatment_pct": treatment.astype(float),
            "true_effect_pct": (treatment - control).astype(float),
        }
    )

    for feature in BINARY_FEATURES:
        config[feature] = gt[feature].astype(int)
    for feature in [
        "CONFIG_playerCount",
        "CONFIG_numRounds",
        "CONFIG_MPCR",
        "CONFIG_punishmentCost",
        "CONFIG_punishmentTech",
        "CONFIG_rewardTech",
    ]:
        config[feature] = gt[feature].astype(float)

    meta_rows = []
    pred_effect_cols: dict[str, np.ndarray] = {}
    for variation in pred.index:
        family, mode = parse_variation_name(variation)
        input_group = input_group_from_family(family)
        meta_rows.append(
            {
                "wave": wave,
                "variation": variation,
                "family": family,
                "mode": mode,
                "input_group": input_group,
            }
        )
        pred_vals = pd.to_numeric(pred.loc[variation], errors="coerce").reindex(labels).to_numpy(float)
        pred_effect_cols[f"{variation}_pred"] = pred_vals
        pred_effect_cols[f"{variation}_effect"] = pred_vals - control.to_numpy(float)

    config = pd.concat([config, pd.DataFrame(pred_effect_cols)], axis=1)

    meta = pd.DataFrame(meta_rows)
    return config, meta


def compute_feature_tables(config: pd.DataFrame, meta: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    binary_rows: list[dict[str, object]] = []
    continuous_rows: list[dict[str, object]] = []

    for _, row in meta.iterrows():
        variation = row["variation"]
        effect_col = f"{variation}_effect"

        for feature in BINARY_FEATURES:
            low = config[config[feature] == 0][effect_col]
            high = config[config[feature] == 1][effect_col]
            binary_rows.append(
                {
                    **row.to_dict(),
                    "feature": feature,
                    "effect_stat": "binary_diff_1_minus_0",
                    "value": float(high.mean() - low.mean()),
                    "n_level0": int(low.notna().sum()),
                    "n_level1": int(high.notna().sum()),
                }
            )

        for feature in CONTINUOUS_FEATURES:
            continuous_rows.append(
                {
                    **row.to_dict(),
                    "feature": feature,
                    "effect_stat": "correlation_with_predicted_effect",
                    "value": float(config[feature].corr(config[effect_col])),
                    "n": int(config[effect_col].notna().sum()),
                }
            )

    return pd.DataFrame(binary_rows), pd.DataFrame(continuous_rows)


def aggregate_feature_table(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["wave", "input_group", "mode", "feature"], dropna=False)
        .agg(
            median_value=("value", "median"),
            mean_value=("value", "mean"),
            n_variants=("variation", "size"),
        )
        .reset_index()
    )


def build_augmentation_delta_table(agg_df: pd.DataFrame) -> pd.DataFrame:
    baseline = agg_df[agg_df["input_group"] == "baseline"][
        ["wave", "mode", "feature", "median_value", "mean_value"]
    ].rename(
        columns={
            "median_value": "baseline_median_value",
            "mean_value": "baseline_mean_value",
        }
    )
    augmented = agg_df[agg_df["input_group"] != "baseline"].copy()
    merged = augmented.merge(baseline, on=["wave", "mode", "feature"], how="left")
    merged["median_delta_vs_baseline"] = (
        merged["median_value"] - merged["baseline_median_value"]
    )
    merged["mean_delta_vs_baseline"] = merged["mean_value"] - merged["baseline_mean_value"]
    return merged


def order_columns(delta: bool) -> list[tuple[str, str]]:
    if delta:
        return [(g, m) for g in INPUT_ORDER if g != "baseline" for m in MODE_ORDER]
    return [(g, m) for g in INPUT_ORDER for m in MODE_ORDER]


def build_pivot(
    agg_df: pd.DataFrame,
    wave: str,
    features: list[str],
    value_col: str,
    delta: bool,
) -> pd.DataFrame:
    subset = agg_df[agg_df["wave"] == wave].copy()
    pivot = subset.pivot_table(
        index="feature",
        columns=["input_group", "mode"],
        values=value_col,
        aggfunc="first",
    )
    desired_cols = order_columns(delta=delta)
    pivot = pivot.reindex(index=features, columns=pd.MultiIndex.from_tuples(desired_cols))
    pivot.index = [FEATURE_LABELS[f] for f in pivot.index]
    if delta:
        pivot.columns = [DELTA_COL_LABELS[(g, m)] for g, m in desired_cols]
    else:
        pivot.columns = [COL_LABELS[(g, m)] for g, m in desired_cols]
    return pivot


def plot_heatmap_pair(
    source_df: pd.DataFrame,
    features: list[str],
    value_col: str,
    title: str,
    subtitle: str,
    output_png: Path,
    output_pdf: Path,
    delta: bool,
) -> None:
    sns.set_theme(style="white", font_scale=0.95)
    fig, axes = plt.subplots(2, 1, figsize=(15, 10), constrained_layout=True)

    vmax = np.nanmax(np.abs(source_df[value_col].to_numpy(dtype=float)))
    vmax = float(vmax) if np.isfinite(vmax) and vmax > 0 else 1.0

    for ax, wave in zip(axes, WAVE_ORDER):
        pivot = build_pivot(source_df, wave, features, value_col=value_col, delta=delta)
        sns.heatmap(
            pivot,
            ax=ax,
            cmap="RdBu_r",
            center=0.0,
            vmin=-vmax,
            vmax=vmax,
            annot=True,
            fmt=".2f",
            linewidths=0.5,
            linecolor="#e5e7eb",
            cbar=ax is axes[-1],
            annot_kws={"fontsize": 9},
        )
        ax.set_title(f"{wave}: {subtitle}")
        ax.set_xlabel("")
        ax.set_ylabel("")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
        ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

    fig.suptitle(title, y=1.02, fontsize=18)
    fig.savefig(output_png, dpi=200, bbox_inches="tight")
    fig.savefig(output_pdf, bbox_inches="tight")
    plt.close(fig)


def output_paths(prefix: str) -> dict[str, Path]:
    return {
        "binary_table": RESULTS_DIR / f"{prefix}_config_tendency_binary_table.csv",
        "cont_table": RESULTS_DIR / f"{prefix}_config_tendency_continuous_table.csv",
        "binary_agg": RESULTS_DIR / f"{prefix}_config_tendency_binary_aggregated.csv",
        "cont_agg": RESULTS_DIR / f"{prefix}_config_tendency_continuous_aggregated.csv",
        "binary_delta": RESULTS_DIR / f"{prefix}_config_tendency_binary_augmentation_delta.csv",
        "cont_delta": RESULTS_DIR / f"{prefix}_config_tendency_continuous_augmentation_delta.csv",
        "raw_binary_png": PLOTS_DIR / f"{prefix}_config_tendency_binary_heatmap.png",
        "raw_binary_pdf": PLOTS_DIR / f"{prefix}_config_tendency_binary_heatmap.pdf",
        "raw_cont_png": PLOTS_DIR / f"{prefix}_config_tendency_continuous_heatmap.png",
        "raw_cont_pdf": PLOTS_DIR / f"{prefix}_config_tendency_continuous_heatmap.pdf",
        "delta_binary_png": PLOTS_DIR / f"{prefix}_config_augmentation_binary_delta_heatmap.png",
        "delta_binary_pdf": PLOTS_DIR / f"{prefix}_config_augmentation_binary_delta_heatmap.pdf",
        "delta_cont_png": PLOTS_DIR / f"{prefix}_config_augmentation_continuous_delta_heatmap.png",
        "delta_cont_pdf": PLOTS_DIR / f"{prefix}_config_augmentation_continuous_delta_heatmap.pdf",
    }


def main() -> None:
    args = parse_args()
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    paths = output_paths(args.output_prefix)

    val_config, val_meta = build_wave_dataset(
        "validation",
        validation_pred_path=args.validation_pred,
        learning_pred_path=args.learning_pred,
        learning_baseline_pred_path=args.learning_baseline_pred,
    )
    learn_config, learn_meta = build_wave_dataset(
        "learning",
        validation_pred_path=args.validation_pred,
        learning_pred_path=args.learning_pred,
        learning_baseline_pred_path=args.learning_baseline_pred,
    )

    binary_val, cont_val = compute_feature_tables(val_config, val_meta)
    binary_learn, cont_learn = compute_feature_tables(learn_config, learn_meta)

    binary_table = pd.concat([binary_val, binary_learn], ignore_index=True)
    cont_table = pd.concat([cont_val, cont_learn], ignore_index=True)
    binary_table.to_csv(paths["binary_table"], index=False)
    cont_table.to_csv(paths["cont_table"], index=False)

    binary_agg = aggregate_feature_table(binary_table)
    cont_agg = aggregate_feature_table(cont_table)
    binary_agg.to_csv(paths["binary_agg"], index=False)
    cont_agg.to_csv(paths["cont_agg"], index=False)

    binary_delta = build_augmentation_delta_table(binary_agg)
    cont_delta = build_augmentation_delta_table(cont_agg)
    binary_delta.to_csv(paths["binary_delta"], index=False)
    cont_delta.to_csv(paths["cont_delta"], index=False)

    plot_heatmap_pair(
        binary_agg,
        BINARY_FEATURES,
        value_col="median_value",
        title="CONFIG Effects On Predicted Treatment Effect",
        subtitle="binary feature effect: mean(predicted effect | 1) - mean(predicted effect | 0)",
        output_png=paths["raw_binary_png"],
        output_pdf=paths["raw_binary_pdf"],
        delta=False,
    )
    plot_heatmap_pair(
        cont_agg,
        CONTINUOUS_FEATURES,
        value_col="median_value",
        title="CONFIG Correlations With Predicted Treatment Effect",
        subtitle="continuous feature effect: correlation(feature, predicted effect)",
        output_png=paths["raw_cont_png"],
        output_pdf=paths["raw_cont_pdf"],
        delta=False,
    )
    plot_heatmap_pair(
        binary_delta,
        BINARY_FEATURES,
        value_col="median_delta_vs_baseline",
        title="Augmentation Shift In Binary CONFIG Effects",
        subtitle="median augmented effect minus matched no-input baseline effect",
        output_png=paths["delta_binary_png"],
        output_pdf=paths["delta_binary_pdf"],
        delta=True,
    )
    plot_heatmap_pair(
        cont_delta,
        CONTINUOUS_FEATURES,
        value_col="median_delta_vs_baseline",
        title="Augmentation Shift In Continuous CONFIG Effects",
        subtitle="median augmented correlation minus matched no-input baseline correlation",
        output_png=paths["delta_cont_png"],
        output_pdf=paths["delta_cont_pdf"],
        delta=True,
    )

    print(f"Wrote {paths['binary_table'].name}")
    print(f"Wrote {paths['cont_table'].name}")
    print(f"Wrote {paths['binary_agg'].name}")
    print(f"Wrote {paths['cont_agg'].name}")
    print(f"Wrote {paths['binary_delta'].name}")
    print(f"Wrote {paths['cont_delta'].name}")
    print(f"Wrote {paths['raw_binary_png'].name}")
    print(f"Wrote {paths['raw_cont_png'].name}")
    print(f"Wrote {paths['delta_binary_png'].name}")
    print(f"Wrote {paths['delta_cont_png'].name}")


if __name__ == "__main__":
    main()
