# student_etl.py
import sqlite3
import pandas as pd

# Step 1: Load CSV data
# df = pd.read_csv("student_marks.csv")
df = pd.read_csv("C:/Users/hiran/Documents/Python/StudentProject/student_marks.csv")

# Step 2: Connect to SQLite (or MySQL if preferred)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Step 3: Create raw table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students_raw (
    student_id INTEGER,
    name TEXT,
    math INTEGER,
    english INTEGER,
    science INTEGER
)
""")

# Step 4: Insert data into raw table
df.to_sql("students_raw", conn, if_exists="replace", index=False)

# Step 5: Process data
def calculate_grade(avg):
    if avg >= 85:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'Fail'

# Add new columns
df["total"] = df[["math", "english", "science"]].sum(axis=1)
df["average"] = df["total"] / 3
df["grade"] = df["average"].apply(calculate_grade)

# Step 6: Create processed table
cursor.execute("DROP TABLE IF EXISTS students_processed")
cursor.execute("""
CREATE TABLE students_processed (
    student_id INTEGER,
    name TEXT,
    total INTEGER,
    average REAL,
    grade TEXT
)
""")

# Insert processed data
df_processed = df[["student_id", "name", "total", "average", "grade"]]
df_processed.to_sql("students_processed", conn, if_exists="append", index=False)

# Step 7: Example queries
print("Top Scorer:")
print(pd.read_sql("SELECT name, total FROM students_processed ORDER BY total DESC LIMIT 1", conn))

print("\nGrade Distribution:")
print(pd.read_sql("SELECT grade, COUNT(*) as count FROM students_processed GROUP BY grade", conn))

print("\nSubject-wise Average:")
print(df[["math", "english", "science"]].mean())

# Done
conn.commit()
conn.close()


# cd "C:\Users\hiran\Documents\Python\StudentProject"
# python student_etl.py
# streamlit run student_dashboard.py

