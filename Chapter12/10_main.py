# In Python, if __name__ == "__main__": is used to check whether a Python file is being run directly or being imported into another file.

# Every Python file has a special built-in variable called __name__.

# If the file is run directly, Python sets:
# __name__ = "__main__"
# If the file is imported into another program, then __name__ becomes the file/module name instead of "__main__".

# So this condition:

# if __name__ == "__main__":

# means:

# "Run this code only when this file is executed directly."

# It helps prevent certain code from running automatically when the file is imported as a module.

# Example:

# def greet():
#     print("Hello")

# if __name__ == "__main__":
#     greet()
# If this file is run directly → Hello prints.
# If this file is imported somewhere else → greet() does not run automatically.

# This is mainly used for:

# testing code
# running main programs
# avoiding automatic execution during imports
# making reusable modules in Python

from module import func
func()  #-->only then this function will be called and not directly