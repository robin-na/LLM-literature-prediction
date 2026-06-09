# Reproduction materials for "Integrative Experiments Identify How Punishment Impacts Welfare in Public Goods Games" 

This repository contains the instructions and code required to reproduce the analyses reported in "Integrative Experiments Identify How Punishment Impacts Welfare in Public Goods Games", and to run the experimental platform used to collect the study's data. 

## Data and analysis code 
### Raw data
The raw data for the study is included in the `./data/raw_data` folder, split into `learning_wave` and `validation_wave` folders. Experimental configuration files (.csv and YAML) are included in `./data/exp_config_files`. We note that the raw conversation logs from games with chat enabled have been processed to redact 86 instances of personally identifiable information and 20 instances of sexually/racially-charged comments. These will appear in the transcripts as "REDACTED BY RESEARCHER"; for any questions regarding this processing, please contact the authors. 

### Computing environment 
To run the preprocessing and analysis code, use the included `requirements.txt` file to prepare a new Python `3.10.9` virtual environment with the required packages. The typical install time for these packages is ~5 minutes. 

For example, using Conda, execute these commands in the terminal from within the main `data_and_code` folder containing the `requirements.txt` file: 
```bash
conda create -n pgg_env python=3.10.9 
conda activate pgg_env 
pip install -r pgg_requirements.txt
```
**Note:** The analyses in this work were tested using the Python environment described above with the **macOS Sonoma 14.5 operating system on an Apple M2 Pro processor.** While drafting the manuscript we noted that, holding the hardware and Python environment constant, the MLP model selection procedure produces a different model when run on macOS Sequoia 15.3; given that all other model selection procedures are unaffected, this is likely due to changes in system-level computational libraries between the operating system versions. On macOS 15.3, the MLP hyperparameters selected are 5 layers, 80 units per layer, and a learning rate of 0.006; the dropout rate and number of epochs remain the same. With this set of parameters, the cross-validated RMSE is 13.38, and the out-of-sample RMSE is 5.07. The study reports the values as calculated on the tested computing environment. 

### Pre-processing and generating manuscript figures
After setting up the Python environment, **and before running other scripts/notebooks,** the main script `./code/pgg_reproduction.py` should be run to: 
1. Process the raw data and store the processed data in `./data/processed_data`, consisting of the following files: 
    * `df_analysis_[learn/val].csv`: contains game-level data for the respective wave of data collection. 
    * `df_paired_[learn/val].csv`: contains condition-level data for the respective wave of data collection — this is the level of analysis used in the prediction task. 
    * `df_rounds_[learn/val].csv`: contains player-level data for the respective wave of data collection, e.g. contributions and punishment/reward decisions for each round of the PGG. 
2. Run the model selection procedure and store the selected hyperparameters in `./data/hpo_model_configs.json`. If `./data/hpo_model_configs.json` already exists, this step will be skipped. 
3. Generate figures 2-5 in the manuscript and write them to `./figures`. 

On the hardware and software specified above, the expected runtime of this script is approximately 5 minutes. 

The `./data` directory in the repository already includes the output of this script, so you can proceed directly to the analyses notebooks if desired. 

### Manuscript and supplemental information analyses
After running the preprocessing script (`./code/pgg_reproduction.py`), the following notebooks can be run to generate the analyses in the manuscript and SI. To ensure that notebooks reproduce the reported results, please be sure to run all cells in sequence.  
* `./code/ms_analysis.ipynb`: Contains summary statistics and other analyses reported in the manuscript. 
* `./code/ms_analysis_R.Rmd`: Contains regressions and the Fisherian randomization test of heterogeneity reported in the manuscript. This notebook only has 6 direct package dependencies, the versions for which are listed in the notebook. This notebook was tested on R version 4.4.2.
* `./code/si_analyses.ipynb`: Contains analyses and visualizations included in the SI accompanying the paper. 


