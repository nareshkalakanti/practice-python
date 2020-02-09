# bytes data type
# represents group of byte values
# handle images etc byte data type to handle
# values only from 0 to 255
# immutable by default
l = [10, 20, 30, 40]
b = bytes(l)
print(type(b))

for x in b:
    print(x)

# bytearray :
# Muttable
l = [10, 20, 30, 40]
b = bytearray(l)
print(type(b))
print(b[0])
print(b[-1])
b[0] = 77
for x in b:
    print(x)
