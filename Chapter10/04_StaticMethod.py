# Static methods do not use self parameter

class Employee:

    lang = "Python"
    salary = 123

    @staticmethod
    def greet():

        print("Good Morning")


obj = Employee()

obj.greet()       # Good Morning


# Static method is used when
# no object data is needed