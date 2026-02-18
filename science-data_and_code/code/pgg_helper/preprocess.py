import pandas as pd 
import ast
import numpy as np 

from .constants import DICT_CONDITION_BUNDLES


# Loading data 
class master_data():
    def __init__(self, DATA_FOLDER, CONFIG_CSV_PATH):
        
        # Load basic dataframes 
        self.df_input = pd.read_csv(f"../data/{DATA_FOLDER}/player-inputs.csv")
        self.df_players = (pd.read_csv(f"../data/{DATA_FOLDER}/players.csv").assign(exitReason = lambda x: x.exitReason.fillna("noExit")))
        
        self.df_stages_meta = pd.read_csv(f"../data/{DATA_FOLDER}/stages.csv")
        self.df_rounds_meta = pd.read_csv(f"../data/{DATA_FOLDER}/rounds.csv")
        self.df_rounds = pd.read_csv(f"../data/{DATA_FOLDER}/player-rounds.csv").merge(self.df_rounds_meta[["_id", "index"]].rename(columns={"index":"round_index"}), left_on="roundId", right_on="_id", how="left").assign(player_removed = lambda x: x["data.contribution"].isnull())
        self.df_games = pd.read_csv(f"../data/{DATA_FOLDER}/games.csv").rename(columns={"data.messages":"chat_log"})
        # df_logs = pd.read_csv(f"../data/{DATA_FOLDER}/player-logs.csv")
        self.df_treatments = pd.read_csv(f"../data/{DATA_FOLDER}/treatments.csv")
        
        # Load configurations as output by the Sobol sampling procedure in generate_configs.ipynb 
        self.df_treatment_config = pd.read_csv(CONFIG_CSV_PATH)
        self.df_treatment_config.columns = ["CONFIG_" + x for x in self.df_treatment_config.columns]
        self.df_treatment_config["CONFIG_punishmentTech"] = self.df_treatment_config["CONFIG_punishmentMagnitude"] / self.df_treatment_config["CONFIG_punishmentCost"]
        self.df_treatment_config["CONFIG_MPCR"] = self.df_treatment_config["CONFIG_multiplier"] / self.df_treatment_config["CONFIG_playerCount"]
        self.df_treatment_config["CONFIG_scaledPunishmentCost"] = (self.df_treatment_config["CONFIG_punishmentCost"] / self.df_treatment_config["CONFIG_endowment"]).astype(float)
        
