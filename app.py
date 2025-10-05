import streamlit as st
import pandas as pd
import joblib
# from sklearn.preprocessing import StandardScaler
# scaler=StandardScaler()
# Load saved model, scaler, and expected columns
model = joblib.load("heart_disease_model.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")
scaling_col=['Age','RestingBP','Cholesterol','MaxHR','Oldpeak']
st.title("Heart Stroke Prediction by Devansh")
st.markdown("Provide the following details to check your heart stroke risk:")

# Collect user input
age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex", ["M", "F"])
chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.slider("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

d={'M':1,'F':0}
e={'Y':1,'N':0}
# raw_input = {
#         'Age': age,
#         'RestingBP': resting_bp,
#         'Cholesterol': cholesterol,
#         'FastingBS': fasting_bs,
#         'MaxHR': max_hr,
#         'Oldpeak': oldpeak,
#         'Sex':d[sex],
#         'ChestPainType_' + chest_pain: 1,
#         'RestingECG_' + resting_ecg: 1,
#         'ExerciseAngina_Y': e[exercise_angina],
#         'ST_Slope_' + st_slope: 1
#     }

#     # Create input dataframe
# input_df = pd.DataFrame([raw_input])
# for col in expected_columns:
#         if col not in input_df.columns:
#             input_df[col] = 0

#     # Reorder columns
# input_df = input_df[expected_columns]
# scaled_input = scaler.transform(input_df)
# print(input_df.info())


if st.button("Predict"):

    # Create a raw input dictionary
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex':d[sex],
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_Y': e[exercise_angina],
        'ST_Slope_' + st_slope: 1
    }

    # Create input dataframe
    input_df = pd.DataFrame([raw_input])


    # Fill in missing columns with 0s
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[expected_columns]

    # Scale the input
    input_df[scaling_col] = scaler.fit_transform(input_df[scaling_col])

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Show result
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")