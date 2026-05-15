# 7. Write a program to print the following star pattern.
#  for n = 3

#   *
#  ***
# *****


# spaces
# i=1, spaces=2  --> 3-1=2 -->n-1=2
# i=2, spaces=1
# i=3, spaces=0

# stars
# i=1 print 1  --> 2*i-1
# i=2 print 3
# i=3 print 5
# odd series 

n=int(input("Input pattern lines number: "))
for i in range (1,n+1):

    print( " " *(n-i), end="")
    print("*" *(2*i-1), end="")
    print("")