# 5. Write a program to find the sum of first n natural numbers using while loop.

n=int(input("Enter the limit for 1st n natural numbers sum : "))
sum=0
i=1
while i<n+1:
    sum=i+sum
    i+=1

print(sum)
