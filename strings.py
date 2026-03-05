# A string in python can be sliced for a part of the string ..

# string immutable hoti h jisko change nhi kiya ja skta h ! ..

""" name = "hello" --> Length = 5
        --> 01234
           -5..-1 <-- """ 

# The index in a string starts from 0 to (length -1). In order to slice to slice a string. We use the following syntax ..

""" sl = name [ind_start:ind_end] 
                                  """

# ye ek string h ..
name = "sumit"

# ek string ki lenth ko print krne ke liye ..
namelength = len(name)
print(namelength)

# string ko slice ki tarah use krne ke liye code ..
# Exampl : start from index 0 to all the way till 3 (excluding 3) .. 

nameshort = name[0:3] # ye 0 --> 3 tak work hoga , lekin 3 wala include nhi hoga ..
print(nameshort)

# agr string ke kisi character wale part ko print krna h tab ..
character = name[1] # index number 1 ke liye ..
print(character)  # u print ho jayega ..

# Now , we understand negative slice ke bare me ..
print(name[-4:-1]) # sumit --> umi print hoga ..

print(name[:4]) # iska matlb h ki 0 --> (length -1) tak ..
print(name[1:]) # iska matlb h ki 1 --> lenth tak ..
print(name[1:5]) # ye wala or iske just upar wala same h , jisme ki print(name[1:]) h .. 

# Slicing with skip value ..
word = "amazing" # len --> 7
print(word[1:6:2])  # 'mzn' print hoga [me jo 2 h wo skip ya jump ke liye hota h ..]

# other advanced slicing techniques ..
# word [:7] # word [0:7] --> 'amazing'
# word [0:] # word [0:7] --> 'amazing'

# slicing with skip ka example h ..
alphabets = "abcdefghijklmopqrstuvwxyz"
print(alphabets[1:9:4]) # 'bf' print hoga ..