def amNumsAll(max):
    amNums = []
    for i in range(2, max + 1):
        if i not in amNums:
            compare = amNumsSum(i)
            if compare != i and i == amNumsSum(compare):
                if i not in amNums:
                    amNums.append(i)
                if compare not in amNums:
                    amNums.append(compare)
    print amNums
    return sum(x for x in amNums)


def amNumsSum(num):
    return sum(x for x in findDivs(num))


def findDivs(num):
    divs = [1]
    for i in range(2, int(num**0.5 + 1)):
        if i not in divs:
            if num % i == 0:
                divs.extend((i, num/i))
    return divs


print amNumsAll(10000)
