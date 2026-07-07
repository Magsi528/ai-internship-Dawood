"""
Task 04 - Part B: Pandas Fundamentals
PKCERT AI & Software Development Internship
"""

import pandas as pd
import numpy as np

print("========== 1. Series and DataFrames ==========")

# Series - basically a labeled 1D array
marks = pd.Series([85, 90, 78, 92, 65], index=["Ali", "Sara", "Bilal", "Hina", "Usman"])
print("Marks Series:\n", marks)
print("\nMarks above 80:\n", marks[marks > 80])

# DataFrame from a dictionary
data = {
    "Name": ["Ali", "Sara", "Bilal", "Hina", "Usman"],
    "Age": [21, 22, 20, 23, 21],
    "Department": ["CS", "SE", "CS", "AI", "SE"],
    "Marks": [85, 90, 78, 92, 65]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

print("\nInfo:")
print(df.info())

print("\nDescribe:\n", df.describe())

print("\n========== 2. Indexing, Filtering, Sorting ==========")

# indexing / selection
print("Name column:\n", df["Name"])
print("\nFirst two rows (loc):\n", df.loc[0:1])
print("\nRow at index 2 (iloc):\n", df.iloc[2])

# filtering
print("\nStudents from CS department:\n", df[df["Department"] == "CS"])
print("\nStudents with Marks > 80 and Age < 22:\n", df[(df["Marks"] > 80) & (df["Age"] < 22)])

# sorting
print("\nSorted by Marks (descending):\n", df.sort_values("Marks", ascending=False))
print("\nSorted by Department then Marks:\n", df.sort_values(["Department", "Marks"]))

# adding a new column
df["Grade"] = pd.cut(df["Marks"], bins=[0, 70, 85, 100], labels=["C", "B", "A"])
print("\nDataFrame with Grade column:\n", df)

print("\n========== 3. GroupBy Operations ==========")

grouped = df.groupby("Department")
print("Average marks per department:\n", grouped["Marks"].mean())
print("\nCount of students per department:\n", grouped["Name"].count())
print("\nMultiple aggregations per department:\n", grouped["Marks"].agg(["mean", "min", "max"]))

print("\n========== 4. Merging and Joining DataFrames ==========")

# a second dataframe with department details
dept_info = pd.DataFrame({
    "Department": ["CS", "SE", "AI"],
    "HOD": ["Dr. Zubair", "Dr. Kamran", "Dr. Ayesha"],
    "Building": ["Block A", "Block B", "Block C"]
})
print("Department info:\n", dept_info)

# inner join - keeps only matching departments
merged_inner = pd.merge(df, dept_info, on="Department", how="inner")
print("\nInner join result:\n", merged_inner)

# left join - keeps all rows from df even if no match in dept_info
merged_left = pd.merge(df, dept_info, on="Department", how="left")
print("\nLeft join result:\n", merged_left)

print("""
Explanation: inner join only keeps rows where Department exists in
both DataFrames, so any department not present in dept_info would be
dropped. Left join keeps every row from df (the left table) regardless
of whether a match exists in dept_info, filling missing values with NaN
where there's no match.
""")

# concat example (stacking two dataframes)
new_students = pd.DataFrame({
    "Name": ["Zara"],
    "Age": [22],
    "Department": ["CS"],
    "Marks": [88],
    "Grade": ["A"]
})
combined = pd.concat([df, new_students], ignore_index=True)
print("After concatenating a new student:\n", combined)
