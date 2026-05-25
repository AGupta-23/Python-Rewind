# The global keyword is used to modify a global variable inside a function.

x = 10   # global variable

def change():
    global x
    x = 50   # changes global variable
    print(x)

print(x)
change()
print(x)