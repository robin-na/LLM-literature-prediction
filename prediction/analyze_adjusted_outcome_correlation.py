from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize


ROOT = Path(__file__).resolve().parents[1]
PAIRED_VAL_CSV = ROOT / "science_data" / "data" / "processed_data" / "df_paired_val.csv"
RAW_VAL_CSV = ROOT / "science_data" / "data" / "processed_data" / "df_analysis_val.csv"
BASELINE_AVG_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5"
    / "validation_literature_collection_analysis_report_repeat5_baseline_avg_predictions.csv"
)
AUG_AVG_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5"
    / "validation_literature_collection_analysis_report_repeat5_avg_predictions.csv"
)
RESULTS_DIR = ROOT / "results" / "paper" / "robustness"

MODELS = ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
Q_COLS = [f"Q{i}" for i in range(1, 21)]
BENCHMARK_VARIANT_ID = "benchmark_pgg_ms"


def load_truth_and_sem() -> tuple[np.ndarray, np.ndarray]:
    paired = pd.read_csv(PAIRED_VAL_CSV).sort_values("CONFIG_configId")
    truth = paired["treatment_itt_efficiency"].to_numpy(dtype=float) * 100.0
    config_ids = paired["CONFIG_configId"].to_numpy(dtype=int)

    raw = pd.read_csv(RAW_VAL_CSV)
    raw = raw.loc[raw["valid_number_of_starting_players"] == True].copy()
    raw_t = raw.loc[raw["CONFIG_treatmentName"].astype(str).str.endswith("_T")].copy()
    stats = raw_t.groupby("CONFIG_configId")["itt_efficiency"].agg(n="count", std="std").reset_index()
    stats["std"] = stats["std"].fillna(0.0)
    stats["sem_t"] = stats["std"] / np.sqrt(stats["n"])
    sem_map = dict(zip(stats["CONFIG_configId"], stats["sem_t"] * 100.0))
    sem_y = np.array([sem_map[c] for c in config_ids], dtype=float)
    return truth, sem_y


def fit_latent_corr(x: np.ndarray, y: np.ndarray, se_y: np.ndarray) -> dict[str, float | bool]:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    se_y = np.asarray(se_y, dtype=float)

    mx0, my0 = float(x.mean()), float(y.mean())
    sx0 = max(float(x.std(ddof=1)), 1e-3)
    sy0 = max(float(np.sqrt(max(y.var(ddof=1) - np.mean(se_y**2), 1e-6))), 1e-3)
    r0 = float(np.corrcoef(x, y)[0, 1])
    z0 = float(np.arctanh(np.clip(r0, -0.95, 0.95)))

    def nll(params: np.ndarray) -> float:
        mx, my, log_sx, log_sy, zrho = params
        sx = float(np.exp(log_sx))
        sy = float(np.exp(log_sy))
        rho = float(np.tanh(zrho))
        cov = rho * sx * sy
        total = 0.0
        for xi, yi, se in zip(x, y, se_y):
            s11 = sx * sx
            s22 = sy * sy + se * se
            s12 = cov
            det = s11 * s22 - s12 * s12
            if det <= 0:
                return float("inf")
            dx = xi - mx
            dy = yi - my
            quad = (s22 * dx * dx - 2 * s12 * dx * dy + s11 * dy * dy) / det
            total += 0.5 * (np.log(det) + quad + 2 * np.log(2 * np.pi))
        return float(total)

    res = minimize(
        nll,
        x0=np.array([mx0, my0, np.log(sx0), np.log(sy0), z0]),
        method="L-BFGS-B",
    )
    rho = float(np.tanh(res.x[-1]))
    return {
        "raw_r": r0,
        "r_adj": rho,
        "fit_ok": bool(res.success),
        "nll": float(res.fun),
    }


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    truth, sem_y = load_truth_and_sem()

    baseline_df = pd.read_csv(BASELINE_AVG_CSV)
    aug_df = pd.read_csv(AUG_AVG_CSV)
    benchmark_df = aug_df.loc[aug_df["variant_id"] == BENCHMARK_VARIANT_ID].copy()

    rows = []
    for model in MODELS:
        for condition, df in [
            ("No augmentation", baseline_df),
            ("Benchmark paper augmented", benchmark_df),
        ]:
            part = df.loc[df["model"] == model].iloc[0]
            preds = part[Q_COLS].to_numpy(dtype=float)
            metrics = fit_latent_corr(preds, truth, sem_y)
            rows.append(
                {
                    "model": model,
                    "condition": condition,
                    **metrics,
                }
            )

    out = pd.DataFrame(rows)
    out.to_csv(RESULTS_DIR / "adjusted_outcome_correlation_baseline_benchmark.csv", index=False)


if __name__ == "__main__":
    main()
