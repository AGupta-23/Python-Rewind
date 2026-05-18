# Parent Class / Base Class
class Employee:

    company = "Google"

    def show_details(self):
        print("This is an employee")
        print("Company:", self.company)


# Child Class / Derived Class
# Programmer inherits Employee
class Programmer(Employee):

    language = "Python"

    def show_language(self):
        print("Programming Language:", self.language)


# Creating object of child class
obj = Programmer()

# Child class can access its own method
obj.show_language()

# Child class can also access parent class method
obj.show_details()

# Child class can also access parent class attributes
print(obj.company)



# OUTPUT:
# Programming Language: Python
# This is an employee
# Company: Google
# Google