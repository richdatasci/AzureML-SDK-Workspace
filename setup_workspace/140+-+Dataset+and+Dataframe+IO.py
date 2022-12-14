
# -----------------------------------------------------
# Import required classes from Azureml
# -----------------------------------------------------
from azureml.core import Workspace, Datastore, Dataset


# -----------------------------------------------------
# Access the Workspace, Datastore and Datasets
# -----------------------------------------------------
ws                = Workspace.from_config("./config")
az_store          = Datastore.get(ws, '')
az_dataset        = Dataset.get_by_name(ws, '')
az_default_store  = ws.get_default_datastore()


# -----------------------------------------------------
# Load the Azureml Dataset into the pandas dataframe
# -----------------------------------------------------
df = az_dataset.to_pandas_dataframe()


# -----------------------------------------------------
# Upload the dataframe to the azureml dataset
# -----------------------------------------------------
df_sub = df[["", "", ""]]

az_ds_from_df = Dataset.Tabular.register_pandas_dataframe(
                dataframe=df_sub,
                target=az_store,
                name="")
