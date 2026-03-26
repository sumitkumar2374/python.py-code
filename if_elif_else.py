# In python programming too, we must be able to execute instruction on a condition(s) being met.

# int ke form me user se input lena h age ke liye ..
input_age = int(input("Enter your age: "))

# if condition(s) --> condition is True ..
if(input_age>=18):
    print("You are above the age of consent")
    print("you can drive")

# elif condition(s) --> condition is True ..
elif(input_age<0):
    print("You are entering a negative invalid age")
    print("Please try again")
    
# else condition(s) --> otherwise
else:
    print("You are below the age of consent")
    
# out from if-elif-else condition(s) ..
print("Now terminate code for condition's")

    
