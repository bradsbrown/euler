def listFibs(max):
    list = [1, 2]
    while True:
        # print list
        next_one = list[-1] + list[-2]
        list.append(next_one)
        if list[-1] >= max:
            break
    evens = []
    for entry in list:
        if entry % 2 == 0:
            evens.append(entry)
    print evens
    return evens


def sumFibs(max):
    list = listFibs(max)
    sum = 0
    for entry in list:
        sum += entry
    return sum

print sumFibs(4000000)
