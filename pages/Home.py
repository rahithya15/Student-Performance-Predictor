import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

st.title("🎓 Student Performance Predictor")

st.markdown("---")

st.header("Welcome")

st.write("""
The **Student Performance Predictor** is a Machine Learning application that helps
predict whether a student is likely to **Pass** or **Fail** based on their academic
performance and study habits.

This project analyzes key factors such as study hours, attendance, previous scores,
and assignment completion to provide a quick performance prediction.
""")

st.markdown("---")

st.subheader("✨ Project Features")

st.write("""
✅ Predict student performance using Machine Learning

✅ View student records in an interactive dashboard

✅ Analyze academic data with charts and statistics

✅ Simple and user-friendly interface
""")

st.markdown("---")

st.subheader("📊 Input Parameters")

col1, col2 = st.columns(2)

with col1:
    st.info("📚 Hours Studied")
    st.info("📅 Attendance (%)")

with col2:
    st.info("📝 Previous Score")
    st.info("📖 Assignments Completed")

st.markdown("---")

st.success("👈 Select **Dashboard** or **Prediction** from the sidebar to begin.")