# MULTILEVEL INHERITANCE
# Grandparent -> Parent -> Child

class Grandfather:

    def house(self):
        print("Grandfather's House")


class Father(Grandfather):

    def car(self):
        print("Father's Car")


class Son(Father):

    def laptop(self):
        print("Son's Laptop")


obj = Son()

# Son can access methods from all classes
obj.house()
obj.car()
obj.laptop()


# OUTPUT:
# Grandfather's House
# Father's Car
# Son's Laptop