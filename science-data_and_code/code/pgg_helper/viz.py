import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


def space_exploration_viz(
    df_paired_learn, df_paired_val, display_lit, display_learn, display_val
):
    lit_review_param_mapping = {
        "CONFIG_playerCount": "# players",
        "CONFIG_numRounds": "# rounds",
        "CONFIG_showNRounds": "# rounds known?",
        "CONFIG_endowment": "Endowment",
        "CONFIG_MPCR": "MPCR",
        "CONFIG_allOrNothing": "All or Nothing",
        "CONFIG_chat": "Chat",
        "CONFIG_defaultContribProp": "Default contrib.",
        "CONFIG_scaledPunishmentCost": "Scaled punishment cost",
        "CONFIG_punishmentTech": "Punishment tech",
        "CONFIG_rewardExists": "Reward exists?",
        "CONFIG_showOtherSummaries": "Peer outcomes shown?",
        "CONFIG_showPunishmentId": "Are punishers known?",
    }

    scaler = StandardScaler()
    dim_reduction = PCA()

    df_lit_review = pd.read_csv("../data/PGG Lit Review - Machine Readable.csv")
    df_lit_review.columns = [x.strip() for x in df_lit_review.columns]
    df_lit_review["Multiplier"] = (
        df_lit_review["MPCR"] * df_lit_review["# players"]
    ).astype(float)
    df_lit_review["Punishment magnitude"] = (
        df_lit_review["Punishment cost"] * df_lit_review["Punishment tech"]
    ).astype(float)
    df_lit_review["Scaled punishment cost"] = (
        df_lit_review["Punishment cost"] / df_lit_review["Endowment"]
    ).astype(float)

    # First we standardize the columns then we fit the PCA
    low_dim_lit = dim_reduction.fit_transform(
        scaler.fit_transform(
            df_lit_review[lit_review_param_mapping.values()]
            .apply(pd.to_numeric, axis=1)
            .to_numpy()
        )
    )
    low_dim_learn = dim_reduction.transform(
        scaler.transform(
            df_paired_learn[lit_review_param_mapping.keys()]
            .apply(pd.to_numeric, axis=1)
            .to_numpy()
        )
    )
    low_dim_val = dim_reduction.transform(
        scaler.transform(
            df_paired_val[lit_review_param_mapping.keys()]
            .apply(pd.to_numeric, axis=1)
            .to_numpy()
        )
    )

    plt.figure(figsize=(8, 8))
    if display_lit:
        plt.scatter(
            low_dim_lit[:, 0],
            low_dim_lit[:, 1],
            color="red",
            label="Punishment Literature",
            marker="s",
            s=80,
        )
    if display_learn:
        plt.scatter(
            low_dim_learn[:, 0],
            low_dim_learn[:, 1],
            color="orange",
            label="Learning Set (Wave 1)",
        )
    if display_val:
        plt.scatter(
            low_dim_val[:, 0],
            low_dim_val[:, 1],
            color="blue",
            label="Validation Set (Wave 2)",
            marker="s",
            s=80,
        )

    plt.xlabel("PC1", fontsize=18)
    plt.ylabel("PC2", fontsize=18)
    plt.tick_params("both", labelsize=14)
    plt.legend(loc="upper left")

    if display_lit:
        plt.text(-1.8, 1, "Gächter (2008)", color="blue")
        plt.text(3.5, -3.2, "Rockenbach (2006)", color="blue")
        plt.text(4.45, 3.3, "Rand (2009)", color="blue")
        plt.text(-1.3, -0.8, "Nikiforakis (2010)", color="blue")

    plt.xlim(-3, 6)
    plt.ylim(-4, 4)


