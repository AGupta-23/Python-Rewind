# 2. A list contains the multiplication table of 7. Write a program to convert it to vertical string
# of same numbers.
# 7
# 14
# .
# .
# .

# use join function

l=[str(7*i) for i in range(1,11)]
table="\n".join(l)
print(table)