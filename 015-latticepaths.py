def findPaths(gridsize):
    paths = 1
    for i in range(0,gridsize):
        paths *= (2 * gridsize) - i
        paths /= i + 1
    return paths


print findPaths(20)
