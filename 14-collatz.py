def longestChain(top):
    biggestChain = 1
    winner = 1
    for i in range(1, top):
        start = i
        chainCount = 1
        while i != 1:
            if i % 2 == 0:
                i = i/2
                chainCount += 1
            else:
                i = (i*3) + 1
                chainCount += 1
        if chainCount > biggestChain:
            biggestChain = chainCount
            winner = start
    return winner


print longestChain(1000000)
