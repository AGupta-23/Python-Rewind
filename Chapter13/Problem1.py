# 1. Write a program to input name, marks and phone number of a student and format it using
# the format function like below:
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

name=input("Input name: ")
marks=int(input("Input marks: "))
MNo=input("Input Phone number: ")

s="The name of the student is {}, her marks are {} and phone number is {}".format(name,marks,MNo)
print(s)
