from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_repeat5_human_reference"
HUMAN_PREDICTIONS_CSV = ROOT / "science-data_and_code" / "data" / "processed_data" / "prediction_survey.csv"
MODEL_PAIR_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5_model_sampling"
    / "validation_literature_collection_analysis_report_repeat5_model_sampling_prediction_corr_pairs.csv"
)

SOURCE_ORDER = ["sspp", "prolific"]
SOURCE_LABELS = {
    "sspp": "Experts",
    "prolific": "Laypeople",
}
GROUP_SIZE = 5
N_BOOTSTRAP = 2_000


def load_complete_human_predictions() -> pd.DataFrame:
    df = pd.read_csv(HUMAN_PREDICTIONS_CSV)
    return df.query("prediction.between(-0.2, 1.2) and n_predictions_made == 20").copy()


def build_wide_predictions(df: pd.DataFrame, source: str) -> pd.DataFrame:
    wide = (
        df.loc[df["source"] == source, ["CONFIG_configId", "playerID", "prediction"]]
        .pivot_table(index="CONFIG_configId", columns="playerID", values="prediction", aggfunc="mean")
        .sort_index()
    )
    return wide.loc[:, wide.notna().all(axis=0)]


def pairwise_corr_within(wide: pd.DataFrame) -> np.ndarray:
    values = wide.to_numpy(dtype=float).T * 100.0
    corr_mat = np.corrcoef(values)
    upper = np.triu_indices_from(corr_mat, k=1)
    return corr_mat[upper]


def pairwise_corr_between(left: pd.DataFrame, right: pd.DataFrame) -> np.ndarray:
    left_values = left.to_numpy(dtype=float).T * 100.0
    right_values = right.to_numpy(dtype=float).T * 100.0
    rows: list[float] = []
    for left_vec in left_values:
        joined = np.vstack([left_vec, right_values])
        corrs = np.corrcoef(joined)[0, 1:]
        rows.extend(corrs.tolist())
    return np.asarray(rows, dtype=float)


def sample_group_corrs_same_source(
    wide: pd.DataFrame,
    *,
    group_size: int,
    n_bootstrap: int,
    rng: np.random.Generator,
) -> np.ndarray:
    players = wide.columns.to_numpy()
    values = wide.to_numpy(dtype=float) * 100.0
    player_index = {player: idx for idx, player in enumerate(players)}
    corrs: list[float] = []
    for _ in range(n_bootstrap):
        perm = rng.permutation(players)
        left_ids = perm[:group_size]
        right_ids = perm[group_size : 2 * group_size]
        left = values[:, [player_index[player] for player in left_ids]].mean(axis=1)
        right = values[:, [player_index[player] for player in right_ids]].mean(axis=1)
        corrs.append(float(np.corrcoef(left, right)[0, 1]))
    return np.asarray(corrs, dtype=float)


def sample_group_corrs_between_sources(
    left: pd.DataFrame,
    right: pd.DataFrame,
    *,
    group_size: int,
    n_bootstrap: int,
    rng: np.random.Generator,
) -> np.ndarray:
    left_players = left.columns.to_numpy()
    right_players = right.columns.to_numpy()
    left_values = left.to_numpy(dtype=float) * 100.0
    right_values = right.to_numpy(dtype=float) * 100.0
    left_index = {player: idx for idx, player in enumerate(left_players)}
    right_index = {player: idx for idx, player in enumerate(right_players)}
    corrs: list[float] = []
    for _ in range(n_bootstrap):
        left_ids = rng.choice(left_players, size=group_size, replace=False)
        right_ids = rng.choice(right_players, size=group_size, replace=False)
        left_mean = left_values[:, [left_index[player] for player in left_ids]].mean(axis=1)
        right_mean = right_values[:, [right_index[player] for player in right_ids]].mean(axis=1)
        corrs.append(float(np.corrcoef(left_mean, right_mean)[0, 1]))
    return np.asarray(corrs, dtype=float)


def summarize_values(values: np.ndarray) -> dict[str, float]:
    series = pd.Series(values, dtype=float)
    return {
        "n_pairs": int(series.size),
        "mean": float(series.mean()),
        "median": float(series.median()),
        "std": float(series.std(ddof=0)),
        "q10": float(series.quantile(0.10)),
        "q90": float(series.quantile(0.90)),
        "min": float(series.min()),
        "max": float(series.max()),
    }


