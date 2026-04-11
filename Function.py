""" Functions:
            A function is a group of statement performing a specific task ..
            When a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code is doing what! ..
            A function can be reused by the programmer in a given program any number of .. """
            
# Syntax:
def func1():
    print("hello")  # This Function can be call any number of times, anywhere in the program ..

            
""" Function call:
                Whenever we want to call a function, we put the name of the function followed by parentheses as follows .. """
                
# Syntax:
func1()  # This is called function call ..

""" Function Defination:
                The part containing the exact set of instructions which are executed during the function call.. """
                
# Q. Write a program to greet a user with "Good Day" using functions ..
def goodDay():
    print("Good Day")
goodDay()


# Type of Functions ..
""" Type of function in python: 
    These are two type of function in python ..
    
    1. Built in functions (EX: print(), range(), len() etc..)
    2. user defined functions (EX: func1(), printHello(), greet() etc ..) """

 
 # Function with arguments ..   
""" Function with arguments:
                        A function can accept some value it can work with we can put these valuese in the parenthese..
                        A function can also return value as show below.. """
# EXAMPLE:-                    
def goodDay(name,ending):
    print("Good day" + name)
    print(ending)
    
goodDay("Harry","Thank you")
goodDay("Rohan","Thank You")
goodDay("Divya","Thank You")


# Default parameter value ..
""" Default Parameter Value:-
    
    1. We can have a value as default as default argument in a function ..
    2. If we specify name = "stranger" in the line containing def this value is used when no argument is passsed."""
# EXAMPLE 1.  
def greet (name = "stranger"):
    # function body
    greet()
    greet("Harry")
    
# EXAMPLE 2.
def goodDay (name,ending = "Thank You"):
    print(f"Good Day,{name}")
    print(ending)
    
goodDay("Harry","Thanks")
goodDay("Rohan")          # isme by default parameter add ho jayega!

# ye line function ke bahr wali line h!
print("Here are the full theory and code for functions in python!")
    