# Tuple : datatype
# exactly same as List except it is immutable
# Read only version of List is Tuple
# slicing and indexing applicable

t = (10, 20, 30, 10, 'naresh')
print(type(t))
print(t[0])
print(t[-1])
print(t[1:4])
#t[0] = 7777
# print(t) # TypeError
# t.append(50) # Attribute error
# t.remove(50)

## imp ###

t2 = ()  #  empty tuple
print(type(t2))

# int type
t2 = (10)
print(type(t2))  #  int its not tuple

# single value tuple we need to add ,
t2 = (10, )
print(type(t2))  #  int its not tuple
