# CALLING PARENT CONSTRUCTOR USING super()

class Employee:

    def __init__(self):
        print("Employee Constructor Called")


class Programmer(Employee):

    def __init__(self):

        # Calls parent constructor
        super().__init__()

        print("Programmer Constructor Called")


obj = Programmer()


# OUTPUT:
# Employee Constructor Called
# Programmer Constructor Called