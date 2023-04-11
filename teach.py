

'''
# string reverse
str1 = "hello"
print(str1[::-1])

statement = "Hello! how are you"
print(' '.join(reversed(statement.split(' '))))

str3 = "geeks for geeks"
print(str3.count("geeks"))

list1 = [10, 20, 3, 40, 50]
if 95 in list1:
    print("YES")
else:
    print("no")

# list comparehension
print([x * 2 for x in list1 if x % 2 == 0])

str4 = "Abcde"
lowercase = str4.lower()
vowel_counts = {}
for vowels in "aeiou":
    #print(vowels)
    count1 = lowercase.count(vowels)
    vowel_counts[vowels] = count1
print(vowel_counts)

#palindrome string
str5 = "david"
if str5 == str5[::-1]:
    print("yes")
else:
    print("no")

'''

# list = [1,2,3,4,5,6,7,8]
# mid = len(list)//2
# print("left:",list[:mid])
# print("right:",list[mid:])
for i in range(5):
    try:
        print(i)
        result = 5 // 0
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

