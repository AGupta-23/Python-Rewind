# The raise keyword in Python is used to manually generate an exception or error during program execution. 
# It allows the programmer to stop the normal flow of the program and display a specific error when a certain condition occurs. raise is commonly used when the built-in errors are not enough or when we want to create custom validation rules in a program. 
# For example, if a user enters a negative age or invalid value, we can use raise to generate an appropriate exception. It helps in better error handling, debugging, and making programs more secure and controlled.

a=int(input("Enter a value: "))
b=int(input("Enter a value: "))

if(b==0):
    raise ZeroDivisionError("Cannot divide a number by 0")

else:
    print(f"{a/b} is the answer when {b} divides {a}")

