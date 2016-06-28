def maxNum(side):
    if side % 2 == 0:
        return -1
    max = 1
    for sq in range(3, side+1, 2):
        max += sq*4 - 4
    return max


def sqSum(side):
    start = maxNum(side)
    return 4*start -6*side + 6


def numSpiDiag(side):
    tot = 1
    for sq in range(3, side+1, 2):
        tot += sqSum(sq)
    return tot


print numSpiDiag(1001)
