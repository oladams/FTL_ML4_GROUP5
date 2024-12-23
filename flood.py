import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Load feature names and model with error handling
try:
    # replace the path with feature_name.pkl path
    with open(r'C:\Users\Hp\Downloads\Flood Prediction Project\feature_names.pkl', 'rb') as f:
        feature_names = pickle.load(f)
    # replace the path with model path, you will download a model from google drive, check in the readme file.
    with open(r'C:\Users\Hp\Downloads\Flood Prediction Project\random_forest_flood_model1.pkl', 'rb') as f:
        model = pickle.load(f)

        # Ensure the loaded model is a regressor
        if not isinstance(model, RandomForestRegressor):
            st.error("Invalid model format. Please ensure the model is a RandomForestRegressor.")
            st.stop()

except FileNotFoundError:
    st.error("Model or feature files not found. Please check file paths.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model: {str(e)}")
    st.stop()

# App Title and Description
st.title("South Sudan Flood Prediction App")
st.markdown("""
Welcome to the Flood Prediction App for South Sudan. This tool helps forecast flood events
and assess risk levels to improve preparedness and response.
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Predict"])

if page == "Home":
    st.header("About the App")
    st.markdown("""
    Flood prediction is crucial for mitigating the effects of floods. This app uses machine learning to provide:
    - Risk Levels: Low, Medium, High
    - Potential Impacted Areas
    - Interactive Visualizations
    """)

elif page == "Predict":
    st.header("Flood Prediction")
    st.subheader("Input Features")

    # Input Section
    user_input = {}
    for feature in feature_names:
        if feature == "Date":
            user_input[feature] = st.date_input(f"Select {feature}")
        elif feature in ["Precipitation", "Temperature"]:  # Example conditions
            user_input[feature] = st.slider(f"Select {feature}", 0, 10, step=1)
        else:
            user_input[feature] = st.number_input(f"Input {feature}", min_value=1, max_value=10, value=1, step=1)

    # Convert user input to DataFrame
    try:
        input_df = pd.DataFrame([user_input], columns=feature_names)

        if st.button("Predict Flood Risk"):
            prediction = model.predict(input_df)[0]

            # Convert prediction to risk level
            if prediction < 0.4:
                risk = "Low"
            elif prediction < 0.6:
                risk = "Medium"
            else:
                risk = "High"

            # Display results
            st.subheader("Prediction Results")
            st.write(f"**Flood Risk Level:** {risk}")
            st.write(f"**Flood Risk Score:** {prediction:.2f}")
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")
