import numpy


def nameScores():
    names = numpy.loadtxt("022_names.txt", dtype=str, delimiter=",")
    names = sorted(names, key=str.lower)

    totScore = 0
    for i in range(0, len(names)):
        name = names[i]
        name = name[1:-1]
        nameVal = sum((ord(lett.lower())-96) for lett in name)
        totScore += (nameVal * (i+1))
    return totScore

print nameScores()
