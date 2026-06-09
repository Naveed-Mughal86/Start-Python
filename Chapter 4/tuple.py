a = (1, 2, 3, 4, 5)
print(type(a))    
    
     # unlike lists tuples are immutable their value cannot be changed
     # a[0] = 43  ❌

print(a.count(3))
print(a)

b = (6, 7, 8, 9, 10)
concatenated = a + b
print(concatenated)