from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import chi2


ROOT = Path(__file__).resolve().parents[1]
PAIRED_VAL_CSV = ROOT / "science_data" / "data" / "processed_data" / "df_paired_val.csv"
RAW_VAL_CSV = ROOT / "science_data" / "data" / "processed_data" / "df_analysis_val.csv"


def load_truth_and_sem() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    paired = pd.read_csv(PAIRED_VAL_CSV).sort_values("CONFIG_configId")
    truth = paired["treatment_itt_efficiency"].to_numpy(dtype=float) * 100.0
    control = paired["control_itt_efficiency"].to_numpy(dtype=float) * 100.0
    config_ids = paired["CONFIG_configId"].to_numpy(dtype=int)

    raw = pd.read_csv(RAW_VAL_CSV)
    raw = raw.loc[raw["valid_number_of_starting_players"] == True].copy()
    raw_t = raw.loc[raw["CONFIG_treatmentName"].astype(str).str.endswith("_T")].copy()
    stats = raw_t.groupby("CONFIG_configId")["itt_efficiency"].agg(n="count", std="std").reset_index()
    stats["std"] = stats["std"].fillna(0.0)
    stats["sem_t"] = stats["std"] / np.sqrt(stats["n"])
    sem_map = dict(zip(stats["CONFIG_configId"], stats["sem_t"] * 100.0))
    sem_y = np.array([sem_map[c] for c in config_ids], dtype=float)
    return truth, control, sem_y


def _fit_adjusted_corr_impl(
    x: np.ndarray,
    y: np.ndarray,
    se_y: np.ndarray,
    *,
    init_params: np.ndarray | None = None,
) -> tuple[float, np.ndarray, bool]:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    se_y = np.asarray(se_y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y) & np.isfinite(se_y)
    x = x[mask]
    y = y[mask]
    se_y = se_y[mask]

    if x.size < 3:
        return float("nan"), np.full(5, np.nan), False

    if init_params is None or not np.isfinite(init_params).all():
        mx0, my0 = float(x.mean()), float(y.mean())
        sx0 = max(float(x.std(ddof=1)), 1e-3)
        sy0 = max(float(np.sqrt(max(y.var(ddof=1) - np.mean(se_y**2), 1e-6))), 1e-3)
        r0 = float(np.corrcoef(x, y)[0, 1])
        z0 = float(np.arctanh(np.clip(r0, -0.95, 0.95)))
        init_params = np.array([mx0, my0, np.log(sx0), np.log(sy0), z0], dtype=float)

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

    res = minimize(nll, x0=init_params, method="L-BFGS-B")
    params = res.x if np.isfinite(res.x).all() else init_params
    rho = float(np.tanh(params[-1]))
    return rho, params, bool(res.success)


def fit_adjusted_corr(
    x: np.ndarray,
    y: np.ndarray,
    se_y: np.ndarray,
    *,
    init_params: np.ndarray | None = None,
) -> dict[str, object]:
    rho, params, ok = _fit_adjusted_corr_impl(x, y, se_y, init_params=init_params)
    return {"r_adj": rho, "params": params, "fit_ok": ok}


def profile_likelihood_ci_adjusted_corr(
    x: np.ndarray,
    y: np.ndarray,
    se_y: np.ndarray,
    *,
    level: float = 0.95,
) -> dict[str, object]:
    fit = fit_adjusted_corr(x, y, se_y)
    mle_r = float(fit["r_adj"])
    mle_params = np.asarray(fit["params"], dtype=float)
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    se_y = np.asarray(se_y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y) & np.isfinite(se_y)
    x = x[mask]
    y = y[mask]
    se_y = se_y[mask]

    def nll_fixed_rho(rho: float, init: np.ndarray) -> tuple[float, np.ndarray]:
        rho = float(np.clip(rho, -0.999999, 0.999999))
        zrho = float(np.arctanh(rho))

        def nll_nuisance(params: np.ndarray) -> float:
            mx, my, log_sx, log_sy = params
            sx = float(np.exp(log_sx))
            sy = float(np.exp(log_sy))
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

        init4 = np.array([init[0], init[1], init[2], init[3]], dtype=float)
        res = minimize(nll_nuisance, x0=init4, method="L-BFGS-B")
        out = np.array([res.x[0], res.x[1], res.x[2], res.x[3], zrho], dtype=float)
        return float(res.fun), out

    mle_nll, _ = nll_fixed_rho(mle_r, mle_params)
    cutoff = mle_nll + 0.5 * float(chi2.ppf(level, df=1))

    def search_bound(direction: str) -> float:
        target = -0.999 if direction == "lower" else 0.999
        if (direction == "lower" and mle_r <= -0.995) or (direction == "upper" and mle_r >= 0.995):
            return mle_r
        grid = np.linspace(mle_r, target, 160)
        prev_r = mle_r
        prev_nll = mle_nll
        prev_params = mle_params
        for rho in grid[1:]:
            nll, params = nll_fixed_rho(float(rho), prev_params)
            if np.isfinite(nll) and nll > cutoff:
                if np.isfinite(prev_nll) and nll != prev_nll:
                    frac = (cutoff - prev_nll) / (nll - prev_nll)
                    return float(prev_r + frac * (rho - prev_r))
                return float(rho)
            prev_r = float(rho)
            prev_nll = nll
            prev_params = params
        return float(target)

    return {
        "r_adj": mle_r,
        "ci_low": search_bound("lower"),
        "ci_high": search_bound("upper"),
        "fit_ok": bool(fit["fit_ok"]),
    }


