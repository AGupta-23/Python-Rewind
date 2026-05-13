# 3. A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

msg=["Make a lot of money" , "buy now","subscribe this",'click this' ]

n=input("Enter a msg: ")

if n in msg:
    print("Spam detected")
else:
    print("Msg clear and not fraud")