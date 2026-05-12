student = {
    "name": "Aman",
    "age": 21
}

# Get Value
print(student.get("name"))     
# Aman

# Update Dictionary
student.update({"city": "Delhi"})
print(student)
# {'name': 'Aman', 'age': 21, 'city': 'Delhi'}

# Remove Item
student.pop("age")
print(student)
# {'name': 'Aman', 'city': 'Delhi'}

# Remove Last Item
student.popitem()
print(student)
# {'name': 'Aman'}

# Copy Dictionary
newDict = student.copy()
print(newDict)
# {'name': 'Aman'}

# Clear Dictionary
newDict.clear()
print(newDict)
# {}

# Create Keys
keys = ("a", "b", "c")

new = dict.fromkeys(keys, 0)
print(new)
# {'a': 0, 'b': 0, 'c': 0}