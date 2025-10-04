# ⚡ Goa Power Supply Prediction for Goa Electricity Consumers - Machine Learning Project 
### Author: Shaunak Damodar Sinai Kunde  

This is a personal data science project of mine, that demonstrates how machine learning can be used to analyze and predict **average hours of steady electricity supply** for different towns, substations, feeders, and localities in Goa.  

The goal of this project is to help **Goa electricity consumers** gain better insights into their expected power supply based on their location.  

---

The app is deployed online on **Streamlit Cloud** and can be accessed here:  
[Goa Electricity Supply Duration Estimator](https://goa-electricity-supply.streamlit.app/)

---

## 📂 Project Structure

├── goa_power_outage_app.py # Streamlit app for deployment
├── Goa Power Outage Report June 2025.xlsx # Original dataset
├── end_to_end_data_science_deploy.ipynb # Jupyter notebook with full workflow
├── model.pkl # Trained Random Forest model
├── preprocessor.pkl # Preprocessing pipeline
├── requirements.txt # Project dependencies
└── README.md # Project documentation

markdown
Copy code

---

## 🔑 Features

- Input **Town**, **Locality**, **Substation**, and **Feeder Name** to predict expected electricity supply duration.
- Provides a **numerical estimate** of average hours of steady electricity supply.
- Interactive web app with **Streamlit** for easy usage by any consumer.
- Helps compare electricity supply across towns, feeders, and substations.

---

## ⚙️ Tech Stack

- **Python** – Data handling and model training (`pandas`, `numpy`, `scikit-learn`)
- **Joblib** – Model and pipeline serialization
- **Streamlit** – Web app development and deployment
- **GitHub + Streamlit Cloud** – Version control and hosting

---

## 🔍 Workflow Overview

### 1. Data Loading & Cleaning
- Reads Excel data with details such as town, substation, feeder, and locality type (urban/rural).
- Cleans newline characters and handles missing values.
- Converts the target column `Average_Hours_of_Steady_Supply` from `HH:MM:SS` format to numerical seconds.
- Applies **one-hot encoding** for categorical features.

### 2. Model Training
- Splits dataset into **training and testing sets**.
- Trains a **Random Forest Regressor**.
- Evaluates model performance using **R² score**.

### 3. Model Saving
- Saves both the **trained model** (`model.pkl`) and **preprocessing pipeline** (`preprocessor.pkl`) using Joblib for reuse in predictions.

### 4. Deployment with Streamlit
- Users enter **Town, Locality, Substation, and Feeder Name**.
- The app uses the saved preprocessing pipeline and model to predict the **average hours of steady supply**.

---

## 🚀 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/Shaunak-Kunde/10_Goa-Power-Supply-Duration-Estimator-using-ML.git
cd 10_Goa-Power-Supply-Duration-Estimator-using-ML
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run goa_power_outage_app.py

```

## 🌍 Use Case for Goa
This project can help Goa electricity consumers:

Check the expected steady supply duration based on location.

Compare electricity supply across towns, feeders, and substations.

Make data-driven decisions regarding electricity usage and planning.

## 🌟 Learning Outcomes
Worked with real-world utility datasets in Excel format.

Learned data cleaning and preprocessing, including time format conversion and one-hot encoding.

Trained and evaluated a Random Forest Regressor.

Deployed an interactive web app using Streamlit Cloud.

Applied end-to-end machine learning workflow from dataset to deployment.

### 🙌 Acknowledgement
### Dataset: Goa Electricity Department – Power Outage Report June 2025 avilable at Goa Electricity Department Website

Support decision-making for local consumers by providing data-driven insights.
