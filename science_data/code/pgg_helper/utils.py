import copy
from scipy.stats import qmc
import pandas as pd 
import numpy as np
from numpy.random import default_rng
import random
from yaml import load, dump
import os

def print_prereg_conditions(df_paired_val, print_prediction=False):
    temp_df_print = copy.deepcopy(df_paired_val)
    temp_df_print.loc[
        ~temp_df_print["CONFIG_rewardExists"],
        ["CONFIG_rewardCost", "CONFIG_rewardTech"],
    ] = "NA"
    temp_df_print[["treatment_itt_efficiency", "control_itt_efficiency"]] = (
        temp_df_print[["treatment_itt_efficiency", "control_itt_efficiency"]].round(2)
    )

    temp_df_print["CONFIG_defaultContribProp"] = temp_df_print[
        "CONFIG_defaultContribProp"
    ].astype(bool)
    for bool_col in [
        "CONFIG_showNRounds",
        "CONFIG_allOrNothing",
        "CONFIG_chat",
        "CONFIG_defaultContribProp",
        "CONFIG_rewardExists",
        "CONFIG_showOtherSummaries",
        "CONFIG_showPunishmentId",
    ]:
        temp_df_print[bool_col] = temp_df_print[bool_col].astype(str).str.slice(0, 1)

    param_labels = {
        "CONFIG_playerCount": "Player Count",
        "CONFIG_numRounds": "Number of Rounds",
        "CONFIG_showNRounds": "Show # Rounds (T/F)",
        "CONFIG_MPCR": "Marginal per capita return",
        "CONFIG_allOrNothing": "All or Nothing (T/F)",
        "CONFIG_chat": "Chat (T/F)",
        "CONFIG_defaultContribProp": "Contribution default (T/F)",
        "CONFIG_punishmentCost": "Punishment Cost",
        "CONFIG_punishmentTech": "Punishment Effectiveness",
        "CONFIG_rewardExists": "Reward Enabled (T/F)",
        "CONFIG_rewardCost": "Reward Cost",
        "CONFIG_rewardTech": "Reward Effectiveness",
        "CONFIG_showOtherSummaries": "Peer Summaries Visible (T/F)",
        "CONFIG_showPunishmentId": "Punishers/Rewarders Known (T/F)",
        "control_itt_efficiency": "Efficiency (Control)",
        "treatment_itt_efficiency": "Efficiency (Treatment)",
    }

    if print_prediction:
        param_labels["ols_prereg_pred"] = "OLS Prediction (Treatment)"
        param_labels["rf_prereg_pred"] = "RF Prediction (Treatment)"
        param_labels["xgb_prereg_pred"] = "XGB Prediction (Treatment)"
        param_labels["mlp_prereg_pred"] = "MLP Prediction (Treatment)"
        param_labels["elastic_prereg_pred"] = "ElasticNet Prediction (Treatment)"

        temp_df_print[
            ["ols_prereg_pred", "rf_prereg_pred", "xgb_prereg_pred", "mlp_prereg_pred", "elastic_prereg_pred"]
        ] = temp_df_print[
            ["ols_prereg_pred", "rf_prereg_pred", "xgb_prereg_pred", "mlp_prereg_pred", "elastic_prereg_pred"]
        ].round(
            2
        )

    print(", ".join(param_labels.values()))

    for configId in range(20):
        print(
            f"Exp {configId+1}: {', '.join(temp_df_print.query('CONFIG_configId == @configId').reset_index().loc[0][list(param_labels.keys())].astype(str).values)}"
        )

