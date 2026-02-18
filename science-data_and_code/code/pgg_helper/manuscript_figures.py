# Standard library imports
from copy import deepcopy

# Third-party scientific computing
import numpy as np
import pandas as pd

# Machine learning imports
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error

# Statistical modeling
import statsmodels.formula.api as smf

# Visualization imports
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import MaxNLocator, PercentFormatter
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import seaborn as sns

# Local imports
from .analysis import calc_q_i2, get_models, oos_permutation_feature_importance
from .constants import PREDICTION_FEATURE_COLS
import shap



def fig2_heterogeneity_viz(processed_data_dir, fig_output_path):
    def fit_cluster_params(group, outcome):
        model = smf.ols(f"{outcome} ~ CONFIG_punishmentExists", data=group).fit()
        return pd.Series({
            'estimate': model.params["CONFIG_punishmentExists[T.True]"],
            'se': model.bse["CONFIG_punishmentExists[T.True]"]
        })
    
    CLUSTER_COLUMNS = ['CONFIG_playerCount', 'CONFIG_numRounds', 'CONFIG_showNRounds', 
                   'CONFIG_MPCR', 'CONFIG_allOrNothing', 'CONFIG_chat', 'CONFIG_defaultContribProp', 
                   'CONFIG_rewardExists', 'CONFIG_showOtherSummaries', "CONFIG_punishmentCost", "CONFIG_punishmentTech",
                   'CONFIG_showPunishmentId']
    
    # LOAD DATA 
    df_paired_val = pd.read_csv(processed_data_dir + "df_paired_val.csv")
    df_paired_learn = pd.read_csv(processed_data_dir + "df_paired_learn.csv")
    df_analysis_val = pd.read_csv(processed_data_dir + "df_analysis_val.csv")
    df_analysis_learn = pd.read_csv(processed_data_dir + "df_analysis_learn.csv")
    df_rounds_learn = pd.read_csv(processed_data_dir + "df_rounds_learn.csv")
    df_rounds_val = pd.read_csv(processed_data_dir + "df_rounds_val.csv")

    df_paired_val["ols_model"] = df_paired_val["CONFIG_configId"].map(df_analysis_val.query("valid_number_of_starting_players").groupby("CONFIG_configId").apply(lambda x: smf.ols("itt_relative_efficiency ~ CONFIG_punishmentExists", data=x).fit()))
    df_paired_val["treatment_effect_mean"] = df_paired_val["ols_model"].apply(lambda x: x.params["CONFIG_punishmentExists[T.True]"])
    df_paired_val["treatment_effect_se"] = df_paired_val["ols_model"].apply(lambda x: x.bse["CONFIG_punishmentExists[T.True]"])

    df_analysis_learn_kmeans = deepcopy(df_analysis_learn)
    df_analysis_learn_kmeans.loc[:,["CONFIG_playerCount", "CONFIG_numRounds", "CONFIG_punishmentCost", "CONFIG_punishmentTech"]] = MinMaxScaler().fit_transform(df_analysis_learn_kmeans.loc[:,["CONFIG_playerCount", "CONFIG_numRounds", "CONFIG_punishmentCost", "CONFIG_punishmentTech"]])

    kmeans = KMeans(n_clusters=20, random_state=2024)
    df_cluster_learn = deepcopy(df_analysis_learn_kmeans).assign(cluster=kmeans.fit_predict(df_analysis_learn_kmeans[CLUSTER_COLUMNS])).query("valid_number_of_starting_players")
    df_cluster_params = df_cluster_learn.groupby("cluster").apply(lambda x: fit_cluster_params(x, "itt_relative_efficiency")).reset_index()

    valid_game_ids = set(df_analysis_learn.query("valid_number_of_starting_players")["gameId"]).union(set(df_analysis_val.query("valid_number_of_starting_players")["gameId"]))

    # VISUALIZATION CODE 
    # Style setup
    plt.style.use('default')
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42
    matplotlib.rcParams['font.sans-serif'] = ['Arial']
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['axes.facecolor'] = 'white'
    matplotlib.rcParams['figure.facecolor'] = 'white'
    matplotlib.rcParams['grid.alpha'] = 0.0

    # Define color schemes
    wave_colors = {
        'Learning dataset': '#1f77b4',    # Blue
        'Validation dataset': '#ff7f0e'    # Orange
    }

    # Colors for learning/validation experiments
    learning_colors = sns.color_palette("Blues", n_colors=4)
    learning_punishment_colors = {
        'Without punishment': learning_colors[1],
        'With punishment': learning_colors[2]
    }

    validation_colors = sns.color_palette("Oranges", n_colors=4)
    validation_punishment_colors = {
        'Without punishment': validation_colors[1],
        'With punishment': validation_colors[2]
    }

    punishment_markers = {
        'Without punishment': 'o',  # Circle
        'With punishment': '^'     # Triangle
    }

    # Define y-axis limits for clipping (only for panels C & E)
    Y_MIN = -0.55
    Y_MAX = 1.25

    # Create figure (Nature/Science standard size)
    height_mm = 220  # Reduced from 240
    width_mm = 183
    width_inches = width_mm / 25.4
    height_inches = height_mm / 25.4
    fig = plt.figure(figsize=(width_inches, height_inches), dpi=300)

    # Create GridSpec with adjusted ratios
    gs = GridSpec(5, 2, 
                height_ratios=[1.5, 2, 1.5, 2, 1.5],
                hspace=0.4,    # This will be overridden by per-row spacing
                wspace=0.15)

    # Get the GridSpec's position
    pos = gs.get_grid_positions(fig)

    # Manually adjust the height positions to create different spacing between paired panels
    # Original positions are in figure coordinates (0-1)
    row_positions = pos[0]  # These are the y-positions of each row

    # Adjust positions to bring E closer to D and G closer to F
    # Move row 2 (E) up closer to row 1 (D)
    row_positions[2] = row_positions[1] - 0.15  # Adjust this value to control D-E spacing

    # Move row 4 (G) up closer to row 3 (F)
    row_positions[4] = row_positions[3] - 0.15  # Adjust this value to control F-G spacing

    # Update GridSpec with new positions
    gs.update(top=0.95, bottom=0.08, hspace=0.4)

    # Create subplots
    ax_coins = fig.add_subplot(gs[0, 0])
    # ax_efficiency = fig.add_subplot(gs[0, 1])
    ax_normalized_efficiency = fig.add_subplot(gs[0, 1])
    ax_learning_efficiency = fig.add_subplot(gs[1, :])
    ax_learning_effect = fig.add_subplot(gs[2, :], sharex=ax_learning_efficiency)
    ax_validation_efficiency = fig.add_subplot(gs[3, :])
    ax_validation_effect = fig.add_subplot(gs[4, :], sharex=ax_validation_efficiency)

    # Common parameters
    err_kws = {'linewidth': 1.0}
    title_fontsize = 11
    label_fontsize = 9
    tick_fontsize = 8
    legend_fontsize = 8

    # Panel A: Coins
    sns.pointplot(
        y="CONFIG_punishmentExists", x="coins_contributed", orient="y",
        hue="wave", dodge=0.15,
        markers=['o', 'o'], linestyles="",
        markersize=5, err_kws=err_kws,
        ax=ax_coins, order=[True, False],
        palette=[wave_colors['Learning dataset'], wave_colors['Validation dataset']],
        data=(
            pd.concat([
                df_rounds_learn.merge(df_analysis_learn[["gameId", "CONFIG_punishmentExists"]],
                                    how="left", on="gameId").assign(wave="Learning dataset"),
                df_rounds_val.merge(df_analysis_val[["gameId", "CONFIG_punishmentExists"]],
                                how="left", on="gameId").assign(wave="Validation dataset")
            ], ignore_index=True)
            .rename(columns={"data.contribution": "coins_contributed"})
            .assign(coins_contributed=lambda x: x.coins_contributed / 20)
            .query("gameId in @valid_game_ids")
            .dropna(subset=["data.roundPayoff"])
        )
    )
    ax_coins.legend().remove()

    # Panel B: Normalized Efficiency
    sns.pointplot(
        y="CONFIG_punishmentExists", x="itt_relative_efficiency", orient="y",
        hue="wave", dodge=0.15,
        markers=['o', 'o'], linestyles="",
        markersize=5, err_kws=err_kws,
        ax=ax_normalized_efficiency, order=[True, False],
        palette=[wave_colors['Learning dataset'], wave_colors['Validation dataset']],
        data=pd.concat([
            df_analysis_learn.assign(wave="Learning dataset").query("valid_number_of_starting_players"),
            df_analysis_val.assign(wave="Validation dataset").query("valid_number_of_starting_players")
        ], ignore_index=True)
    )
    ax_normalized_efficiency.legend().remove()

    # Style top row plots
    for ax in [ax_coins, ax_normalized_efficiency]:
        ax.set_ylabel("")
        ax.tick_params(axis="both", labelsize=tick_fontsize)
        ax.set_yticks(ticks=range(2))
        ax.set_yticklabels(labels=["With\npunishment", "Without\npunishment"], fontsize=label_fontsize)
        ax.xaxis.set_major_locator(MaxNLocator(4))
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_linewidth(0.5)
        ax.spines['bottom'].set_linewidth(0.5)
        

    ax_normalized_efficiency.set_yticklabels(labels=["", ""], fontsize=label_fontsize)

    ax_coins.set_xlabel("Average contribution", fontsize=label_fontsize)
    ax_normalized_efficiency.set_xlabel("Normalized efficiency", fontsize=label_fontsize)

    ax_coins.xaxis.set_major_formatter(PercentFormatter(xmax=1.0, decimals=0))
    ax_coins.set_xlim(0.72, 0.86)
    ax_normalized_efficiency.set_xlim(0.55, 0.90)

    # Add legend for top row
    handles, labels = ax_coins.get_legend_handles_labels()
    fig.legend(handles, ['Learning dataset', 'Validation dataset'],
            loc='upper center',
            bbox_to_anchor=(0.5, 0.98),
            ncol=2,
            frameon=False,
            fontsize=legend_fontsize,
            borderaxespad=0,
            handlelength=1.5)

    # Learning panels (C, D)
    df_cluster_learn = df_cluster_learn.assign(
        CONFIG_punishmentExists=lambda x: x.CONFIG_punishmentExists.map(
            {False: 'Without punishment', True: 'With punishment'}
        )
    ).dropna(subset=['CONFIG_punishmentExists'])

    hue_order_learn = ['Without punishment', 'With punishment']
    hue_order_learn = [hue for hue in hue_order_learn if hue in df_cluster_learn['CONFIG_punishmentExists'].unique()]
    markers_learn = [punishment_markers[hue] for hue in hue_order_learn]
    palette_learn = [learning_punishment_colors[hue] for hue in hue_order_learn]

    # Function to handle clipped plotting and indicators with numeric labels - IMPROVED
    def plot_with_clipping_and_labels(ax, x, y, color, marker, size=15, alpha=0.4, y_min=Y_MIN, y_max=Y_MAX):
        # Separate points into normal, below, and above ranges
        normal_mask = (y >= y_min) & (y <= y_max)
        below_mask = y < y_min
        above_mask = y > y_max
        
        # Track outliers for labeling
        outliers = []
        
        # Plot normal points with open markers (empty)
        if normal_mask.any():
            ax.scatter(
                x=x[normal_mask],
                y=y[normal_mask],
                color=color,
                s=size,
                alpha=alpha,
                marker=marker,
                edgecolor=color,  # Make the edge the same color as the fill
                facecolor='none',  # Open markers for individual data points
                linewidth=0.8,
                zorder=1
            )
        
        # Plot and mark points below range with the same marker (triangle/circle) but with red border
        if below_mask.any():
            for i, (x_pos, y_val) in enumerate(zip(x[below_mask], y[below_mask])):
                ax.scatter(
                    x=x_pos,
                    y=y_min+0.05,  # Position at bottom of axis
                    color=color,
                    s=size+10,
                    alpha=1.0,  # Make more visible
                    marker=marker,  # Same marker as normal points
                    edgecolor='red',  # Red edge for outliers
                    #facecolor='none',  # Open markers
                    linewidth=1.2,  # Thicker border
                    zorder=2
                )
                # Add to outliers list for labeling
                outliers.append((x_pos, y_min, y_val, 'below'))
            
        # Plot and mark points above range with the same marker (triangle/circle) but with red border
        if above_mask.any():
            for i, (x_pos, y_val) in enumerate(zip(x[above_mask], y[above_mask])):
                ax.scatter(
                    x=x_pos,
                    y=y_max-0.05,  # Position at top of axis
                    color=color,
                    s=size+10,
                    alpha=1.0,  # Make more visible
                    marker=marker,  # Same marker as normal points
                    edgecolor='red',  # Red edge for outliers
                    #facecolor='none',  # Open markers
                    linewidth=1.2,  # Thicker border
                    zorder=2
                )
                # Add to outliers list for labeling
                outliers.append((x_pos, y_max, y_val, 'above'))
        
        return normal_mask.sum(), below_mask.sum(), above_mask.sum(), outliers

    # Panel C: Learning Efficiency
    sns.pointplot(
        x="cluster", y="itt_relative_efficiency", hue="CONFIG_punishmentExists",
        data=df_cluster_learn,
        order=df_cluster_params.sort_values("estimate")["cluster"].astype(str).values,
        dodge=0.4, markers=markers_learn, linestyles="",
        markersize=5, err_kws=err_kws,
        ax=ax_learning_efficiency,
        palette=palette_learn,
        hue_order=hue_order_learn
    )
    
    # Set y-axis limits for panel C only
    ax_learning_efficiency.set_ylim(Y_MIN, Y_MAX)
    
    # Add jittered individual data points for panel C (Learning Efficiency) with clipping and labels
    outliers_info_learn = {"normal": 0, "below": 0, "above": 0}
    all_outliers_learn = []
    
    for i, cluster in enumerate(df_cluster_params.sort_values("estimate")["cluster"].astype(str).values):
        cluster_data = deepcopy(df_cluster_learn[df_cluster_learn["cluster"] == int(cluster)])
        
        for punishment_type in cluster_data["CONFIG_punishmentExists"].unique():
            subset = cluster_data[cluster_data["CONFIG_punishmentExists"] == punishment_type]
            
            # Add jitter to x-position to avoid overlap
            x_jitter = np.random.uniform(-0.15, 0.15, size=len(subset))
            x_pos = i + (0.2 if punishment_type == "With punishment" else -0.2) + x_jitter
            
            # Plot with clipping indicators and collect outliers
            normal, below, above, outliers = plot_with_clipping_and_labels(
                ax_learning_efficiency,
                x=x_pos,
                y=subset["itt_relative_efficiency"].values,
                color=learning_punishment_colors[punishment_type],
                marker=punishment_markers[punishment_type]
            )
            
            outliers_info_learn["normal"] += normal
            outliers_info_learn["below"] += below
            outliers_info_learn["above"] += above
            all_outliers_learn.extend(outliers)

    # Add numeric labels for outliers in panel C
    for x_pos, y_pos, actual_value, position in all_outliers_learn:
        # Format the value with 1 decimal place
        value_str = f"{actual_value:.1f}"
        # Position the text slightly offset from the marker
        if position == 'above':
            ax_learning_efficiency.annotate(
                value_str, 
                xy=(x_pos, y_pos),
                xytext=(0, 5),  # 5 points above
                textcoords='offset points',
                ha='center', 
                va='bottom',
                fontsize=6,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.7)
            )
        else:  # below
            ax_learning_efficiency.annotate(
                value_str, 
                xy=(x_pos, y_pos),
                xytext=(0, -5),  # 5 points below
                textcoords='offset points',
                ha='center', 
                va='top',
                fontsize=6,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.7)
            )
    
    ax_learning_efficiency.legend(
        title='', loc='lower right', frameon=False, fontsize=legend_fontsize
    )

    # Panel D: Learning Effect - UNCHANGED
    df_cluster_params_sorted = df_cluster_params.sort_values("estimate")
    bar_colors = [learning_punishment_colors['Without punishment'] if x > 0 else learning_punishment_colors['With punishment']
                for x in df_cluster_params_sorted["estimate"]]

    sns.barplot(
        x="cluster", y="estimate",
        data=df_cluster_params_sorted,
        palette=bar_colors,
        order=df_cluster_params_sorted["cluster"].astype(str).values,
        ax=ax_learning_effect,
        errorbar="se"
    )

    ax_learning_effect.errorbar(
        x=range(len(df_cluster_params_sorted)),
        y=df_cluster_params_sorted["estimate"].values,
        yerr=(1.96 * df_cluster_params_sorted["se"]).values,
        linestyle="", color="black", linewidth=0.5, zorder=1000
    )

    # Validation panels (E, F)
    df_analysis_val_processed = df_analysis_val.query("valid_number_of_starting_players").assign(
        CONFIG_punishmentExists=lambda x: x.CONFIG_punishmentExists.map(
            {False: 'Without punishment', True: 'With punishment'}
        )
    ).dropna(subset=['CONFIG_punishmentExists'])

    hue_order_val = ['Without punishment', 'With punishment']
    hue_order_val = [hue for hue in hue_order_val if hue in df_analysis_val_processed['CONFIG_punishmentExists'].unique()]
    markers_val = [punishment_markers[hue] for hue in hue_order_val]
    palette_val = [validation_punishment_colors[hue] for hue in hue_order_val]

    # Panel E: Validation Efficiency
    sns.pointplot(
        x="CONFIG_configId", y="itt_relative_efficiency", hue="CONFIG_punishmentExists",
        data=df_analysis_val_processed,
        order=df_paired_val.sort_values("treatment_effect_mean")["CONFIG_configId"].astype(str).values,
        dodge=0.4, markers=markers_val, linestyles="",
        markersize=5, err_kws=err_kws,
        ax=ax_validation_efficiency,
        palette=palette_val,
        hue_order=hue_order_val
    )
    
    # Set y-axis limits for panel E only
    ax_validation_efficiency.set_ylim(Y_MIN, Y_MAX)
    
    # Add jittered individual data points for panel E (Validation Efficiency) with clipping and labels
    outliers_info_val = {"normal": 0, "below": 0, "above": 0}
    all_outliers_val = []
    
    for i, config_id in enumerate(df_paired_val.sort_values("treatment_effect_mean")["CONFIG_configId"].astype(str).values):
        config_data = df_analysis_val_processed[df_analysis_val_processed["CONFIG_configId"] == int(config_id)]
        
        for punishment_type in config_data["CONFIG_punishmentExists"].unique():
            subset = config_data[config_data["CONFIG_punishmentExists"] == punishment_type]
            
            # Add jitter to x-position to avoid overlap
            x_jitter = np.random.uniform(-0.15, 0.15, size=len(subset))
            x_pos = i + (0.2 if punishment_type == "With punishment" else -0.2) + x_jitter
            
            # Plot with clipping indicators and collect outliers
            normal, below, above, outliers = plot_with_clipping_and_labels(
                ax_validation_efficiency,
                x=x_pos,
                y=subset["itt_relative_efficiency"].values,
                color=validation_punishment_colors[punishment_type],
                marker=punishment_markers[punishment_type]
            )
            
            outliers_info_val["normal"] += normal
            outliers_info_val["below"] += below
            outliers_info_val["above"] += above
            all_outliers_val.extend(outliers)
    
    # Add numeric labels for outliers in panel E
    for x_pos, y_pos, actual_value, position in all_outliers_val:
        # Format the value with 1 decimal place
        value_str = f"{actual_value:.1f}"
        # Position the text slightly offset from the marker
        if position == 'above':
            ax_validation_efficiency.annotate(
                value_str, 
                xy=(x_pos, y_pos),
                xytext=(0, 5),  # 5 points above
                textcoords='offset points',
                ha='center', 
                va='bottom',
                fontsize=6,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.7)
            )
        else:  # below
            ax_validation_efficiency.annotate(
                value_str, 
                xy=(x_pos, y_pos),
                xytext=(0, -5),  # 5 points below
                textcoords='offset points',
                ha='center', 
                va='top',
                fontsize=6,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.7)
            )

    ax_validation_efficiency.legend(
        title='', loc='lower right', frameon=False, fontsize=legend_fontsize
    )

    # Panel F: Validation Effect - UNCHANGED
    df_paired_val_sorted = df_paired_val.sort_values("treatment_effect_mean")
    bar_colors_val = [validation_punishment_colors['Without punishment'] if x > 0 else validation_punishment_colors['With punishment']
                    for x in df_paired_val_sorted["treatment_effect_mean"]]

    sns.barplot(
        x="CONFIG_configId", y="treatment_effect_mean",
        data=df_paired_val_sorted,
        palette=bar_colors_val,
        order=df_paired_val_sorted["CONFIG_configId"].astype(str).values,
        ax=ax_validation_effect,
        errorbar="se"
    )

    ax_validation_effect.errorbar(
        x=range(len(df_paired_val_sorted)),
        y=df_paired_val_sorted["treatment_effect_mean"].values,
        yerr=(1.96 * df_paired_val_sorted["treatment_effect_se"]).values,
        linestyle="", color="black", linewidth=0.5, zorder=1000
    )

    # Add reference lines
    ax_learning_efficiency.axhline(
        y=np.clip(df_cluster_learn["itt_relative_efficiency"].mean(), Y_MIN, Y_MAX),
        color="black", linestyle="--", alpha=0.3, zorder=-10
    )
    ax_learning_effect.axhline(0, linestyle="--", color="black", alpha=0.3)
    ax_validation_efficiency.axhline(
        y=np.clip(df_analysis_val_processed["itt_relative_efficiency"].mean(), Y_MIN, Y_MAX),
        color="black", linestyle="--", alpha=0.3, zorder=-10
    )
    ax_validation_effect.axhline(0, linestyle="--", color="black", alpha=0.3)

    # Style all panels C through F
    for ax in [ax_learning_efficiency, ax_learning_effect, ax_validation_efficiency, ax_validation_effect]:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_linewidth(0.5)
        ax.spines['bottom'].set_linewidth(0.5)
        ax.yaxis.set_major_locator(MaxNLocator(6))
        ax.set_xlabel("")
        ax.tick_params(axis="both", which="major", labelsize=tick_fontsize)

    # Remove x-tick labels for efficiency panels
    ax_learning_efficiency.set_xticklabels([])
    ax_validation_efficiency.set_xticklabels([])

    # Set shared x-axis labels
    ax_learning_effect.set_xlabel("Learning Experiments", fontsize=label_fontsize, labelpad=8)
    ax_validation_effect.set_xlabel("Validation Experiments", fontsize=label_fontsize, labelpad=8)

    # Add panel labels
    labels = ['A', 'B', 'C', 'D', 'E', 'F']
    axes = [
        ax_coins, ax_normalized_efficiency,
        ax_learning_efficiency, ax_learning_effect,
        ax_validation_efficiency, ax_validation_effect
    ]

    for label, ax in zip(labels, axes):
        ax.text(0.02, 0.98, label, transform=ax.transAxes,
                fontsize=title_fontsize, fontweight='bold', 
                va='top', ha='left',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=0.1))

    # Fine-tune the layout with the new spacing
    plt.subplots_adjust(
        left=0.12,      # Left margin for y-axis labels
        right=0.95,     # Right margin
        top=0.95,       # Top margin
        bottom=0.08,    # Bottom margin for x-axis labels
        hspace=0.4      # This provides space for labels between other panels
    )

    # Add extra adjustment for paired panels
    for ax1, ax2 in [(ax_learning_efficiency, ax_learning_effect), 
                    (ax_validation_efficiency, ax_validation_effect)]:
        # Get the positions of both axes
        pos1 = ax1.get_position()
        pos2 = ax2.get_position()
        
        # Move the second axis up closer to the first
        new_pos2 = [pos2.x0, pos2.y0 + 0.05, pos2.width, pos2.height]  # Adjust the 0.05 to control spacing
        ax2.set_position(new_pos2)
        
    # Add I² statistics
    learn_het_stats = calc_q_i2(df_cluster_params.rename(
        columns={"estimate": "treatment_effect_mean", "se": "treatment_effect_se"}))

    val_het_stats = calc_q_i2(df_paired_val[["treatment_effect_mean", "treatment_effect_se"]])

    # Add I² annotations
    ax_learning_effect.text(0.98, 0.05, f'$I^2 = {learn_het_stats["i2"]}$',
                        transform=ax_learning_effect.transAxes,
                        fontsize=legend_fontsize, va='bottom', ha='right')
    ax_validation_effect.text(0.98, 0.05, f'$I^2 = {val_het_stats["i2"]}$',
                            transform=ax_validation_effect.transAxes,
                            fontsize=legend_fontsize, va='bottom', ha='right')

    # Set y-axis labels for efficiency and effect panels
    ax_learning_efficiency.set_ylabel("Normalized Efficiency", fontsize=label_fontsize)
    ax_learning_effect.set_ylabel("Punishment Effect", fontsize=label_fontsize)
    ax_validation_efficiency.set_ylabel("Normalized Efficiency", fontsize=label_fontsize)
    ax_validation_effect.set_ylabel("Punishment Effect", fontsize=label_fontsize)

    for ax in [ax_learning_efficiency, ax_learning_effect, ax_validation_efficiency, ax_validation_effect]:
        # Left-align the y-axis labels 
        ax.yaxis.set_label_coords(-0.075, 0.5)


    # Fine-tune the layout
    plt.subplots_adjust(
        left=0.12,      # Increased left margin for y-axis labels
        right=0.95,     # Reduced right margin
        top=0.95,       # Reduced top margin
        bottom=0.08,    # Slightly increased bottom margin for x-axis labels
        hspace=0.2      # Reduced vertical spacing between subplots
    )

    plt.savefig(fig_output_path, 
            dpi=300, 
            bbox_inches='tight',
            metadata={'Creator': 'Matplotlib'})

