from __future__ import annotations

import sys
from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr


ANALYSIS_ROOT = Path(__file__).resolve().parent
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from jsonl_parser import jsonl_to_dataframe  # noqa: E402
from literature_analysis_report_sources.analyze_validation_analysis_report_sources_repeat3 import (  # noqa: E402
    Q_COLS as SOURCE_Q_COLS,
)
from literature_analysis_report_sources.analyze_validation_analysis_report_sources_repeat3 import (  # noqa: E402
    RUN_SPECS,
    _available_row,
    _extract_source_ids,
    _load_aug_tables,
)
from literature_collection_analysis_reports.analyze_validation_collection_analysis_reports_metadata_filters import (  # noqa: E402
    MODEL_BACKFILL_SPECS,
    MODEL_SPECS,
    Q_COLS as COLLECTION_Q_COLS,
    _resolve_row_ids,
    load_metadata_filter_index,
)


ROOT = ANALYSIS_ROOT.parent
VAL_CSV = ROOT / "science_data" / "data" / "processed_data" / "df_paired_val.csv"
RESULTS_DIR = ROOT / "results" / "paper" / "robustness"
PLOTS_DIR = ROOT / "plots" / "paper" / "exploratory"

MODELS = ["GPT-5 Mini", "GPT-5 Nano", "GPT-4.1", "GPT-4.1 Mini", "GPT-5.1"]
Q_COLS = [f"Q{i}" for i in range(1, 21)]


def load_truth() -> np.ndarray:
    return (
        pd.read_csv(VAL_CSV)
        .sort_values("CONFIG_configId")["treatment_itt_efficiency"]
        .to_numpy(dtype=np.float32)
        * 100.0
    )


def rowwise_corr(preds: np.ndarray, truth: np.ndarray) -> np.ndarray:
    pred_center = preds - preds.mean(axis=1, keepdims=True)
    truth_center = truth - truth.mean()
    numer = np.sum(pred_center * truth_center[None, :], axis=1)
    denom = np.sqrt(np.sum(pred_center**2, axis=1) * np.sum(truth_center**2))
    return np.divide(
        numer,
        denom,
        out=np.full(preds.shape[0], np.nan, dtype=np.float32),
        where=denom > 0,
    )


def safe_spearman(a: np.ndarray, b: np.ndarray) -> float:
    mask = np.isfinite(a) & np.isfinite(b)
    if mask.sum() < 3:
        return float("nan")
    return float(spearmanr(a[mask], b[mask]).statistic)


def spearman_brown(r: float, k: int) -> float:
    if np.isnan(r):
        return np.nan
    denom = 1.0 + (k - 1.0) * r
    if denom <= 0:
        return np.nan
    value = (k * r) / denom
    return float(np.clip(value, -1.0, 1.0))


def draw_heatmap(ax: plt.Axes, matrix: pd.DataFrame, title: str, ylabel: str = "") -> None:
    sns.heatmap(
        matrix,
        ax=ax,
        cmap="YlGnBu",
        vmin=0,
        vmax=1,
        annot=True,
        fmt=".2f",
        cbar=False,
        square=True,
        linewidths=0.6,
        linecolor="white",
        annot_kws={"fontsize": 9},
    )
    ax.set_title(title, fontsize=12, pad=8)
    ax.set_xlabel("")
    ax.set_ylabel(ylabel, fontsize=12 if ylabel else 10)
    ax.tick_params(axis="x", rotation=45, labelsize=9)
    ax.tick_params(axis="y", rotation=0, labelsize=9)


def build_matrix(df: pd.DataFrame, value_col: str) -> pd.DataFrame:
    matrix = pd.DataFrame(np.eye(len(MODELS)), index=MODELS, columns=MODELS)
    for row in df.itertuples(index=False):
        val = getattr(row, value_col)
        matrix.loc[row.model_a, row.model_b] = val
        matrix.loc[row.model_b, row.model_a] = val
    return matrix


