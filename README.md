=> CreditWise Loan Approval System

An end-to-end Machine Learning Loan Approval System with an interactive Streamlit web application that predicts whether a loan should be Approved or Rejected based on applicant details.


=> Problem Statement

Traditional loan approval processes rely heavily on manual verification, which can be:
- Time-consuming  
- Biased  
- Inconsistent  

This project aims to solve that problem by using Machine Learning to automatically analyze customer data and assist in making fast, unbiased, and accurate loan approval decisions.


=> Project Objective

- Build a machine learning model to predict loan approval
- Create an interactive web interface for real-time prediction
- Deploy the model as a web application
- Make the project production-ready and portfolio-worthy



=> Dataset Description

Each row in the dataset represents a loan applicant with the following attributes:

| Feature | Description |
|------|------------|
| Applicant_Income | Monthly income of applicant |
| Coapplicant_Income | Monthly income of co-applicant |
| Age | Applicant age |
| Credit_Score | Credit bureau score |
| Loan_Amount | Loan amount requested |
| Loan_Term | Loan duration (months) |
| Employment_Status | Salaried / Self-Employed / Business |
| Education_Level | Graduate / Postgraduate / Undergraduate |
| Property_Area | Urban / Semi-Urban / Rural |
| Gender | Male / Female |
| Loan_Approved | Target variable (1 = Approved, 0 = Rejected)|



 => Machine Learning Models Used

- Logistic Regression(Primary model)
- Feature Scaling using StandardScaler
- One-Hot Encoding for categorical variables

> Logistic Regression was chosen for its simplicity, interpretability, and effectiveness in binary classification problems.



 => Project Workflow

1. Data Loading & Cleaning  
2. Feature Encoding  
3. Feature Scaling  
4. Model Training  
5. Model Serialization (`.pkl`)  
6. Streamlit UI Integration  
7. Model Deployment  


=> Tech-Stack

Python|Pandas|NumPy|matplotlib|seaborn|Scikit-learn
|Streamlit|Git & GitHub|


 => Web Application (Streamlit)

The Streamlit web app allows users to:
- Enter applicant details
- Instantly get loan approval prediction
- View approval probability
- Interact with a user in easy way




