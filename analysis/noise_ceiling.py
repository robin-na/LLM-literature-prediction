import argparse
import math

import numpy as np
import pandas as pd
from scipy.stats import norm


def load_pairs(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df[df["valid_number_of_starting_players"] == True].copy()
    df = df[["CONFIG_treatmentName", "itt_efficiency"]].dropna()
    parsed = df["CONFIG_treatmentName"].astype(str).str.extract(r"^(.*)_(C|T)$")
    df["base"] = parsed[0]
    df["arm"] = parsed[1]
    df = df.dropna(subset=["base", "arm"])

    stats = (
        df.groupby(["base", "arm"])["itt_efficiency"]
        .agg(n="count", mean="mean", std="std")
        .reset_index()
    )

    pivot = stats.pivot(index="base", columns="arm")
    pivot.columns = [f"{a}_{b}" for a, b in pivot.columns]
    pivot = pivot.reset_index()
    pivot = pivot.dropna(subset=["n_C", "n_T", "mean_C", "mean_T"])

    pivot["std_C"] = pivot["std_C"].fillna(0.0)
    pivot["std_T"] = pivot["std_T"].fillna(0.0)
    pivot["sem_C"] = pivot["std_C"] / np.sqrt(pivot["n_C"])
    pivot["sem_T"] = pivot["std_T"] / np.sqrt(pivot["n_T"])

    return pivot


def compute_metrics(pairs: pd.DataFrame) -> dict:
    x = pairs["mean_C"].to_numpy(float)
    y = pairs["mean_T"].to_numpy(float)
    sem_x = pairs["sem_C"].to_numpy(float)
    sem_y = pairs["sem_T"].to_numpy(float)

    g = len(pairs)
    rmse_min_y = math.sqrt(float(np.mean(sem_y**2))) if g else float("nan")
    rmse_min_delta = (
        math.sqrt(float(np.mean(sem_y**2 + sem_x**2))) if g else float("nan")
    )

    var_y = float(np.var(y, ddof=1)) if g > 1 else 0.0
    var_x = float(np.var(x, ddof=1)) if g > 1 else 0.0
    noise_y = float(np.mean(sem_y**2)) if g else 0.0
    noise_x = float(np.mean(sem_x**2)) if g else 0.0

    var_true_y = max(0.0, var_y - noise_y)
    var_true_x = max(0.0, var_x - noise_x)
    rel_y = 0.0 if var_y == 0 else var_true_y / var_y
    rel_x = 0.0 if var_x == 0 else var_true_x / var_x
    r_max = math.sqrt(rel_x * rel_y)

    delta_hat = y - x
    sem_delta = np.sqrt(sem_y**2 + sem_x**2)
    p = np.where(
        sem_delta == 0,
        np.where(delta_hat == 0, 0.5, 1.0),
        norm.cdf(np.abs(delta_hat) / sem_delta),
    )
    dir_ceiling = float(np.mean(p)) if g else float("nan")

    r_obs = float(np.corrcoef(x, y)[0, 1]) if g > 1 else float("nan")
    rmse_identity = math.sqrt(float(np.mean((y - x) ** 2))) if g else float("nan")

    return {
        "G": g,
        "rmse_min_y": rmse_min_y,
        "rmse_min_delta": rmse_min_delta,
        "rel_x": rel_x,
        "rel_y": rel_y,
        "r_max": r_max,
        "dir_ceiling": dir_ceiling,
        "r_obs": r_obs,
        "rmse_identity": rmse_identity,
    }


def bootstrap_cis(pairs: pd.DataFrame, b: int, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    g = len(pairs)

    x_all = pairs["mean_C"].to_numpy(float)
    y_all = pairs["mean_T"].to_numpy(float)
    sem_x_all = pairs["sem_C"].to_numpy(float)
    sem_y_all = pairs["sem_T"].to_numpy(float)

    def stats_for_idx(idx: np.ndarray) -> np.ndarray:
        x = x_all[idx]
        y = y_all[idx]
        sem_x = sem_x_all[idx]
        sem_y = sem_y_all[idx]

        rmse_min_y = math.sqrt(float(np.mean(sem_y**2)))
        rmse_min_delta = math.sqrt(float(np.mean(sem_y**2 + sem_x**2)))

        var_y = float(np.var(y, ddof=1)) if len(y) > 1 else 0.0
        var_x = float(np.var(x, ddof=1)) if len(x) > 1 else 0.0
        noise_y = float(np.mean(sem_y**2))
        noise_x = float(np.mean(sem_x**2))
        var_true_y = max(0.0, var_y - noise_y)
        var_true_x = max(0.0, var_x - noise_x)
        rel_y = 0.0 if var_y == 0 else var_true_y / var_y
        rel_x = 0.0 if var_x == 0 else var_true_x / var_x
        r_max = math.sqrt(rel_x * rel_y)

        delta_hat = y - x
        sem_delta = np.sqrt(sem_y**2 + sem_x**2)
        p = np.where(
            sem_delta == 0,
            np.where(delta_hat == 0, 0.5, 1.0),
            norm.cdf(np.abs(delta_hat) / sem_delta),
        )
        dir_ceiling = float(np.mean(p))

        return np.array(
            [rmse_min_y, rmse_min_delta, rel_x, rel_y, r_max, dir_ceiling], dtype=float
        )

    if g == 0:
        return {}

    boots = np.empty((b, 6), dtype=float)
    for i in range(b):
        idx = rng.integers(0, g, size=g)
        boots[i] = stats_for_idx(idx)

    lo = np.quantile(boots, 0.025, axis=0)
    hi = np.quantile(boots, 0.975, axis=0)

    labels = ["rmse_min_y", "rmse_min_delta", "rel_x", "rel_y", "r_max", "dir_ceiling"]
    return {labels[i]: (lo[i], hi[i]) for i in range(len(labels))}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        default="science-data_and_code/data/processed_data/df_analysis_val.csv",
    )
    parser.add_argument("--bootstrap", type=int, default=0)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    pairs = load_pairs(args.path)
    metrics = compute_metrics(pairs)

    print(f"N bases (paired configs): {metrics['G']}")
    print(f"RMSE noise-floor (predicting mean_T): {metrics['rmse_min_y']}")
    print(f"RMSE noise-floor (predicting delta=T-C): {metrics['rmse_min_delta']}")
    print(f"Reliability control mean: {metrics['rel_x']}")
    print(f"Reliability treatment mean: {metrics['rel_y']}")
    print(f"Correlation ceiling for mapping C->T: {metrics['r_max']}")
    print(f"Directional accuracy ceiling (mean over bases): {metrics['dir_ceiling']}")
    print(f"Observed corr(mean_C, mean_T): {metrics['r_obs']}")
    print(f"RMSE of identity yhat=x: {metrics['rmse_identity']}")

    if args.bootstrap > 0:
        cis = bootstrap_cis(pairs, args.bootstrap, args.seed)
        for k, (lo, hi) in cis.items():
            print(f"{k} 95% CI: {lo} .. {hi}")


if __name__ == "__main__":
    main()
