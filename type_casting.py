# type casting :- a number can be convert into a string and vice versa (if possible)
# simple :- iske help se koi sa bhi data type ko hm another data type me convert kr skte h ..

a = "31.2" # "31.2" --> string h 

b = float(a) # isme a --> 'str' hjisko float me convert kiya ja rha h ..
t = type(b)

print(t)  # <class 'float'>

# example 01
a = 5  # int
b = 2.5  # float

c = a + b
print(c)        # 7.5
print(type(c))  # float
   
# example 02
x = "10"   # x--> 'str'
y = int(x) # 'str' --> 'int'

print(y)   # y --> 10
print(type(y))  # <class'int'>


# example 03
x = "10.5"  # x --> 'str'
y = float(x)  # 'str' --> 'float'

print(y)       # y = 10.5
print(type(y))  # <class'float'>


# example 04
x = 100
y = str(x) # 'int' --> 'str'

print(y)    # y = 100
print(type(y))  # <class'str'>


# example 05
x = "hello" # x--> 'str'
y = list(x)  # 'str' --> 'list'

print(y)     # ['h','e','l','l','o']

# here are the complete explaination of type_casting ..
