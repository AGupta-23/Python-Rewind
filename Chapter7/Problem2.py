# 2. Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.


# startswith() function use
l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if name.startswith("S"):
        print("Good evening," + name)