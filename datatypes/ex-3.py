# Type casting / Type cohesion
# int() : to convert other types to int & complex number cannot be converted to int type
# a) float to int
print(int(10.989))
# b) complext to int : error
# print(int(10+20j))
# c) bool to int
print(int(True))
print(int(False))
# d) string to int
# string internally contains only integral value & base-10
print(int('15'))
# print(int('0B1111'))
# print(int('10.5'))


# complex (x)
# second argument should not be string
print(complex(10))
print(complex(0B1111))
print(complex(10.5))
print(complex(True))
print(complex(False))
print(complex("10.5"))
# print(complex("0B1111"))  type error
print(complex(10, 20))
print(complex(10.5, 20.6))
# print(complex("10", "20")) type error

# bool()
# int
print(bool(10))
print(bool(0))
# float
print(bool(0.0))
print(bool(0.1))
# complex
print(bool(0+0j))
print(bool(1+0j))

# str
print(bool('True'))
print(bool('False'))
print(bool('yes'))
print(bool('no'))
print(bool(''))  # false for empty string


# str()
print(str(10))
print(str(0B1111))
print(str(10.5))
print(str(10+20j))
print(str(True))
print(str(False))
