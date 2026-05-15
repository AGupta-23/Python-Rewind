class Employee:

    # Class Attributes
    lang = "Python"
    salary = 123


# Object 1
obj = Employee()

print(obj.lang)       # Python
print(obj.salary)     # 123


# Object 2
obj2 = Employee()

# Creating Instance Attribute
obj2.salary = 67537

print(obj2.salary)    # 67537

# Class attribute remains same
print(obj.salary)     # 123


# Python first checks:
# 1. Instance Attribute
# 2. Then Class Attribute