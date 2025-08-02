# 📊 Student Performance ETL & Dashboard

This is a beginner-friendly full-stack **Python + SQL** project that demonstrates how to build a complete **ETL (Extract, Transform, Load) pipeline** and visualize data using a **Streamlit dashboard**.

The project takes raw student marks from a CSV file, calculates total scores, averages, and assigns grades. It stores both raw and processed data in a **SQLite** database, then visualizes the results in a clean and interactive web interface.

---

## 💡 Project Objectives

- Read student exam data from a `.csv` file
- Clean and process the data (total marks, average, grade)
- Store both raw and processed data into a local SQLite database
- Build a dashboard with **Streamlit** to display:
  - 🏆 Top scorer
  - 📈 Grade distribution
  - 📚 Subject-wise averages
  - 📋 Full student performance table

---

## 🛠 Tech Stack

- **Python 3**
- **pandas** – Data manipulation
- **sqlite3** – Lightweight local SQL database
- **Streamlit** – Interactive dashboarding

---

## 📁 Project Structure
StudentPerformanceETL/
├── student_marks.csv # Sample input data
├── student_etl.py # ETL script (runs once)
├── student_dashboard.py # Streamlit dashboard (runs on browser)
├── students.db # SQLite DB (auto-created)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


