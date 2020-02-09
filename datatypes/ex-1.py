s = 'naresh'
# print Naresh
t = s[0].upper() + s[1:]
print(t)

# print naresH
t1 = s[0: len(s)-1] + s[-1].upper()
print(t1)

# print NaresH

t2 = s[0].upper()+s[1:len(s)-1]+s[-1].upper()
print(t2)
