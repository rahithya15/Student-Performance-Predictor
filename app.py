import streamlit as st
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)
st.title("🎓 Student Performance Predictor")
st.markdown("### Predicting Student Academic Performance")
st.markdown("---")
col1, col2 = st.columns([2, 1])
with col1:
    st.header("Welcome")
    st.write("""
    The Student Performance Predictor is designed to evaluate a student's
    academic performance based on important academic factors.

    By entering a student's details, the application predicts whether the
    student is likely to pass or fail. It also provides a dashboard to
    view student records and basic academic statistics.
    """)
with col2:
    st.info("""
**Project Objective**

To analyze student academic information
and provide a simple performance
prediction that can assist in
understanding learning outcomes.
""")
st.markdown("---")
st.header("Application Modules")
col1, col2, col3 = st.columns(3)
with col1:
    st.success("🏠 Home")
    st.write("""
Learn about the project,
its purpose, and how
the application works.
""")

with col2:
    st.warning("📊 Dashboard")
    st.write("""
View student records,
summary information,
and performance charts.
""")

with col3:
    st.info("🎯 Prediction")
    st.write("""
Enter student details
and predict whether
the student is likely
to pass or fail.
""")
st.markdown("---")
st.header("How to Use")

st.write("""
1. Open the **Prediction** page.
2. Enter the student's academic details.
3. Click the **Predict Performance** button.
4. View the prediction result.
""")
st.markdown("---")
st.header("Key Features")
col1, col2 = st.columns(2)
with col1:
    st.write("✔ Student Performance Prediction")
    st.write("✔ Student Records Dashboard")
    st.write("✔ Easy-to-use Interface")
with col2:
    st.write("✔ Academic Performance Analysis")
    st.write("✔ Summary Statistics")
    st.write("✔ Performance Visualization")
st.markdown("---")
st.success("Select a page from the navigation menu to begin using the application.")