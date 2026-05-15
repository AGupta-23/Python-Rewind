# 6. Write a program to calculate the factorial of a given number using for loop.

n=int(input("Enter a value: "))
prod=1
for i in range(1,n+1):
    prod=i*prod

print(f"Factorial of n is {prod}")