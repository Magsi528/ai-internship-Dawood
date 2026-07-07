"""
Task 04 - Part A: NumPy Fundamentals
PKCERT AI & Software Development Internship
"""

import numpy as np
import time

print("========== 1. Creating Arrays ==========")

# 1D array from a list
arr1d = np.array([1, 2, 3, 4, 5])
print("1D array:", arr1d)

# 2D array from a nested list
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", arr2d)

# using built-in creation functions
zeros_arr = np.zeros((2, 3))
ones_arr = np.ones((3, 3))
range_arr = np.arange(0, 20, 2)
lin_arr = np.linspace(0, 1, 5)
rand_arr = np.random.randint(1, 100, size=(3, 3))

print("\nzeros:\n", zeros_arr)
print("\nones:\n", ones_arr)
print("\narange (0 to 20 step 2):", range_arr)
print("\nlinspace (0 to 1, 5 values):", lin_arr)
print("\nrandom 3x3 array:\n", rand_arr)

print("\n========== 2. Indexing, Slicing, Reshaping ==========")

arr = np.arange(1, 13)
print("Original array:", arr)

# indexing
print("Element at index 4:", arr[4])
print("Last element:", arr[-1])

# slicing
print("Slice [2:7]:", arr[2:7])
print("Every 2nd element:", arr[::2])

# reshape into a 3x4 matrix
matrix = arr.reshape(3, 4)
print("\nReshaped into 3x4:\n", matrix)

# 2D indexing/slicing
print("Row 1:", matrix[1])
print("Column 2:", matrix[:, 2])
print("Sub-matrix [0:2, 1:3]:\n", matrix[0:2, 1:3])

# mathematical operations
print("\nMatrix + 10:\n", matrix + 10)
print("Matrix * 2:\n", matrix * 2)
print("Sum of all elements:", matrix.sum())
print("Mean:", matrix.mean())
print("Max:", matrix.max(), " Min:", matrix.min())
print("Column-wise sum:", matrix.sum(axis=0))
print("Row-wise sum:", matrix.sum(axis=1))

print("\n========== 3. Broadcasting ==========")

# broadcasting a scalar to a whole array
a = np.array([1, 2, 3])
print("array a:", a, " + 5 ->", a + 5)

# broadcasting a 1D array across a 2D array (row-wise)
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_vector = np.array([10, 20, 30])
print("\n3x3 matrix b:\n", b)
print("row_vector:", row_vector)
print("b + row_vector (broadcast across each row):\n", b + row_vector)

# broadcasting a column vector
col_vector = np.array([[100], [200], [300]])
print("\ncol_vector:\n", col_vector)
print("b + col_vector (broadcast across each column):\n", b + col_vector)

print("""
Advantage of broadcasting: it lets NumPy apply operations between arrays
of different shapes without manually looping or copying data to match
shapes. This saves memory and is much faster than writing explicit loops,
since the operation is handled internally in optimized C code instead of
Python level iteration.
""")

print("========== 4. Vectorized Operations vs Loops ==========")

n = 1_000_000
big_arr = np.arange(n)

# using a plain python loop
start = time.time()
result_loop = []
for i in big_arr:
    result_loop.append(i * 2)
loop_time = time.time() - start

# using vectorized numpy operation
start = time.time()
result_vec = big_arr * 2
vec_time = time.time() - start

print(f"Loop time for {n} elements: {loop_time:.4f} sec")
print(f"Vectorized time for {n} elements: {vec_time:.4f} sec")
print(f"Vectorized version is roughly {loop_time / vec_time:.1f}x faster")

print("\n========== 5. Linear Algebra ==========")

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# dot product / matrix multiplication
print("\nDot product A.B:\n", np.dot(A, B))
print("Matrix multiplication A @ B:\n", A @ B)

# transpose
print("\nTranspose of A:\n", A.T)

# inverse (only works for square, non-singular matrices)
det_A = np.linalg.det(A)
print("\nDeterminant of A:", det_A)
if det_A != 0:
    print("Inverse of A:\n", np.linalg.inv(A))
else:
    print("A is singular, inverse does not exist")

# quick check: A * A_inverse should give identity matrix
A_inv = np.linalg.inv(A)
print("\nA @ A_inverse (should be identity):\n", np.round(A @ A_inv))
