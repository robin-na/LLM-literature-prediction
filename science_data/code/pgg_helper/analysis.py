# Standard library imports
import random
import json
import copy

# Third-party scientific computing
import numpy as np
import pandas as pd
from scipy.stats import chi2

# Machine learning imports
from sklearn.model_selection import cross_val_predict, KFold
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error

# ML Models
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import Lasso, ElasticNet, LinearRegression
from sklearn.dummy import DummyRegressor
from xgboost import XGBRegressor

# Deep learning
import keras
from scikeras.wrappers import KerasRegressor

# Optimization
from skopt import gp_minimize
from skopt.space import Real, Integer, Categorical

# Set random seed for reproducibility
keras.utils.set_random_seed(2023)
np.random.seed(2023)
random.seed(2023)



def calc_q_i2(df_effect_sizes):
    n = len(df_effect_sizes)
    df_effect_sizes["weight"] = 1 / df_effect_sizes["treatment_effect_se"]**2
    weighted_effect_mean = ((df_effect_sizes["weight"] * df_effect_sizes["treatment_effect_mean"]) / df_effect_sizes["weight"].sum()).sum()
    
    cochran_q = (df_effect_sizes["weight"] * (df_effect_sizes["treatment_effect_mean"] - weighted_effect_mean)**2).sum()
    
    i2 = (cochran_q - (n-1)) / cochran_q
    
    
    return {"Q":cochran_q.round(2), "Q_pval":(1 - chi2.cdf(abs(cochran_q), df=n-1)).round(3), "Q_dof":n-1, "i2":i2.round(2)}

def get_keras_mlp(n_layers, n_units_per_layer, dropout_rate, meta):
    # note that meta is a special argument that will be
    # handed a dict containing input metadata
    X_shape_ = meta["X_shape_"]

    model = keras.models.Sequential()
    model.add(keras.layers.Input(X_shape_[1:]))
    # model.add(keras.layers.Dropout(rate=dropout_rate))
    
    for _ in range(n_layers-1):
        model.add(keras.layers.Dense(units=n_units_per_layer, activation="relu"))
        model.add(keras.layers.Dropout(rate=dropout_rate))
    
    model.add(keras.layers.Dense(1))

    return model
    
