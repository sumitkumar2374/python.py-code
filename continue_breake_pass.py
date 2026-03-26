""" Continue Statement: 
                    Continue is used to stop the current iteration of the loop and continue with the next one. It instructs the program to "skip this iteration" ..
"""
# write a program using continue statements ..
for i in range (0,4):
    if i == 2:
         continue
    print(i)
    
""" Breake statements: 
                    Breake is used to come out of the loop when encountered. It instructs the program to exist the loop now ..
"""

# write a program using breake statements ..
for i in range(0,80):
    if i == 3:
        break
    print(i)
    
""" Pass Statements:
                Pass is a null statements in python in instruct to "do nothing" ..
"""

# write a program using pass statements ..
l = [1,7,8]
for item in l:
    pass        # ye likhne se hoga kya ki agr ye code hme yaha tak bhi chor ke apna dusra code ko age bada skte h.
                # without any error ke .. 

# ye code loop se bahr h ..
print("Code will ending ..")