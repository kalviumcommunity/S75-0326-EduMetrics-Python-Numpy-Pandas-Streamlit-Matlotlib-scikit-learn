# array_demo.py
# Demonstration of NumPy array shape, dimensions, and index positions

import numpy as np

# ------------------------------
# Part 1: 1D Array
# ------------------------------
print("=== 1D Array Demo ===")
# Create a 1D array
array_1d = np.array([10, 20, 30, 40, 50])
print("1D Array:", array_1d)

# Inspect shape
print("Shape of 1D array:", array_1d.shape)  # (5,)
# Inspect number of dimensions
print("Number of dimensions (ndim):", array_1d.ndim)

# Accessing elements using indices
print("First element (index 0):", array_1d[0])
print("Third element (index 2):", array_1d[2])
print("Last element (index -1):", array_1d[-1])

print("\n")  # Line break for readability

# ------------------------------
# Part 2: 2D Array
# ------------------------------
print("=== 2D Array Demo ===")
# Create a 2D array (matrix)
array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("2D Array:\n", array_2d)

# Inspect shape
print("Shape of 2D array:", array_2d.shape)  # (3, 3) -> 3 rows, 3 columns
# Inspect number of dimensions
print("Number of dimensions (ndim):", array_2d.ndim)

# Accessing elements using row and column indices
print("Element at row 0, column 0:", array_2d[0, 0])  # 1
print("Element at row 1, column 2:", array_2d[1, 2])  # 6
print("Element at last row, last column:", array_2d[-1, -1])  # 9

# ------------------------------
# Part 3: Common Indexing Mistake
# ------------------------------
print("\n=== Common Index Error Example ===")
try:
    print(array_1d[10])  # Out of range
except IndexError as e:
    print("Error accessing array_1d[10]:", e)

try:
    print(array_2d[3, 0])  # Out of range row
except IndexError as e:
    print("Error accessing array_2d[3, 0]:", e)

