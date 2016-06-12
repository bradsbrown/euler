def listNums(max):
    list = []
    for x in range(0, max):
        if x % 3 == 0 or x % 5 == 0:
            list.append(x)
    return list


def sumMults(max):
    list = listNums(max)
    total = 0
    for item in list:
        total += item
    return total

print sumMults(1000)
