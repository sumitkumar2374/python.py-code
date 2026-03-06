# Write a program to find the greatest of four number entered by the user ....
a1 = int(input("Enter no. 1: "))  # user niput in term's of 'a'
a2 = int(input("Enter no. 2: "))  # user niput in term's of 'a'
a3 = int(input("Enter no. 3: "))  # user niput in term's of 'a'
a4 = int(input("Enter no. 4: "))  # user niput in term's of 'a'

# condition(s) apply...
if (a1>a2 and a1>a3 and a1>a4):
    print("greatest no. is a1: ",a1)
elif (a2>a1 and a2>a3 and a2>a4):
    print("greatest no. is a2: ",a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("greatest no. is a3: ",a3)
elif(a4>a1 and a4>a2 and a4>a3):
    print("greatest no. is a4: ",a4)
else:
    print("invalaid number..")

# ye condition(s) se bahar wala code h...
print("code will terminated!")
    