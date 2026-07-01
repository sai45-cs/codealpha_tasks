Iris Flower Classification using Random Forest

Overview

This project uses the Random Forest Classification algorithm from Scikit-learn to classify iris flowers into three species based on their physical characteristics. The model is trained and evaluated using the famous Iris dataset.

Dataset

The dataset used is the Iris dataset, which contains measurements of iris flowers belonging to three species:

* Iris-setosa
* Iris-versicolor
* Iris-virginica

Features

The model uses the following features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

Target Variable

* Species

Technologies Used

* Python
* Pandas
* Scikit-learn

Libraries Required

Install the required libraries using:

pip install pandas scikit-learn

Project Structure

project/
│
├── Iris.csv
├── iris_classification.py
└── README.md

Implementation Steps

1. Load the Iris dataset using Pandas.
2. Remove the unnecessary Id column.
3. Split the dataset into training and testing sets.
4. Train a Random Forest Classifier.
5. Make predictions on the test data.
6. Evaluate the model using:
    * Accuracy Score
    * Classification Report
    * Confusion Matrix

Code

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
df = pd.read_csv("Iris.csv")
df = df.drop("Id", axis=1)
X = df.drop("Species", axis=1)
y = df["Species"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

Sample Output

Accuracy: 1.0
Classification Report:
                 precision    recall  f1-score   support
    Iris-setosa       1.00      1.00      1.00        10
Iris-versicolor       1.00      1.00      1.00         9
 Iris-virginica       1.00      1.00      1.00        11
Confusion Matrix:
[[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]

Results

The Random Forest Classifier achieved excellent performance on the Iris dataset, obtaining high accuracy and correctly classifying the flower species.

Future Improvements

* Perform hyperparameter tuning.
* Compare multiple classification algorithms.
* Visualize feature importance.
* Deploy the model as a web application.

Author

Created as a machine learning practice project using Python and Scikit-learn.
