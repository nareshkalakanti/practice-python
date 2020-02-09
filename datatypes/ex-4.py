# Fundamental data types vs immutability
# example 1
x = 10
print(id(x))
x = x+1
print(id(x))

# example 2
a = 10
b = a
# pointing to same address
print(id(a))
print(id(b))
b = b+1
print(a)
print(b)
# pointing to different address
print(id(a))
print(id(b))
