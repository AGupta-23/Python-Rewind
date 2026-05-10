# 1. BASIC VARIABLES
name = "AG"
age = 20
height = 5.9
is_student = True

print(name)
print(age)
print(height)
print(is_student)

# 2. MULTIPLE VARIABLES
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)

# 3. SAME VALUE TO MULTIPLE VARIABLES
x = y = z = 100

print(x)
print(y)
print(z)

# 4. VARIABLE REASSIGNMENT
score = 50
print(score)

score = 90
print(score)

# 5. VARIABLE NAME RULES
# VALID VARIABLE NAMES
student_name = "Rahul"
studentName = "Aman"
_student = "Karan"
student123 = "Riya"

print(student_name)
print(studentName)
print(_student)
print(student123)

# 6. INVALID VARIABLE NAMES
# 1student = "ABC"      # Cannot start with number
# student-name = "ABC"  # Hyphen not allowed
# student name = "ABC"  # Spaces not allowed
# class = "Python"      # Keywords not allowed

# 7. CASE SENSITIVE VARIABLES
name = "AG"
Name = "Python"

print(name)
print(Name)

# 8. SWAP VARIABLES
a = 5
b = 10

print("Before swap:")
print(a, b)

a, b = b, a

print("After swap:")
print(a, b)

# 9. CONSTANT STYLE VARIABLES
# (Python doesn't enforce constants)
PI = 3.14159
MAX_USERS = 1000

print(PI)
print(MAX_USERS)

# 10. DELETE VARIABLE
temp = 500
print(temp)

del temp

# print(temp)  # Error: variable deleted
