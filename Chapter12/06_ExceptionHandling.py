# Exception handling in Python is a method used to handle runtime errors so that the program does not crash suddenly. Errors such as dividing by zero, entering invalid input, accessing wrong indexes, or using incorrect data types can stop normal program execution. To avoid this, Python uses try and except blocks. The code that may cause an error is written inside the try block, and if an error occurs, Python immediately transfers control to the except block where the error is handled properly. 
# This allows the remaining program to continue executing normally. Python also provides else and finally blocks, where else runs if no error occurs and finally runs in every situation whether an error occurs or not.


try:
    t=int(input("Enter a numeric int value: "))
    print(t)

except Exception as e:
    print(e)

print("Code ended")

#different types of custom exceptions-
# Important Exception Types

# 1. ZeroDivisionError
# Occurs when dividing by zero.
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")

# 2. ValueError
# Occurs when invalid value is given.
try:
    n = int("abc")

except ValueError:
    print("Invalid integer")

# 3. TypeError
# Occurs when wrong data types are used together.
try:
    print("5" + 5)

except TypeError:
    print("Type mismatch")

# 4. IndexError
# Occurs when invalid list index is used.
try:
    l = [1, 2, 3]
    print(l[5])

except IndexError:
    print("Index out of range")

# 5. KeyError
# Occurs when dictionary key does not exist.
try:
    d = {"name": "Harry"}
    print(d["age"])

except KeyError:
    print("Key not found")

# Using Multiple Exceptions
try:
    a = int(input("Enter number: "))
    print(10 / a)

except ValueError:
    print("Enter valid integer")

except ZeroDivisionError:
    print("Cannot divide by zero")


# Simple Real-Life Analogy
# Think of exception handling like:
# Try to ride a bike.
# If you fall, handle the injury.
# Then continue life normally.
# Program also continues normally after handling errors.