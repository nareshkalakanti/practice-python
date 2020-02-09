# Set Data Type
# Duplicates not allowed
# Order not required
# Mathematic sets => s1 = {1,2,3} s2 = {2,3,1} s3 = {1,3,2} [equal]
# index order not applicable
# indexing and slicing  not applicable
# Heterogenous objects ae allowed
# set is growable
# set is mutable
s = {10, 20, 30}
print(type(s))
s = {10, 20, 10, 'naresh', 30, 40}
print(s)  # o/p : {40, 10, 'naresh', 20, 30} order is not preserved
# print(s[0])  # type error : set object doesnot support indexing
# print(s[1:4])
s.add(50)
print(s)
s.remove(30)
print(s)

# ex : append() vs add()
# append = existing + new content 50 will be added at last
l = [10, 20, 30, 40]
l.append(50)
print(l)  # [10, 20, 30, 40, 50]

# it can add anywhere
s1 = {10, 20, 30, 40}
s1.add(50)
print(s1)  # {40, 10, 50, 20, 30}

# Important example
# empty set
s = {}
print(type(s))  # dict type

# how to create empty set
s = set()  #  by using set() function
print(type(s))
