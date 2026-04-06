# =========================================
# FUNCTION WITH PARAMETERS AND RETURN VALUE
# =========================================

# Function to add two numbers
def add_numbers(a, b):
    result = a + b
    return result   # returning value instead of printing


# Call the function and store result
sum_result = add_numbers(5, 3)

print("Sum is:", sum_result)


# =========================================
# FUNCTION WITH MULTIPLICATION
# =========================================

def multiply_numbers(x, y):
    return x * y


# Store returned value
product = multiply_numbers(4, 2)

print("Product is:", product)


# =========================================
# USING RETURNED VALUE IN ANOTHER FUNCTION
# =========================================

# Function to square a number
def square(num):
    return num * num


# Passing result of one function into another
square_result = square(sum_result)

print("Square of sum is:", square_result)


# =========================================
# BAD PRACTICE (ONLY PRINTING, NO RETURN)
# =========================================

def bad_add(a, b):
    print(a + b)   # only prints, does not return


# Trying to store result
bad_result = bad_add(2, 3)

print("Bad result is:", bad_result)  # will print None