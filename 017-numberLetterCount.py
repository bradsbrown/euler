from num2words import num2words

def numberLetterCount(max):
    letters = 0
    for number in range(1, max + 1):
        name = num2words(number)
        letters += countNumber(name)
    return letters

def countNumber(name):
    count = 0
    for i in range(0, len(name)):
        if name[i] not in [" ", "-"]:
            count += 1
    return count


print numberLetterCount(1000)
