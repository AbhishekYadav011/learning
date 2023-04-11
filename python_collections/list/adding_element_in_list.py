# using append method
L1 = [1, 4, 6, 7, 8, 4]
L1.append(2)
print(L1)

# Adding elements to the List
# using Iterator
L2 = []
for i in range(0,4):
    L2.append(i)
print(L2)

# Adding Tuples to the List
tuple = (2,4)
L2.append(tuple)
print(L2)

# Addition of List to a List
L3 = [0,9,8,7]
L2.append(L3)
print(L2)

# Using insert() method:append() method only works for addition of elements at the end of the List,
# for addition of element at the desired position, insert() method is used.
# Unlike append() which takes only one argument,
# insert() method requires two arguments(position, value).

L2.insert(4,6)
print(L2)

# Using extend() method:Other than append() and insert() methods,
# there’s one more method for Addition of elements, extend(),
# this method is used to add multiple elements at the same time at the end of the list.
# Note – append() and extend() methods can only add elements at the end.

L2.extend(["abhi",30,"tinku"])
print(L2)
L4 = [56,78,90]
L2.extend(L4)
print(L2)