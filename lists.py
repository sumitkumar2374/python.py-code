# python lists are containers to store a set of any data type ..
"""example's :-
   friends = ["apple","akash","rohan",7,false] 
   1. apple --> str() 2. akash --> can store value of any datatype 3. 7 --> int() 4. bool() """
   
# create a list ..
friends = ["apple","orange","rohan",7,False,345.06]

# print index number 0 ..
print(friends[0])

# agr hmlog index number list se bahar wala print kewaye to wo error dega ..
# example :- print(friends[10])

# now we can change the index -->0 in list ..
# list --> are mutable (chanagable) ..
friends[0] = "Grapes"
print(friends[0]) # ye change hua list show krega ..

# List Method ..
# create a new list L1 ..
L1 = [1,8,7,2,15,21]

# L1.sort(): updates the list to[1,2,7,8,15,21] ..
L1.sort()
print(L1)

# L1.reverse(): update the list to [21,15,8,7,2,1]
L1.reverse()
print(L1)

# L1.append(8) at the end of the list ..
L1.append(8)
print(L1)

# L1.insert(3,8): This will add 8 at 3 index ..
L1.insert(3,8)
print(L1)

# L1.remove(21): Will remove 21 from the list ..
L1.remove(21)
print(L1)

# L1.pop(2): Will delete element at index 2 until return its value ..
L1.pop(2)
print(L1)

# agr hme pop() hua value return krwana h ..
print(L1.pop(2))
print(L1) 

# ye code ke end me aane wala code h!
print("Here is the complete code for lists in python")