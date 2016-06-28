def fifthPowers():
    L = 335000
    fivePows = 0
    for x in range(2, L):
        sum = 0
        num = str(x)
        for d in range(0, len(num)):
            sum += int(num[d])**5
        if sum == x:
            fivePows += x

    return fivePows

print fifthPowers()
