# 🏦 CreditWise Loan Approval System

_Predicting loan approval decisions using Machine Learning to enable faster, unbiased, and data-driven financial decision-making._

---

## 📌 Table of Contents
- [Overview](#overview)
- [Live Application](#live-application)
- [Application Preview](#application-preview)
- [Business Problem](#business-problem)
- [Dataset](#dataset)
- [Machine Learning Approach](#machine-learning-approach)
- [Tools & Technologies](#tools--technologies)
- [Project Structure](#project-structure)
- [Application Features](#application-features)
- [Deployment](#deployment)
- [Author](#author)

---

## Overview

This project implements an end-to-end **Machine Learning Loan Approval System** that predicts whether a loan application should be approved or rejected based on applicant financial and demographic information.

The system integrates a trained classification model with a **Streamlit-based web application**, allowing real-time predictions through a clean and professional user interface.

---

## 🚀 Live Application

🔗 **Live Demo:**  
https://creditwise-loan-approval-htjfef6ccughuoyswbe7gu.streamlit.app/

---

## 🖼 Application Preview

![CreditWise Loan Approval App](images/app_preview.png)

---

## Business Problem

Traditional loan approval processes depend heavily on manual document verification and human judgment, which leads to:

- Delays in loan processing  
- Inconsistent decision-making  
- Potential bias in approvals  
- Higher operational costs  

The objective of this project is to automate the initial loan approval decision using historical data and machine learning, enabling faster, fairer, and more reliable evaluations.

---

## Dataset

Each record in the dataset represents a loan applicant with attributes describing personal, financial, and credit information.

**Key Features**
- Applicant Income  
- Coapplicant Income  
- Age  
- Credit Score  
- Loan Amount  
- Loan Term  
- Employment Status  
- Education Level  
- Property Area  
- Gender  

**Target Variable**
- `Loan_Approved`  
  - `1` → Approved  
  - `0` → Rejected  

---

## Machine Learning Approach

- **Problem Type:** Binary Classification  
- **Model Used:** Logistic Regression  
- **Preprocessing Steps:**
  - One-Hot Encoding for categorical variables  
  - Feature Scaling using StandardScaler  
- **Model Serialization:** Pickle  

Logistic Regression was selected due to its interpretability and effectiveness in financial risk assessment problems.

---

## Tools & Technologies

- **Python** – Core programming language  
- **Scikit-learn** – Model training and preprocessing  
- **Pandas & NumPy** – Data manipulation and numerical analysis  
- **Matplotlib & Seaborn** – Data visualization  
- **Streamlit** – Web application framework  
- **Pickle** – Model serialization  
- **Git & GitHub** – Version control and collaboration  
- **Streamlit Cloud** – Application deployment  

---

## Project Structure

```text
creditwise-loan-approval/
│
├── app.py                  # Streamlit web application
├── train_model.py          # Model training script
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── model/
│   ├── loan_model.pkl      # Trained ML model
│   ├── scaler.pkl          # Feature scaler
│   └── features.pkl        # Feature names used during training
│
├── data/
│   └── loan_approval_data.csv
│
└── .streamlit/
    └── config.toml         # Dark theme configuration
```

---

## Application Features

- Real-time loan approval prediction
- Probability-based output for decision confidence
- Clean, dark-themed professional UI
- Cloud-hosted and publicly accessible application

---

## Deployment

The application is deployed using Streamlit Cloud, enabling public access to the machine learning model through a web interface.

Repository connected directly to Streamlit Cloud

app.py configured as the main entry point

Model artifacts loaded at runtime for inference

---

## Author

**Ravi Aghara**
📧 Email: aaghararavi@gmail.com

🐙 GitHub: https://github.com/raviaghara007

🔗 LinkedIn: https://www.linkedin.com/in/raviaghara07/