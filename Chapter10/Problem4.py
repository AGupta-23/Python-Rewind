# 4. Add a static method in problem 2, to greet the user with hello.


class Calculator:

    def __init__(self, num):
        self.num=num

    def square(self):
        print(f"Square of num is: {self.num*self.num}")
    def cube(self):
        print(f"Square of num is: {self.num*self.num*self.num}")
    def cubeRoot(self):
        print(f"Square of num is: {self.num**1/2}")


    @staticmethod
    def greet():
        print("Hello User!")

obj=Calculator(4)
obj.square()
obj.cube()
obj.cubeRoot()
obj.greet()