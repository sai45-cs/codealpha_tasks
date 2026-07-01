🌸 Iris Flower Classification using Random Forest

A Machine Learning project that classifies iris flowers into different species using the Random Forest Classification algorithm from Scikit-learn.

⸻

📌 Project Overview

The goal of this project is to build a classification model that can accurately predict the species of an iris flower based on its physical measurements.

The model is trained on the famous Iris dataset and evaluated using standard classification metrics.

⸻

📊 Dataset

The dataset contains 150 samples of iris flowers belonging to three species:

* Iris-setosa
* Iris-versicolor
* Iris-virginica

Features

Feature	Description
SepalLengthCm	Length of the sepal
SepalWidthCm	Width of the sepal
PetalLengthCm	Length of the petal
PetalWidthCm	Width of the petal

Target Variable

* Species

⸻

🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn

⸻

📁 Project Structure

Iris-Flower-Classification/
│
├── Iris.csv
├── iris_classification.py
└── README.md

⸻

⚙️ Installation

Clone the repository:

git clone <repository-url>
cd Iris-Flower-Classification

Install the required dependencies:

pip install pandas scikit-learn

⸻

🚀 How to Run

Run the Python script:

python iris_classification.py

⸻

🔍 Implementation Steps

1. Load the Iris dataset.
2. Remove the unnecessary Id column.
3. Split the dataset into training and testing sets.
4. Train a Random Forest Classifier.
5. Predict the species of test samples.
6. Evaluate the model performance.

⸻

📈 Evaluation Metrics

The model is evaluated using:

* Accuracy Score
* Classification Report
* Confusion Matrix

⸻

📋 Sample Output

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

⸻

✅ Results

The Random Forest model achieved excellent performance on the Iris dataset, demonstrating its effectiveness for multi-class classification tasks.

⸻

🔮 Future Improvements

* Hyperparameter tuning
* Feature importance visualization
* Comparison with other classification algorithms
* Model deployment using Flask or Streamlit

⸻

👨‍💻 Author

Sai
