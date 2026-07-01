🚗 Car Price Prediction using Random Forest Regression

A Machine Learning project that predicts the selling price of used cars using the Random Forest Regression algorithm. The model analyzes various car attributes such as manufacturing year, fuel type, transmission, ownership history, and kilometers driven to estimate the selling price.

⸻

📌 Project Overview

The objective of this project is to build a regression model capable of accurately predicting the selling price of a used car based on its features.

The project involves data preprocessing, feature encoding, model training, and performance evaluation using standard regression metrics.

⸻

📊 Dataset

The project uses a used car dataset containing information about different vehicles and their selling prices.

Features

Feature	Description
Year	Year of manufacture
Present_Price	Current ex-showroom price
Kms_Driven	Total kilometers driven
Fuel_Type	Fuel type of the vehicle
Selling_type	Dealer or individual seller
Transmission	Manual or automatic transmission
Owner	Number of previous owners

Target Variable

* Selling_Price

⸻

🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn

⸻

📁 Project Structure

Car-Price-Prediction/
│
├── car data.csv
├── car_price_prediction.py
└── README.md

⸻

⚙️ Installation

Clone the repository:

git clone <repository-url>
cd Car-Price-Prediction

Install the required libraries:

pip install pandas scikit-learn

⸻

🚀 How to Run

Execute the Python script:

python car_price_prediction.py

⸻

🔍 Implementation Steps

1. Load the car dataset using Pandas.
2. Remove the Car_Name column.
3. Encode categorical features using Label Encoding.
4. Split the dataset into training and testing sets.
5. Train a Random Forest Regressor.
6. Predict selling prices on the test set.
7. Evaluate the model performance.

⸻

📈 Evaluation Metrics

The model is evaluated using:

* R² Score
* Mean Absolute Error (MAE)
* Actual vs Predicted Price Comparison

⸻

📋 Sample Output

R² Score: 0.9629
Mean Absolute Error: 0.6173
Actual vs Predicted Prices:
   Actual  Predicted
0    0.35     0.4408
1   10.11    11.1578
2    4.95     4.9040
...

⸻

✅ Results

The Random Forest Regressor achieved a high R² score and low prediction error, demonstrating strong performance in predicting used car prices based on historical data.

⸻

🔮 Future Improvements

* Perform hyperparameter tuning
* Compare multiple regression algorithms
* Visualize feature importance
* Build an interactive car price prediction application
* Deploy the model using Flask or Streamlit

⸻

👨‍💻 Author

Sai
