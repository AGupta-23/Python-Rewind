# 2. Write a python program using function to convert Celsius to Fahrenheit.

# round(value, places) function rounds the value to c places

def f_to_c(f):
    c=(5*(f-32))/9
    return c

f=int(input("Enter temp in F: "))
c=f_to_c(f)
print(f"{round(c,2)} Degree C ")