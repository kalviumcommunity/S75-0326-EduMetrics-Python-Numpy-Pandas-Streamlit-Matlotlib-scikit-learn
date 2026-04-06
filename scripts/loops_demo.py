# ===================================
# FOR LOOP EXAMPLE
# ===================================

print("---- FOR LOOP ----")

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Loop through list
for num in numbers:
    print("Current number:", num)

# Explanation:
# This loop runs 5 times because list has 5 items


# ===================================
# WHILE LOOP EXAMPLE
# ===================================

print("\n---- WHILE LOOP ----")

# Start value
count = 1

# Loop runs while condition is TRUE
while count <= 5:
    print("Count is:", count)
    
    # Update is VERY IMPORTANT
    count += 1

# Explanation:
# Loop stops when count becomes 6


# ===================================
# BREAK EXAMPLE
# ===================================

print("\n---- BREAK EXAMPLE ----")

for i in range(1, 10):
    
    if i == 5:
        print("Breaking loop at:", i)
        break   # stops loop completely
    
    print("Value:", i)

# Explanation:
# Loop stops when i becomes 5


# ===================================
# CONTINUE EXAMPLE
# ===================================

print("\n---- CONTINUE EXAMPLE ----")

for i in range(1, 6):
    
    if i == 3:
        continue   # skip this value
    
    print("Value:", i)

# Explanation:
# 3 is skipped, rest are printed


# ===================================
# INFINITE LOOP EXAMPLE (DON'T RUN)
# ===================================

# count = 1
# while count <= 5:
#     print(count)

# Problem:
# count is never updated → loop runs forever

# Fix:
# add → count += 1