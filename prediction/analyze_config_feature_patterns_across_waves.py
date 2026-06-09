from __future__ import annotations

from pathlib import Path

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = REPO_ROOT / "results"

LEARNING_PRED = RESULTS_DIR / "prediction_learning_wave_elicitation_41.csv"
VALIDATION_PRED = RESULTS_DIR / "prediction_positive_case_variations_41.csv"

LEARNING_DF = REPO_ROOT / "science_data" / "data" / "processed_data" / "df_paired_learn.csv"
VALIDATION_DF = REPO_ROOT / "input" / "pgg_CONFIGmerged_validation.csv"

VARIATIONS = [
    "baseline",
    "baseline_reasoning",
    "baseline_joint",
    "baseline_joint_reasoning",
]

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


def build_wave_frame(wave: str) -> pd.DataFrame:
    if wave == "learning_wave":
        pred = pd.read_csv(LEARNING_PRED, index_col=0)
        df = pd.read_csv(LEARNING_DF).sort_values("CONFIG_configId").reset_index(drop=True)
        labels = [f"L{i}" for i in range(1, len(df) + 1)]
        control = df["control_itt_efficiency"] * 100
        treatment = df["treatment_itt_efficiency"] * 100
    elif wave == "validation_20":
        pred = pd.read_csv(VALIDATION_PRED, index_col=0).loc[VARIATIONS]
        df = pd.read_csv(VALIDATION_DF).reset_index(drop=True)
        labels = [f"Q{i}" for i in range(1, len(df) + 1)]
        control = df["efficiency_np"] * 100
        treatment = df["efficiency_p"] * 100
    else:
        raise ValueError("wave must be learning_wave or validation_20")

    out = pd.DataFrame(
        {
            "wave": wave,
            "label": labels,
            "CONFIG_configId": df["CONFIG_configId"].astype(int),
            "control_pct": control,
            "true_treatment_pct": treatment,
            "true_effect_pct": treatment - control,
        }
    )

    for feature in BINARY_FEATURES:
        out[feature] = df[feature].astype(int)

    for feature in [
        "CONFIG_playerCount",
        "CONFIG_numRounds",
        "CONFIG_MPCR",
        "CONFIG_punishmentCost",
        "CONFIG_punishmentTech",
        "CONFIG_rewardTech",
    ]:
        out[feature] = df[feature].astype(float)

    for variation in VARIATIONS:
        pred_vals = pd.to_numeric(pred.loc[variation], errors="coerce").reindex(labels).to_numpy(float)
        out[f"{variation}_pred"] = pred_vals
        out[f"{variation}_effect"] = pred_vals - control.to_numpy(float)

    return out


def binary_level_summary(wave_df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for wave in wave_df["wave"].unique():
        wave_sub = wave_df[wave_df["wave"] == wave]
        for feature in BINARY_FEATURES:
            for level in [0, 1]:
                sub = wave_sub[wave_sub[feature] == level]
                row: dict[str, object] = {
                    "wave": wave,
                    "feature": feature,
                    "level": level,
                    "n": len(sub),
                    "true_mean_effect": float(sub["true_effect_pct"].mean()),
                    "true_positive_share": float((sub["true_effect_pct"] > 0).mean()),
                }
                for variation in VARIATIONS:
                    eff = sub[f"{variation}_effect"]
                    row[f"{variation}_mean_effect"] = float(eff.mean())
                    row[f"{variation}_positive_share"] = float((eff > 0).mean())
                rows.append(row)
    return pd.DataFrame(rows)


def binary_contrast_summary(level_df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for wave in level_df["wave"].unique():
        wave_sub = level_df[level_df["wave"] == wave]
        for feature in BINARY_FEATURES:
            low = wave_sub[(wave_sub["feature"] == feature) & (wave_sub["level"] == 0)].iloc[0]
            high = wave_sub[(wave_sub["feature"] == feature) & (wave_sub["level"] == 1)].iloc[0]
            row: dict[str, object] = {
                "wave": wave,
                "feature": feature,
                "n_level0": int(low["n"]),
                "n_level1": int(high["n"]),
                "true_mean_effect_diff_1_minus_0": float(high["true_mean_effect"] - low["true_mean_effect"]),
                "true_positive_share_diff_1_minus_0": float(high["true_positive_share"] - low["true_positive_share"]),
            }
            signs = []
            for variation in VARIATIONS:
                diff = float(high[f"{variation}_mean_effect"] - low[f"{variation}_mean_effect"])
                row[f"{variation}_mean_effect_diff_1_minus_0"] = diff
                row[f"{variation}_positive_share_diff_1_minus_0"] = float(
                    high[f"{variation}_positive_share"] - low[f"{variation}_positive_share"]
                )
                signs.append(1 if diff > 0 else (-1 if diff < 0 else 0))

            row["n_variants_up"] = int(sum(s > 0 for s in signs))
            row["n_variants_down"] = int(sum(s < 0 for s in signs))
            row["consistent_direction"] = (
                "up"
                if row["n_variants_up"] == len(VARIATIONS)
                else "down"
                if row["n_variants_down"] == len(VARIATIONS)
                else "mixed"
            )
            rows.append(row)
    return pd.DataFrame(rows)


def continuous_correlation_summary(wave_df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for wave in wave_df["wave"].unique():
        sub = wave_df[wave_df["wave"] == wave]
        for feature in CONTINUOUS_FEATURES:
            row: dict[str, object] = {
                "wave": wave,
                "feature": feature,
                "true_effect_corr": float(sub[feature].corr(sub["true_effect_pct"])),
            }
            signs = []
            for variation in VARIATIONS:
                corr = float(sub[feature].corr(sub[f"{variation}_effect"]))
                row[f"{variation}_corr"] = corr
                signs.append(1 if corr > 0 else (-1 if corr < 0 else 0))
            row["n_variants_positive_corr"] = int(sum(s > 0 for s in signs))
            row["n_variants_negative_corr"] = int(sum(s < 0 for s in signs))
            row["consistent_direction"] = (
                "positive"
                if row["n_variants_positive_corr"] == len(VARIATIONS)
                else "negative"
                if row["n_variants_negative_corr"] == len(VARIATIONS)
                else "mixed"
            )
            rows.append(row)
    return pd.DataFrame(rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    learning_df = build_wave_frame("learning_wave")
    validation_df = build_wave_frame("validation_20")
    combined = pd.concat([learning_df, validation_df], ignore_index=True)

    combined.to_csv(RESULTS_DIR / "config_effect_patterns_by_wave.csv", index=False)

    level_df = binary_level_summary(combined)
    level_df.to_csv(RESULTS_DIR / "config_binary_feature_levels_by_wave.csv", index=False)

    contrast_df = binary_contrast_summary(level_df)
    contrast_df.to_csv(RESULTS_DIR / "config_binary_feature_contrasts_by_wave.csv", index=False)

    cont_df = continuous_correlation_summary(combined)
    cont_df.to_csv(RESULTS_DIR / "config_continuous_feature_correlations_by_wave.csv", index=False)

    print("Wrote config_effect_patterns_by_wave.csv")
    print("Wrote config_binary_feature_levels_by_wave.csv")
    print("Wrote config_binary_feature_contrasts_by_wave.csv")
    print("Wrote config_continuous_feature_correlations_by_wave.csv")


if __name__ == "__main__":
    main()
