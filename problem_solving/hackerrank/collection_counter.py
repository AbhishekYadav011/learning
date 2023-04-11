# https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter

if __name__ == '__main__':
    numberofshoes = int(input())
    shoevarietysize = Counter(map(int,input().split()))
    numberofcustomer = int(input())
    totalincome = 0

    for _ in range(numberofcustomer):
        shoesizeaskedbycustomer , priceofshoe = map(int,input().split())
        if shoevarietysize[shoesizeaskedbycustomer]:
            totalincome += priceofshoe
            shoevarietysize[shoesizeaskedbycustomer] -=1
print(totalincome)