def export_empirica_pgg_json(df_paired_val):

    EXPERT_PRED_COLUMNS = {
        "control_efficiency": "control_efficiency",
        "treatment_efficiency": "treatment_efficiency",
        "CONFIG_configId": "CONFIG_configId",
        "CONFIG_playerCount": "n_players",
        "CONFIG_numRounds": "n_rounds",
        "CONFIG_showNRounds": "n_rounds_shown",
        "CONFIG_MPCR": "mpcr",
        "CONFIG_allOrNothing": "all_or_nothing",
        "CONFIG_chat": "chat",
        "CONFIG_defaultContribProp": "contrib_default",
        "CONFIG_punishmentExists": "punishment_exists",
        "CONFIG_punishmentCost": "punishment_cost",
        "CONFIG_punishmentTech": "punishment_magnitude",
        "CONFIG_rewardExists": "reward_exists",
        "CONFIG_rewardCost": "reward_cost",
        "CONFIG_rewardTech": "reward_magnitude",
        "CONFIG_showOtherSummaries": "peer_info_shown",
        "CONFIG_showPunishmentId": "punish_reward_id_known",
    }

    df_expert_prediction = (
        df_paired_val.assign(CONFIG_punishmentExists=True)
        .assign(control_efficiency=lambda x: (x.control_itt_efficiency * 100).round(1))
        .assign(
            treatment_efficiency=lambda x: (x.treatment_itt_efficiency * 100).round(1)
        )
    )

    expert_pred_json = dict(
        zip(
            df_expert_prediction["CONFIG_configId"].astype(str),
            df_expert_prediction[EXPERT_PRED_COLUMNS.keys()]
            .rename(columns=EXPERT_PRED_COLUMNS)
            .to_dict(orient="records"),
        )
    )

    return expert_pred_json




