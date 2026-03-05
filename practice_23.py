# what will be the length of following set s ..

# create a empty set ..
s = set()

# add 20 in a set ..
s.add(20)

# again add 20.0 in a set ..
# python me 20 == 20.0 same h set me, but return me ye exist nhi krega kyuki dono same h to set me unique value hi return hoga!
s.add(20.0)    

# add '20' as a 'str' in a set ..
s.add("20")

# return set ..
print(s)

# return length of set ..
print(len(s))