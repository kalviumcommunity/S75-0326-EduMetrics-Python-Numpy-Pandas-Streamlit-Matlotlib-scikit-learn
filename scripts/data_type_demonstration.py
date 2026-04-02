# In this script, we will demonstrate the use of numeric and string data types in Python.

# Numeric Data Types
# Integer
age = 25
number_of_students = 100

# Floating-point
pi = 3.14
temperature = 98.6

# String Data Types
student_name = "John Doe"
course_name = 'Data Science'

# Arithmetic Operations
sum_of_numbers = age + number_of_students
product_of_numbers = pi * 2

print(f"Sum of numbers: {sum_of_numbers}")
print(f"Product of numbers: {product_of_numbers}")

# String Concatenation
greeting = "Hello, " + student_name + "!"
print(greeting)

# Type Mismatch and Conversion
# The following line will cause a TypeError because you can't concatenate a string with an integer.
# print("Your age is: " + age)

# To fix this, we need to convert the integer to a string.
print("Your age is: " + str(age))
