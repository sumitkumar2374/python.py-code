# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user..

marks1 = int(input("Enter marks1: "))  # user input in term's of marks
marks2 = int(input("Enter marks2: "))  # user input in term's of marks
marks3 = int(input("Enter marks3: "))  # user input in term's of marks
marks4 = int(input("Enter marks4: "))  # user input in term's of marks

# total_percentage formula use..
total_percentage = ((marks1+marks2+marks3+marks4)*100)/300

# condition(s) apply..
if (total_percentage>=40):
    print("You are passed: ",total_percentage)
else:
    print("You failed try again: ",total_percentage)

# ye condition ke bahar h ..
print("Code will terminated!")
    
