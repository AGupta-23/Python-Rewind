# 7. Override the __len__() method on vector of problem 5 to display the dimension of the
# vector.

class Vector:
    def __init__(self,l):
        self.l=l
    
    def __len__(self):
        return len(self.l)

obj=Vector([1,56,7])
print(len(obj))    #-->3