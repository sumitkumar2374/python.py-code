""" Recursion: 
            Recursion is a function which call itself..
            It's used to directly use a mathematical as function.. 
            
            EXAMPLE:
                factorial(n) = n x factorial (n-1)
                This function can be defined as follows: """
                
# Print Factorial using recursion ..
n = int(input("Enter a number: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
print(f"The Factorial of this number is: {factorial(n)}")

"""     This work as follows:
            
            Factorial(5)
            5 x Factorial(4)
            5 x 4 x Factorial(3)
            5 x 4 x 3 Factorial(2)
            5 x 4 x 3 x 2 Factorial(1)
            5 x 4 x 3 x 2 x 1   -----> 120     """ 
            
            


