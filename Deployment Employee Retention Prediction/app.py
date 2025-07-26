import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and encoders
model = joblib.load("xgb_model.pkl")
label_encoders = {
    col: joblib.load(f"le_{col}.pkl") 
    for col in ["city", "gender", "relevent_experience", "enrolled_university", 
                "education_level", "major_discipline", "experience", "company_size", 
                "company_type", "last_new_job"]
}

# Streamlit app
st.title("💼 Employee Retention Prediction")
st.write("📥 Enter employee details to predict if they are likely to stay or leave.")

# Input form
with st.form("🧾 employee_form"):
    st.subheader("Employee Details")
    
    # City
    city = st.selectbox("🏙️ City", label_encoders["city"].classes_.tolist())
    
    # City Development Index
    cdi = st.slider("🌆 City Development Index", min_value=0.0, max_value=1.0, value=0.9, step=0.001)
    
    # Gender
    gender = st.selectbox("⚧️ Gender", label_encoders["gender"].classes_.tolist())
    
    # Relevant Experience
    experience = st.selectbox("💼 Relevant Experience", label_encoders["relevent_experience"].classes_.tolist())
    
    # Enrolled University
    university = st.selectbox("🎓 Enrolled University", label_encoders["enrolled_university"].classes_.tolist())
    
    # Education Level
    education = st.selectbox("📚 Education Level", label_encoders["education_level"].classes_.tolist())
    
    # Major Discipline
    discipline = st.selectbox("🧪 Major Discipline", label_encoders["major_discipline"].classes_.tolist())
    
    # Experience
    exp = st.selectbox("⏳ Experience (Years)", label_encoders["experience"].classes_.tolist())
    
    # Company Size
    company_size = st.selectbox("🏢 Company Size", label_encoders["company_size"].classes_.tolist())
    
    # Company Type
    company_type = st.selectbox("🏭 Company Type", label_encoders["company_type"].classes_.tolist())
    
    # Last New Job
    last_job = st.selectbox("🔄 Last New Job (Years)", label_encoders["last_new_job"].classes_.tolist())
    
    # Training Hours
    training_hours = st.number_input("📈 Training Hours", min_value=0, max_value=336, value=50)
    
    # Submit button
    submitted = st.form_submit_button("🔍Predict")

# Process input and predict
if submitted:
    # Create input DataFrame
    input_data = {
        "city": [city],
        "city_development_index": [cdi],
        "gender": [gender],
        "relevent_experience": [experience],
        "enrolled_university": [university],
        "education_level": [education],
        "major_discipline": [discipline],
        "experience": [exp],
        "company_size": [company_size],
        "company_type": [company_type],
        "last_new_job": [last_job],
        "training_hours": [training_hours]
    }
    input_df = pd.DataFrame(input_data)
    
    # Encode categorical inputs
    for col in label_encoders:
        try:
            input_df[col] = label_encoders[col].transform(input_df[col])
        except ValueError:
            st.error(f"Invalid value for {col}. Please select a valid option.")
            st.stop()
    
    # Predict
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]
    
    # Display result
    st.subheader("Prediction Result")
    if prediction == 1.0:
        st.error(f"Employee is likely to LEAVE (Probability: {probability[1]:.2%})")
    else:
        st.success(f"Employee is likely to STAY (Probability: {probability[0]:.2%})")