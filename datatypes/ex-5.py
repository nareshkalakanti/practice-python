# example for need of immutability
# python virtual machine is responsible for creating object
# checks object with required content
# Three ref variable pointing to same object
# memory utilization is improved
# performance will be improved
# PVM does search operation will take less time | create operation will take more time
a = 10
b = 10
c = 10
print(id(a))
print(id(b))
print(id(c))

# bool
x = True
y = True
print(x is y)

# str
i = "naresh"
j = "naresh"
print(i is j)

# Complex type immutability not available
k = 10+20j
l = 10+20j
# print(k is l) flase

# example list
# list group of objects
# rep mutiple values
# access using index : python is zero index based
# All fundamental data types are immutable
m = 10
n = [10, 20, 30, 40]
# list is mutable
# all changes will happen in existing object only
print(id(n))
print(n[0])
print(id(n))
o = [10, 20, 30, 40]
n = o
print(n)
print(o)
n[0] = 5555
print(n)
print(o)

o[0] = 7777
print(n)
print(o)
