# 1. Write a program to find the greatest of four numbers entered by the user.

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3: "))
num4=int(input("Enter num4: "))

if(num1>num2 and num1>num3 and num1>num4):
    print("num 1 is the greatest")
elif(num2>num1 and num2>num3 and num2>num4):
    print("num 2 is the greatest")
elif(num3>num1 and num3>num2 and num3>num4):
    print("num 3 is the greatest")
else:
    print("num 4 is the greatest")
