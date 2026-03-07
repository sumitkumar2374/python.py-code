# Write a program to calculate the grade of a student's from his mark's the following scheme ..

""" 90 - 100 --> EX
    80 - 90 --> A
    70 - 80 --> B
    60 - 70 --> C
    50 - 60 --> D
         <50 -->F 
"""
# User input ..
marks = int(input("Enter your mark's: "))

# if-elif conditions..
if (marks<=100 and marks>=90):
    grade = "Ex"
elif (marks<=90 and marks>=80):
    grade = "A"
elif (marks<=80 and marks>=70):
    grade = "B"
elif (marks<=70 and marks>=60):
    grade = "C"
elif (marks<=60 and marks>=50):
    grade = "D"
elif (marks<50):
    grade = "F"

# print grade ..
print("Your grade is: ",grade)

# end of code ..
print("code will terminated!")