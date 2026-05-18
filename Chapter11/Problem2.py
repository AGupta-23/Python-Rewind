# 2. Create a class ‘Petsʼ from a class ‘Animalsʼ and further create a class ‘Dogʼ from ‘Petsʼ.
# Add a method ‘barkʼ to class ‘Dogʼ.

class Animals:

    def animal(self):
        pass

class Pets(Animals):

    def pet(self):
        pass


class Dog(Pets):

    def bark(self):
        print("Dog barks")


# Object
d = Dog()

d.bark()