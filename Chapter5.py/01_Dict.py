# Creating Dictionary
student = {
    "name": "Aman",
    "age": 21,
    "course": "Python"
}

print(student)
# {'name': 'Aman', 'age': 21, 'course': 'Python'}

# Accessing Values
print(student["name"])      # Aman
print(student.get("age"))   # 21

# Adding New Key
student["city"] = "Delhi"
print(student)
# {'name': 'Aman', 'age': 21, 'course': 'Python', 'city': 'Delhi'}

# Updating Value
student["age"] = 22
print(student["age"])       # 22

# Removing Items
student.pop("city")
print(student)
# {'name': 'Aman', 'age': 22, 'course': 'Python'}

# Length
print(len(student))         # 3

# Keys, Values, Items
print(student.keys())       
# dict_keys(['name', 'age', 'course'])

print(student.values())     
# dict_values(['Aman', 22, 'Python'])

print(student.items())      
# dict_items([('name', 'Aman'), ('age', 22), ('course', 'Python')])

# Looping
for key in student:
    print(key, student[key])

# Membership
print("name" in student)    # True

# Nested Dictionary
data = {
    "user1": {"name": "Aman"},
    "user2": {"name": "Riya"}
}

print(data["user1"]["name"])   # Aman