def plot(pairwise_df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(10.5, 8))
    specs = [
        ("papers", "observed_spearman", "Observed exact-rank\n(Spearman ρ)", "Individual papers"),
        ("papers", "repeat_rank_ceiling_avg5", "Repeat-based rank\nceiling (avg-5)", ""),
        ("collections", "observed_spearman", "Observed exact-rank\n(Spearman ρ)", "Collections"),
        ("collections", "repeat_rank_ceiling_avg5", "Repeat-based rank\nceiling (avg-5)", ""),
    ]
    for ax, (kind, value_col, title, ylabel) in zip(axes.flatten(), specs):
        sub = pairwise_df.loc[pairwise_df["kind"] == kind]
        draw_heatmap(ax, build_matrix(sub, value_col), title, ylabel)
    fig.text(
        0.5,
        0.02,
        "Repeat ceiling uses within-model repeat-to-repeat ranking agreement, projected to the 5-repeat aggregate via a Spearman-Brown correction.",
        ha="center",
        fontsize=10,
    )
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig(PLOTS_DIR / "cross_model_repeat_rank_ceiling.png", dpi=300, bbox_inches="tight")
    fig.savefig(PLOTS_DIR / "cross_model_repeat_rank_ceiling.pdf", dpi=300, bbox_inches="tight")
    plt.close(fig)


def load_paper_repeat_predictions() -> dict[str, dict[str, pd.DataFrame]]:
    out: dict[str, dict[str, pd.DataFrame]] = {}
    spec_by_model = {str(spec["model"]): spec for spec in RUN_SPECS}
    for model in MODELS:
        spec = spec_by_model[model]
        initial_df, repeat23_df, repeat45_df = _load_aug_tables(spec)
        source_ids = _extract_source_ids(initial_df, [repeat23_df, repeat45_df])
        repeat_map: dict[str, pd.DataFrame] = {}
        run_specs = [
            ("rep1", initial_df, "paper_analysis_report_joint/{source_id}"),
            ("rep2", repeat23_df, "paper_analysis_report_joint_rep2/{source_id}"),
            ("rep3", repeat23_df, "paper_analysis_report_joint_rep3/{source_id}"),
            ("rep4", repeat45_df, "paper_analysis_report_joint_rep4/{source_id}"),
            ("rep5", repeat45_df, "paper_analysis_report_joint_rep5/{source_id}"),
        ]
        for run_label, df, template in run_specs:
            rows = []
            for source_id in source_ids:
                row_id = template.format(source_id=source_id)
                series = _available_row(df, row_id)
                if series is None:
                    continue
                row = {"item_id": source_id}
                row.update({q: float(series[q]) for q in SOURCE_Q_COLS})
                rows.append(row)
            repeat_map[run_label] = pd.DataFrame(rows).set_index("item_id").sort_index()
        out[model] = repeat_map
    return out


def load_collection_repeat_predictions() -> dict[str, dict[str, pd.DataFrame]]:
    out: dict[str, dict[str, pd.DataFrame]] = {}
    index_df = load_metadata_filter_index()
    variant_ids = sorted(index_df["variant_id"].astype(str).tolist())

    for model in MODELS:
        source_df = jsonl_to_dataframe(MODEL_SPECS[model]).reindex(columns=COLLECTION_Q_COLS)
        backfill_path = MODEL_BACKFILL_SPECS.get(model)
        if backfill_path and Path(backfill_path).exists():
            backfill_df = jsonl_to_dataframe(backfill_path).reindex(columns=COLLECTION_Q_COLS)
            if not backfill_df.empty:
                mask = backfill_df.index.to_series().astype(str).str.startswith("collection_analysis_report_joint_rep")
                if mask.any():
                    source_df = pd.concat([source_df, backfill_df.loc[mask]], axis=0)
                    source_df = source_df[~source_df.index.duplicated(keep="last")]
        repeat_map: dict[str, pd.DataFrame] = {}
        for rep in range(1, 6):
            rows = []
            for variant_id in variant_ids:
                requested_ids = [f"collection_analysis_report_joint_rep{rep}/{variant_id}"]
                resolved = _resolve_row_ids(source_df, requested_ids)
                if resolved is None:
                    continue
                series = pd.to_numeric(source_df.loc[resolved[0]], errors="coerce").reindex(COLLECTION_Q_COLS)
                row = {"item_id": variant_id}
                row.update({q: float(series[q]) for q in COLLECTION_Q_COLS})
                rows.append(row)
            repeat_map[f"rep{rep}"] = pd.DataFrame(rows).set_index("item_id").sort_index()
        out[model] = repeat_map
    return out


def common_ids(repeat_predictions: dict[str, dict[str, pd.DataFrame]]) -> pd.Index:
    shared: set[str] | None = None
    for model in MODELS:
        model_ids = set.intersection(*(set(df.index.tolist()) for df in repeat_predictions[model].values()))
        shared = model_ids if shared is None else (shared & model_ids)
    assert shared is not None
    return pd.Index(sorted(shared))


