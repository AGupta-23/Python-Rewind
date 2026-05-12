# Important Set Operations & Methods
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union
print(a.union(b))       
# {1, 2, 3, 4, 5, 6}

# Intersection
print(a.intersection(b)) 
# {3, 4}

# Difference
print(a.difference(b))  
# {1, 2}

# Symmetric Difference
print(a.symmetric_difference(b))  
# {1, 2, 5, 6}

# Update Set
a.update({7, 8})
print(a)
# {1, 2, 3, 4, 7, 8}

# Copy Set
newSet = a.copy()
print(newSet)

# Clear Set
newSet.clear()
print(newSet)           
# set()

# Subset
x = {1, 2}
y = {1, 2, 3}

print(x.issubset(y))    
# True

# Superset
print(y.issuperset(x))  
# True