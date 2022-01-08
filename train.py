import json
import pickle

# Additional imports
import matplotlib.pyplot as plt
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns

# Evaluation metrics
from sklearn.metrics import confusion_matrix

# Data splitting/parameter tuning
from sklearn.model_selection import cross_val_predict
from xgboost import XGBClassifier

# read train data
train_data = pd.read_csv("train_data.csv")

# Getting features and target
X = train_data.drop(["target"], axis=1)
y = train_data["target"]

# train and evaluate XGBoost model with 5 folds
xgb_model = XGBClassifier(
    base_score=0.5,
    colsample_bylevel=1,
    colsample_bytree=1,
    learning_rate=0.05,
    max_depth=5,
    n_estimators=30,
)
xgb_predictions = cross_val_predict(xgb_model, X, y, cv=5)

# train final model
model = xgb_model.fit(X, y)

# save model
filename = "model.pkl"
pickle.dump(model, open(filename, "wb"))

# metrics
acc = np.mean(xgb_predictions == y)
tn, fp, fn, tp = confusion_matrix(y, xgb_predictions).ravel()
specificity = tn / (tn + fp)
sensitivity = tp / (tp + fn)

# print to file metrics and confusion_matrix
with open("metrics.json", "w") as outfile:
    json.dump(
        {
            "accuracy": acc,
            "specificity": specificity,
            "sensitivity": sensitivity,
        },
        outfile,
    )

ax = sns.heatmap(confusion_matrix(y, xgb_predictions), annot=True)
plt.savefig("confusion_matrix.png", dpi=80)
