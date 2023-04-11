# In Python, negative sequence indexes represent positions from the end of the array.
# Instead of having to compute the offset as in List[len(List)-3], it is enough to just write List[-3].
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second-last item, etc.

L1 = ["abhi","tinku","tom","jerry",23,78]
print(L1[4])
print(L1[-4])
print(L1[-2])