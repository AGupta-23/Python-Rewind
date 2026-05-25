
list1=[1,2,3,4,5,6,7,8,9,10]

list2=[ i*i for i in list1]
print(list2)

squaredList=[]
for item in list1:
    squaredList.append(item*item)
print(squaredList)

# List comprehension in Python is a short and efficient way to create a new list using a single line of code. It allows us to generate, modify, or filter elements from an existing sequence like a list, tuple, or string using a compact syntax instead of writing multiple lines with loops. List comprehension improves code readability and reduces the amount of code needed for creating lists. It is commonly used with for loops and optional if conditions inside square brackets [].