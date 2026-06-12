from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = REPO_ROOT / "results"
PRED_PATH = RESULTS_DIR / "prediction_learning_wave_elicitation_41.csv"
LEARN_PATH = (
    REPO_ROOT / "science_data" / "data" / "processed_data" / "df_paired_learn.csv"
)

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


def build_effect_frame() -> pd.DataFrame:
    pred = pd.read_csv(PRED_PATH, index_col=0)
    learn = pd.read_csv(LEARN_PATH).sort_values("CONFIG_configId").reset_index(drop=True)
    control = learn["control_itt_efficiency"] * 100
    treatment = learn["treatment_itt_efficiency"] * 100

    df = pd.DataFrame(
        {
            "L": [f"L{i}" for i in range(1, len(learn) + 1)],
            "CONFIG_configId": learn["CONFIG_configId"].astype(int),
            "control_pct": control,
            "true_treatment_pct": treatment,
            "true_effect_pct": treatment - control,
        }
    )

    for col in BINARY_FEATURES:
        df[col] = learn[col].astype(int)
    for col in [
        "CONFIG_playerCount",
        "CONFIG_numRounds",
        "CONFIG_MPCR",
        "CONFIG_punishmentCost",
        "CONFIG_punishmentTech",
        "CONFIG_rewardCost",
        "CONFIG_rewardTech",
    ]:
        df[col] = learn[col].astype(float)

    for variation in pred.index:
        pred_vals = pd.to_numeric(pred.loc[variation], errors="coerce").to_numpy(float)
        df[f"{variation}_pred"] = pred_vals
        df[f"{variation}_effect"] = pred_vals - control.to_numpy(float)

    effect_cols = [f"{variation}_effect" for variation in pred.index]
    df["n_positive_pred_variants"] = (df[effect_cols] > 0).sum(axis=1)
    df["n_negative_pred_variants"] = (df[effect_cols] < 0).sum(axis=1)
    df["all_positive_pred"] = df["n_positive_pred_variants"].eq(len(pred.index))
    df["all_negative_pred"] = df["n_negative_pred_variants"].eq(len(pred.index))
    df["sign_flip_across_variants"] = (
        df["n_positive_pred_variants"].gt(0) & df["n_negative_pred_variants"].gt(0)
    )
    return df


def binary_feature_summary(effect_df: pd.DataFrame, variations: list[str]) -> pd.DataFrame:
    records: list[dict[str, float | int | str]] = []
    for feature in BINARY_FEATURES:
        for level in [0, 1]:
            sub = effect_df[effect_df[feature] == level]
            record: dict[str, float | int | str] = {
                "feature": feature,
                "level": level,
                "n": len(sub),
                "true_mean_effect": float(sub["true_effect_pct"].mean()),
                "true_positive_share": float((sub["true_effect_pct"] > 0).mean()),
            }
            for variation in variations:
                eff = sub[f"{variation}_effect"]
                record[f"{variation}_mean_effect"] = float(eff.mean())
                record[f"{variation}_positive_share"] = float((eff > 0).mean())
            records.append(record)
    return pd.DataFrame.from_records(records)


def continuous_feature_correlations(
    effect_df: pd.DataFrame, variations: list[str]
) -> pd.DataFrame:
    records: list[dict[str, float | str]] = []
    for feature in CONTINUOUS_FEATURES:
        record: dict[str, float | str] = {
            "feature": feature,
            "true_effect_corr": float(effect_df[feature].corr(effect_df["true_effect_pct"])),
        }
        for variation in variations:
            record[f"{variation}_corr"] = float(
                effect_df[feature].corr(effect_df[f"{variation}_effect"])
            )
        records.append(record)
    return pd.DataFrame.from_records(records)