def build_human_rows(complete_predictions: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    rng = np.random.default_rng(0)
    wide_by_source = {source: build_wide_predictions(complete_predictions, source) for source in SOURCE_ORDER}

    participant_rows = []
    for source, wide in wide_by_source.items():
        participant_rows.append(
            {
                "source": source,
                "source_label": SOURCE_LABELS[source],
                "n_complete_participants": int(wide.shape[1]),
                "n_questions": int(wide.shape[0]),
            }
        )
    participants = pd.DataFrame(participant_rows)

    human_rows: list[dict[str, object]] = []

    for source in SOURCE_ORDER:
        values = pairwise_corr_within(wide_by_source[source])
        label = SOURCE_LABELS[source]
        for value in values:
            human_rows.append(
                {
                    "family": "human",
                    "comparison_type": "individual",
                    "category": f"Humans: {label.lower()} vs {label.lower()}",
                    "value": float(value),
                }
            )

    between_values = pairwise_corr_between(wide_by_source["sspp"], wide_by_source["prolific"])
    for value in between_values:
        human_rows.append(
            {
                "family": "human",
                "comparison_type": "individual",
                "category": "Humans: experts vs laypeople",
                "value": float(value),
            }
        )

    for source in SOURCE_ORDER:
        values = sample_group_corrs_same_source(
            wide_by_source[source],
            group_size=GROUP_SIZE,
            n_bootstrap=N_BOOTSTRAP,
            rng=rng,
        )
        label = SOURCE_LABELS[source]
        for value in values:
            human_rows.append(
                {
                    "family": "human",
                    "comparison_type": "subcrowd_5",
                    "category": f"Human subcrowds (5): {label.lower()} vs {label.lower()}",
                    "value": float(value),
                }
            )

    between_group_values = sample_group_corrs_between_sources(
        wide_by_source["sspp"],
        wide_by_source["prolific"],
        group_size=GROUP_SIZE,
        n_bootstrap=N_BOOTSTRAP,
        rng=rng,
    )
    for value in between_group_values:
        human_rows.append(
            {
                "family": "human",
                "comparison_type": "subcrowd_5",
                "category": "Human subcrowds (5): experts vs laypeople",
                "value": float(value),
            }
        )

    expert_crowd = wide_by_source["sspp"].mean(axis=1).to_numpy(dtype=float) * 100.0
    lay_crowd = wide_by_source["prolific"].mean(axis=1).to_numpy(dtype=float) * 100.0
    full_crowd_summary = pd.DataFrame(
        [
            {
                "category": "Human full crowds: experts vs laypeople",
                "value": float(np.corrcoef(expert_crowd, lay_crowd)[0, 1]),
                "n_experts": int(wide_by_source["sspp"].shape[1]),
                "n_laypeople": int(wide_by_source["prolific"].shape[1]),
            }
        ]
    )

    rows = pd.DataFrame(human_rows)
    return rows, participants, full_crowd_summary


def build_model_rows() -> pd.DataFrame:
    model_pairs = pd.read_csv(MODEL_PAIR_CSV)
    category = np.select(
        [
            (model_pairs["condition"] == "baseline") & (model_pairs["pair_type"] == "within_model"),
            (model_pairs["condition"] == "baseline") & (model_pairs["pair_type"] == "between_model"),
            (model_pairs["condition"] == "benchmark") & (model_pairs["pair_type"] == "within_model"),
            (model_pairs["condition"] == "benchmark") & (model_pairs["pair_type"] == "between_model"),
        ],
        [
            "LLM baseline: same model, different repeat",
            "LLM baseline: different model",
            "LLM benchmark: same model, different repeat",
            "LLM benchmark: different model",
        ],
        default="Other",
    )
    return pd.DataFrame(
        {
            "family": "llm",
            "comparison_type": model_pairs["pair_type"],
            "category": category,
            "value": model_pairs["prediction_corr"].astype(float),
        }
    )


def build_summary(rows: pd.DataFrame) -> pd.DataFrame:
    summary_rows: list[dict[str, object]] = []
    for (family, comparison_type, category), part in rows.groupby(["family", "comparison_type", "category"], observed=True):
        summary_rows.append(
            {
                "family": family,
                "comparison_type": comparison_type,
                "category": category,
                **summarize_values(part["value"].to_numpy(dtype=float)),
            }
        )
    return pd.DataFrame(summary_rows).sort_values(["family", "comparison_type", "mean"], ascending=[True, True, False]).reset_index(drop=True)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    complete_predictions = load_complete_human_predictions()
    human_rows, participants, full_crowd_summary = build_human_rows(complete_predictions)
    model_rows = build_model_rows()
    comparison_rows = pd.concat([model_rows, human_rows], ignore_index=True)
    comparison_summary = build_summary(comparison_rows)

    participants.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_reference_participants.csv",
        index=False,
    )
    human_rows.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_reference_human_rows.csv",
        index=False,
    )
    comparison_rows.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_reference_comparison_rows.csv",
        index=False,
    )
    comparison_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_reference_comparison_summary.csv",
        index=False,
    )
    full_crowd_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_reference_full_crowd_summary.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
