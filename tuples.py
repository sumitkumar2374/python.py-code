# A tuple is an immutable data type in python ..

# empty tuple's ..
a = ()
print(a)

# tuple with only one element needs a coma ..
a = (5,)
print(a)

# tuples with more than one element's ..
a = (1,3,5,7,5,"sumit",35.45,"hello")
print(a)
print(type(a))  # ye code pta krta h ki kon sa type ka h!

# Tuples Method's ..
# 1 --> a.count(): will return of times 1 occur in a ..
a.count(1)
print(a)

# 2 --> a.index(): will return the index of first occur in a ..
a.index(3)
print(a)

# Operation in Tuples ..
# 1. Concatenation: tuple can be concatenation using the '+' operation.
tuples1 = (1,2,3)
tuples2 =(4,5,6)
concatenation = tuples1 + tuples2
print(concatenation)

# 2. Repetition: Tuples can be repeated using the '*' operator.
my_tuple = (1,2,3)
repeated = my_tuple * 3
print(repeated)

# 3. Membership: You can check if an item exists in a tuples using 'in' keyword.
my_tuple = (1,2,3)
print(2 in my_tuple)
print(4 in my_tuple)

# 4. Length: use the 'len()' function to get the length of a tuples.
my_tuple = (1,2,3,4)
print(len(my_tuple))

# 5. Min & Max: use the 'min()' & 'Max()' function to get the smallest and largest elements in a tuples..
my_tuple = (3,1,4,2)
print(min(my_tuple))
print(max(my_tuple))

# 6. Slicing: tuple support slicing to create a new tuple from a subset of the original..
my_tuple = (1,2,3,4,5)
sliced = my_tuple[1:4] # 0 index se (last_index-1) tak..
print(sliced)

# 7. Unpaking: tuples can be unpacking into individual variable..
my_tuple = (1,2,3,4)
a,b,c = my_tuple
print(a,b,c)

