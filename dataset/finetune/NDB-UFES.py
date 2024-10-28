import os
import shutil
import pandas as pd
from sklearn.model_selection import train_test_split

origin_prefix = "original/NDB-UFES/patch"
target_prefix = "NDB-UFES"

train_val = pd.read_csv(os.path.join(origin_prefix, "sabpatch_parsed_folders.csv"))
test = pd.read_csv(os.path.join(origin_prefix, "sabpatch_parsed_test.csv"))

train_val_oscc_files = [row["path"] for index, row in train_val.iterrows() if row["lesion"] == "OSCC"]
train_oscc_files, val_oscc_files = train_test_split(train_val_oscc_files, test_size=0.2, random_state=12)
train_val_others_files = [row["path"] for index, row in train_val.iterrows() if row["lesion"] != "OSCC"]
train_others_files, val_others_files = train_test_split(train_val_others_files, test_size=0.2, random_state=12)
test_oscc_files = [row["path"] for index, row in test.iterrows() if row["lesion"] == "OSCC"]
test_others_files = [row["path"] for index, row in test.iterrows() if row["lesion"] != "OSCC"]

train_dir = os.path.join(target_prefix, "train")
val_dir = os.path.join(target_prefix, "val")
test_dir = os.path.join(target_prefix, "test")

for index, row in train_val.iterrows():
    if row["path"] in train_oscc_files:
        target_dir = os.path.join(train_dir, "oscc")
    elif row["path"] in train_others_files:
        target_dir = os.path.join(train_dir, "others")
    elif row["path"] in val_oscc_files:
        target_dir = os.path.join(val_dir, "oscc")
    elif row["path"] in val_others_files:
        target_dir = os.path.join(val_dir, "others")
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    origin_dir = os.path.join(origin_prefix, "images", row["path"])
    shutil.copy(origin_dir, target_dir)

for index, row in test.iterrows():
    if row["path"] in test_oscc_files:
        target_dir = os.path.join(test_dir, "oscc")
    else:
        target_dir = os.path.join(test_dir, "others")
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    origin_dir = os.path.join(origin_prefix, "images", row["path"])
    shutil.copy(origin_dir, target_dir)
