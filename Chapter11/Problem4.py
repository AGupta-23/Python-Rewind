# 4. Write a class ‘Complexʼ to represent complex numbers, along with overloaded operators
# ‘+ʼ and ‘*ʼ which adds and multiplies them.
class Complex:

    def __init__(self, real, imaginary):

        # Real part
        self.real = real

        # Imaginary part
        self.imaginary = imaginary


    # Operator Overloading for +
    def __add__(self, other):

        # Formula:
        # (a + bi) + (c + di)
        # = (a+c) + (b+d)i

        return Complex(
            self.real + other.real,
            self.imaginary + other.imaginary
        )


    # Operator Overloading for *
    def __mul__(self, other):

        # Formula:
        # (a + bi)(c + di)
        # = (ac - bd) + (ad + bc)i

        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)

        imaginary_part = (self.real * other.imaginary) + (self.imaginary * other.real)

        return Complex(real_part, imaginary_part)


    # String Representation
    def __str__(self):

        return f"{self.real} + {self.imaginary}i"



# Objects
c1 = Complex(1, 2)     # 1 + 2i
c2 = Complex(3, 4)     # 3 + 4i


# Addition
print(c1 + c2)

# Multiplication
print(c1 * c2)