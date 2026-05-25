# 2. Write a program to print third, fifth and seventh element from a list using enumerate
# function.


l=[0,1,2,3,4,5,6,7,8,9]

for i, item in enumerate(l):
    if i==3 or i==5 or i==7:
        print(i , item)