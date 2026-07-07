# Task 04 - NumPy & Pandas for Data Analysis

PKCERT AI & Software Development Internship

## Folder Structure

```
Task04/
├── part_a_numpy.py       -> Part A: NumPy fundamentals (40 marks)
├── part_b_pandas.py      -> Part B: Pandas fundamentals (30 marks)
├── mini_project/         -> Part C: Data analysis mini project (30 marks)
│   ├── titanic.csv
│   ├── titanic_analysis.py
│   ├── titanic_cleaned.csv
│   └── README.md
└── README.md             -> this file
```

## Part A - NumPy Fundamentals

`part_a_numpy.py` covers:
- Creating 1D and multi-dimensional arrays (from lists, zeros, ones, arange, linspace, random)
- Indexing, slicing, and reshaping arrays
- Mathematical operations on arrays (sum, mean, max/min, row/column sums)
- Broadcasting examples (scalar, row vector, column vector) with an explanation of why it's useful
- Vectorized operations compared against a plain Python loop, with timing to show the speed difference
- Linear algebra: dot product, matrix multiplication, transpose, determinant, and inverse

## Part B - Pandas Fundamentals

`part_b_pandas.py` covers:
- Creating a Pandas Series and DataFrame
- Indexing/selection with `loc` and `iloc`, filtering rows with conditions, sorting values
- GroupBy operations with aggregation (mean, min, max, count)
- Merging two DataFrames (inner join and left join) with an explanation of the difference,
  plus an example of concatenating DataFrames

## Part C - Data Analysis Mini Project

See `mini_project/README.md` for full details. In short: the Titanic dataset is loaded, cleaned
(missing Age filled with median, Cabin column dropped, missing Embarked filled with mode),
then explored with summary statistics and groupby-based analysis (survival by gender, class,
age group, and family size).

## How to Run

```
pip install numpy pandas

python3 part_a_numpy.py
python3 part_b_pandas.py
cd mini_project && python3 titanic_analysis.py
```
