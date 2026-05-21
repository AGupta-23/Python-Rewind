# 1. Write a program using functions to find greatest of three numbers


def func(a,b,c):

    if(a>b and a>c):
        print("a is the largest number")
    elif(b>a and b>c):
        print("b is the largest number")
    else:
        print("c is the largest number")

a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))

func(a,b,c)
