# -----------------------------------------------------
# Import required classes from azureml
# -----------------------------------------------------
from azureml.core import Workspace, Datastore, Dataset


# -----------------------------------------------------
# Access the workspace by name
# -----------------------------------------------------
ws = Workspace.from_config("./config")


# -----------------------------------------------------
# List all the workspaces within a subscription
# -----------------------------------------------------

ws_list = Workspace.list(subscription_id="")
ws_list = list(ws_list)


# -----------------------------------------------------
# Access the default datastore from workspace
# -----------------------------------------------------
az_default_store = ws.get_default_datastore()


# -----------------------------------------------------
# List all the datastores
# -----------------------------------------------------
store_list = list(ws.datastores)


# -----------------------------------------------------
# Get the dataset by name from a workspace
# -----------------------------------------------------
az_dataset = Dataset.get_by_name(ws, "")


# -----------------------------------------------------
# List datasets from a workspace
# -----------------------------------------------------

ds_list = list(ws.datasets.keys())

for items in ds_list:
    print(items)
