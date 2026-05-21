# 7. Write a python function to remove a given word from a list and strip it at the same time.

# The strip() function in Python is a built-in string method that removes leading and trailing characters from a string, returning a new copy of the string with those characters stripped.  By default, it removes whitespace characters (such as spaces, tabs, and newlines) from both the start and end of the text.  If a specific set of characters is provided as an argument, Python treats it as a collection of individual characters to remove from either end, stopping when it encounters a character not in that set. 

def remove(list,word):
    n=[] #created an empty list

    for item in list:
        if not(item==word):
            x=item.strip(word)
            n.append(x)
    return n

list =["Abhidha", "Gupta", "Seqabh", "Female"]
print(remove(list, "Abh"))