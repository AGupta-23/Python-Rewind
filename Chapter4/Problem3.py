# 3. Check that a tuple type cannot be changed in python.

tuple=(3,"44", "ax", True, 677827)
print(tuple, type(tuple))
#(3, '44', 'ax', True, 677827) <class 'tuple'>

# tuple[3]="hayahyah"  --> TypeError: 'tuple' object does not support item assignment