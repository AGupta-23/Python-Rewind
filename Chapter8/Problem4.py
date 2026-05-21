# 4. Write a recursive function to calculate the sum of first n natural numbers.


def func(n):
    # base case
    if n==1:
        return 1
    else:
        return n + func(n-1)

print(func(6))