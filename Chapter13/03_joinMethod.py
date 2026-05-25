# join() Function in Python
# The join() function is used to combine multiple strings into a single string.
# It joins the elements of a list, tuple, or other iterable using a specified separator.

# Syntax
# "separator".join(iterable)
# "separator" → the string placed between elements
# iterable → list/tuple containing strings

l=["apple", "carrot", "banana"]

result="-".join(l)
print(result)

# Important Points
# Works only with strings
# Returns a new string

# Common separators:
# " " → space
# "," → comma
# "-" → hyphen
# "\n" → new line

# Uses of join()
# Combining words into sentences
# Formatting output
# Creating CSV-style text
# Building strings efficiently