def paired_adjusted_corr_bootstrap(
    baseline: np.ndarray,
    benchmark: np.ndarray,
    truth: np.ndarray,
    sem_y: np.ndarray,
    *,
    n_boot: int = 1000,
    seed: int = 42,
) -> dict[str, object]:
    base_fit = fit_adjusted_corr(baseline, truth, sem_y)
    bench_fit = fit_adjusted_corr(benchmark, truth, sem_y)
    base_r = float(base_fit["r_adj"])
    bench_r = float(bench_fit["r_adj"])
    observed_delta = bench_r - base_r

    idx = np.arange(len(truth))
    rng = np.random.default_rng(seed)
    base_boot = np.empty(n_boot, dtype=float)
    bench_boot = np.empty(n_boot, dtype=float)
    delta_boot = np.empty(n_boot, dtype=float)

    base_params = np.asarray(base_fit["params"], dtype=float)
    bench_params = np.asarray(bench_fit["params"], dtype=float)
    for i in range(n_boot):
        sample = rng.choice(idx, size=idx.size, replace=True)
        base_res = fit_adjusted_corr(baseline[sample], truth[sample], sem_y[sample], init_params=base_params)
        bench_res = fit_adjusted_corr(benchmark[sample], truth[sample], sem_y[sample], init_params=bench_params)
        base_boot[i] = float(base_res["r_adj"])
        bench_boot[i] = float(bench_res["r_adj"])
        delta_boot[i] = bench_boot[i] - base_boot[i]
        base_params = np.asarray(base_res["params"], dtype=float)
        bench_params = np.asarray(bench_res["params"], dtype=float)

    def q(arr: np.ndarray, lo: float, hi: float) -> tuple[float, float]:
        finite = arr[np.isfinite(arr)]
        return float(np.nanpercentile(finite, lo)), float(np.nanpercentile(finite, hi))

    base_ci95 = q(base_boot, 2.5, 97.5)
    bench_ci95 = q(bench_boot, 2.5, 97.5)
    delta_ci95 = q(delta_boot, 2.5, 97.5)
    delta_ci99 = q(delta_boot, 0.5, 99.5)
    delta_ci999 = q(delta_boot, 0.05, 99.95)

    return {
        "baseline_r_adj": base_r,
        "benchmark_r_adj": bench_r,
        "baseline_ci_low": base_ci95[0],
        "baseline_ci_high": base_ci95[1],
        "benchmark_ci_low": bench_ci95[0],
        "benchmark_ci_high": bench_ci95[1],
        "delta_r_adj": observed_delta,
        "delta_ci95_low": delta_ci95[0],
        "delta_ci95_high": delta_ci95[1],
        "delta_ci99_low": delta_ci99[0],
        "delta_ci99_high": delta_ci99[1],
        "delta_ci999_low": delta_ci999[0],
        "delta_ci999_high": delta_ci999[1],
    }


def ci_to_sig_label(ci95_low: float, ci95_high: float, ci99_low: float, ci99_high: float, ci999_low: float, ci999_high: float) -> str:
    if np.isfinite(ci999_low) and np.isfinite(ci999_high) and (ci999_low > 0 or ci999_high < 0):
        return "***"
    if np.isfinite(ci99_low) and np.isfinite(ci99_high) and (ci99_low > 0 or ci99_high < 0):
        return "**"
    if np.isfinite(ci95_low) and np.isfinite(ci95_high) and (ci95_low > 0 or ci95_high < 0):
        return "*"
    return "n.s."


