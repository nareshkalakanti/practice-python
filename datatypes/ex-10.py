# dict
# If you want to represent group of objects as key value pairs
# Dictionary : word:meaning
# Order is not preserved
# Duplicate keys not allowed but value can be duplicated
# Heterogeneous objects
# mutable : changable
# indezing , slicing not applicable
# Map in Java


d = {100: 'naresh', 200: 'kumar', 300: 'kalakanti'}
print(type(d))

# create empty dic and add key:value
d1 = {}
# d[key] = value
d1[100] = 'naresh'
d1[200] = 'kalakanti'
print(d1)

# Duplicate keys not allowed but value can be duplicated
d1[100] = 'siva'  #  doesnt throw error so old value will be replaced with new value
print(d1)  # {100: 'siva', 200: 'kalakanti'}
