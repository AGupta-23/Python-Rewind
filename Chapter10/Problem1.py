# 1. Create a class “Programmer” for storing information of few programmers working at
# Microsoft.

class Programmer:

    company="Microsoft" 

    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
        print("Information retracted!")

obj=Programmer("Abhidha", "30Lakhs")
print(obj.name, obj.company, obj.salary)