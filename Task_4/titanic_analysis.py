"""
Task 04 - Part C: Data Analysis Mini Project
Titanic Dataset - Exploratory Data Analysis
PKCERT AI & Software Development Internship
"""

import pandas as pd

# ---------- Load Dataset ----------

df = pd.read_csv("titanic.csv")

print("========== Dataset Overview ==========")
print("Shape (rows, columns):", df.shape)
print("\nColumns:", list(df.columns))
print("\nFirst 5 rows:\n", df.head())
print("\nData types:\n", df.dtypes)

# ---------- Checking for Missing Values ----------

print("\n========== Missing Values Before Cleaning ==========")
print(df.isnull().sum())

# ---------- Cleaning the Data ----------

# Age has a good number of missing values, fill with median age
df["Age"] = df["Age"].fillna(df["Age"].median())

# Cabin is missing for most rows, too many missing to fill meaningfully
# so just drop the column instead
df = df.drop(columns=["Cabin"])

# Embarked has just a couple of missing values, fill with the most common port
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("\n========== Missing Values After Cleaning ==========")
print(df.isnull().sum())

# ---------- Summary Statistics ----------

print("\n========== Summary Statistics ==========")
print(df.describe())

print("\nSurvival counts:\n", df["Survived"].value_counts())
print("\nSurvival rate overall:", round(df["Survived"].mean() * 100, 2), "%")

# ---------- Exploratory Data Analysis ----------

print("\n========== Survival by Gender ==========")
survival_by_sex = df.groupby("Sex")["Survived"].mean() * 100
print(survival_by_sex)

print("\n========== Survival by Passenger Class ==========")
survival_by_class = df.groupby("Pclass")["Survived"].mean() * 100
print(survival_by_class)

print("\n========== Survival by Class and Gender ==========")
survival_by_class_sex = df.groupby(["Pclass", "Sex"])["Survived"].mean() * 100
print(survival_by_class_sex)

print("\n========== Average Age and Fare by Class ==========")
print(df.groupby("Pclass")[["Age", "Fare"]].mean())

print("\n========== Age Distribution ==========")
bins = [0, 12, 18, 35, 60, 100]
labels = ["Child", "Teen", "Young Adult", "Adult", "Senior"]
df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels)
print(df["AgeGroup"].value_counts())

print("\nSurvival rate by age group:\n", df.groupby("AgeGroup", observed=True)["Survived"].mean() * 100)

print("\n========== Family Size vs Survival ==========")
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
print(df.groupby("FamilySize")["Survived"].mean() * 100)

# ---------- Save cleaned dataset ----------
df.to_csv("titanic_cleaned.csv", index=False)
print("\nCleaned dataset saved as titanic_cleaned.csv")
