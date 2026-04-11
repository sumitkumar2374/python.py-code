# Some of the most used function to perform operation on or manipulates are ..

# create a string ..
name = "sumit"

# len() function - This function return the length of the strings.
print(len(name))

# String.endswith("mit") - This function_tells whether the variable string ends with the string "mit" or not. If string is "sumit", it return true for "mit" since sumit ends with mit. 
print(name.endswith("mit")) # return true

# string.startswith("su") - This function_tells whether the variable string starts with the string "su" or not. If string is "sumit" , it return true for "su" since sumit ends with su .
print(name.startswith("su")) # return true (ye case sensetive hota !)

# string.capitalize() - this function capitalize the first character of a given string.
# Note:- only 1st character ko hi capitalize krta h, example : "hello rani" --> isme 'Hello rani' ye return hoga ..
str_capital = "sumit kumar"
capitalized_str = str_capital.capitalize()
print(capitalized_str)

# string.tittle() - ye jitna bhi word h sbka 1st character capital return krta h ..
str_tittle = "free fire"
tittlized_str = str_tittle.title()
print(tittlized_str)

# string.lower() - ye jitna bhi word h sbko lower case me convert krta h ..
str_lower = "FREE FIRE"
lowered_str = str_lower.lower()
print(lowered_str)

# string.upper () - ye jitna bhi h sbko upper case me convert krega ..
str_upper = "welcome to free fire"
uppered_str = str_upper.upper()
print(uppered_str)

# string.find(word) - this function find a word and return the index of first occurence of that word in the string ..
# ye basically hme index word kitna number se start ho rha h wo batata h ..
# create h new_name string..
new_name = " rani kumari"
index = new_name.find("kumari")
print(index)

# string.replace() ..
""" string.replace - (old word , new word) :- this function replace the old word with new word in the entire string ..

# syntax --> s.replace("isme wo aayega jisko change krna h" , "isme wo aayega jo add ya replace krna h")  """
str_name = "sumit is a good good coder"
replace_str = str_name.replace("good" , "better")
print(replace_str)

# string.count() - count the totall number's of occurrence of any character ..
# In simple --> ek pura word me koi ek character kitna baar aa rha h wo count krta h ..
str_count = "abracadabra"
counted_str = str_count.count("c")
print(counted_str)

# ye end me aayega!
print("here are the full concept of string..")







