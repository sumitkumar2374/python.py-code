# sets is a collection of non-repetitive elments ..

# create a empty sets ..
s = set()
print(type(s))

s = {1,5,8,32,54,5,5,5,"harry"}  # repeate nhi hoga ..
print(s) # unordered sets return hoga ..

# Method's in set's ..
# 1. s.add(): set ke andr ek element add kr skte h ..
s.add(35)
print(s,type(s))

# Operation in set's ..
# 1. len(s): return krega set's me kitna element's h ..
print(len(s))

# 2. s.remove(): ye sets me se ek element's ko remove krta h ..
# print(s.remove(8))

# 3. s.clear(): ye sets ko clear krta h ..

# 4. s.pop(): remove an arbitary element from the set and return the element removed ..

# 5. s.union({}): ye koi do sets ko merge krta h ..
s1 = {1,45,6,78}
s2 = {7,8,1,78}

print(s1.union(s2))

# 6. s.intersection({}): ye koi do set me se jo common hoga usi ko return krega ..
print(s1.intersection(s2))

# union & intersection other example's ..
u = {1,8,2,3}
print(u.union({8,11}))
print(u.intersection({8,11}))

# 7. s.issubset(): ye kisi set ka subset h to true return hoga ..
set1 = {1,2,3}
set2 = {3,4,5}
print({1,2}.issubset(set1))


