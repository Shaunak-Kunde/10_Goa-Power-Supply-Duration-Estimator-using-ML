# Power Supply Prediction for Goa Electricity Consumers ⚡  
### Author: Shaunak Damodar Sinai Kunde  

This is a personal data science project that demonstrates how machine learning can be used to analyze and predict **average hours of steady electricity supply** for different towns, substations, feeders, and localities in Goa.  

The goal of this project is to help **Goa electricity consumers** gain better insights into their expected power supply based on their location.  

---

## 🚀 Project Workflow  

1. **Data Loading & Cleaning**  
   - Reads Excel data with details like **town, substation, feeder, and locality type (urban/rural)**.  
   - Cleans newline characters and missing values.  
   - Converts the target column (`Average_Hours_of_Steady_Supply`) from `HH:MM:SS` format into numerical seconds.  
   - Applies one-hot encoding for categorical features.  

2. **Model Training**  
   - Splits dataset into training and testing sets.  
   - Trains a **Random Forest Regressor**.  
   - Evaluates the model using **R² score** to measure accuracy.  

3. **Model Saving**  
   - Saves both the trained model (`model.pkl`) and preprocessing pipeline (`preprocessor.pkl`) using `joblib`.  

4. **Deployment with Streamlit**  
   - Users can enter their **Town, Locality, Substation, and Feeder Name**.  
   - The app predicts the **expected average hours of steady electricity supply**.  

---

## 🛠️ Technologies Used  

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Joblib  
- Streamlit  

---

## 📂 Files in Repository  

- `project_notebook.ipynb` → Jupyter Notebook with full workflow  
- `model.pkl` → Trained Random Forest model  
- `preprocessor.pkl` → Preprocessing pipeline  
- `app.py` → Streamlit app for deployment  
- `requirements.txt` → List of dependencies  
- `README.md` → Documentation  

---

## ▶️ How to Run Locally  

1. Clone this repository:  
   ```bash
   git clone <repo-url>
   cd <repo-folder>
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run app.py
🌍 Use Case for Goa
This project can be used by Goa electricity consumers to:

Check the expected steady supply duration based on their location.

Compare electricity supply across towns, feeders, and substations.

Support decision-making for local consumers by providing data-driven insights.