def generate_df_analysis(df_players, df_rounds, df_games, 
                         df_treatments, df_treatment_config, 
                         PAIRED_MATCH_PLAYER_DIFF_PCT, REL_EFF_SMOOTHING_FACTOR, 
                         is_validation, filtered=True):
    # Attrition: count number of players
    dict_actual_playerCount = dict(df_rounds.dropna(subset=["data.roundPayoff"])
                                   .query("round_index == 0").groupby("gameId")["playerId"].nunique())

    set_failed_readycheck = set(df_players.query("exitReason == 'failedReadyCheck'")["_id"])
    dict_round_first_player_removed = dict(df_rounds.query("player_removed and playerId not in @set_failed_readycheck").groupby(["gameId", "round_index"])["playerId"].nunique()
                                           .reset_index().groupby("gameId")["round_index"].min())

    # Count n players who failed the readycheck
    list_player_ids = []
    list_game_ids = []

    for row in df_games.rename(columns={"_id":"gameId"}).itertuples():
        list_player_ids += row.playerIds.split(",")
        list_game_ids += [row.gameId]*len(row.playerIds.split(","))

    dict_players_games = dict(zip(list_player_ids, list_game_ids))
    df_players["gameId"] = df_players["_id"].map(dict_players_games)
    dict_failed_readycheck = dict(df_players.query("exitReason == 'failedReadyCheck'").groupby(["gameId"]).size())

    del list_player_ids, list_game_ids

    # Count number of players who started the game
    dict_num_players_starting = dict(zip(df_games["_id"], df_games.apply(lambda x: len(x.playerIds.split(",")), axis=1)))

    # Generate main DF
    df_analysis = (df_games
                   .rename(columns={"_id":"gameId"})
                   .merge(df_treatments[["_id", "name"]], left_on="treatmentId", right_on="_id", how="left")
                   .merge(df_treatment_config, left_on="name", right_on="CONFIG_treatmentName", how="left")
                   .assign(num_completed_first_round = lambda x: x.gameId.map(dict_actual_playerCount))
                   .assign(num_failed_readycheck = lambda x: x.gameId.map(dict_failed_readycheck).fillna(0))
                   .assign(num_started_game = lambda x: x.gameId.map(dict_num_players_starting))
                   .assign(num_started_and_readycheck = lambda x: x.num_started_game - x.num_failed_readycheck)
                   .assign(num_actual_players = lambda x: x[["num_completed_first_round", "num_started_and_readycheck"]].min(axis=1))
                   .assign(first_round_with_removed_player = lambda x: x.gameId.map(dict_round_first_player_removed))
                   .assign(total_coin_gen = lambda x: x.gameId.map(df_rounds.groupby("gameId")["data.roundPayoff"].sum()))
                   .assign(total_costs = lambda x: x.gameId.map(df_rounds.groupby("gameId")["data.costs"].sum()))
                   .assign(total_penalties = lambda x: x.gameId.map(df_rounds.groupby("gameId")["data.penalties"].sum()))
                   .assign(total_rewards = lambda x: x.gameId.map(df_rounds.groupby("gameId")["data.rewards"].sum()))
                  )

    # Calculate efficiency and coin counts
    df_itt_efficiency = df_rounds.groupby("roundId").agg({"gameId":"first", "data.roundPayoff":["sum", lambda x: (~x.isnull()).sum()]}).reset_index()
    df_itt_efficiency.columns = ["roundId", "gameId", "round_total_coin_gen", "round_n_players"]
    df_itt_efficiency = df_itt_efficiency.merge(df_analysis[["gameId", "CONFIG_multiplier"]].drop_duplicates(), on="gameId", how="left")
    df_itt_efficiency["round_defecting_coin_gen"] = 20 * df_itt_efficiency["round_n_players"] 
    df_itt_efficiency["round_max_coin_gen"] = 20 * df_itt_efficiency["round_n_players"] * df_itt_efficiency["CONFIG_multiplier"]
    df_itt_efficiency = (df_itt_efficiency.groupby("gameId")[["round_total_coin_gen", "round_defecting_coin_gen", "round_max_coin_gen"]].sum()
                         .reset_index()
                         .assign(itt_efficiency = lambda x: x.round_total_coin_gen / x.round_max_coin_gen)
                         .assign(itt_relative_efficiency = lambda x: (x.round_total_coin_gen - x.round_defecting_coin_gen + REL_EFF_SMOOTHING_FACTOR) / (x.round_max_coin_gen - x.round_defecting_coin_gen + REL_EFF_SMOOTHING_FACTOR)))

    df_analysis = df_analysis.merge(df_itt_efficiency, on="gameId", how="left")

    # Transformations of config parameters
    df_analysis["CONFIG_MPCR"] = (df_analysis["CONFIG_multiplier"] / df_analysis["CONFIG_playerCount"]).round(2)
    df_analysis["CONFIG_MPCR_adjusted"] = (df_analysis["CONFIG_multiplier"] / df_analysis["num_actual_players"]).round(2)
    df_analysis["CONFIG_punishmentTech"] = (df_analysis["CONFIG_punishmentMagnitude"] / df_analysis["CONFIG_punishmentCost"]).round(2)
    df_analysis["CONFIG_rewardTech"] = (df_analysis["CONFIG_rewardMagnitude"] / df_analysis["CONFIG_rewardCost"]).round(2)

    # Add flag for valid number of starting players
    df_analysis["valid_number_of_starting_players"] = ((df_analysis["CONFIG_playerCount"] - df_analysis["num_actual_players"]) / df_analysis["CONFIG_playerCount"]) <= PAIRED_MATCH_PLAYER_DIFF_PCT


    # Filtering and additional calculations
    if filtered:
        if is_validation:
            df_analysis = df_analysis.query("round_total_coin_gen != 0", engine="python").reset_index(drop=True)
        else:
            # QkNKFYHokbndpGhph is an excluded game with a reward cycle -- see SI for details. 
            df_analysis = df_analysis.query("CONFIG_multiplier != 1 and gameId != 'QkNKFYHokbndpGhph' and round_total_coin_gen != 0", engine="python").reset_index(drop=True)
    else:
        df_analysis = df_analysis.query("round_total_coin_gen != 0", engine="python").reset_index(drop=True)


    if is_validation:
        df_analysis["bundle"] = df_analysis["CONFIG_configId"].map(DICT_CONDITION_BUNDLES)
    else:
        set_paired_conditions = set((df_analysis.query("valid_number_of_starting_players")
                                     .groupby("CONFIG_configId")["CONFIG_punishmentExists"].nunique()
                                     .reset_index().query("CONFIG_punishmentExists == 2"))["CONFIG_configId"])
        df_analysis["paired_config"] = [x in set_paired_conditions for x in df_analysis["CONFIG_configId"]]

    return df_analysis

def generate_df_paired(df_analysis, is_validation):
    query_condition = "valid_number_of_starting_players" if is_validation else "valid_number_of_starting_players and paired_config"
    
    temp_df_treatment = (df_analysis.drop(columns="CONFIG_MPCR_adjusted").query(query_condition)
                         .query("CONFIG_punishmentExists")
                         .groupby("CONFIG_configId")[["itt_efficiency", "itt_relative_efficiency"]]
                         .mean().reset_index()
                         .rename(columns={"itt_efficiency":"treatment_itt_efficiency", "itt_relative_efficiency":"treatment_itt_relative_efficiency"}))

    temp_df_control = (df_analysis.drop(columns="CONFIG_MPCR_adjusted").query(query_condition)
                         .query("~CONFIG_punishmentExists")
                         .groupby("CONFIG_configId")[["itt_efficiency", "itt_relative_efficiency"]]
                         .mean().reset_index()
                         .rename(columns={"itt_efficiency":"control_itt_efficiency", "itt_relative_efficiency":"control_itt_relative_efficiency"}))

    df_prediction = (df_analysis.drop(columns="CONFIG_MPCR_adjusted").query(query_condition)
                    .filter(like="CONFIG").drop(columns=["CONFIG_punishmentExists", "CONFIG_treatmentName"]).drop_duplicates()
                    .merge(temp_df_treatment, on="CONFIG_configId", how="left")
                    .merge(temp_df_control, on="CONFIG_configId", how="left")
                    .dropna(subset=["treatment_itt_efficiency","treatment_itt_relative_efficiency", "control_itt_efficiency", "control_itt_relative_efficiency"])
                    .reset_index(drop=True))

    df_prediction["treatment_effect"] = df_prediction["treatment_itt_efficiency"] - df_prediction["control_itt_efficiency"]
    df_prediction["positive_treatment_effect"] = (df_prediction["treatment_effect"] >= 0).astype(int)

    assert len(df_prediction) == df_prediction["CONFIG_configId"].nunique()

    return df_prediction