def _corr_matrix_unconstrained(a: float, b: float, c: float) -> np.ndarray:
    r12 = float(np.tanh(a))
    r13 = float(np.tanh(b))
    p23 = float(np.tanh(c))
    r23 = float(r12 * r13 + np.sqrt(max(1e-12, (1 - r12**2) * (1 - r13**2))) * p23)
    return np.array([[1.0, r12, r13], [r12, 1.0, r23], [r13, r23, 1.0]], dtype=float)


def _corr_matrix_equal(r12_z: float, ry_z: float) -> np.ndarray:
    r12 = float(np.tanh(r12_z))
    ry = float(np.tanh(ry_z))
    corr = np.array([[1.0, r12, ry], [r12, 1.0, ry], [ry, ry, 1.0]], dtype=float)
    return corr


def _joint_nll(
    x0: np.ndarray,
    x1: np.ndarray,
    y: np.ndarray,
    se_y: np.ndarray,
    params: np.ndarray,
    *,
    equal_r: bool,
) -> float:
    if equal_r:
        mx0, mx1, my, log_sx0, log_sx1, log_sy, a, b = params
        corr = _corr_matrix_equal(a, b)
    else:
        mx0, mx1, my, log_sx0, log_sx1, log_sy, a, b, c = params
        corr = _corr_matrix_unconstrained(a, b, c)
    if np.linalg.det(corr) <= 0:
        return float("inf")
    sx0 = float(np.exp(log_sx0))
    sx1 = float(np.exp(log_sx1))
    sy = float(np.exp(log_sy))
    D = np.diag([sx0, sx1, sy])
    Sigma = D @ corr @ D
    total = 0.0
    mu = np.array([mx0, mx1, my], dtype=float)
    for xi0, xi1, yi, se in zip(x0, x1, y, se_y):
        V = Sigma.copy()
        V[2, 2] += se * se
        det = np.linalg.det(V)
        if det <= 0:
            return float("inf")
        diff = np.array([xi0, xi1, yi], dtype=float) - mu
        quad = float(diff.T @ np.linalg.inv(V) @ diff)
        total += 0.5 * (np.log(det) + quad + 3 * np.log(2 * np.pi))
    return float(total)


def compare_adjusted_corr_conditions(
    baseline: np.ndarray,
    benchmark: np.ndarray,
    truth: np.ndarray,
    se_y: np.ndarray,
) -> dict[str, float | str]:
    x0 = np.asarray(baseline, dtype=float)
    x1 = np.asarray(benchmark, dtype=float)
    y = np.asarray(truth, dtype=float)
    se_y = np.asarray(se_y, dtype=float)
    mask = np.isfinite(x0) & np.isfinite(x1) & np.isfinite(y) & np.isfinite(se_y)
    x0, x1, y, se_y = x0[mask], x1[mask], y[mask], se_y[mask]

    init_u = np.array(
        [
            float(x0.mean()),
            float(x1.mean()),
            float(y.mean()),
            np.log(max(float(x0.std(ddof=1)), 1e-3)),
            np.log(max(float(x1.std(ddof=1)), 1e-3)),
            np.log(max(float(np.sqrt(max(y.var(ddof=1) - np.mean(se_y**2), 1e-6))), 1e-3)),
            np.arctanh(np.clip(np.corrcoef(x0, x1)[0, 1], -0.95, 0.95)),
            np.arctanh(np.clip(np.corrcoef(x0, y)[0, 1], -0.95, 0.95)),
            0.0,
        ],
        dtype=float,
    )
    res_u = minimize(lambda p: _joint_nll(x0, x1, y, se_y, p, equal_r=False), x0=init_u, method="L-BFGS-B")
    mx0, mx1, my, log_sx0, log_sx1, log_sy, a, b, c = res_u.x
    corr_u = _corr_matrix_unconstrained(a, b, c)
    rho0 = float(corr_u[0, 2])
    rho1 = float(corr_u[1, 2])

    init_c = np.array([mx0, mx1, my, log_sx0, log_sx1, log_sy, a, np.arctanh(np.clip((rho0 + rho1) / 2, -0.95, 0.95))], dtype=float)
    res_c = minimize(lambda p: _joint_nll(x0, x1, y, se_y, p, equal_r=True), x0=init_c, method="L-BFGS-B")

    lr = max(0.0, 2.0 * (float(res_c.fun) - float(res_u.fun)))
    p_value = float(chi2.sf(lr, df=1))
    if p_value < 0.01:
        sig = "**"
    elif p_value < 0.05:
        sig = "*"
    else:
        sig = "n.s."
    return {"baseline_r_adj": rho0, "benchmark_r_adj": rho1, "lr_stat": lr, "p_value": p_value, "sig_label": sig}
