"""Shared constants and utilities for extraction model comparison scripts."""
from __future__ import annotations

import numpy as np

BINARY_FIELDS: frozenset[str] = frozenset({
    "METHOD_empirical", "METHOD_experiment", "METHOD_lab",
    "METHOD_simulation", "METHOD_analytical",
    "CONFIG_allOrNothing", "CONFIG_chat",
    "CONFIG_showOtherSummaries", "CONFIG_showPunishmentId",
    "CONFIG_showRewardId", "CONFIG_showNRounds",
    "CONFIG_punishmentExists", "CONFIG_rewardExists",
    "DV_efficiencyReported",
    "source_data", "experiment_environment",
})
NUMERIC_FIELDS: frozenset[str] = frozenset({
    "CONFIG_playerCount", "CONFIG_numRounds",
    "CONFIG_defaultContribProp", "CONFIG_MPCR",
    "CONFIG_punishmentCost", "CONFIG_punishmentTech",
    "CONFIG_rewardCost", "CONFIG_rewardTech",
    "CONFIG_endowment",
    "number_IVs", "number_DVs",
})
TEXT_FIELDS: frozenset[str] = frozenset({
    "data_id", "indep_var", "IVs", "DVs", "DVs_Definitions",
    "participant_country", "participant_age",
    "participant_gender", "participant_education",
    "other_game_info",
})
ALL_FIELDS: list[str] = sorted(BINARY_FIELDS | NUMERIC_FIELDS | TEXT_FIELDS)

MISSING_TOKENS: frozenset[str] = frozenset({
    "", "nan", "none", "n/a", "n/r", "na", "null", "missing",
})


def cosine(u: np.ndarray, v: np.ndarray) -> float:
    nu = np.linalg.norm(u)
    nv = np.linalg.norm(v)
    if nu == 0.0 or nv == 0.0:
        return 0.0
    return float(np.dot(u, v) / (nu * nv))
