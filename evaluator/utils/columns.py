from __future__ import annotations

from collections import OrderedDict

COLUMN_MAP: OrderedDict[str, tuple[str, str]] = OrderedDict(
    [
        ("Empirical", ("Empirical", "METHOD_empirical")),
        ("Controled_Or_Observational", ("Controled_Or_Observational", "METHOD_lab")),
        ("Lab_Or_Field", ("Lab_Or_Field", "METHOD_experiment")),
        ("CONFIG_playerCount", ("CONFIG_playerCount", "CONFIG_playerCount")),
        ("CONFIG_numRounds", ("CONFIG_numRounds", "CONFIG_numRounds")),
        ("CONFIG_showNRounds", ("CONFIG_showNRounds", "CONFIG_showNRounds")),
        ("CONFIG_allOrNothing", ("CONFIG_allOrNothing", "CONFIG_allOrNothing")),
        ("CONFIG_defaultContribProp", ("CONFIG_defaultContribProp", "CONFIG_defaultContribProp")),
        ("CONFIG_MPCR", ("CONFIG_MPCR", "CONFIG_MPCR")),
        ("CONFIG_chat", ("CONFIG_chat", "CONFIG_chat")),
        ("CONFIG_showOtherSummaries", ("CONFIG_showOtherSummaries", "CONFIG_showOtherSummaries")),
        ("CONFIG_showPunishmentId", ("CONFIG_showPunishmentId", "CONFIG_showPunishmentId")),
        ("CONFIG_punishmentExists", ("CONFIG_punishmentExists", "CONFIG_punishmentExists")),
        ("CONFIG_punishmentCost", ("CONFIG_punishmentCost", "CONFIG_punishmentCost")),
        ("CONFIG_punishmentTech", ("CONFIG_punishmentTech", "CONFIG_punishmentTech")),
        ("CONFIG_showRewardId", ("CONFIG_showRewardId", "CONFIG_showRewardId")),
        ("CONFIG_rewardExists", ("CONFIG_rewardExists", "CONFIG_rewardExists")),
        ("CONFIG_rewardCost", ("CONFIG_rewardCost", "CONFIG_rewardCost")),
        ("CONFIG_rewardTech", ("CONFIG_rewardTech", "CONFIG_rewardTech")),
        # ("DV_contributionRate", ("DV_contributionRate", "DV_contributionRate")),  # removed: not evaluating numeric DV values
        # ("DV_efficiency", ("DV_efficiency", "DV_efficiency")),                    # removed: replaced by DV_efficiencyReported
        ("DV_efficiencyReported", ("DV_efficiencyReported", "DV_efficiencyReported")),
        ("DVs", ("Dependent Variables", "DVs")),
        ("DVs_Definitions", ("Dependent Variables Definitions", "DVs_Definitions")),
    ]
)

GROUND_TRUTH_COLUMNS: list[str] = (
    ["Filename", "Alignment_Label", "Granularity"]
    + [human_col for human_col, _ in COLUMN_MAP.values()]
)
