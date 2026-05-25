# try with else in Python is used when we want some code to run only if no exception occurs in the try block. The try block contains risky code, the except block handles errors, and the else block executes only when the try block runs successfully without any error. It is useful for separating normal execution code from error-handling code.

try:
    t=int(input("Enter a numeric int value: "))
    print(t)

except Exception as e:
    print(e)

else:
 print("Inside else clause")

#else only works when try was successful