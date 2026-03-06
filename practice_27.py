# A spam comment is defined as a text containing following keywords ..
# "Make a lot of money","buy now","Subscribe this", write a program to detect these spams..

# Here is some test ...
text1 = "Make a lot of money"
text2 = "buy now"
text3 = "subscribe this"
text4 = "click this"

# user input in term's of message ...
message = input("Enter your comment: ")

# condition(s) apply ..
if ((text1 in message) or (text3 in message) or (text2 in message) or (text4 in message)):
    print("This comment is a spam")
else:
    print("This comment is not a spam's")
    
# ye condition(s) ka part nhi h ..    
print("code will terminated!")
