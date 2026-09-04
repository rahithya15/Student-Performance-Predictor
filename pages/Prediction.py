import streamlit as st
import pandas as pd
import joblib
import os
st.title("🎯 Student Performance Prediction")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "student_model.pkl")
model = joblib.load(MODEL_PATH)
st.subheader("Enter Student Details")
student_name = st.text_input("Student Name")
hours = st.number_input(
    "Hours Studied (per day)",
    min_value=0,
    max_value=12,
    value=5
)
attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=75
)
previous = st.number_input(
    "Previous Score",
    min_value=0,
    max_value=100,
    value=70
)
assignments = st.number_input(
    "Assignments Completed",
    min_value=0,
    max_value=10,
    value=5
)
if st.button("Predict Performance"):
    if student_name.strip() == "":
        st.warning("Please enter the student's name.")
    else:
        data = pd.DataFrame({
            "Hours_Studied": [hours],
            "Attendance": [attendance],
            "Previous_Score": [previous],
            "Assignments": [assignments]
        })
        prediction = model.predict(data)
        average = (attendance + previous + (hours * 10) + (assignments * 10)) / 4
        if average < 40:
            performance = "Poor"
        elif average < 60:
            performance = "Average"
        elif average < 75:
            performance = "Good"
        elif average < 90:
            performance = "Outstanding"
        else:
            performance = "Excellent"
        st.markdown("---")
        st.subheader("Prediction Result")
        st.write(f"**Student Name:** {student_name}")
        st.write(f"**Hours Studied:** {hours}")
        st.write(f"**Attendance:** {attendance}%")
        st.write(f"**Previous Score:** {previous}")
        st.write(f"**Assignments Completed:** {assignments}")
        st.write(f"**Overall Performance:** {performance}")
        if prediction[0] == 1:
            st.success("Result: PASS ✅")
        else:
            st.error("Result: FAIL ❌")