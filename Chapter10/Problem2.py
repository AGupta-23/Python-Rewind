# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:

    def __init__(self, num):
        self.num=num

    def square(self):
        print(f"Square of num is: {self.num*self.num}")
    def cube(self):
        print(f"Square of num is: {self.num*self.num*self.num}")
    def cubeRoot(self):
        print(f"Square of num is: {self.num**1/2}")

obj=Calculator(4)
obj.square()
obj.cube()
obj.cubeRoot()