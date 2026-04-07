# This script demonstrates the definition and usage of Python functions.

# --- Function Definitions ---

# 1. Function with one parameter: greets a student.
def greet_student(name):
    """
    Greets a student by their name.
    
    Args:
        name (str): The name of the student.
    """
    greeting = f"Hello, {name}! Welcome to the EduMetrics project."
    print(greeting)

# 2. Function with two parameters: calculates grade and returns it.
def calculate_grade(score, passing_score=50):
    """
    Calculates a student's grade based on their score.
    
    Args:
        score (int/float): The student's score.
        passing_score (int/float): The score required to pass.
        
    Returns:
        str: 'Pass' or 'Fail' based on the score.
    """
    if score >= passing_score:
        return "Pass"
    else:
        return "Fail"

# --- Function Calls ---

# Call the first function from outside its definition
student_name = "Alice"
greet_student(student_name)

# Call the second function and capture its output
alice_score = 85
alice_grade = calculate_grade(alice_score)
print(f"Alice's score: {alice_score}, Grade: {alice_grade}")

# Call the second function with a custom passing score
bob_score = 45
bob_grade = calculate_grade(bob_score, passing_score=60)
print(f"Bob's score: {bob_score}, Passing Score Required: 60, Grade: {bob_grade}")

# --- Clean Indentation and Readable Structure ---
# Notice how each function has a docstring (the text in triple quotes) 
# to explain its purpose and arguments, which makes the code readable.
