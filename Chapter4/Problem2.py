# 2. Write a program to accept marks of 3 students and display them in a sorted manner.

Marks=[]  #-->empty list

f1=input("Enter marks 1: ")
Marks.append(f1)

f2=input("Enter marks 2: ")
Marks.append(f2)

f3=input("Enter marks 3: ")
Marks.append(f3)

Marks.sort()
print(Marks)