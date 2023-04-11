# In Python List, there are multiple ways to print the whole List with all the elements,
# but to print a specific range of elements from the list, we use Slice operation.
# Slice operation is performed on Lists with the use of a colon(:).
# To print elements from beginning to a range use [: Index],
# to print elements from end-use [:-Index],
# to print elements from specific Index till the end use [Index:],
# to print elements within a range, use [Start Index:End Index]
# and to print the whole List with the use of slicing operation, use [:].
# Further, to print the whole List in reverse order, use [::-1].
# Note – To print elements of List from rear end, use Negative Indexes.

List = ['a','b','c','d','e','f','g','h','i','j','k','l']
# Print elements of a range
# using Slice operation
sliced_list = List[3:9]
print("\n Slicing elements in a range 3-9",sliced_list)

# Print elements from a
# pre-defined point to end
sliced_list = List[5:]
print("\n Elements sliced from 5th till the end",sliced_list)

# Printing elements from
# beginning till end
sliced_list = List[:]
print("\n Printing all elements using slice operation",sliced_list)

# Negative  index List slicing
# Print elements from beginning
# to a pre-defined point using Slice
List1 = ['G','E','E','K','S','F','O','R','G','E','E','K','S']
sliced_list =List1[:-6]
print("\n Elements sliced till 6th element from last:",sliced_list)

# Print elements of a range
# using negative index List slicing
Sliced_List = List1[-6:-1]
print("\n Elements sliced from index -6 to -1",Sliced_List)

# Printing elements in reverse
# using Slice operation
sliced_list = List1[:: -1]
print("\n List in reverse order:",sliced_list)