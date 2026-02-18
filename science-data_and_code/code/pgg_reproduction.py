import pgg_helper as pgg 
import os
import pandas as pd 
import numpy as np 
import os.path

# TODO: Decide how to handle warnings, silence for now 
import warnings
warnings.filterwarnings("ignore")



if __name__ == '__main__':
    print("Generating experimental conditions...")
    # Write the experimental conditions for learning and validation
    pgg.utils.generate_experimental_conditions("learning", "../data/exp_config_files")
    pgg.utils.generate_experimental_conditions("validation", "../data/exp_config_files")

    print("Processing raw data...")
    # Process the raw data for learning and validation
    md_learn = pgg.preprocess.master_data("../data/raw_data/learning_wave", 
                                        "../data/exp_config_files/learning.csv")

    df_analysis_learn = pgg.preprocess.generate_df_analysis(
                                    df_players = md_learn.df_players, 
                                    df_rounds = md_learn.df_rounds, 
                                    df_games = md_learn.df_games, 
                                    df_treatments = md_learn.df_treatments, 
                                    df_treatment_config = md_learn.df_treatment_config, 
                                    PAIRED_MATCH_PLAYER_DIFF_PCT=pgg.constants.PAIRED_MATCH_PLAYER_DIFF_PCT, 
                                                            REL_EFF_SMOOTHING_FACTOR=pgg.constants.REL_EFF_SMOOTHING_FACTOR,
                                                is_validation=False)


    md_val = pgg.preprocess.master_data("../data/raw_data/validation_wave/", 
                                        "../data/exp_config_files/validation.csv")
    df_analysis_val = pgg.preprocess.generate_df_analysis(
                                    df_players = md_val.df_players, 
                                    df_rounds = md_val.df_rounds, 
                                    df_games = md_val.df_games, 
                                    df_treatments = md_val.df_treatments, 
                                    df_treatment_config = md_val.df_treatment_config, 
                                    PAIRED_MATCH_PLAYER_DIFF_PCT=pgg.constants.PAIRED_MATCH_PLAYER_DIFF_PCT, 
                                                            REL_EFF_SMOOTHING_FACTOR=pgg.constants.REL_EFF_SMOOTHING_FACTOR,
                                            is_validation=True)

    df_paired_learn = pgg.preprocess.generate_df_paired(df_analysis_learn, is_validation=False)
    df_paired_val = pgg.preprocess.generate_df_paired(df_analysis_val, is_validation=True)

    hpo_config_path = "../data/hpo_model_configs.json"
    
    # Check if HPO config file already exists
    if not os.path.exists(hpo_config_path):
        print("Running hyperparameter optimization...")
        pgg.analysis.run_hpo(df_paired_learn=df_paired_learn,
                            feature_cols=["CONFIG_playerCount",
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
                                        "control_itt_efficiency"],
                            outcome_col="treatment_itt_efficiency",
                            hpo_config_output_path=hpo_config_path)
    else:
        print("HPO config file already exists, skipping optimization...")

    fitted_models = pgg.analysis.get_models(hpo_json_filepath="../data/hpo_model_configs.json", 
                                            df_paired_learn=df_paired_learn,
                                            feature_cols=["CONFIG_playerCount",
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
                                                        "control_itt_efficiency"],
                                            target_col="treatment_itt_efficiency",
                                            fitted=True)

    df_paired_val["ols_prereg_pred"] = fitted_models["ols"].predict(df_paired_val[pgg.constants.PREDICTION_FEATURE_COLS])
    df_paired_val["rf_prereg_pred"] = fitted_models["rf"].predict(df_paired_val[pgg.constants.PREDICTION_FEATURE_COLS])
    df_paired_val["xgb_prereg_pred"] = fitted_models["xgb"].predict(df_paired_val[pgg.constants.PREDICTION_FEATURE_COLS])
    df_paired_val["mlp_prereg_pred"] = fitted_models["mlp"].predict(df_paired_val[pgg.constants.PREDICTION_FEATURE_COLS])
    df_paired_val["elastic_prereg_pred"] = fitted_models["enet"].predict(df_paired_val[pgg.constants.PREDICTION_FEATURE_COLS])

    # Export to processed data folder 
    os.makedirs("../data/processed_data", exist_ok=True)
    df_analysis_learn.to_csv("../data/processed_data/df_analysis_learn.csv", index=False)
    df_analysis_val.to_csv("../data/processed_data/df_analysis_val.csv", index=False)
    df_paired_learn.to_csv("../data/processed_data/df_paired_learn.csv", index=False)
    df_paired_val.to_csv("../data/processed_data/df_paired_val.csv", index=False)
    md_learn.df_rounds.to_csv("../data/processed_data/df_rounds_learn.csv")
    md_val.df_rounds.to_csv("../data/processed_data/df_rounds_val.csv")


    print("Generating figures...")
    os.makedirs("../figures", exist_ok=True)
    print("Generating Figure 2...")
    pgg.manuscript_figures.fig2_heterogeneity_viz(processed_data_dir="../data/processed_data/", fig_output_path="../figures/manuscript_figure2.png")
    print("Generating Figure 3...")
    pgg.manuscript_figures.fig3_prediction_viz(processed_data_dir="../data/processed_data/", fig_output_path="../figures/manuscript_figure3.png")
    print("Generating Figure 4...")
    pgg.manuscript_figures.fig4_feature_importance_viz(processed_data_dir="../data/processed_data/", hpo_json_filepath="../data/hpo_model_configs.json", 
                                                   fig_output_path="../figures/manuscript_figure4.png", model_key="enet", model_label="E-net")
    print("Generating Figure 5...")
    pgg.manuscript_figures.fig5_shap_viz(processed_data_dir="../data/processed_data/", hpo_json_filepath="../data/hpo_model_configs.json", 
                                                   fig_output_path="../figures/manuscript_figure5.png")