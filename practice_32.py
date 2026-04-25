# Write a program using function to find greatest of three numbers.

# here are the given value of a, b & c ..
a = 4
b = 10
c = 20

# Now using function print above the question..
def greatest(a,b,c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>b and c>a):
        return c

# now print the greatest of three number's..
print(f"gratest number is: {greatest(a,b,c)}")