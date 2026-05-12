# 9. Can you change the values inside a list which is contained in set S?

# s = {8, 7, 12, "Harry", [1,2]}
# s.update()


# Traceback (most recent call last):
#   File "d:\PracticePython\Chapter5\Problem9.py", line 3, in <module>
#     s = {8, 7, 12, "Harry", [1,2]}
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: unhashable type: 'list'
# PS D:\PracticePython> 
# NO - error 

s2={1,2,3,4}
s2.add(5)
print(s2)  #-->this is runnable