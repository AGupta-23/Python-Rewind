# __init__ runs automatically
# when object is created

class Employee:

    def __init__(self, name, salary, lang):

        self.name = name
        self.salary = salary
        self.lang = lang

        print("Object Created")


obj = Employee("Shantanu", 120000, "Python")

print(obj.name)       # Shantanu
print(obj.salary)     # 120000
print(obj.lang)       # Python


# Constructor is mainly used
# to initialize object data