## Public goods game experiment platform code 
The platform used to run the public good games described in the paper was built using 1.17.0 of the open-source [Empirica](https://docsv1.empirica.ly/) framework; the code for this platform is included in `./code/pgg_empirica`. 

### To run the platform locally: 
1. Install Node v18. For example, using [nvm](https://github.com/nvm-sh/nvm):
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.2/install.sh | bash 
nvm install 18 
```
2. Install Meteor v1.10.2. Note that if you are using an Apple processor (e.g. M1, M2, etc.) you will need to emulate the Intel architecture by running `arch -x86_64 zsh` before using Meteor, as Apple processors are incompatible with the required Meteor version. If `arch -x86_64 zsh` fails, you may be missing the `rosetta` utility on macOS, which you can install by running `softwareupdate --install-rosetta`. Meteor may take several minutes to install. 
```bash
npm install -g meteor 
meteor update --release 1.10.2
```
3. Unzip the `pgg_empirica.zip` file then, within the `./code/pgg_empirica` directory, run `npm install` to install the required JavaScript packages. 
4. After installing the required packages, run `meteor` within the `./code/pgg_empirica` directory to start the server. Reminder: users with Apple processors will need to run `arch -x86_64 zsh` before running `meteor`. Starting the server for the first time may take 5-10 minutes. 
5. The server will be launched locally, with the address, username, and password for the admin panel printed to the terminal. 
6. Use your browser to navigate to the admin panel at `localhost:3000/admin`, and login using the given credentials. 
7. To load the experimental factors and treatments used in the study, navigate to the `Configuration` panel, click `Import`, then import the YAML for the relevant wave provided in `./data/exp_config_files`. 
8. To begin a game with a given treatment, navigate to the `Monitoring` tab of the admin panel, then `Create batch`, use the dropdown menu to select the desired treatment, then click `Start` for the newly-created batch.
9. To enter a game in a launched batch, navigate to the server's local address by dropping `\admin` from the admin panel's URL; by default, the server is accessible at `localhost:3000`. 

### To deploy the server online: 
The easiest way to create a publicly accessible deployment is to: 
1. **Host a MongoDB v4.2 database:** Empirica is incompatible with other versions of MongoDB. Amazon Web Services' (AWS) marketplace contains several Amazon Machine Images (AMIs, a.k.a preconfigured servers) for MongoDB 4.2 to ease this process. 
2. **Deploy the Meteor app onto Meteor Galaxy:** Once you've configured a MongoDB 4.2 database for use in your deployment, you'll need to configure Empirica to point to that database once it's deployed. Within the `./code/pgg_empirica` directory, create a new file `settings.json` containing the following (replacing `YOUR_X` with the relevant values): 

```json
{
  "admins": [
    {
      "username": "YOUR_ADMIN_PANEL_USERNAME",
      "password": "YOUR_ADMIN_PANEL_PASSWORD"
    }
  ],
  "galaxy.meteor.com": {
    "env": {
      "MONGO_URL": "mongodb+srv://YOUR_DB_READWRITE_USER:YOUR_DB_READWRITE_PASS@YOUR_MONGO_URL/YOUR_DB_NAME?retryWrites=true&w=majority",
      "MONGO_OPLOG_URL": "mongodb+srv://YOUR_DB_OPLOG_USER:YOUR_DB_OPLOG_PASS@YOUR_MONGO_URL/local"
    }
  },
  "public": {
    "playerIdParam": "workerId",
    "playerIdParamExclusive": false,
    "debug_newPlayer": false,
    "debug_resetSession": false,
    "debug_resetDatabase": true,
    "debug_gameDebugMode": true
  }
}
```

Then, after creating an account on [Meteor Galaxy](https://www.meteor.com/cloud), run the following to deploy the app to Galaxy as configured in your new `settings.json` file: 

```bash
DEPLOY_HOSTNAME=galaxy.meteor.com meteor deploy YOUR_DEPLOYMENT_NAME.meteorapp.com --settings settings.json --owner YOUR_GALAXY_ORG_NAME
```

After the server is built and deployed by Meteor Galaxy, the admin panel should be accessible at `YOUR_DEPLOYMENT_NAME.meteorapp.com/admin` using the username and password specified in `settings.json`. After that, configuration and use is the same as steps 6-9 for local deployment. 

## Prediction survey platform code 
The platform used to run the public good games described in the paper was built using version 2 of the open-source [Empirica](https://docs.empirica.ly/) framework (within the versioning system for the second major release, it's version 1.12.0); the code for this platform is included in `./code/pgg_survey_empirica`. 

### To run the platform locally: 
1. Install Empirica following the instructions [here](https://docs.empirica.ly/getting-started/setup).
2. Unzip the `pgg_survey_empirica.zip` file then:
    1. Install the client-side packages by running `npm install` within `./code/pgg_survey_empirica/client` 
    2. Install the server-side packages by running `npm install` within `./code/pgg_survey_empirica/server` 
3. From the main `./code/pgg_survey_empirica` folder, run `empirica` to launch the server. By default, the admin panel should be accessible through your browser at `localhost:3000/admin`. The default username is `admin` and the default password is `defaultpass` -- these can be changed in the file `./code/pgg_survey_empirica/.empirica/empirica.toml`. 
4. In the admin panel, create a new batch, add games with the `quantitative` treatment (this is the configuration used in the prediction survey for the paper), then click "Start" to launch the batch. 
5. Navigate to `localhost:3000` to access the survey. 

### To deploy the server online:
Follow [this guide](https://docs.empirica.ly/guides/deploying-my-experiment/ubuntu-tutorial) on deploying Empirica v2 experiments to Digital Ocean. 