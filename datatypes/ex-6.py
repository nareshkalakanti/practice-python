# Collection related data types :
# A.List
# Group of objects as single entity
# Duplicates allowed + order is preserved
# heterogenious object are allowed like ex int , str
# indexing and slicing concept applicable
# list is growable in nature [ since we can add and delete object in list ]
# list is mutable : perform modification to object
# [10,20,30,40]- list
# (10,20,30) - tuple
# {10,20,30 } - set
# {10:'naresh', 200:'ravi} -dict

l = [10, 'naresh', 10, 20, 30]
print(type(l))
print(l)  # order is preserved as stored
print(l[0])
print(l[-1])  #  indexing applicable [last elemment]
print(l[1:4])  # list of elements from 1 index to (4-1) index
l = []  #  empty list
# add elements to the list we need to use append
# insertion order will be preserved
l.append(10)
l.append(20)
l.append(30)
l.append(40)
print(l)
l.remove(30)
print(l)

# example 2
l2 = [10, 20, 30, 40]
l2[0] = 7777
print(l2)
