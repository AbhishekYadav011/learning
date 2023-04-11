def nthlargestnumber(list,n):
    list.sort()
    return list[-n:]


if __name__ == "__main__":
    l1 = [-78,-86,98,-34,-12,67,90]

    print(nthlargestnumber(l1,4))