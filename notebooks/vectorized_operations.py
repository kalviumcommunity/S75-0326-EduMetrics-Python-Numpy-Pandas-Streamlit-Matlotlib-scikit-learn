# vectorized_operations.py
# Demonstrates replacing Python loops with vectorized NumPy operations

import numpy as np

# -----------------------------
# 1. Create a NumPy array
# -----------------------------
array = np.array([1, 2, 3, 4, 5])
print("Original Array:", array)
print("\n")

# -----------------------------
# 2. Loop-based operation
# Example: multiply each element by 2 using a loop
# -----------------------------
loop_result = []
for x in array:
    loop_result.append(x * 2)

print("Loop-based result (each element * 2):", loop_result)

# -----------------------------
# 3. Vectorized operation
# -----------------------------
vector_result = array * 2  # This multiplies all elements at once
print("Vectorized result (each element * 2):", vector_result)
print("\n")

# -----------------------------
# 4. Verify both results are the same
# -----------------------------
# Convert loop_result to NumPy array for comparison
loop_result_np = np.array(loop_result)

print("Are loop and vectorized results equal?", np.array_equal(loop_result_np, vector_result))
print("\n")

# -----------------------------
# 5. Vectorized comparisons
# Example: check which elements are greater than 3
# -----------------------------
comparison_result = array > 3
print("Vectorized comparison (array > 3):", comparison_result)
print("\n")

# -----------------------------
# 6. Summary notes for video explanation
# -----------------------------
print("Note:")
print("- Loop-based code iterates over elements explicitly.")
print("- Vectorized code performs the operation on the whole array at once.")
print("- Vectorization improves readability and performance, especially on larger datasets.")