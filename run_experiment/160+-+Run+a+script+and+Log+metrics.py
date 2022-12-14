
# -----------------------------------------------------
# Import required classes from Azureml
# -----------------------------------------------------
from azureml.core import Workspace, Datastore, Dataset, Experiment


# -----------------------------------------------------
# Access the Workspace, Datastore and Datasets
# -----------------------------------------------------
ws                = Workspace.from_config("./config")
az_store          = Datastore.get(ws, '')
az_dataset        = Dataset.get_by_name(ws, '')
az_default_store  = ws.get_default_datastore()

# -----------------------------------------------------
# Create/Access an experiment object
# -----------------------------------------------------
experiment = Experiment(workspace=ws,
                        name="")


# -----------------------------------------------------
# Run an experiment using start_logging method
# -----------------------------------------------------
new_run = experiment.start_logging()


# -----------------------------------------------------
# Do your stuff here
# -----------------------------------------------------
df = az_dataset.to_pandas_dataframe()

# Count the observations
total_observations = len(df)

# Get the null/missing values
nulldf = df.isnull().sum()


# -----------------------------------------------------
# Log metrics and Complete an experiment run
# -----------------------------------------------------

# Log the metrics to the workspace
new_run.log("Total Observations", total_observations)

# Log the missing data values
for columns in df.columns:
    new_run.log(columns, nulldf[columns])

new_run.complete()
