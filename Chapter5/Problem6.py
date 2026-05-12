# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# use key as their names. Assume that the names are unique.

d={}

f1=input("Enter your name: ")
l1=input("Enter your fav language:")

d.update({f1:l1})

f1=input("Enter your name: ")
l1=input("Enter your fav language:")

d.update({f1:l1})

f1=input("Enter your name: ")
l1=input("Enter your fav language:")

d.update({f1:l1})

f1=input("Enter your name: ")
l1=input("Enter your fav language:")

d.update({f1:l1})

print(d)
# {'Abhidha': 'English', 'Naru': 'Tamil', 'Manya': 'Hindi', 'Geeta': 'Sanskrit'}