# 3. Create a class with a class attribute a; create an object from it and set ‘aʼ directly using
# ‘object.a = 0ʼ. Does this change the class attribute?

class Demo:
    a=4

obj=Demo()
print(obj.a)

obj.a=456
print(obj.a)

print(Demo.a)

# OUTPUT
# 4
# 456
# 4