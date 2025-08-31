import streamlit as st
import pandas as pd
import joblib
from datetime import timedelta
import os
import math

# --- Inject custom CSS for a shiny and bright look ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main {
        background: #1a1a1a;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stApp {
        background-color: #e6f7ff; /* Light blue background */
    }

    .css-1d391kg, .css-1dp5q97 {
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .stSelectbox, .stTextInput {
        border-radius: 8px;color: #000000;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.9);
    }

    /* 🔥 Selector title header background changed to black */
    label.css-1pahdxg, label.css-17eq0hr {
        color: #ffffff !important;
        font-weight: 600;
        background-color: #000000 !important;
        padding: 4px 8px;
        border-radius: 4px;
        display: inline-block;
    }

    /* 🔥 Force all form labels (TOWN NAME, LOCALITY, etc.) to appear dark black */
    .stSelectbox label, .stTextInput label, div[data-baseweb="select"] > label {
        color: #000000 !important;
        font-weight: 700 !important;
    }
    
    .stButton>button {
        background-color: #007bff; /* Bright Blue */
        color: black;
        font-weight: 600;
        border-radius: 8px;
        padding: 10px 24px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease-in-out;
    }
    
    .stButton>button:hover {
        background-color: #0056b3;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.25);
    }

    .header-text {
        font-size: 2.5rem;
        font-weight: 700;
        color: #004d99; /* Dark Blue */
        text-align: center;
        margin-bottom: 0.5rem;
    }

    .subheader-text {
        font-size: 1.2rem;
        font-weight: 400;
        color: #333;
        text-align: left; /* Changed from center */
        margin-bottom: 2rem;
    }
    
    .prediction-output {
        font-size: 1.5rem;
        font-weight: 600;
        color: #008000; /* Green for success */
        background-color: #e8f5e9;
        padding: 1.5rem;
        border-radius: 12px;
        border: 2px solid #a5d6a7;
        text-align: center;
        margin-top: 2rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    
    .footer-comment {
        font-size: 0.8rem;
        color: #666;
        text-align: center;
        margin-top: 4rem;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. Load the Model and Preprocessor ---
@st.cache_resource
def load_resources():
    try:
        model_path = os.path.join(os.getcwd(), 'model.pkl')
        preprocessor_path = os.path.join(os.getcwd(), 'preprocessor.pkl')
        model = joblib.load(model_path)
        preprocessor = joblib.load(preprocessor_path)
        return model, preprocessor
    except FileNotFoundError:
        st.error("Model files not found. Please run the `preprocess_and_train.py` script first.")
        return None, None

model, preprocessor = load_resources()

# --- Load Excel Data for cascading filters ---
try:
    df = pd.read_excel("Goa Power Outage Report June 2025.xlsx")
except FileNotFoundError:
    st.error("⚠️ Could not load Excel file 'Goa Power Outage Report June 2025.xlsx'. Please place it in the app folder.")
    st.stop()

# --- 2. Streamlit App Interface ---
st.set_page_config(page_title="Goa Electricity Department", layout="wide")

st.markdown('<div class="header-text">Power Supply Duration Estimator</div>', unsafe_allow_html=True)
st.markdown('<div class="header-text">for Consumers of Goa Electricity Department</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader-text">This web app by Shaunak Kunde uses Artificial Intelligence to predict the duration of steady power supply for any region in the state of Goa.<br>Enter the details below to know the results for your locality.</div>', unsafe_allow_html=True)

if model and preprocessor:
    # --- Cascading Filters ---
    towns = ['-select-'] + sorted(df['Town Name'].dropna().unique().tolist())
    town_name = st.selectbox("TOWN NAME", options=towns, index=0)

    if town_name != '-select-':
        substations = ['-select-'] + sorted(df[df['Town Name'] == town_name]['Substation'].dropna().unique().tolist())
    else:
        substations = ['-select-']
    substation = st.selectbox("SUBSTATION", options=substations, index=0)

    if substation != '-select-':
        feeders = ['-select-'] + sorted(df[df['Substation'] == substation]['Feeder Name'].dropna().unique().tolist())
    else:
        feeders = ['-select-']
    feeder_name = st.selectbox("FEEDER NAME", options=feeders, index=0)

    rural_urban = ['-select-'] + sorted(df['Rural/Urban'].dropna().unique().tolist())
    rural_urban_label = st.selectbox("LOCALITY", options=rural_urban, index=0)

    # --- Predict ---
    if st.button("Show Result"):
        if any(val == '-select-' for val in [town_name, rural_urban_label, substation, feeder_name]):
            st.warning("Please select a value for all fields before predicting.")
        else:
            input_data = pd.DataFrame([[town_name, substation, feeder_name, rural_urban_label]],
                                      columns=['Town Name', 'Substation', 'Feeder Name', 'Rural/Urban'])
            
            try:
                input_processed = preprocessor.transform(input_data)
            except ValueError as e:
                st.error(f"Error during data transformation. Please check the inputs. Details: {e}")
                st.stop()
            
            predicted_seconds = model.predict(input_processed)[0]
            
            if predicted_seconds < 0:
                predicted_seconds = 0
                
            predicted_time_delta = timedelta(seconds=int(predicted_seconds))
            hours = math.floor(predicted_time_delta.total_seconds() // 3600)
            minutes = math.floor((predicted_time_delta.total_seconds() % 3600) // 60)
            
            st.markdown(
                f"""
                <div class="prediction-output">
                    We expect a steady electricity supply for {hours} hours {minutes} minutes per day, in your locality.
                </div>
                """,
                unsafe_allow_html=True
            )

# --- Footer ---
st.markdown(
    """
    <div class="footer-comment">
        The predictions are based on the 'Outage Report for June 2025' dataset available with Goa Electricity Department
    </div>
    """,
    unsafe_allow_html=True
)
