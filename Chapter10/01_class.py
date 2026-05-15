# Class:
# A class is a blueprint/template for creating objects.

# Object:
# An object is an instance of a class.

class Employee:

    # Class Attributes
    name = "Abhidha"
    lang = "Py"
    salary = 3000000


# Object Creation
obj = Employee()

print(obj.name)       # Abhidha
print(obj.lang)       # Py
print(obj.salary)     # 3000000


# Creating Instance Attribute
obj.name = "Shantanu"

print(obj.name)       # Shantanu
print(obj.lang)       # Py