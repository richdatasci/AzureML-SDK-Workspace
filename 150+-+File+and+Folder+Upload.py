
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
# Upload local files to storage account using datastore
# -----------------------------------------------------
files_list = ["./data/test.csv", "./data/test1.csv"]

az_store.upload_files(files=files_list,
                      target_path="/",
                      relative_root="",
                      overwrite=True)


# -----------------------------------------------------
# Upload folder or directory to the storage account
# -----------------------------------------------------
az_store.upload(src_dir=".",
                target_path="",
                overwrite=True)
