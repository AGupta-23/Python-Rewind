# The enumerate() function in Python is used to get both the index number and the value of items while looping through a sequence like a list, tuple, or string. It makes loops easier because we do not need to manually create and update a counter variable. By default, indexing starts from 0, but we can also provide a custom starting index. It is commonly used with for loops for cleaner and more readable code.


l=[1,2,3,4,5,6,7,8,9]

index=0
for item in l:
    print(f" Item at index num {index} is {item}", end =" ")
    index +=1

#using enumerate func instead

for index, item in enumerate(l):
    print(f" Item at index num {index} is {item}")
    if index==4:
        break