def fig3_prediction_viz(processed_data_dir, fig_output_path):
    def bootstrap_model_evaluation(prediction_column, df_validation_sample):
        rmse = np.sqrt(mean_squared_error(y_true=df_validation_sample["treatment_itt_efficiency"]*100, y_pred=df_validation_sample[prediction_column]*100))
        return rmse
    
    dict_perf_fig_labels = {
        "median_prolific_pred": "Median\nlayperson",
        "median_sspp_pred": "Median\nexpert",
        "woc_sspp_pred": "WOC\nexperts",
        "best_sspp_pred": "Best\nexpert",
        "xgb_prereg_pred": "XGB",
        "best_prolific_pred": "Best\nlayperson",
        "woc_prolific_pred": "WOC\nlaypeople",
        "mlp_prereg_pred": "MLP",
        "rf_prereg_pred": "RF",
        "ols_prereg_pred": "OLS",
        "elastic_prereg_pred": "E-Net"
        }


    # LOAD DATA 
    df_paired_val = pd.read_csv(processed_data_dir + "df_paired_val.csv")
    df_paired_learn = pd.read_csv(processed_data_dir + "df_paired_learn.csv")
    df_analysis_val = pd.read_csv(processed_data_dir + "df_analysis_val.csv")
    df_analysis_learn = pd.read_csv(processed_data_dir + "df_analysis_learn.csv")
    df_rounds_learn = pd.read_csv(processed_data_dir + "df_rounds_learn.csv")
    df_rounds_val = pd.read_csv(processed_data_dir + "df_rounds_val.csv")
    df_predictions = pd.read_csv(processed_data_dir + "prediction_survey.csv").query("prediction.between(-0.2,1.2)")

    df_paired_val["baseline"] = df_paired_learn["treatment_itt_efficiency"].mean()
    df_paired_val = (df_paired_val
                     .merge(df_predictions.query("source == 'prolific'").groupby("CONFIG_configId")["prediction"].mean().reset_index().rename(columns={"prediction":"woc_prolific_pred"}), on="CONFIG_configId", how="left")
                     .merge(df_predictions.query("source == 'sspp'").groupby("CONFIG_configId")["prediction"].mean().reset_index().rename(columns={"prediction":"woc_sspp_pred"}), on="CONFIG_configId", how="left")
                     )
    
    dict_model_perf_bootstrap = {}
    for model_label in ["ols_prereg_pred","rf_prereg_pred","xgb_prereg_pred","mlp_prereg_pred","elastic_prereg_pred", "woc_prolific_pred", "woc_sspp_pred", "baseline"]:
        dict_model_perf_bootstrap[model_label] = [bootstrap_model_evaluation(model_label, df_paired_val.sample(n=20, replace=True, random_state=x)) for x in range(1000)]
    


    # VISUALIZATION
    def predictive_scatterplot(axis, prediction_col, panel_label="", scatter_color='#0072B2'):
        # Define colors
        mean_line_color = '#666666'  # darker red
        identity_line_color = '#000000'  # dark gray
        fill_color = '#95D840'  # green
        
        # Plot mean line
        axis.axhline(100*df_paired_learn["treatment_itt_efficiency"].mean(), 
                    color=mean_line_color, 
                    linestyle="--", 
                    linewidth=1, 
                    label="Mean in the learning dataset",
                    zorder=1)
        
        # Plot identity line
        min_val = 100*df_paired_val["treatment_itt_efficiency"].min()
        max_val = 100*df_paired_val["treatment_itt_efficiency"].max()
        axis.plot([min_val, max_val], 
                [min_val, max_val], 
                linestyle="-", 
                color=identity_line_color, 
                linewidth=1, 
                label="Identity",
                zorder=2)
        
        axis.fill_between(x=[min_val, max_val],
                        y1=[min_val-(100*df_paired_learn["treatment_itt_efficiency"].mean()-min_val), max_val+(max_val-100*df_paired_learn["treatment_itt_efficiency"].mean())],
                        y2=100*df_paired_learn["treatment_itt_efficiency"].mean(), 
                        color=fill_color, 
                        alpha=0.25,
                        zorder=0)        
       
        # Modified scatter plot with filled circles and opacity
        axis.scatter(x=100*df_paired_val["treatment_itt_efficiency"], 
                    y=100*df_paired_val[prediction_col], 
                    facecolor=scatter_color,
                    edgecolor='none',
                    s=25,
                    alpha=0.6,
                    zorder=3)
        
        # Calculate statistics
        temp_r2 = 1 - np.sum((df_paired_val[prediction_col] - df_paired_val["treatment_itt_efficiency"])**2) / \
                np.sum((df_paired_val["baseline"] - df_paired_val["treatment_itt_efficiency"])**2)
        
        temp_rmse = np.sqrt(np.mean((df_paired_val[prediction_col]*100 - df_paired_val["treatment_itt_efficiency"]*100)**2))
        
        # Add statistics text with smaller font
        axis.text(0.55, 0.23, f'$R^2 = {temp_r2.round(2)}$', 
                transform=axis.transAxes, 
                fontsize=8, 
                fontweight='normal', 
                va='top', 
                ha='left')
        axis.text(0.55, 0.13, f'$RMSE = {temp_rmse.round(2)}$', 
                transform=axis.transAxes, 
                fontsize=8, 
                fontweight='normal', 
                va='top', 
                ha='left')
        
        # Add panel label
        axis.text(0.05, 0.95, panel_label, 
                transform=axis.transAxes, 
                fontsize=11, 
                fontweight='bold', 
                va='top', 
                ha='left')
        
        # Set shared axis limits
        axis.set_xlim(60, 100)
        axis.set_ylim(60, 100)


    # Create figure
    width_mm = 183
    height_mm = 120
    width_inches = width_mm / 25.4
    height_inches = height_mm / 25.4
    fig = plt.figure(figsize=(width_inches, height_inches), dpi=300)

    # Create GridSpec
    gs = GridSpec(2, 3, width_ratios=[1, 1, 1.2], height_ratios=[1, 1],
                hspace=0.4, wspace=0.5)

    # Initialize all axes
    ax1 = fig.add_subplot(gs[:, 2])
    ax2_1 = fig.add_subplot(gs[0, 0])
    ax2_2 = fig.add_subplot(gs[0, 1])
    ax2_3 = fig.add_subplot(gs[1, 0])
    ax2_4 = fig.add_subplot(gs[1, 1])

    ax = [ax2_1, ax2_2, ax2_3, ax2_4]

    # Define group colors - darker and more saturated
    group_colors = {
        'statistical': '#0072B2',  # Dark blue (kept)
        'experts': '#CCA97A',      # Dark orange (kept)
        'laypeople': '#E41A1C'     # Rich purple
    }


    # Create a color mapping for each model
    color_mapping = {
        'elastic_prereg_pred': group_colors['statistical'],
        'ols_prereg_pred': group_colors['statistical'],
        'rf_prereg_pred': group_colors['statistical'],
        'mlp_prereg_pred': group_colors['statistical'],
        'xgb_prereg_pred': group_colors['statistical'],
        'best_sspp_pred': group_colors['experts'],
        'woc_sspp_pred': group_colors['experts'],
        'median_sspp_pred': group_colors['experts'],
        'best_prolific_pred': group_colors['laypeople'],
        'woc_prolific_pred': group_colors['laypeople'],
        'median_prolific_pred': group_colors['laypeople']
    }

    # Calculate CIs and means
    ci_data = {}
    for model in dict_model_perf_bootstrap.keys():
        values = dict_model_perf_bootstrap[model]
        ci_data[model] = {
            'mean': np.mean(values),
            'ci_lower': np.percentile(values, 2.5),
            'ci_upper': np.percentile(values, 97.5)
        }

    # Create sorted order based on means
    order = pd.DataFrame(ci_data).filter(regex="prereg|woc").T.sort_values('mean', ascending=True).index
    bar_colors = [color_mapping[col] for col in order]

    # Create the bar plot
    sns.barplot(y="model", x="mean", 
            data=pd.DataFrame(ci_data).T.reset_index().rename(columns={"index":"model"}),
            order=order,
            palette=bar_colors,
            ax=ax1,
            ci=None)

    for idx, model in enumerate(order):
        ax1.errorbar(x=ci_data[model]['mean'], 
                    y=idx,  # Note: y and x are swapped for vertical orientation
                    xerr=[[ci_data[model]['mean'] - ci_data[model]['ci_lower']], 
                        [ci_data[model]['ci_upper'] - ci_data[model]['mean']]],
                    fmt='none',
                    color='black',
                    capsize=3)



    # Update y-tick labels with the proper names
    ax1.set_yticks(range(len(order)))
    ax1.set_yticklabels([dict_perf_fig_labels[model] for model in order], 
                        fontsize=8)

    # Style main bar plot
    ax1.set_ylabel("", fontsize=10, labelpad=10)
    ax1.set_xlabel("RMSE", fontsize=10, labelpad=10)
    ax1.tick_params(axis='both', which='major', labelsize=8, length=4, width=0.5)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_linewidth(0.5)
    ax1.spines['bottom'].set_linewidth(0.5)

    # Add baseline
    baseline_color = '#666666'  # darker red
    ax1.axvline(x=np.sqrt(mean_squared_error(y_true=df_paired_val["treatment_itt_efficiency"]*100, y_pred=df_paired_val["baseline"]*100)), 
                linestyle='--', color=baseline_color, 
                label="Mean in the learning dataset",
                linewidth=1)

    # Add panel letter "E"
    ax1.text(0.05, 1.02, "E", fontsize=11, fontweight='bold', transform=ax1.transAxes)

    # Create unified legend elements
    legend_elements = [
        Patch(facecolor=group_colors['statistical'], label='Statistical models'),
        Patch(facecolor=group_colors['experts'], label='Experts'),
        Patch(facecolor=group_colors['laypeople'], label='Laypeople'),
        Line2D([0], [0], color=baseline_color, linestyle="--", label='Mean in the learning dataset'),
        Line2D([0], [0], color='#000000', linestyle='-', label='Identity')
    ]

    # Add unified legend at the top of the figure
    fig.legend(handles=legend_elements, 
            loc='upper center',
            bbox_to_anchor=(0.5, 1.025),
            ncol=5,
            frameon=False,
            fontsize=8,
            borderaxespad=0,
            handlelength=1.5)

    # Calculate global min/max for shared axes
    # plot_order = ["elastic_prereg_pred", "ols_prereg_pred", "best_prolific_pred", 
    #               "best_sspp_pred", "woc_prolific_pred", "woc_sspp_pred", 
    #               "median_prolific_pred", "median_sspp_pred"]

    plot_order = ["elastic_prereg_pred", "ols_prereg_pred",
                "woc_sspp_pred", "woc_prolific_pred"]

    all_vals = []
    for col in plot_order:
        all_vals.extend(100*df_paired_val[col])
    all_vals.extend(100*df_paired_val["treatment_itt_efficiency"])
    global_min = min(all_vals)
    global_max = max(all_vals)

    # Add padding to limits
    padding = (global_max - global_min) * 0.05
    global_min -= padding
    global_max += padding

    # Style all scatter plots
    for idx, axi in enumerate(ax):
        predictive_scatterplot(axi, plot_order[idx], 
                            ["A", "B", "C", "D"][idx],
                            scatter_color=color_mapping[plot_order[idx]])
        
        # Set titles and style
        titles = ["E-Net", "OLS", 
                "Expert wisdom of crowds", "Layperson wisdom of crowds"]
        axi.set_title(titles[idx], fontsize=9, pad=8)
        
        # Style scatter plots
        axi.tick_params(axis='both', which='major', labelsize=8, length=3, width=0.5)
        axi.spines['top'].set_visible(False)
        axi.spines['right'].set_visible(False)
        axi.spines['left'].set_linewidth(0.5)
        axi.spines['bottom'].set_linewidth(0.5)
        
        # Remove labels from inner axes
        if idx not in [6, 7]:
            axi.set_xlabel('')
        if idx % 2 != 0:
            axi.set_ylabel('')

    # Adjust layout with updated spacing
    plt.subplots_adjust(left=0.15, right=0.95, bottom=0.12, top=0.92, wspace=0.2)

    # Add labels with adjusted positioning
    scatter_center = 0.4
    fig.supxlabel("True Efficiency", fontsize=10, x=scatter_center, y=0.025)
    fig.text(0.07, 0.5, "Predicted Efficiency", fontsize=10, rotation=90, va='center')

    plt.savefig(fig_output_path, 
            dpi=300, 
            bbox_inches='tight',
            metadata={'Creator': 'Matplotlib'})
    


