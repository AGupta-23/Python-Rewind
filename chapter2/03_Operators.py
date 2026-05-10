# Arithmetic Operators
print(10 + 5)   # 15
print(10 - 5)   # 5
print(10 * 5)   # 50
print(10 / 5)   # 2.0  -->always gives float results
print(10 % 3)   # 1    -->modulus gives remainder
print(10 ** 2)  # 100  -->square
print(10 // 3)  # 3    -->floor division always gives quotient result towards -ve axis of number system


# Comparison Operators -->Only gives answer in True/False
print(10 == 10) # True
print(10 != 5)  # True
print(10 > 5)   # True
print(10 < 5)   # False
print(10 >= 10) # True
print(10 <= 5)  # False


# Logical Operators   -->according to truth tables
print(True and False) # False
print(True or False)  # True
print(not True)       # False


# Assignment Operators
x = 5
x += 2
print(x) # 7

x -= 1
print(x) # 6

x *= 2
print(x) # 12


# Membership Operators
print("a" in "apple")     # True
print("z" not in "apple") # True


# Identity Operators
a = [1, 2]
b = a

print(a is b)     # True
print(a is not b) # False


# Bitwise Operators
print(5 & 3) # 1
print(5 | 3) # 7
print(5 ^ 3) # 6