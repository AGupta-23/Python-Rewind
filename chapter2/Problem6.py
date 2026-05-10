# 6. Write a python program to calculate the square of a number entered by the user.

a= int(input("Enter num : "))
#ValueError: invalid literal for int() with base 10: 'a'  -->runtime error if input a string literal

print("Square of a = ", a**2)