# HIERARCHICAL INHERITANCE
# Multiple child classes inherit one parent class

class Parent:

    def show(self):
        print("Parent Class")


class Child1(Parent):
    pass


class Child2(Parent):
    pass


obj1 = Child1()
obj2 = Child2()

obj1.show()
obj2.show()