def generate_experimental_conditions(wave, destination_folder):
    # Create the destination directory if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    def generate_empirica_uuid():
        return "".join(random.choices("23456789ABCDEFGHJKLMNPQRSTWXYZabcdefghijkmnopqrstuvwxyz", k=17))

    def generate_experiment_config(method_space, scramble_sobol, n1 = 1, n2 = 2**8, seed=None):
        n_dim = len([dim for dim in method_space if dim['value_type'] != "const"])
        sampler = qmc.Sobol(d=n_dim, scramble=scramble_sobol, seed=seed)
        sample = sampler.random_base2(m=int(np.log2(n2))) # generate 2**m points 

        df = pd.DataFrame(sample, columns=[dim['name'] for dim in method_space if dim['value_type'] != "const"])

        for dimension in method_space: 
            dim_name = dimension['name']
            dim_val_type = dimension['value_type']

            if dim_val_type == "bool":
                df[dim_name] = df[dim_name].round()

            elif dim_val_type == "const":
                df[dim_name] = dimension['value']

            elif dim_val_type == "integer":
                interval_width = dimension['max_value'] - dimension['min_value']
                df[dim_name] = (dimension['min_value'] + df[dim_name] * interval_width).round().astype(int)

            elif dim_val_type == "float":
                interval_width = dimension['max_value'] - dimension['min_value']
                df[dim_name] = (dimension['min_value'] + df[dim_name] * interval_width).astype(float)
                
        if n1 == 1:
            return df 
        else: 
            return pd.concat([df]*n1, ignore_index=True)
        
    def emit_yaml_csv_files(df_config, output_path, is_validation):
        factor_descriptions = {"playerCount":"The number of players in the game.",
                        "numRounds":"The number of rounds played in the game.",
                        "showNRounds":"Is the total number of rounds shown to players?",
                        "endowment":"The coins given to players at the beginning of each round.",
                        "multiplier":"The multiplying factor of the total contributions to the public fund.",
                        "allOrNothing":"Are players only allowed to contribute/withhold the entire endowment?",
                        "chat":"Can players chat with each other?",
                        "defaultContribProp":"The proportion of the endowment contributed to the fund by default.",
                        "punishmentExists":"Can players punish?",
                        "punishmentCost":"The number of coins it costs to impose a single punishment.",
                        "punishmentMagnitude":"The number of coins deducted per punishment inflicted.",
                        "rewardExists":"Can players reward?",
                        "rewardCost":"The number of coins it costs to grant a single reward.",
                        "rewardMagnitude":"The number of coins added per reward granted.",
                        "showOtherSummaries":"Can players see the summaries of other players?",
                        "showPunishmentId":"Can players see who punished them?",
                        "showRewardId":"Can players see who rewarded them?",
                        "contributionDuration":"The length of the contribution phase, in seconds.",
                        "outcomeDuration":"The length of the outcome phase, in seconds.",
                        "summaryDuration":"The length of the summary phase, in seconds.",
                        "basePay":"The base pay given to participants, in USD.",
                        "conversionRate":"The rate of exchange from coins to USD."}

        factor_types = []
        for column in df_config.drop(["configId", "treatmentName"], axis=1).columns: 
            factor_type_dict = {"_id":generate_empirica_uuid(),
                                "name":column,
                                "description":factor_descriptions[column],
                                "required":True,
                                "type":{"int64":"Integer", "float64":"Number", "bool":"Boolean"}[str(df_config[column].dtype)]}

            factor_types.append(factor_type_dict)    
            
        
        factors = []
        for index, column in enumerate(df_config.drop(["configId", "treatmentName"], axis=1).columns): 
            for factor_value in df_config[column].unique().tolist():
                factor_dict = {"_id":generate_empirica_uuid(),
                            "name":'{}'.format(factor_value),
                            "value":factor_value,
                            "factorTypeId":factor_types[index]['_id']}
                factors.append(factor_dict)

        assert(df_config.drop(["configId", "treatmentName"], axis=1).nunique().sum() == len(factors))


        # Format the factors 
        factor_type_ids  = dict(zip([x['name'] for x in factor_types], [x['_id'] for x in factor_types]))

        factor_level_map = dict(zip(factor_type_ids.keys(),
            [dict(zip([level['value'] for level in [factor for factor in factors if factor['factorTypeId'] == factor_type_ids[factor_type]]],
                [level['_id'] for level in [factor for factor in factors if factor['factorTypeId'] == factor_type_ids[factor_type]]])) for factor_type in factor_type_ids.keys()]))


        # Format the treatments 
        treatments = []
        for index, treatment in enumerate(df_config.drop(["configId", "treatmentName"], axis=1).to_dict(orient="records")):
            treatments.append({"name": ("VALIDATION_" if is_validation else "") + df_config["treatmentName"][index],
                            "factorIds":[factor_level_map[factor_type][factor_value] for factor_type,factor_value in treatment.items()]})

        # Configure the lobby 
        lobbies = [{"name":"15min_ignore",
                    "timeoutType":"lobby",
                    "timeoutInSeconds":900,
                    "timeoutStrategy":"ignore",
                    "gameLobbyIds":[]}]
        
        # Output to yaml and pickle 
        with open(f'{output_path}.yaml', 'w') as file:
            yaml_file = dump({"treatments":treatments,
                            "factorTypes":factor_types,
                            "factors":factors,
                            "lobbyConfigs":lobbies}, 
                            file)

        if is_validation:
            df_config["treatmentName"] = "VALIDATION_"+df_config["treatmentName"]

        df_config.to_csv(f'{output_path}.csv', index=False)

    def process_raw_config(df_exp):
        df_exp['multiplier'] = ( (1 + df_exp["roi_modified"] * (0.7 * df_exp["playerCount"] - 1)) * 10).round() / 10


        #rounding 
        df_exp['punishmentMagnitude'] = (df_exp['punishmentCost'] * df_exp['punishmentTech']).round()
        df_exp['rewardCost'] = df_exp['punishmentCost']
        df_exp['rewardMagnitude'] = (df_exp['rewardCost'] * df_exp['rewardTech']).round()

        #Config logic 
        df_exp['showRewardId'] = df_exp['showPunishmentId']
        df_exp['configId'] = np.arange(len(df_exp))
        df_exp["punishmentExists"] = None

        
        factor_list = ["playerCount", "numRounds", "showNRounds", "endowment", "multiplier", 
                    "allOrNothing", "chat", "defaultContribProp",
                    "punishmentExists", "punishmentCost", "punishmentMagnitude", 
                    "rewardExists", "rewardCost", "rewardMagnitude",
                    "showOtherSummaries", "showPunishmentId", "showRewardId",
                    "contributionDuration", "outcomeDuration", "summaryDuration",
                    "basePay", "conversionRate"]

        df_config = df_exp[["configId"] + factor_list]

        # Format column types for YAML writing
        df_config = pd.concat([df_config.assign(punishmentExists=True, treatmentName=lambda x: x.configId.astype(str) + "_T"), df_config.assign(punishmentExists=False, treatmentName=lambda x: x.configId.astype(str) + "_C")], ignore_index=True)
        df_config['showNRounds'] = df_config['showNRounds'].astype(bool)
        df_config['showOtherSummaries'] = df_config['showOtherSummaries'].astype(bool)
        df_config['showPunishmentId'] = df_config['showPunishmentId'].astype(bool)
        df_config['allOrNothing'] = df_config['allOrNothing'].astype(bool)
        df_config['chat'] = df_config['chat'].astype(bool)
        df_config['rewardExists'] = df_config['rewardExists'].astype(bool)
        df_config['showRewardId'] = df_config['showRewardId'].astype(bool)
        df_config["basePay"] = np.round(0.1 * df_config["numRounds"],2)

        return df_config
    
    assert wave in ["learning", "validation"]

    if wave == "learning":
        method_space = [{"name": "playerCount", "value_type": "integer", "min_value": 2, "max_value": 20},
                {"name": "numRounds", "value_type": "integer", "min_value": 1, "max_value": 30},
                {"name": "showNRounds", "value_type": "bool"},
                {"name": "endowment", "value_type": "const", "value":20},
                {"name": "roi_modified", "value_type": "float", "min_value": 0, "max_value": 1},
                {"name": "punishmentCost", "value_type": "integer", "min_value": 1, "max_value": 4},
                {"name": "punishmentTech", "value_type": "float", "min_value": 1, "max_value": 4},
                {"name": "basePay", "value_type": "const", "value":3},
                {"name": "conversionRate", "value_type": "const", "value":300},
                {"name": "contributionDuration", "value_type": "const", "value":45}, 
                {"name": "outcomeDuration", "value_type": "const", "value":45}, 
                {"name": "summaryDuration", "value_type": "const", "value":45},
                {"name": "showOtherSummaries", "value_type": "bool"},
                {"name": "showPunishmentId", "value_type": "bool"},
                {"name": "chat", "value_type": "bool"},
                {"name": "rewardExists", "value_type": "bool"}, 
                {"name": "rewardTech", "value_type": "float", "min_value": 0.5, "max_value": 1.5},
                {"name": "defaultContribProp", "value_type": "integer", "min_value": 0, "max_value": 1},
                {"name": "allOrNothing", "value_type": "bool"}]

        df_exp = generate_experiment_config(method_space, scramble_sobol=True, n1=1, n2=256, seed=2022)
        df_config = process_raw_config(df_exp)
        emit_yaml_csv_files(df_config, f'{destination_folder}/learning', is_validation=False)

    elif wave == "validation":
        rng = default_rng(seed=2023)
        n_validation_conditions = 20
        validation_conditions = {"playerCount": rng.integers(low=2, high=20, endpoint=True, size=n_validation_conditions),
                                "numRounds": rng.integers(low=1, high=30, endpoint=True, size=n_validation_conditions),
                                "showNRounds": rng.integers(low=0, high=1, endpoint=True, size=n_validation_conditions),
                                "endowment": [20] * n_validation_conditions,
                                "roi_modified": rng.uniform(low=0, high=1, size=n_validation_conditions),
                                "punishmentCost": rng.integers(low=1, high=4, endpoint=True, size=n_validation_conditions),
                                "punishmentTech": rng.uniform(low=1, high=4, size=n_validation_conditions),
                                "basePay": [3] * n_validation_conditions,
                                "conversionRate": [300] * n_validation_conditions,
                                "contributionDuration": [45] * n_validation_conditions,
                                "outcomeDuration": [45] * n_validation_conditions,
                                "summaryDuration": [45] * n_validation_conditions,
                                "showOtherSummaries": rng.integers(low=0, high=1, endpoint=True, size=n_validation_conditions),
                                "showPunishmentId": rng.integers(low=0, high=1, endpoint=True, size=n_validation_conditions),
                                "chat": rng.integers(low=0, high=1, endpoint=True, size=n_validation_conditions),
                                "rewardExists": rng.integers(low=0, high=1, endpoint=True, size=n_validation_conditions),
                                "rewardTech": rng.uniform(low=0.5, high=1.5, size=n_validation_conditions),
                                "defaultContribProp": rng.integers(low=0, high=1, endpoint=True, size=n_validation_conditions),
                                "allOrNothing": rng.integers(low=0, high=1, endpoint=True, size=n_validation_conditions),
                                }
            
            
        df_exp = pd.DataFrame(validation_conditions)
        df_config = process_raw_config(df_exp)
        emit_yaml_csv_files(df_config, f'{destination_folder}/validation', is_validation=True)





