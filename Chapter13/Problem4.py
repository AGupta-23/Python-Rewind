# 4. Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce
l=[111,2,3,4,5,6,8764]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))
