def smallestnumber(list):
    list.sort()
    return list[0]


if __name__ == "__main__":
    l1 = [23,45,12, 8, 45]
    print(smallestnumber(l1))