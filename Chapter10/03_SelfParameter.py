# self refers to the current object

class Employee:

    lang = "Python"
    salary = 123

    def getInfo(self):

        print(self.lang)
        print(self.salary)


obj = Employee()

obj.getInfo()

# Internally Python converts:
# obj.getInfo()

# into:
# Employee.getInfo(obj)