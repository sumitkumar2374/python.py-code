# Dictionary is a collection of keys-value pair's ..

# Syntax:-
a = {"key":"value",   # key wale side me hmlog 'int' & 'str' bhi ho skta h ..
     "sumit":"code",
     "marks":"95",
     "list":[1,2,3]
}

print(a["key"])  # return "value"
print(a["list"])   # return [1,2,3]
print(a,type(a)) # pehle return a hoga, phir type of a return hoga ..

# # Methods of dictionary ..
# 1. a.item(): ye tuples ke form me dict. ko return krta h..
print(a.items())

# 2. a.keys(): ye key wale side me jo jo h usko return krta h..
print(a.keys())

# 3. a.values(): ye values ki taraf wala ko return krta h..
print(a.values())

# 4. a.update(): iske help se hm dict. me update kr skte h..
a.update({"sumit":"99", "rani":"100"})
print(a)

# 5. a.get(): ye hme keys ki value's return krta h..
print(a.get("sumit"))

""" print(a.get("sumit2")) --> ye hme None return krega ..
    print(a["sumit2"]) --> ye hme error dega, dono same hi chiz return krta h pr error ke case me alag .. """

# 5. a.clear(): dict. ko clear krta h ..
# print(a.clear())  # {} --> clear ho jayega..
print(a)

# 6. a.pop(key,default): ye method ka use hm dict. se kisi specific key ko remove krane ke liye hota h-aur saath hi us key ki value key ki value return bhi krta h.. 
remov_value = a.pop("marks")
print(remov_value)  # 95
print(a) # ye marks wala section remove kr dega ..