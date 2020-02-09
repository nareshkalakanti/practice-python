# Imp : range data type
# rep number 0 to 10
# range is inbuild data type
# rep sequence of numbers
# range object is immutable


# Form 1 : range(n)   from 0 to n-1
r = range(10)  #  0 to 9
print(type(r))
print(r)  # range(0, 10)
for x in r:
    print(x)

# Form 2 : range(begin, end)   from begin to end-1
r = range(1, 11)  # 1 to 10

for x in r:
    print(x)

# Form 3 : range(begin, end, increment/decrement)   from begin to end-1
r = range(1, 21, 2)
for x in r:
    print(x)
r = range(20, 1, -5)
for x in r:
    print(x)

#  index and slicing
r = range(10, 21)
print(r[0])
print(r[-1])
print('################')
r1 = r[1:5]
for x in r1:
    print(x)
