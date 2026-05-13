# A while loop runs AGAIN and AGAIN
# until the condition becomes False.

# Syntax:
# while condition:
#     code

# 1. BASIC WHILE LOOP
i = 1

while i <= 5:
    print(i)
    i += 1   # IMPORTANT: update variable

# Output:
# 1
# 2
# 3
# 4
# 5

# If you forget to update i,
# the loop becomes an infinite loop.

# 2. INFINITE LOOP


# while True:
#     print("Runs forever")

# while True always stays True.
# Used in games, servers, menus, etc.



# 3. TAKING INPUT WITH WHILE LOOP

num = 1

while num != 0:
    num = int(input("Enter 0 to stop: "))
    print("You entered:", num)

print("Loop ended")


# Loop stops when user enters 0.



# 4. COUNTDOWN PROGRAM

count = 5

while count > 0:
    print(count)
    count -= 1

print("Blast Off!")

# Output:
# 5
# 4
# 3
# 2
# 1
# Blast Off!



# 5. while WITH else

# else runs when loop ends normally.

x = 1

while x <= 3:
    print(x)
    x += 1
else:
    print("Loop finished")

# Output:
# 1
# 2
# 3
# Loop finished


# NOTE:
# else does NOT run if loop breaks.



# 6. break STATEMENT

# break immediately exits the loop.

n = 1

while n <= 10:
    if n == 5:
        break

    print(n)
    n += 1

# Output:
# 1
# 2
# 3
# 4



# 7. continue STATEMENT

# continue skips current iteration.

n = 0

while n < 5:
    n += 1

    if n == 3:
        continue

    print(n)

# Output:
# 1
# 2
# 4
# 5



# 8. PASS STATEMENT

# pass does nothing.
# Used as placeholder.

x = 1

while x <= 3:
    pass
    break

print("pass used")


# 9. NESTED WHILE LOOP

# Loop inside another loop.

i = 1

while i <= 3:
    j = 1

    while j <= 2:
        print("i =", i, "j =", j)
        j += 1

    i += 1

# Output:
# i = 1 j = 1
# i = 1 j = 2
# i = 2 j = 1
# i = 2 j = 2
# i = 3 j = 1
# i = 3 j = 2



# 10. USING while WITH LIST

fruits = ["apple", "banana", "mango"]

i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1

# Output:
# apple
# banana
# mango



# 11. FACTORIAL USING while LOOP

num = 5
fact = 1

while num > 0:
    fact *= num
    num -= 1

print("Factorial =", fact)

# Output:
# Factorial = 120



# 12. IMPORTANT POINTS ABOUT while LOOP

# 1. while loop works on CONDITION.
# 2. Loop runs while condition is True.
# 3. Condition becomes False -> loop stops.
# 4. Updating variable is very important.
# 5. break exits loop completely.
# 6. continue skips one iteration.
# 7. else runs after normal completion.
# 8. Infinite loops are possible.
# 9. Nested while loops are allowed.
# 10. Used when number of iterations is unknown.


# 14. DIFFERENCE BETWEEN for AND while

# for loop:
# Used when iterations are known

# while loop:
# Used when iterations are unknown
# or condition-base
# 15. SHORT EXAMP

password = ""

while password != "python":
    password = input("Enter password: ")

print("Access Granted")

# Runs until correct password is entered.