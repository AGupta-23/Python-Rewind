# MULTIPLE INHERITANCE
# One child class inherits from multiple parent classes

class Father:

    def skill1(self):
        print("Father: Gardening")


class Mother:

    def skill2(self):
        print("Mother: Cooking")


# Child inherits both Father and Mother
class Child(Father, Mother):

    def skill3(self):
        print("Child: Python Programming")


obj = Child()

# Accessing methods from both parent classes
obj.skill1()
obj.skill2()

# Accessing child method
obj.skill3()


# OUTPUT:
# Father: Gardening
# Mother: Cooking
# Child: Python Programming