def skopt_param_optimization_kfold(
    model_label, n_calls, df_paired, feature_cols, outcome_col, n_folds, metric, scaled=False, interactions=False, random_seed=None, n_jobs=-1
):
    def objective(params):
        if model_label == "RF":
            estimator = RandomForestRegressor(
                max_depth=params[0],
                min_samples_leaf=params[1],
                random_state=random_seed
            )
        elif model_label == "XGB":
            estimator = XGBRegressor(
                n_estimators=params[0],
                max_depth=params[1],
                gamma=params[2],
                random_state=random_seed
            )
        elif model_label == "MLP":
            estimator = MLPRegressor(
                hidden_layer_sizes=(params[1],) * params[0],
                alpha=params[2],
                max_iter=200,
                random_state=random_seed
            )
        elif model_label == "LASSO":
            estimator = Lasso(
                alpha=params[0],
                random_state=random_seed
            )
        elif model_label == "KERAS_MLP":
            estimator = KerasRegressor(
                model=get_keras_mlp,loss="mean_squared_error", metrics=["mean_squared_error"],
                n_layers=params[0],
                n_units_per_layer=params[1],
                optimizer=keras.optimizers.Adam(learning_rate=params[2]),
                dropout_rate=params[3],
                epochs=params[4],
                batch_size=32,
                verbose=0,
                random_state=random_seed
            )
        elif model_label == "ELASTICNET":
            estimator = ElasticNet(
                alpha=params[0],
                l1_ratio=params[1],
                random_state=random_seed
            )
        else:
            raise ValueError(f"Unknown model label: {model_label}")
        
        cv  = KFold(n_splits=n_folds, shuffle=True, random_state=random_seed)

        pipeline = Pipeline(steps=[])
        if scaled:
            pipeline.steps.append(("scaler", StandardScaler()))
        if interactions:
            # pipeline.steps.append(("interactions", InteractionTransformer()))
            pipeline.steps.append(("interactions", PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)))
        pipeline.steps.append(("estimator", estimator))

        predictions = cross_val_predict(
        pipeline,
        X=df_paired[feature_cols],
        y=df_paired[outcome_col],
        cv=cv,
        n_jobs=n_jobs,
    )

        means = cross_val_predict(
            Pipeline(steps=[("dummy", DummyRegressor(strategy="mean"))]),
            X=df_paired[feature_cols],
            y=df_paired[outcome_col],
            cv=cv,
            n_jobs=n_jobs,
        )

        r2_score = 1 - np.sum((predictions - df_paired[outcome_col]) ** 2) / np.sum((means - df_paired[outcome_col]) ** 2)
        mse_score = np.mean((predictions - df_paired[outcome_col]) ** 2)

        return {"r2": -r2_score, "mse": mse_score}[metric]

    # Define the search space
    if model_label == "RF":
        space = [
            Integer(2, 6, name="max_depth"),
            Integer(1, 20, name="min_samples_leaf")
        ]
    elif model_label == "XGB":
        space = [
            Integer(2, 15, name="n_estimators"),
            Integer(2, 6, name="max_depth"),
            Real(0.0, 1.0, name="gamma")
        ]
    elif model_label == "MLP":
        space = [
            Integer(1, 5, name="n_layers"),
            Integer(20, 80, name="n_neurons"),
            Real(0.0001, 0.1, "log-uniform", name="alpha")
        ]
    elif model_label == "LASSO":
        space = [
            Real(0.001, 0.1, "log-uniform", name="alpha")
        ]
    elif model_label == "KERAS_MLP":
        space = [
            Integer(2, 5, name="n_layers"),
            Integer(20, 80, name="n_units_per_layer"),
            Real(1e-6, 1e-1, "log-uniform", name="learning_rate"),
            Real(0.0, 0.3, name="dropout_rate"),
            Categorical([25, 50, 100], name="epochs")
        ]
    elif model_label == "ELASTICNET":
        space = [
            Real(0.001, 0.1, "log-uniform", name="alpha"),
            Real(0.0, 1.0, name="l1_ratio")
        ]
    else:
        raise ValueError(f"Unknown model label: {model_label}")

    # Run the optimization
    result = gp_minimize(
        objective,
        space,
        n_calls=n_calls,
        random_state=random_seed,
        n_jobs=-1,
        verbose=False
    )

    # Prepare the output
    best_params = dict(zip([dim.name for dim in space], result.x))
    best_score = -result.fun if metric == "r2" else result.fun

    output = {
        "model_label": model_label,
        "feature_cols": feature_cols,
        "target_col": outcome_col,
        "scaled": scaled,
        "interactions": interactions,
        "random_seed": random_seed,
        metric: best_score,
        **best_params
    }

    return output

def run_hpo(df_paired_learn, feature_cols, outcome_col, hpo_config_output_path):
    keras.utils.set_random_seed(2023)
    np.random.seed(2023)
    random.seed(2023)


    print("Running RF HPO...")
    hpo_rf = skopt_param_optimization_kfold("RF", n_calls=50, 
                            df_paired=df_paired_learn, 
                            feature_cols=feature_cols, 
                            outcome_col=outcome_col,
                                                    n_folds=10, scaled=False, interactions=False, random_seed=2023, metric="mse")
    print("Running XGB HPO...")
    hpo_xgb = skopt_param_optimization_kfold("XGB", n_calls=50, 
                            df_paired=df_paired_learn, 
                            feature_cols=feature_cols, 
                            outcome_col=outcome_col,
                                                    n_folds=10, scaled=False, interactions=False, random_seed=2023, metric="mse")

    print("Running MLP HPO...")
    hpo_mlp = skopt_param_optimization_kfold("KERAS_MLP", n_calls=50, 
                            df_paired=df_paired_learn, 
                            feature_cols=feature_cols, 
                            outcome_col=outcome_col,
                                                    n_folds=10, scaled=True, interactions=False, random_seed=2023, metric="mse")
    print("Running ENet HPO...")
    hpo_elastic = skopt_param_optimization_kfold("ELASTICNET", n_calls=50, 
                            df_paired=df_paired_learn, 
                            feature_cols=feature_cols, 
                            outcome_col=outcome_col,
                                                    n_folds=10, scaled=True, interactions=True, random_seed=2023, metric="mse", n_jobs=1)
    
    json.dump(obj={"RF":hpo_rf, "XGB":hpo_xgb, "MLP":hpo_mlp, "ELASTIC":hpo_elastic},
              fp=open(hpo_config_output_path, "w"), default=int)
    
