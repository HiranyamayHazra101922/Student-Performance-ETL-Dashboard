# student_dashboard.py

import sqlite3
import pandas as pd
import streamlit as st

# Connect to DB
conn = sqlite3.connect("students.db")

st.title("📊 Student Performance Dashboard")

# Load processed data
df = pd.read_sql("SELECT * FROM students_processed", conn)

# Top Scorer
st.subheader("🏆 Top Scorer")
topper = df.sort_values(by="total", ascending=False).head(1)
st.table(topper[["name", "total"]])

# Grade Distribution
st.subheader("📈 Grade Distribution")
grade_dist = df["grade"].value_counts().reset_index()
grade_dist.columns = ["Grade", "Count"]
st.bar_chart(grade_dist.set_index("Grade"))

# Subject-wise Average
st.subheader("📚 Subject-wise Averages")
raw_df = pd.read_sql("SELECT * FROM students_raw", conn)
subject_avg = raw_df[["math", "english", "science"]].mean().to_frame(name="Average")
st.table(subject_avg)

# Full Table
st.subheader("📋 Full Student Performance Table")
st.dataframe(df)

# Close DB
conn.close()
