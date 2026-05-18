# MULTIPLE INHERITANCE WITH SAME METHOD NAME

class A:

    def show(self):
        print("Class A")


class B:

    def show(self):
        print("Class B")


# A is checked first because it comes first
class C(A, B):
    pass


obj = C()

obj.show()


# OUTPUT:
# Class A