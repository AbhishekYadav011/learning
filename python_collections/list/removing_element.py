# Using remove() method
# Elements can be removed from the List by using built-in remove() function
# but an Error arises if element doesn’t exist in the set.
# Remove() method only removes one element at a time, to remove range of elements, iterator is used.
# The remove() method removes the specified item.
# Note – Remove method in List will only remove the first occurrence of the searched element.

List = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,5,6,7]
print("Complete list without removal\n", List)

List.remove(5)
List.remove(6)
print("\nList after removal of 5,6:", List)
for i in range (1,5):
    List.remove(i)
print(List)

# Using pop() method: Pop() function can also be used to remove and return an element from the set,
# but by default it removes only the last element of the set,
# to remove element from a specific position of the List,
# index of the element is passed as an argument to the pop() method.
L1 = [1,2,3,4,5]
# Removing element from the
# Set using the pop() method
L1.pop()
print("\n List after popping an element:")
print(L1)
# Removing element at a
# specific location from the
# Set using the pop() method
L1.pop(2)
print("\n List after removing element from position 2")
print(L1)

