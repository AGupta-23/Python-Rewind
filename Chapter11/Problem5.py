# 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator
# which calculates the sum and the dot(.) product of them.

# VECTOR CLASS

class Vector:

    def __init__(self, values):

        # Store vector values in list
        self.values = values


    # Operator Overloading for +
    def __add__(self, other):

        result = []

        # Add corresponding elements
        for i in range(len(self.values)):

            result.append(self.values[i] + other.values[i])

        return Vector(result)


    # Operator Overloading for *
    # Dot Product
    def __mul__(self, other):

        result = 0

        # Multiply corresponding elements and add them
        for i in range(len(self.values)):

            result += self.values[i] * other.values[i]

        return result


    # String Representation
    def __str__(self):

        return f"{self.values}"



# Objects
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])


# Vector Addition
print(v1 + v2)

# Dot Product
print(v1 * v2)