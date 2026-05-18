# HOW SINGLE INHERITANCE WORKS

class Parent:

    def greet(self):
        print("Good Morning")


class Child(Parent):
    pass


obj = Child()

# Child inherited greet() method from Parent
obj.greet()


# OUTPUT:
# Good Morning