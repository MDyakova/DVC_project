# Additional imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data splitting/parameter tuning
from sklearn.model_selection import train_test_split

# read data
heart_path = "heart.csv"
heart_data = pd.read_csv(heart_path)

# drop na rows
heart_data.dropna(inplace=True)

# change data types
heart_data["sex"] = heart_data["sex"].astype("object")
heart_data["cp"] = heart_data["cp"].astype("object")
heart_data["fbs"] = heart_data["fbs"].astype("object")
heart_data["restecg"] = heart_data["restecg"].astype("object")
heart_data["exang"] = heart_data["exang"].astype("object")
heart_data["slope"] = heart_data["slope"].astype("object")
heart_data["thal"] = heart_data["thal"].astype("object")

# value encoding
heart_data = pd.get_dummies(heart_data)

# data balance
heart_data_0 = heart_data[heart_data["target"] == 0].copy()
heart_data_1 = heart_data[heart_data["target"] == 1].copy()

k_target = len(heart_data_0) / len(heart_data_1)
k_0 = np.minimum(1 / k_target, 1)
k_1 = np.minimum(k_target, 1)

heart_data_0 = heart_data[heart_data["target"] == 0].sample(
    frac=k_0, random_state=None
)
heart_data_1 = heart_data[heart_data["target"] == 1].sample(
    frac=k_1, random_state=None
)

heart_data = pd.concat([heart_data_0, heart_data_1]).sample(
    frac=1, random_state=None
)

# split to train and test
train_data, test_data = train_test_split(
    heart_data, test_size=0.1, random_state=0, shuffle=True
)

# save train/test sets
train_data.to_csv("train_data.csv", index=None)
test_data.to_csv("test_data.csv", index=None)