def shift_summary(effect_df: pd.DataFrame) -> pd.DataFrame:
    def summarize_shift(a: str, b: str) -> dict[str, float | int | str]:
        eff_a = effect_df[f"{a}_effect"].to_numpy(float)
        eff_b = effect_df[f"{b}_effect"].to_numpy(float)
        sign_a = np.sign(eff_a)
        sign_b = np.sign(eff_b)
        flip = sign_a != sign_b
        return {
            "comparison": f"{b}_minus_{a}",
            "mean_shift": float(np.mean(eff_b - eff_a)),
            "median_shift": float(np.median(eff_b - eff_a)),
            "sign_flip_count": int(np.sum(flip)),
            "neg_to_pos": int(np.sum((eff_a < 0) & (eff_b > 0))),
            "pos_to_neg": int(np.sum((eff_a > 0) & (eff_b < 0))),
            "zero_involved": int(np.sum(flip & ((eff_a == 0) | (eff_b == 0)))),
        }

    return pd.DataFrame.from_records(
        [
            summarize_shift("baseline", "baseline_reasoning"),
            summarize_shift("baseline_joint", "baseline_joint_reasoning"),
            summarize_shift("baseline", "baseline_joint"),
            summarize_shift("baseline_reasoning", "baseline_joint_reasoning"),
        ]
    )


def sign_pattern_summary(effect_df: pd.DataFrame, variations: list[str]) -> pd.DataFrame:
    effect_cols = [f"{variation}_effect" for variation in variations]
    rows = [
        {
            "pattern": "all_positive_pred",
            "count": int(effect_df["all_positive_pred"].sum()),
        },
        {
            "pattern": "all_negative_pred",
            "count": int(effect_df["all_negative_pred"].sum()),
        },
        {
            "pattern": "sign_flip_across_variants",
            "count": int(effect_df["sign_flip_across_variants"].sum()),
        },
        {
            "pattern": "true_positive_effect",
            "count": int((effect_df["true_effect_pct"] > 0).sum()),
        },
        {
            "pattern": "true_negative_effect",
            "count": int((effect_df["true_effect_pct"] < 0).sum()),
        },
    ]

    for variation in variations:
        eff = effect_df[f"{variation}_effect"]
        rows.extend(
            [
                {
                    "pattern": f"{variation}_positive_pred",
                    "count": int((eff > 0).sum()),
                },
                {
                    "pattern": f"{variation}_negative_pred",
                    "count": int((eff < 0).sum()),
                },
            ]
        )
    return pd.DataFrame(rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    pred = pd.read_csv(PRED_PATH, index_col=0)
    effect_df = build_effect_frame()
    variations = pred.index.tolist()

    effect_df.to_csv(
        RESULTS_DIR / "prediction_learning_wave_elicitation_41_effects_by_config.csv",
        index=False,
    )
    binary_feature_summary(effect_df, variations).to_csv(
        RESULTS_DIR / "prediction_learning_wave_elicitation_41_feature_binary_summary.csv",
        index=False,
    )
    continuous_feature_correlations(effect_df, variations).to_csv(
        RESULTS_DIR / "prediction_learning_wave_elicitation_41_feature_continuous_correlations.csv",
        index=False,
    )
    shift_summary(effect_df).to_csv(
        RESULTS_DIR / "prediction_learning_wave_elicitation_41_effect_shift_summary.csv",
        index=False,
    )
    sign_pattern_summary(effect_df, variations).to_csv(
        RESULTS_DIR / "prediction_learning_wave_elicitation_41_effect_sign_pattern_summary.csv",
        index=False,
    )

    print("Wrote prediction_learning_wave_elicitation_41_effects_by_config.csv")
    print("Wrote prediction_learning_wave_elicitation_41_feature_binary_summary.csv")
    print("Wrote prediction_learning_wave_elicitation_41_feature_continuous_correlations.csv")
    print("Wrote prediction_learning_wave_elicitation_41_effect_shift_summary.csv")
    print("Wrote prediction_learning_wave_elicitation_41_effect_sign_pattern_summary.csv")


if __name__ == "__main__":
    main()
