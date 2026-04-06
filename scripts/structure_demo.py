# =========================================
# IMPORTS (none needed here, but section kept for structure)
# =========================================


# =========================================
# GLOBAL VARIABLES / SETUP
# =========================================

numbers = [1, 2, 3, 4, 5]


# =========================================
# HELPER FUNCTIONS (Reusable Logic)
# =========================================

def calculate_sum(nums):
    """Returns the sum of a list"""
    total = 0
    for num in nums:
        total += num
    return total


def calculate_average(nums):
    """Returns the average of a list"""
    total = calculate_sum(nums)   # reuse function
    return total / len(nums)


def print_numbers(nums):
    """Print all numbers"""
    for num in nums:
        print("Number:", num)


# =========================================
# MAIN EXECUTION FUNCTION
# =========================================

def main():
    print("---- PROGRAM START ----\n")

    print("Printing numbers:")
    print_numbers(numbers)

    print("\nCalculating sum:")
    total = calculate_sum(numbers)
    print("Sum is:", total)

    print("\nCalculating average:")
    avg = calculate_average(numbers)
    print("Average is:", avg)

    print("\n---- PROGRAM END ----")


# =========================================
# ENTRY POINT
# =========================================

if __name__ == "__main__":
    main()