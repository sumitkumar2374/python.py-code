# A for loop is used to iterate through a sequence like list, tuples or string [iterables] ..

""" Syntax:
    l = [1,4,7]
    for item in l:
        print(item) # print 1,4,7
"""
# print tuples using for loops ..
t = (6,231,75,122)
for i in t:
    print(i)
    
# print list using for loop ..
l = [1,4,6,234,6,764]
for i in l:
    print(i)
    
# print string using for loop ..
s = "sumit"
for i in s:
    print(i)
    
# write a program to print multiplication table of a given number using for loop ..
n = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
    
# write a program to calculate the factorial of a given number using for loop ..
n = int(input("Enter the number: "))
product = 1
for i in range (1,n+1):
    product = product*1
print(f"The factorial of {n} is {product}")

# Write a program to find whether a given number is prime or not ..

n = int(input("Enter the number: "))
for i in range (2,n):
    if (n%i) == 0:
        print("Number is not prime")
        break
else:
    print("number is prime")
    
# write a program to print multiplication table of a given number using while loop ..
n = int(input("Enter the number: "))
for i in range (2,n):
    if (n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")
    
    
""" For Loop with ELSE: 
                    An optional else can be used with a for loop if the code is to be executed when the loop exhausts ..
                    
                    Syntax:
                    l = [create anything..]
                    for condition(s):
                        print()
                    else:
                    print() # this is printed when the loop exhausted!    
"""
# write a program for loop with else ..
l = [1,7,8]
for item in l:
    print(item)
else:
    print("done") # this is printed when the loop exhausted!
    
    
""" Range function in python:
                        The range() function in python is used to generate a sequence of number, we can also specify the start, stop and step - size as follows:
                        
                        range (start, stop, steps_size)
                        # step_size is usually not used with range()
"""
# An example: Demonstrating range() function ..
for i in range(0,7):  # range (7) can also be used ..
    print(i)          # print 0 to 6 ..

# example of step - size ..
for i in range (0,100,4):   # 4 ka jum hoga 0 to 100 tak me jitna bhi output return ho ..
    print(i)
    
# output: 0 4 8 12 etc..