prime_list = lambda x: [i for i in xrange(2, x+1) if all([i % y for y in xrange(2, int(i**0.5+1))])][10000]
print prime_list(120000)
