DICT_CONDITION_BUNDLES = dict(zip(range(20), [1,2,2,1,1,2,3,3,4,6,2,5,4,7,4,5,6,8,2,2]))
PAIRED_MATCH_PLAYER_DIFF_PCT = 0.18
REL_EFF_SMOOTHING_FACTOR = 0.01
PREDICTION_FEATURE_COLS = ["CONFIG_playerCount",
                           "CONFIG_numRounds",
                           "CONFIG_showNRounds",
                           "CONFIG_MPCR",
                           "CONFIG_allOrNothing",
                           "CONFIG_chat",
                           "CONFIG_defaultContribProp",
                           "CONFIG_rewardExists",
                           "CONFIG_showOtherSummaries",
                           "CONFIG_showPunishmentId",
                           "CONFIG_punishmentCost", 
                           "CONFIG_punishmentTech",
                           "control_itt_efficiency"] 