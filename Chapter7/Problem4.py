# 4. Write a program to find whether a given number is prime or not.

# prime - divided by 1 or itself

n=int(input("Enter ur number: "))

for i in range(2,n):
    if(n%i==0):
        print("Number turns not Prime")
        break
else:
    print("Number is prime")
