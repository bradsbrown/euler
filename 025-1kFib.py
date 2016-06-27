def findFibs(digits):
    x, y = 1, 1
    i = 2
    while True:
        # print list
        x, y = y, x+y
        i += 1
        if len(str(y)) == digits:
            return i

print findFibs(1000)
