# Write a program to find out weather a given post is talking about "Harry" or not ..

# User input ..
post = input("Enter the post: ")

# If-else conditions ..
if ("Harry".lower() in post.lower()):
    print("This post is talking about harry")
else:
    print("This post is not talking about harry")
    
# ye condition ka part nhi h ..
print("code will terminated!")