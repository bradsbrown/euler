from itertools import permutations

def lexPerms(place):
    num = "0123456789"
    perms = permutations(num)
    permslist = [int(''.join(x)) for x in perms]
    return permslist[place-1]

print lexPerms(1000000)
