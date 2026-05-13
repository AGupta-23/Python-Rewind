# 7. Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter the post: ")

post_lower = post.lower()


print("Lowercase Post:", post_lower)


if "harry" in post_lower:
    print("This post is talking about Harry")
else:
    print("This post is NOT talking about Harry")