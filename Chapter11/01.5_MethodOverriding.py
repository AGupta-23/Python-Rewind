# METHOD OVERRIDING IN INHERITANCE

class Animal:

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    # Overriding parent method
    def sound(self):
        print("Dog barks")


obj = Dog()

obj.sound()


# OUTPUT:
# Dog barks