# numpy_array_math.py
# This script demonstrates basic mathematical operations on NumPy arrays

import numpy as np

# -----------------------------
# 1. Create NumPy arrays
# -----------------------------
array1 = np.array([1, 2, 3, 4])
array2 = np.array([5, 6, 7, 8])

print("Array 1:", array1)
print("Array 2:", array2)
print("\n")

# -----------------------------
# 2. Element-wise operations
# -----------------------------
add_result = array1 + array2
print("Element-wise Addition:", add_result)

sub_result = array1 - array2
print("Element-wise Subtraction:", sub_result)

mul_result = array1 * array2
print("Element-wise Multiplication:", mul_result)

div_result = array1 / array2
print("Element-wise Division:", div_result)
print("\n")

# -----------------------------
# 3. Scalar operations
# -----------------------------
add_scalar = array1 + 10
print("Array1 + 10:", add_scalar)

mul_scalar = array2 * 3
print("Array2 * 3:", mul_scalar)
print("\n")

# -----------------------------
# 4. Comparing with Python lists
# -----------------------------
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

list_add = list1 + list2
print("Python list addition (concatenation):", list_add)
print("NumPy array addition (element-wise):", array1 + array2)
print("\n")

# -----------------------------
# 5. Shape compatibility and common mistakes
# -----------------------------
array3 = np.array([1, 2, 3])
print("Array1 shape:", array1.shape)
print("Array3 shape:", array3.shape)

# Uncommenting the next line will raise an error due to incompatible shapes
# error_test = array1 + array3  # ValueError: operands could not be broadcast together

print("\nNote: NumPy arrays must have compatible shapes for element-wise operations.")
print("Attempting operations with incompatible shapes will raise an error.")