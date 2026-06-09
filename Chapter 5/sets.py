s = {1, 2, 3, 4} # this is a set 
# to make an empty set we will use the following
a = set()    # this is an empty set 
# print(type(a))

b = {}   # this is an empty dict
# print(type(b))

 # Methods of sets
        # there is no repetition in the set 

set_S = {1,2,2,3,5,6,7,7,7,8,9,9}
# print(set_S)
# set_S.add(4)
# print(set_S)

# print(s.union(set_S))
# print(s.intersection(set_S))

diff = s - set_S
print(diff)