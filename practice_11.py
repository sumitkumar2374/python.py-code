# Write a program to fill in a letter template given below with name and date ..

""" Dear <|Name|>,
    you are selected!
    <|Date|> """

# create a string ..
letter = '''Dear <|Name|>,
    you are selected!
    <|Date|> '''

# using replace string function replace name & date ..
print(letter.replace("<|Name|>","sumit").replace("<|Date|>","XX july 20XX"))
    
