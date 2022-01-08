import json
import pickle

# Additional imports
import matplotlib.pyplot as plt
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns

# read test data
test_data = pd.read_csv("test_data.csv")

# Getting features and target
X = test_data.drop(["target"], axis=1)
y = test_data["target"]

# load model
model = pickle.load(open("model.pkl", "rb"))

# get feature scores
FI = model.feature_importances_
FI = pd.DataFrame([X.columns, FI]).T
FI.columns = ("feature", "score")
FI = FI.sort_values(by=["score"], ascending=False)

# save to image
# image formatting
axis_fs = 18  # fontsize
title_fs = 22  # fontsize
sns.set(style="whitegrid")

# plot
ax = sns.barplot(x="score", y="feature", data=FI)
ax.set_xlabel("Importance", fontsize=axis_fs)
ax.set_ylabel("Feature", fontsize=axis_fs)
ax.set_title("Random forest\nfeature importance", fontsize=title_fs)

plt.tight_layout()
plt.savefig("feature_importance.png", dpi=120)
plt.close()
