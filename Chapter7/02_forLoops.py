# for loop is used to iterate over
# sequences like list, string, tuple, range, etc.


# 1. BASIC FOR LOOP

for i in range(5):
    print(i)

# Output:
# 0 1 2 3 4


# 2. range(start, stop, step)

for i in range(1, 10, 2):
    print(i)

# Output:
# 1 3 5 7 9


# 3. LOOP THROUGH LIST

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# 4. LOOP THROUGH STRING

for ch in "Python":
    print(ch)


# 5. break

for i in range(10):
    if i == 5:
        break

    print(i)

# Stops loop completely


# 6. continue

for i in range(5):
    if i == 2:
        continue

    print(i)

# Skips current iteration


# 7. else WITH for LOOP

for i in range(3):
    print(i)
else:
    print("Loop finished")

# else runs after normal completion


# 8. NESTED FOR LOOP

for i in range(3):
    for j in range(2):
        print(i, j)


# 9. IMPORTANT POINTS

# 1. for loop is iterator-based
# 2. range() is commonly used
# 3. break exits loop
# 4. continue skips iteration
# 5. else runs if loop ends normally
# 6. Nested loops are allowed
# 7. Best when iterations are known