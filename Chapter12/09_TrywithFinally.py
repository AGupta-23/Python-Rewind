# try with finally in Python is used when we want some code to execute no matter what happens, whether an exception occurs or not. The finally block always runs after the try and except blocks. It is commonly used for important cleanup tasks like closing files, database connections, or releasing resources. Even if the program returns from a function or an error occurs, the finally block still executes.

def main():

    try:
        a=int(input("Enter a numeric value: "))
        print(a)
        return 
    
    except Exception as e:
        print(e)
        return
    
    finally:
        print("Finally will get executed anyhow")

main()