# FrozenSet Data type
# Exactly same as set except its immutable

# set
s = {10, 20, 30, 40}
s.add(50)
s.remove(30)
print(s)  #  {40, 10, 50, 20}

# forzen set is immuta

s2 = {10, 20, 30, 40}
fs = frozenset(s2)
print(type(fs))
# fs.add(50) attribute error
# fs.remove(50)
