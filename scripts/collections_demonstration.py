# This script demonstrates the usage of Python collection data structures: lists, tuples, and dictionaries.

# --- List Demonstration ---
# Lists are mutable, ordered collections of items.
student_names = ["Alice", "Bob", "Charlie", "David"]
print(f"Original list of students: {student_names}")

# Accessing elements using index (starting from 0)
first_student = student_names[0]
print(f"The first student is: {first_student}")

# Modifying a list (mutable)
# Adding a new student
student_names.append("Eve")
print(f"Updated list after adding Eve: {student_names}")

# Changing an element
student_names[1] = "Bobby"
print(f"Updated list after changing Bob to Bobby: {student_names}")


# --- Tuple Demonstration ---
# Tuples are immutable, ordered collections of items.
# They are often used for fixed sets of values.
coordinates = (10.5, 20.3)
print(f"\nCoordinates (Tuple): {coordinates}")

# Accessing elements using index
x_coord = coordinates[0]
y_coord = coordinates[1]
print(f"X coordinate: {x_coord}, Y coordinate: {y_coord}")

# Immutability Check:
# The following line would raise a TypeError because tuples cannot be changed after creation.
# coordinates[0] = 15.0


# --- Dictionary Demonstration ---
# Dictionaries are unordered collections of key-value pairs.
student_scores = {
    "Alice": 85,
    "Bobby": 92,
    "Charlie": 78,
    "David": 88,
    "Eve": 95
}
print(f"\nStudent scores (Dictionary): {student_scores}")

# Accessing elements using keys
alice_score = student_scores["Alice"]
print(f"Alice's score is: {alice_score}")

# Modifying a dictionary (adding or updating key-value pairs)
student_scores["Charlie"] = 82 # Updating an existing key
student_scores["Frank"] = 90  # Adding a new key-value pair
print(f"Updated student scores: {student_scores}")

# Final Clean Output
print("\n--- Summary ---")
print(f"Number of students: {len(student_names)}")
print(f"First coordinate: {coordinates[0]}")
print(f"Average score (calculated manually): {(sum(student_scores.values()) / len(student_scores)):.2f}")
