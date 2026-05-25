# 3. Write a program to filter a list of numbers which are divisible by 5.

l=[25, 5, 9, 10,34]

def func(i):
        if i%5==0:
            return True
        return False
    
f=list(filter(func,l))
print(f)