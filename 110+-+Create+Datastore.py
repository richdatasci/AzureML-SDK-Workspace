# -----------------------------------------------------
# Import the Workspace and Datastore class
# -----------------------------------------------------
from azureml.core import Workspace, Datastore


# -----------------------------------------------------
# Access the workspace from the config.json
# -----------------------------------------------------
ws = Workspace.from_config(path="./config")


# -----------------------------------------------------
# Create a datastore
# -----------------------------------------------------
az_store = Datastore.register_azure_blob_container(
            workspace=ws,
            datastore_name="",
            account_name="",
            container_name="",
            account_key="")
