""" Q1. write a program to print the following star pattern ..

                    *
                   ***
                  ***** for n = 3 
"""
 # user input in the form of number ..
n = int(input("Enter the number: ")) 
for i in range (1,n+1):               # range from 1 to n tak ..
    print(" " * (n-i), end = " ")     # ye wala space ke liye h ..
    print("*" * (2*n-i), end = " ")   # ye wala star ke liye h ..
    print(" ")                        # ye wala line add krega ..
    

""" Q2. Write a program to print the following star pattern.

                    *
                    **
                    ***
                    ****
                    ***** for user input ..
"""
 # user input in the form of number ..
n = int(input("Enter the number: "))
for i in range (1,n+1):
    print("*"*i, end = " ")
    print(" ")
    

""" Q3. write a program to print the following star pattern.

                    * * * * *
                    *       *
                    *       *
                    *       *
                    *       *
                    *       *
                    * * * * *  isme basically itna gap nhi rahega star ke bich me mai ya visible ke liye dekha rha hu ..
"""
 # user input in the form of number ..
n = int(input("Enter the number: "))
for i in range (1,n+1):
    if (i == 1 or i == n):
        print("*"*n, end = " ")
    else:
        print("*", end = " ")
        print(" "* (n-2), end = " ")
        print ("*", end = " ")
    print(" ")

# ye code ke bahr wala code h!
print("code will terminate ..")
    