def get_models(hpo_json_filepath, df_paired_learn, feature_cols, target_col, fitted=False):
    prereg_hpo_params = json.load(open(hpo_json_filepath, "r"))

    ols_prereg = Pipeline(steps=[("estimator", LinearRegression())])

    rf_prereg = Pipeline(steps=[("estimator", RandomForestRegressor(max_depth=prereg_hpo_params["RF"]["max_depth"],
                                                                    min_samples_leaf=prereg_hpo_params["RF"]["min_samples_leaf"],
                                                                    random_state=prereg_hpo_params["RF"]["random_seed"]))])

    xgb_prereg = Pipeline(steps=[("estimator", XGBRegressor(n_estimators=prereg_hpo_params["XGB"]["n_estimators"],
                                                            max_depth=prereg_hpo_params["XGB"]["max_depth"],
                                                            gamma=prereg_hpo_params["XGB"]["gamma"],
                                                            random_state=prereg_hpo_params["XGB"]["random_seed"]))])

    mlp_prereg = Pipeline(steps=[("scaler", StandardScaler()),
                                 ("estimator", KerasRegressor(
        model=get_keras_mlp,loss="mean_squared_error", metrics=["mean_squared_error"],
        n_layers=prereg_hpo_params["MLP"]["n_layers"],
        n_units_per_layer=prereg_hpo_params["MLP"]["n_units_per_layer"],
        optimizer=keras.optimizers.Adam(learning_rate=prereg_hpo_params["MLP"]["learning_rate"]),
        dropout_rate=prereg_hpo_params["MLP"]["dropout_rate"],
        epochs=prereg_hpo_params["MLP"]["epochs"],
        batch_size=32,
        verbose=0,
        random_state=prereg_hpo_params["MLP"]["random_seed"]))])

    elastic_prereg = Pipeline(steps=[("scaler", StandardScaler()),
                                    #  ("interactions", InteractionTransformer()),
                                     ("interactions", PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)),
                                     ("estimator", ElasticNet(alpha=prereg_hpo_params["ELASTIC"]["alpha"], 
                                                              l1_ratio=prereg_hpo_params["ELASTIC"]["l1_ratio"],
                                                              random_state=prereg_hpo_params["ELASTIC"]["random_seed"]))])



    if fitted:
        for pipeline in [ols_prereg, rf_prereg, xgb_prereg, mlp_prereg, elastic_prereg]:
            pipeline.fit(X=df_paired_learn[feature_cols], y=df_paired_learn[target_col])
        
    return {"ols":ols_prereg, "enet":elastic_prereg, "rf":rf_prereg, "mlp":mlp_prereg, "xgb":xgb_prereg}



def oos_permutation_feature_importance(pipeline, df_train, df_test, features, outcome, model_label, n_iterations=10):
        model = copy.deepcopy(pipeline).fit(X=df_train[features], y=df_train[outcome])
        
        baseline = np.sqrt(mean_squared_error(model.predict(df_test[features])*100, df_test[outcome]*100))
        
        iteration_list = []
        permuted_performance_list = []
        feature_list = []
        
        for feature in features:
            iteration_list += list(range(n_iterations))
            feature_list += [feature]*n_iterations
            
            shuffled_performance = []
            df_shuffle = copy.deepcopy(df_test)
            for shuffle_iteration in range(n_iterations):
                df_shuffle[feature] = np.random.RandomState(seed=shuffle_iteration).permutation(df_shuffle[feature].values)
                shuffled_performance.append(np.sqrt(mean_squared_error(model.predict(df_shuffle[features])*100, df_test[outcome]*100)))
                
            permuted_performance_list += shuffled_performance
        
        df_featimp = pd.DataFrame({"baseline":baseline, "feature":feature_list, "iteration":iteration_list, "permuted_performance":permuted_performance_list})
        df_featimp["importance"] = df_featimp["permuted_performance"] / df_featimp["baseline"]
        df_featimp["model"] = model_label
        
        return df_featimp