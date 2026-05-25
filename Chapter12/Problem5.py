# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt .

n=int(input("Enter a value:"))

Table=[i*n for i in range(1,11)]
print(Table)

with open("Tables.txt", "a") as f:
    f.write(f" Table of {n} is {str(Table)} \n")

# Your code already creates the file in the same folder where the Python file is running. - so if we run inside cd folder name then file created inside it otherwise the parent folder
