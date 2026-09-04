import streamlit as st
import pandas as pd
st.title("📊 Student Dashboard")
df = pd.read_csv("student_records.csv")
st.subheader("Student Records")
st.dataframe(df, use_container_width=True)
st.markdown("---")
st.subheader("Summary")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Students", len(df))
with col2:
    st.metric("Average Study Hours", round(df["Hours_Studied"].mean(), 1))
with col3:
    st.metric("Average Attendance", f'{round(df["Attendance"].mean(),1)}%')
with col4:
    st.metric("Average Previous Score", round(df["Previous_Score"].mean(), 1))
st.markdown("---")
st.subheader("Performance Overview")
col1, col2 = st.columns(2)
with col1:
    st.write("#### Study Hours")
    st.bar_chart(df.set_index("Name")["Hours_Studied"])
with col2:
    st.write("#### Attendance")
    st.bar_chart(df.set_index("Name")["Attendance"])
st.markdown("---")
st.subheader("Academic Scores")
st.line_chart(df.set_index("Name")["Previous_Score"])