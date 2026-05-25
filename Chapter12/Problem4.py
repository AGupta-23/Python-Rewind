# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionErrorʼ .

a=int(input("Value of a : "))
b=int(input("Value of b : "))

try:
    print(a/b)

except ZeroDivisionError:
    print("Infinite")