# Lambda Function in Python
# A lambda function is a small anonymous function in Python.

# Anonymous means:
# The function has no name

# It is mainly used for:
# Short operations
# One-line functions
# Temporary functions

# Syntax
# lambda arguments : expression
# lambda → keyword used to create lambda function
# arguments → input values
# expression → operation performed and returned automatically

square=lambda x: x*x
print(square(6))

sum=lambda s,t,r: s+t+r
print(sum(3,4,5))

# Important Points About Lambda Functions
# Single-line function
# No def keyword needed
# No function name required
# Automatically returns value
# Can take multiple arguments
# Mostly used with:
# map()
# filter()
# sorted()