def get_featimp_plot(df_featimp, model, model_label, df_paired_learn, feature_cols, fig_output_path,display_model_label=False):
    df_featimp["pct_increase_in_error"] = 100 * (df_featimp["permuted_performance"] - df_featimp["baseline"]) / df_featimp["baseline"]

    # Define columns and labels for SHAP analysis
    OOS_PRED_COLUMNS_PUNISHPARAMS = [
        'CONFIG_playerCount', 'CONFIG_numRounds', 'CONFIG_showNRounds', 'CONFIG_MPCR',
        'CONFIG_allOrNothing', 'CONFIG_chat', 'CONFIG_defaultContribProp', 'CONFIG_rewardExists',
        'CONFIG_showOtherSummaries', 'CONFIG_showPunishmentId', 'CONFIG_punishmentCost',
        'CONFIG_punishmentTech'
    ]

    DICT_COLUMN_LABELS = {
    'CONFIG_playerCount': 'Group Size',
    'CONFIG_numRounds': 'Game Length',
    'CONFIG_showNRounds': 'Horizon Knowledge',
    'CONFIG_MPCR': 'Return Rate (MPCR)',
    'CONFIG_allOrNothing': 'Contribution Type',
    'CONFIG_chat': 'Communication',
    'CONFIG_defaultContribProp': 'Contribution Framing',
    'CONFIG_rewardExists': 'Reward',
    'CONFIG_showOtherSummaries': 'Peer Outcome Visibility',
    'CONFIG_showPunishmentId': 'Actor Anonymity',
    'CONFIG_punishmentCost': 'Peer Incentive Cost',
    'CONFIG_punishmentTech': 'Punishment Technology'}

    # Style setup
    plt.style.use('default')
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42
    matplotlib.rcParams['font.sans-serif'] = ['Arial']
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['axes.facecolor'] = 'white'
    matplotlib.rcParams['figure.facecolor'] = 'white'
    matplotlib.rcParams['grid.alpha'] = 0.0

    # Define categories and colors
    category_colors = {
        'Game Structure': '#2166AC',         # Blue
        'Contribution Structure': '#92C5DE',    # Light blue
        'Social Information': '#D6604D',        # Red
        'Incentive Mechanisms': '#F4A582'       # Light red
    }

    # Create mapping of old to new feature names and their categories
    feature_info = {
        '# of players': {'new_name': 'Group Size', 'category': 'Game Structure'},
        '# of rounds': {'new_name': 'Game Length', 'category': 'Game Structure'},
        'Visibility of # of rounds': {'new_name': 'Horizon Knowledge', 'category': 'Game Structure'},
        'Marginal per capita return': {'new_name': 'Return Rate (MPCR)', 'category': 'Game Structure'},
        '"All or Nothing" contributions': {'new_name': 'Contribution Type', 'category': 'Contribution Structure'},
        'Default contribution vs withdrawal': {'new_name': 'Contribution Framing', 'category': 'Contribution Structure'},
        'Ability to chat': {'new_name': 'Communication', 'category': 'Social Information'},
        'Peer outcome visibility': {'new_name': 'Peer Outcome Visibility', 'category': 'Social Information'},
        'Punisher/rewarder anonymity': {'new_name': 'Actor Anonymity', 'category': 'Social Information'},
        'Ability to reward': {'new_name': 'Reward', 'category': 'Incentive Mechanisms'},
        'Punishment cost': {'new_name': 'Peer Incentive Cost', 'category': 'Incentive Mechanisms'},
        'Punishment effectiveness': {'new_name': 'Punishment Technology', 'category': 'Incentive Mechanisms'}
    }


    # Create final figure
    width_mm = 183  # Nature full width
    height_mm = 120
    width_inches = width_mm / 25.4
    height_inches = height_mm / 25.4

    fig = plt.figure(figsize=(width_inches, height_inches), dpi=300)
    gs = plt.GridSpec(1, 2, width_ratios=[1, 1], wspace=0.1)  # Reduced wspace for tighter alignment
    ax_left = fig.add_subplot(gs[0])
    ax_right = fig.add_subplot(gs[1])

    # Panel A: Feature Importance Plot
    df_plot = df_featimp.query("model == @model_label").copy()
    df_plot['new_name'] = df_plot['feature'].map({k: v['new_name'] for k, v in feature_info.items()})
    df_plot['category'] = df_plot['feature'].map({k: v['category'] for k, v in feature_info.items()})

    # Get the order based on the mean values
    means = df_plot.groupby('new_name')['pct_increase_in_error'].mean()
    ordered_features = means.sort_values(ascending=False).index

    # Create bar plot with adjusted error bars in the left panel
    bars = sns.barplot(
        x="pct_increase_in_error",
        y="new_name",
        data=df_plot,
        order=ordered_features,
        ax=ax_left,
        estimator='mean',
        errorbar=('ci', 68),
        capsize=0.2,
        errwidth=1
    )

    # Color the bars according to category
    for i, feature in enumerate(ordered_features):
        category = df_plot[df_plot['new_name'] == feature]['category'].iloc[0]
        bars.patches[i].set_facecolor(category_colors[category])

    # Add reference line
    ax_left.axvline(x=0, 
                    linestyle="--", 
                    color="#666666",
                    linewidth=0.8,
                    zorder=0)

    # Style Panel A
    ax_left.spines['top'].set_visible(False)
    ax_left.spines['right'].set_visible(False)
    ax_left.spines['left'].set_linewidth(0.5)
    ax_left.spines['bottom'].set_linewidth(0.5)

    # Adjust labels and ticks for Panel A
    ax_left.tick_params(axis="both", which='major', labelsize=9, length=3, width=0.5)
    ax_left.set_ylabel("")
    ax_left.set_xlabel("Feature Importance\n(% increase in prediction RMSE)", 
                    fontsize=10, 
                    labelpad=10)

    # Format x-axis as percentage
    ax_left.xaxis.set_major_formatter(PercentFormatter(xmax=100))

    # Create legend for Panel A
    legend_elements = [Patch(facecolor=color, label=cat)
                    for cat, color in category_colors.items()]
    ax_left.legend(handles=legend_elements,
                loc='lower right',
                frameon=False,
                fontsize=8,
                ncol=1)

    # Panel B: SHAP Plot
    background_data = df_paired_learn[feature_cols].astype(float).values
    masker = shap.maskers.Independent(background_data)

    def model_wrapper(x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        return model.predict(x)

    shap_explainer = shap.Explainer(
        model=model_wrapper,
        masker=masker,
        feature_names=feature_cols
    )

    shap_values = shap_explainer(df_paired_learn[feature_cols].astype(float).values)

    # Get the original feature names in the SHAP data
    plot_features = [f for f in feature_cols if f != 'control_itt_efficiency']
    original_feature_names = [DICT_COLUMN_LABELS[x] for x in plot_features]
    
    feature_name_to_idx = {name: idx for idx, name in enumerate(original_feature_names)}
    ordered_features_filtered = [f for f in ordered_features if f in original_feature_names]
    
    # Sort indices according to the ordered features (reversed as in original code)
    sort_indices = [feature_name_to_idx[feature] for feature in ordered_features_filtered[::-1]]
    
    # Extract indices from ALL_FEATURES corresponding to plot_features
    plot_feature_indices = [plot_features.index(f) for f in plot_features]
    
    # Map from original feature order to shap_values columns
    shap_plot_indices = [plot_features.index(f) for f in plot_features]  # order as in plot_features
    # Now reorder these indices according to sort_indices
    shap_reorder_indices = [shap_plot_indices[i] for i in sort_indices]
    


    # Sort SHAP values and data according to Panel A's order
    shap_vals = shap_values.values[:, [plot_features.index(f) for f in plot_features]][:, shap_reorder_indices]
    data_for_shap = background_data[:, [feature_cols.index(f) for f in plot_features]][:, shap_reorder_indices]

    # Create the SHAP plot in the right panel
    plt.sca(ax_right)
    shap.summary_plot(
        shap_vals,
        data_for_shap,
        plot_type="dot",
        feature_names=ordered_features_filtered[::-1],
        show=False,
        alpha=0.5,
        sort=False
    )

    # Remove y-axis labels from Panel B and align with Panel A
    ax_right.set_yticklabels([])
    ax_right.set_ylabel('')
    ax_right.set_ylim(ax_left.get_ylim())

    # Match font sizes
    ax_right.tick_params(axis='both', which='major', labelsize=9)
    ax_right.set_xlabel("SHAP Value\n(impact on prediction)", fontsize=10, labelpad=10)

    # Add panel labels
    ax_left.text(-0.1, 1.02, "A", transform=ax_left.transAxes, 
                fontsize=11, fontweight='bold')
    ax_right.text(-0.1, 1.02, "B", transform=ax_right.transAxes,
                fontsize=11, fontweight='bold')

    if display_model_label:
        fig.suptitle(f'Model: {model_label}', fontsize=16)

    # Adjust layout and save figure 
    plt.tight_layout()
    plt.savefig(fig_output_path, 
            dpi=300, 
            bbox_inches='tight',
            metadata={'Creator': 'Matplotlib'})


def fig4_feature_importance_viz(processed_data_dir, hpo_json_filepath, fig_output_path, model_key, model_label, display_model_label=False):
    # LOAD DATA 
    df_paired_val = pd.read_csv(processed_data_dir + "df_paired_val.csv")
    df_paired_learn = pd.read_csv(processed_data_dir + "df_paired_learn.csv")
    df_analysis_val = pd.read_csv(processed_data_dir + "df_analysis_val.csv")
    df_analysis_learn = pd.read_csv(processed_data_dir + "df_analysis_learn.csv")
    df_rounds_learn = pd.read_csv(processed_data_dir + "df_rounds_learn.csv")
    df_rounds_val = pd.read_csv(processed_data_dir + "df_rounds_val.csv")
    df_predictions = pd.read_csv(processed_data_dir + "prediction_survey.csv").query("prediction.between(-0.2,1.2)")

    dict_fitted_models = get_models(hpo_json_filepath=hpo_json_filepath, 
                                        df_paired_learn=df_paired_learn,
                                        feature_cols=PREDICTION_FEATURE_COLS,
                                        target_col="treatment_itt_efficiency",
                                        fitted=True)
    
    dict_unfitted_models = get_models(hpo_json_filepath=hpo_json_filepath, 
                                        df_paired_learn=df_paired_learn,
                                        feature_cols=PREDICTION_FEATURE_COLS,
                                        target_col="treatment_itt_efficiency",
                                        fitted=False)
    
    oos_ols_featimp_prereg = oos_permutation_feature_importance(dict_unfitted_models["ols"], df_paired_learn, df_paired_val, PREDICTION_FEATURE_COLS, "treatment_itt_efficiency", "OLS", n_iterations=30)
    oos_rf_featimp_prereg = oos_permutation_feature_importance(dict_unfitted_models["rf"], df_paired_learn, df_paired_val, PREDICTION_FEATURE_COLS, "treatment_itt_efficiency", "RF", n_iterations=30)
    oos_xgb_featimp_prereg = oos_permutation_feature_importance(dict_unfitted_models["xgb"], df_paired_learn, df_paired_val, PREDICTION_FEATURE_COLS, "treatment_itt_efficiency", "XGB", n_iterations=30)
    oos_mlp_featimp_prereg = oos_permutation_feature_importance(dict_unfitted_models["mlp"], df_paired_learn, df_paired_val, PREDICTION_FEATURE_COLS, "treatment_itt_efficiency", "MLP", n_iterations=30)
    oos_enet_featimp_prereg = oos_permutation_feature_importance(dict_unfitted_models["enet"], df_paired_learn, df_paired_val, PREDICTION_FEATURE_COLS, "treatment_itt_efficiency", "E-net", n_iterations=30)

    oos_master_featimp_prereg = pd.concat([oos_ols_featimp_prereg, oos_xgb_featimp_prereg, oos_enet_featimp_prereg, oos_rf_featimp_prereg, oos_mlp_featimp_prereg], ignore_index = True)

    oos_master_featimp_prereg["feature"] = oos_master_featimp_prereg["feature"].map({'CONFIG_playerCount':"# of players", 
    'CONFIG_numRounds':"# of rounds",
    'CONFIG_showNRounds':"Visibility of # of rounds", 
    'CONFIG_MPCR':"Marginal per capita return",
    'CONFIG_allOrNothing':'"All or Nothing" contributions', 
    'CONFIG_chat':"Ability to chat", 
    'CONFIG_defaultContribProp':"Default contribution vs withdrawal",
    'CONFIG_rewardExists':"Ability to reward", 
    'CONFIG_showOtherSummaries':"Peer outcome visibility",
    'CONFIG_showPunishmentId':"Punisher/rewarder anonymity",
    'CONFIG_punishmentCost':"Punishment cost",
    'CONFIG_punishmentTech':"Punishment effectiveness",
    "control_itt_efficiency":'Efficiency under control ("no punishment")'
    })

    get_featimp_plot(df_featimp=oos_master_featimp_prereg, model=dict_fitted_models[model_key], model_label=model_label, 
                     df_paired_learn=df_paired_learn, feature_cols=PREDICTION_FEATURE_COLS, fig_output_path=fig_output_path, display_model_label=display_model_label)
    

def fig5_shap_viz(processed_data_dir, hpo_json_filepath, fig_output_path):
     # LOAD DATA 
    df_paired_val = pd.read_csv(processed_data_dir + "df_paired_val.csv")
    df_paired_learn = pd.read_csv(processed_data_dir + "df_paired_learn.csv")
    df_analysis_val = pd.read_csv(processed_data_dir + "df_analysis_val.csv")
    df_analysis_learn = pd.read_csv(processed_data_dir + "df_analysis_learn.csv")
    df_rounds_learn = pd.read_csv(processed_data_dir + "df_rounds_learn.csv")
    df_rounds_val = pd.read_csv(processed_data_dir + "df_rounds_val.csv")
    df_predictions = pd.read_csv(processed_data_dir + "prediction_survey.csv").query("prediction.between(-0.2,1.2)")

    elastic_prereg = get_models(hpo_json_filepath=hpo_json_filepath, 
                                        df_paired_learn=df_paired_learn,
                                        feature_cols=PREDICTION_FEATURE_COLS,
                                        target_col="treatment_itt_efficiency",
                                        fitted=True)["enet"]
    
    background_data = df_paired_learn[PREDICTION_FEATURE_COLS].astype(float).values
    masker = shap.maskers.Independent(background_data)

    def model_wrapper(x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        return elastic_prereg.predict(x)

    shap_explainer = shap.Explainer(
        model=model_wrapper,
        masker=masker,
        feature_names=PREDICTION_FEATURE_COLS
    )

    shap_values = shap_explainer(df_paired_learn[PREDICTION_FEATURE_COLS].astype(float).values)

    # Style setup
    plt.style.use('default')
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42
    matplotlib.rcParams['font.sans-serif'] = ['Arial']
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['axes.facecolor'] = 'white'
    matplotlib.rcParams['figure.facecolor'] = 'white'
    matplotlib.rcParams['grid.alpha'] = 0.0

    # Create figure with adjusted spacing (no Panel E)
    width_mm = 183
    height_mm = 160  # Adjust height to fit only 2 rows of panels
    width_inches = width_mm / 25.4
    height_inches = height_mm / 25.4

    fig = plt.figure(figsize=(width_inches, height_inches), dpi=300)
    gs = plt.GridSpec(2, 2, height_ratios=[1, 1], hspace=0.5, wspace=0.4)  # Only 2 rows for Panels A, B, C, and D

    # Create all axes
    ax_game_length_1 = fig.add_subplot(gs[0, 0])
    ax_game_length_2 = fig.add_subplot(gs[0, 1])
    ax_interact_1 = fig.add_subplot(gs[1, 0])
    ax_interact_2 = fig.add_subplot(gs[1, 1])

    # Panel A & B setup: Game Length
    colors_AB = {'peer_visible': '#E69F00', 'peer_hidden': '#0072B2'}
    markers_AB = {'peer_visible': 'o', 'peer_hidden': 's'}

    for idx, (ax, comm_enabled) in enumerate([(ax_game_length_1, 0), (ax_game_length_2, 1)]):
        for peer_visible, label in [(0, 'Peer Feedback Hidden'), (1, 'Peer Feedback Visible')]:
            mask = ((shap_values[:, "CONFIG_chat"].data == comm_enabled) &
                    (shap_values[:, "CONFIG_showOtherSummaries"].data == peer_visible))
            
            ax.scatter(shap_values[:, "CONFIG_numRounds"].data[mask],
                    shap_values[:, "CONFIG_numRounds"].values[mask],
                    color=colors_AB['peer_visible' if peer_visible else 'peer_hidden'],
                    marker=markers_AB['peer_visible' if peer_visible else 'peer_hidden'],
                    s=40, alpha=0.7, label=label)
        ax.set_title(f'Peer Communication {"Enabled" if comm_enabled else "Disabled"}', fontsize=10, pad=10)
        ax.set_xlabel('Game Length', fontsize=9)

    # Set shared y-axis limits and ticks for Panels A & B
    y_min_AB, y_max_AB = min(ax_game_length_1.get_ylim()[0], ax_game_length_2.get_ylim()[0]), max(ax_game_length_1.get_ylim()[1], ax_game_length_2.get_ylim()[1])
    ax_game_length_1.set_ylim(y_min_AB, y_max_AB)
    ax_game_length_2.set_ylim(y_min_AB, y_max_AB)
    ax_game_length_1.set_ylabel('SHAP Value', fontsize=9)

    # Legend for Panels A & B, placed inside Panel A
    handles_AB = [
        Line2D([0], [0], marker=markers_AB['peer_hidden'], color=colors_AB['peer_hidden'],
            label='Peer Outcomes Hidden', markersize=8, linestyle='None'),
        Line2D([0], [0], marker=markers_AB['peer_visible'], color=colors_AB['peer_visible'],
            label='Peer Outcomes Visible', markersize=8, linestyle='None')
    ]
    ax_game_length_1.legend(handles=handles_AB, loc='upper right', frameon=False, fontsize=8)

    # Panel C & D setup: Contribution Framing
    colors_CD = {'Variable': '#7570B3', 'All-or-nothing': '#E7298A'}
    markers_CD = {'Variable': 'D', 'All-or-nothing': 'v'}
    linestyles_CD = {'Variable': '-.', 'All-or-nothing': ':'}

    def plot_interaction(ax, peer_outcome_val, title):
        for cont_type, label in [(0, 'Variable contribution'), (1, 'All-or-nothing contribution')]:
            shap_values_opt_in = shap_values[:, "CONFIG_defaultContribProp"].values[
                (shap_values[:, "CONFIG_showOtherSummaries"].data == peer_outcome_val) & 
                (shap_values[:, "CONFIG_allOrNothing"].data == cont_type) &
                (shap_values[:, "CONFIG_defaultContribProp"].data == 0)
            ].mean()
            
            shap_values_opt_out = shap_values[:, "CONFIG_defaultContribProp"].values[
                (shap_values[:, "CONFIG_showOtherSummaries"].data == peer_outcome_val) & 
                (shap_values[:, "CONFIG_allOrNothing"].data == cont_type) &
                (shap_values[:, "CONFIG_defaultContribProp"].data == 1)
            ].mean()
            
            ax.plot([0, 1], [shap_values_opt_in, shap_values_opt_out],
                    color=colors_CD[label.split()[0]],
                    linestyle=linestyles_CD[label.split()[0]],
                    marker=markers_CD[label.split()[0]],
                    markersize=8,
                    linewidth=2,
                    label=label)
        ax.set_xticks([0, 1])
        ax.set_xticklabels(['Opt-in', 'Opt-out'], fontsize=9)
        ax.set_title(title, fontsize=10, pad=10)
        ax.axhline(y=0, color='grey', linestyle='-', linewidth=0.5, alpha=0.3)

    plot_interaction(ax_interact_1, 0, "Peer Outcomes Hidden")
    plot_interaction(ax_interact_2, 1, "Peer Outcomes Visible")

    # Set shared y-axis limits and ticks for Panels C & D
    y_min_CD, y_max_CD = min(ax_interact_1.get_ylim()[0], ax_interact_2.get_ylim()[0]), max(ax_interact_1.get_ylim()[1], ax_interact_2.get_ylim()[1])
    ax_interact_1.set_ylim(y_min_CD, y_max_CD)
    ax_interact_2.set_ylim(y_min_CD, y_max_CD)
    ax_interact_1.set_ylabel("SHAP Value", fontsize=9)

    # Add x-axis labels for Panels C & D
    ax_interact_1.set_xlabel("Contribution Framing", fontsize=9)
    ax_interact_2.set_xlabel("Contribution Framing", fontsize=9)

    # Legend for Panels C & D, placed inside Panel C
    handles_CD = [
        Line2D([0], [0], color=colors_CD['Variable'], linestyle=linestyles_CD['Variable'],
            marker=markers_CD['Variable'], label='Variable contribution'),
        Line2D([0], [0], color=colors_CD['All-or-nothing'], linestyle=linestyles_CD['All-or-nothing'],
            marker=markers_CD['All-or-nothing'], label='All-or-nothing contribution')
    ]
    ax_interact_1.legend(handles=handles_CD, loc='upper left', frameon=False, fontsize=8)

    # Add panel labels and style all axes
    for idx, ax in enumerate([ax_game_length_1, ax_game_length_2, ax_interact_1, ax_interact_2]):
        ax.text(-0.1, 1.05, chr(65 + idx), transform=ax.transAxes, fontsize=11, fontweight='bold')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    # Apply tight_layout for final adjustments
    plt.tight_layout()
    plt.savefig(fig_output_path, 
            dpi=300, 
            bbox_inches='tight',
            metadata={'Creator': 'Matplotlib'})