from __future__ import annotations

BASE_FIELDS = [
    "data_id",
    "indep_var",
    "METHOD_empirical",
    "METHOD_experiment",
    "METHOD_lab",
    "METHOD_simulation",
    "METHOD_analytical",
    "CONFIG_playerCount",
    "CONFIG_numRounds",
    "CONFIG_allOrNothing",
    "CONFIG_defaultContribProp",
    "CONFIG_MPCR",
    "CONFIG_chat",
    "CONFIG_showOtherSummaries",
    "CONFIG_showPunishmentId",
    "CONFIG_showRewardId",
    "CONFIG_showNRounds",
    "CONFIG_punishmentExists",
    "CONFIG_punishmentCost",
    "CONFIG_punishmentTech",
    "CONFIG_rewardExists",
    "CONFIG_rewardCost",
    "CONFIG_rewardTech",
    "CONFIG_endowment",
    # "DV_contributionRate",   # removed: prof only wants which DVs are reported, not values
    # "DV_contributionAmount", # removed: same reason
    # "DV_efficiency",         # removed: replaced by DV_efficiencyReported (0/1 flag)
    # "DV_groupPayoff",        # removed: same reason
    "DVs",
    "DVs_Definitions",
    "DV_efficiencyReported",
    "participant_country",
    "participant_age",
    "participant_gender",
    "participant_education",
    "experiment_environment",
    "other_game_info",
]

FIELDNAMES = ["custom_id"]
for field in BASE_FIELDS:
    FIELDNAMES.append(field)
    FIELDNAMES.append(f"{field}_reason")
    FIELDNAMES.append(f"{field}_confidence")


def coerce_row(custom_id: str, experiment: dict) -> dict:
    import json as _json
    row = {"custom_id": custom_id}
    for field in BASE_FIELDS:
        value = experiment.get(field, "N/R")
        if field == "DVs" and isinstance(value, list):
            value = _json.dumps(value, ensure_ascii=False)
        if field == "DVs_Definitions" and isinstance(value, dict):
            value = _json.dumps(value, ensure_ascii=False)
        row[field] = value
        row[f"{field}_reason"] = experiment.get(f"{field}_reason", "")
        row[f"{field}_confidence"] = experiment.get(f"{field}_confidence", 0)
    return row
