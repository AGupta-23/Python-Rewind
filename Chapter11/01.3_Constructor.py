# CONSTRUCTOR IN SINGLE INHERITANCE

class Employee:

    def __init__(self):
        print("Employee Constructor Called")


class Programmer(Employee):

    def __init__(self):
        print("Programmer Constructor Called")


obj = Programmer()


# OUTPUT:
# Programmer Constructor Called