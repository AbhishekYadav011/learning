import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
print(THIS_FOLDER)
my_file = os.path.join(THIS_FOLDER, 'myfile.txt')
print(my_file)

testlist = [2, 3, 4, 5, 6]
# print(testlist.append(testlist.pop(2)))
# print(testlist)
for i in range(2,len(testlist)-1):
    testlist[i] = testlist[i+1]
print(testlist)
