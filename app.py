import streamlit as st
import joblib
import pandas as pd

# ===============================
# Configuration
# ===============================
st.set_page_config(page_title="Churn Prediction", layout="centered")
st.title("Customer Churn Prediction")
st.write("Enter customer details below:")

RISK_THRESHOLDS = {"low": 0.4, "moderate": 0.6}

# ===============================
# Load model and feature info
# ===============================
@st.cache_resource
def load_model():
    model = joblib.load("churn_model.pkl")
    feature_dtypes = joblib.load("feature_dtypes.pkl")
    return model, feature_dtypes

try:
    model, feature_dtypes = load_model()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# ===============================
# Only the 8 important features
# ===============================
st.header("Customer Input")

# --- Ensure the options match exactly what the model encoder expects ---
gender_options = ["Male", "Female"]
contract_options = ["Month-to-month", "One year", "Two year"]
internet_options = ["DSL", "Fiber optic", "No"]
payment_options = ["Electronic check", "Mailed check", 
                   "Bank transfer (automatic)", "Credit card (automatic)"]
dependents_options = ["Yes", "No"]
senior_options = [0, 1]

gender = st.selectbox("Gender", gender_options)
monthly_charge = st.number_input("Monthly Charge", min_value=0.0, value=50.0)
contract = st.selectbox("Contract", contract_options)
internet_service = st.selectbox("InternetService", internet_options)
payment_method = st.selectbox("PaymentMethod", payment_options)
tenure = st.number_input("Tenure (months)", min_value=0, value=12)
senior_citizen = st.selectbox("SeniorCitizen", senior_options)
dependents = st.selectbox("Dependents", dependents_options)

# ===============================
# Build input DataFrame with correct types
# ===============================
input_df = pd.DataFrame([{
    "Gender": gender,
    "Monthly Charge": float(monthly_charge),
    "Contract": contract,
    "InternetService": internet_service,
    "PaymentMethod": payment_method,
    "Tenure": int(tenure),
    "SeniorCitizen": int(senior_citizen),
    "Dependents": dependents
}])

# Fill any missing columns expected by the model
for col in model.feature_names_in_:
    if col not in input_df.columns:
        dtype = feature_dtypes.get(col, "float64")
        input_df[col] = 0 if str(dtype) in ["int64", "float64"] else "Unknown"

# Ensure proper column order
input_df = input_df[model.feature_names_in_]

# ===============================
# Predict
# ===============================
if st.button("Predict Churn Risk"):
    try:
        probability = model.predict_proba(input_df)[0][1]
        st.subheader(f"Churn Probability: {probability:.2f}")

        if probability > RISK_THRESHOLDS["moderate"]:
            st.error("High Risk of Churn")
        elif probability > RISK_THRESHOLDS["low"]:
            st.warning("Moderate Risk of Churn")
        else:
            st.success("Low Risk of Churn")

    except Exception as e:
        st.error("Prediction failed")
        st.exception(e)