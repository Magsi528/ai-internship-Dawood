# Titanic Dataset - Exploratory Data Analysis

## PKCERT AI & Software Development Internship - Task 04, Part C

## Dataset

The dataset used is the well known Titanic passenger dataset (`titanic.csv`), which contains
information about 891 passengers who were aboard the Titanic. It includes details like:

- `PassengerId`, `Name`, `Sex`, `Age`
- `Pclass` (ticket class: 1st, 2nd, 3rd)
- `SibSp` (siblings/spouses aboard), `Parch` (parents/children aboard)
- `Ticket`, `Fare`, `Cabin`, `Embarked` (port of embarkation)
- `Survived` (0 = did not survive, 1 = survived) - this is the target column

Source: publicly available Titanic dataset (commonly used for beginner ML/EDA practice).

## Files

- `titanic.csv` - original raw dataset
- `titanic_analysis.py` - Python script that cleans the data and performs the analysis
- `titanic_cleaned.csv` - output file generated after running the script (cleaned version)
- `README.md` - this file

## How to Run

```
python3 titanic_analysis.py
```

Requires `pandas` installed (`pip install pandas`).

## Data Cleaning Process

The raw dataset had missing values in three columns:

| Column   | Missing Values | How it was handled |
|----------|----------------|---------------------|
| Age      | 177            | Filled with the median age of all passengers |
| Cabin    | 687            | Dropped the column entirely (too many missing values to fill reliably) |
| Embarked | 2              | Filled with the most frequent port (mode) |

After cleaning, there were 0 missing values left in the dataset.

## Analysis Performed

- Overall summary statistics (`describe()`) for numeric columns
- Overall survival rate
- Survival rate grouped by gender
- Survival rate grouped by passenger class
- Survival rate grouped by class and gender together
- Average age and fare per passenger class
- Age binned into groups (Child, Teen, Young Adult, Adult, Senior) and survival rate per group
- Family size (SibSp + Parch + 1) vs survival rate

## Key Findings

- **Overall survival rate** was about **38.4%** (342 out of 891 passengers survived).
- **Gender had the biggest impact on survival**: about **74%** of female passengers survived
  compared to only about **19%** of male passengers, matching the "women and children first"
  boarding policy.
- **Passenger class mattered a lot**: 1st class passengers had a survival rate of about **63%**,
  2nd class about **47%**, and 3rd class only about **24%**. This is likely because 1st class
  cabins were located closer to the lifeboat deck.
- Combining class and gender shows the effect stacks: **1st class females had a ~97% survival
  rate**, while **3rd class males had only ~14%**.
- 1st class passengers were on average older and paid a much higher fare (~84) compared to
  3rd class (~14), which lines up with the class-based survival difference.
- **Children had a noticeably higher survival rate (~58%)** compared to other age groups.
- Passengers travelling with a small family (2-4 members) had a higher survival rate than
  people travelling completely alone or in very large families, likely because small groups
  could help each other while very large families struggled to stay together during evacuation.

## Conclusion

The analysis shows that survival on the Titanic was strongly linked to gender, passenger class,
and to some extent age and family size, rather than being random. These findings match the
commonly known historical accounts of the disaster.
