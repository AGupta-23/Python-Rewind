# 5. Write a python program to find an average of two numbers entered by the user.

a= int(input("Enter num 1 : "))
#ValueError: invalid literal for int() with base 10: 'a'  -->runtime error if input a string literal
b= int(input("Enter num 2 : "))
# print("sum = ", a+b) --> whole prior code used from problem 1

print(a+b/2) #-->does not give proper result
print((a+b)/2) #-->does not give proper result