def compute_repeat_scores(
    repeat_predictions: dict[str, dict[str, pd.DataFrame]],
    truth: np.ndarray,
    ids: pd.Index,
) -> dict[str, dict[str, np.ndarray]]:
    out: dict[str, dict[str, np.ndarray]] = {}
    for model in MODELS:
        repeat_scores: dict[str, np.ndarray] = {}
        for rep, df in repeat_predictions[model].items():
            preds = df.reindex(ids)[Q_COLS].to_numpy(dtype=np.float32)
            repeat_scores[rep] = rowwise_corr(preds, truth)
        out[model] = repeat_scores
    return out


def compute_observed_scores(
    repeat_predictions: dict[str, dict[str, pd.DataFrame]],
    truth: np.ndarray,
    ids: pd.Index,
) -> dict[str, np.ndarray]:
    out: dict[str, np.ndarray] = {}
    for model in MODELS:
        mats = [repeat_predictions[model][f"rep{i}"].reindex(ids)[Q_COLS].to_numpy(dtype=np.float32) for i in range(1, 6)]
        avg_preds = np.mean(np.stack(mats, axis=0), axis=0)
        out[model] = rowwise_corr(avg_preds, truth)
    return out


def compute_repeat_reliability(repeat_scores: dict[str, dict[str, np.ndarray]]) -> pd.DataFrame:
    rows = []
    for model in MODELS:
        rhos = []
        reps = repeat_scores[model]
        for rep_a, rep_b in combinations(sorted(reps.keys()), 2):
            rhos.append(safe_spearman(reps[rep_a], reps[rep_b]))
        single = float(np.mean(rhos))
        rows.append(
            {
                "model": model,
                "rank_reliability_single_repeat": single,
                "rank_reliability_single_repeat_sd": float(np.std(rhos, ddof=1)),
                "rank_reliability_avg5": spearman_brown(single, 5),
            }
        )
    return pd.DataFrame(rows)


def analyze_kind(kind: str, repeat_predictions: dict[str, dict[str, pd.DataFrame]], truth: np.ndarray) -> tuple[pd.DataFrame, pd.DataFrame]:
    ids = common_ids(repeat_predictions)
    repeat_scores = compute_repeat_scores(repeat_predictions, truth, ids)
    observed_scores = compute_observed_scores(repeat_predictions, truth, ids)
    reliability_df = compute_repeat_reliability(repeat_scores)
    reliability_df.insert(0, "kind", kind)
    reliability_df.insert(2, "n_items", len(ids))

    rel_lookup = reliability_df.set_index("model")["rank_reliability_avg5"].to_dict()
    pairwise_rows = []
    for model_a, model_b in combinations(MODELS, 2):
        obs = safe_spearman(observed_scores[model_a], observed_scores[model_b])
        ceiling = float(np.sqrt(rel_lookup[model_a] * rel_lookup[model_b]))
        pairwise_rows.append(
            {
                "kind": kind,
                "model_a": model_a,
                "model_b": model_b,
                "n_items": len(ids),
                "observed_spearman": obs,
                "repeat_rank_ceiling_avg5": ceiling,
                "ceiling_fraction": float(obs / ceiling) if ceiling > 0 else np.nan,
            }
        )
    return reliability_df, pd.DataFrame(pairwise_rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    truth = load_truth()

    paper_reliability, paper_pairwise = analyze_kind("papers", load_paper_repeat_predictions(), truth)
    collection_reliability, collection_pairwise = analyze_kind("collections", load_collection_repeat_predictions(), truth)

    reliability_df = pd.concat([paper_reliability, collection_reliability], ignore_index=True)
    pairwise_df = pd.concat([paper_pairwise, collection_pairwise], ignore_index=True)
    summary_df = (
        pairwise_df.groupby("kind", as_index=False)[["observed_spearman", "repeat_rank_ceiling_avg5", "ceiling_fraction"]]
        .mean()
    )

    reliability_df.to_csv(RESULTS_DIR / "cross_model_repeat_rank_ceiling_reliability.csv", index=False)
    pairwise_df.to_csv(RESULTS_DIR / "cross_model_repeat_rank_ceiling_pairwise.csv", index=False)
    summary_df.to_csv(RESULTS_DIR / "cross_model_repeat_rank_ceiling_summary.csv", index=False)
    plot(pairwise_df)


if __name__ == "__main__":
    sns.set_theme(style="white", context="talk")
    main()
