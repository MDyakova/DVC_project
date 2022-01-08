import json
import pickle

# Additional imports
import matplotlib.pyplot as plt
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns

# Evaluation metrics
from sklearn.metrics import confusion_matrix

# read test data
test_data = pd.read_csv("test_data.csv")

# Getting features and target
X = test_data.drop(["target"], axis=1)
y = test_data["target"]

# load model
model = pickle.load(open("model.pkl", "rb"))

# get predictions
predictions = model.predict(X)

# metrics
acc = np.mean(predictions == y)
tn, fp, fn, tp = confusion_matrix(y, predictions).ravel()
specificity = tn / (tn + fp)
sensitivity = tp / (tp + fn)

# print to file
with open("test_metrics.json", "w") as outfile:
    json.dump(
        {
            "accuracy": acc,
            "specificity": specificity,
            "sensitivity": sensitivity,
        },
        outfile,
    )

ax = sns.heatmap(confusion_matrix(y, predictions), annot=True)
plt.savefig("test_confusion_matrix.png", dpi=80)
