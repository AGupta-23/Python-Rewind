# 6. Write __str__() method to print the vector as follows:
# 7i + 8j + 10k
# Assume vector of dimension 3 for this problem.

# VECTOR CLASS

class Vector:

    def __init__(self, values):

        self.values = values


    # String Method
    def __str__(self):

        # values[0] -> i
        # values[1] -> j
        # values[2] -> k

        return f"{self.values[0]}i + {self.values[1]}j + {self.values[2]}k"



# Object
v = Vector([7, 8, 10])

print(v)