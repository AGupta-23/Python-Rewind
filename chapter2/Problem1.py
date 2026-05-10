# 1. Write a python program to add two numbers.

a= int(input("Enter num 1 : "))
#ValueError: invalid literal for int() with base 10: 'a'  -->runtime error if input a string literal
b= int(input("Enter num 2 : "))
print("sum = ", a+b)
