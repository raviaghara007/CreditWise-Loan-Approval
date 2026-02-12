import streamlit as st
import pandas as pd
import pickle

# Load saved objects
model = pickle.load(open("model/loan_model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))
features = pickle.load(open("model/features.pkl", "rb"))


st.set_page_config(
    page_title="CreditWise Loan Approval",
    layout="centered",
)



st.title("🏦 CreditWise Loan Approval System")
st.write("Enter applicant details to predict loan approval")

# ---- Input fields ----
income = st.number_input("Applicant Income", min_value=0)
co_income = st.number_input("Coapplicant Income", min_value=0)
age = st.slider("Age", 18, 70)
credit_score = st.slider("Credit Score", 300, 900)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.selectbox("Loan Term (Months)", [12, 24, 36, 60, 120])

employment = st.selectbox("Employment Status", ["Salaried", "Self-Employed", "Business"])
property_area = st.selectbox("Property Area", ["Urban", "Semi-Urban", "Rural"])
education = st.selectbox("Education Level", ["Graduate", "Postgraduate", "Undergraduate"])
gender = st.selectbox("Gender", ["Male", "Female"])

# ---- Convert input to dataframe ----
input_data = {
    "Applicant_Income": income,
    "Coapplicant_Income": co_income,
    "Age": age,
    "Credit_Score": credit_score,
    "Loan_Amount": loan_amount,
    "Loan_Term": loan_term,
    f"Employment_Status_{employment}": 1,
    f"Property_Area_{property_area}": 1,
    f"Education_Level_{education}": 1,
    f"Gender_{gender}": 1
}

input_df = pd.DataFrame([input_data])

# Match training columns
input_df = input_df.reindex(columns=features, fill_value=0)

# Scale input
input_scaled = scaler.transform(input_df)

# ---- Prediction ----
if st.button("🔍 Predict Loan Status"):
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
