# Loops make it easy for a program to tell the computer which set of instruction to repeat and how! ..

""" While Loops:-

    Syntax: 
    while (condition): # The block keeps executing until the condition is true ..
        # Body of the loop ..
"""

# In while loops, the condition is checked first. If it evaluates to true, the body of the loop is executed otherwise not! ..

# Write a program to print "sumit" - 5 times ..
i = 0
while(i<5):
    print("sumit")
    i=i+1
    
# print 1 to 5 using foor loop/while loop ..
i = 1
while(i<6):
    print(i)
    i+=1
    
# Write a program to print the content of a list using while loop ..

l = [1,"Sumit","Harry","Rohan",False,"shubham","shubhi","This"]

i = 0
while(i<len(l)):
    print(l[i])
    i+=1
    
# Write a program to print multiplication table of a given number using while loop ..

n = int(input("Enter the number: "))

i = 1
while(i<11):
    print(f"{n} X {i} = {n*i}")
    i+=1
    
# Write a program to find the sum of first n natural using while loop ..

n = int(input("Enter the number: "))

i = 1
sum = 0
while(i<=n):
    sum+=i
    i+=1
print(sum)

print("The While Loop Terminated!")