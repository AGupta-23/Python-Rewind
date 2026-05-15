# 9. Write a program to print the following star pattern.
# ***
# * * for n = 3
# ***

# when i==1, i==n print * --> i --n times
# when else print * once then print * -- 

n=int(input("Input pattern lines number: "))
for i in range (1,n+1):
    if (i==1 or i==n):
        print ("*" * n, end="")
    else:
        print( "*", end="")
        print(" " *(n-2), end="")
        print( "*", end="")
    print("")