def within_sample_descriptive_viz(df_rounds_learn, df_analysis_learn, return_models=False):

    WITHIN_SAMPLE_COLS = [
        "CONFIG_playerCount",
        "CONFIG_numRounds",
        "CONFIG_showNRounds",
        "CONFIG_MPCR",
        "CONFIG_allOrNothing",
        "CONFIG_chat",
        "CONFIG_defaultContribProp",
        "CONFIG_rewardExists",
        "CONFIG_showOtherSummaries",
    ]

    WITHIN_SAMPLE_COLS_BOOL = [
        "CONFIG_showNRounds",
        "CONFIG_MPCR",
        "CONFIG_allOrNothing",
        "CONFIG_chat",
        "CONFIG_defaultContribProp",
        "CONFIG_rewardExists",
        "CONFIG_showOtherSummaries",
        "CONFIG_punishmentExists",
    ]

    df_analysis_rounds_learn = (
        df_rounds_learn.merge(
            df_analysis_learn.filter(regex="CONFIG|gameId"), how="left", on="gameId"
        )
        .drop(columns=["CONFIG_treatmentName"])
        .filter(regex="CONFIG|data.contr|gameId|round_index|playerId")
        .dropna()
    )

    df_analysis_rounds_learn["CONFIG_punishmentExists"] = df_analysis_rounds_learn["CONFIG_punishmentExists"].astype(bool)

    # TODO: review the model specifications here... should we also add a random intercept to contributions for the group?
    gamelevel_releff_model = smf.ols(f"itt_relative_efficiency ~ {'+'.join(['CONFIG_punishmentExists']+WITHIN_SAMPLE_COLS)}", data=df_analysis_learn).fit()
    contribution_model_clustered = smf.mixedlm(f"coins_contributed ~ {'+'.join(['round_index','CONFIG_punishmentExists']+WITHIN_SAMPLE_COLS)}", 
                                               data=df_analysis_rounds_learn.rename(columns={"data.contribution":"coins_contributed"}), groups="playerId").fit()
    
    if return_models:
        return gamelevel_releff_model, contribution_model_clustered
    
    fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(10,5))
    plot_coeffs(gamelevel_releff_model, False, axes[1])
    plot_coeffs(contribution_model_clustered, False, axes[0])
    


def plot_coeffs(model, interactions_only=False, ax=None, subset_cols=None, special_case = False):

    print_column_names = {'CONFIG_playerCount':"# players", 
                      'CONFIG_numRounds':"# rounds",
                      'CONFIG_showNRounds':"Is # rounds known?", 
                      'CONFIG_MPCR':"Marginal per capita return",
                      'CONFIG_allOrNothing':"Is game all or nothing?", 
                      'CONFIG_chat':"Can players chat?", 
                      'CONFIG_defaultContribProp':"Is coop. the default?",
                      'CONFIG_punishmentExists':"Is punishment enabled?",
                      'CONFIG_rewardExists':"Is reward enabled?", 
                      'CONFIG_showOtherSummaries':"Are peer outcomes visible?"}
    
    if special_case:
        plot_df = pd.read_csv("../data/master_processed/r_lmer_fixed_effects_table.csv").rename(columns={"Term":"iv", "Estimate":"coef", "Std. Error":"se"})
    else:
        plot_df = pd.DataFrame([model.params, model.bse]).T.reset_index().rename(columns={"index":"iv", 0:"coef", 1:"se"})
        
    if interactions_only:
        plot_df = plot_df[[":" in x for x in plot_df["iv"]]].sort_values("coef").query(f"iv != 'Intercept' and iv != 'gameId Var' and iv != 'playerId Var' and iv != 'round_index'")
    else:
        plot_df = plot_df.sort_values("coef").query("iv != 'Intercept' and iv != 'gameId Var' and iv != 'playerId Var' and iv != 'round_index'")
        
    if subset_cols:
        plot_df = plot_df[[x in subset_cols for x in plot_df["iv"].str.strip("[T.True]")]]

    if not interactions_only:
        plot_df["iv"] = plot_df["iv"].str.strip("[T.True]").map(print_column_names)
    
    else:
        plot_df["iv"] = [x.split(":")[1] for x in plot_df["iv"]]
        plot_df["iv"] = plot_df["iv"].str.strip("[T.True]").map(print_column_names)
        plot_df = plot_df.dropna()
                
    if ax:
        ax.scatter(x=plot_df["coef"], y=plot_df["iv"])
        ax.errorbar(x=plot_df["coef"], y=plot_df["iv"], xerr=1.96*plot_df["se"], ls="none")
        ax.axvline(x=0, color="black", linestyle="--")
    else:
        plt.scatter(x=plot_df["coef"], y=plot_df["iv"])
        plt.errorbar(x=plot_df["coef"], y=plot_df["iv"], xerr=1.96*plot_df["se"], ls="none")
        plt.axvline(x=0, color="black", linestyle="--")