import math
def prime(x):
    a = range(x+1)
    a[1] = 0
    for p in a:
        if not p:continue
        elif p > math.sqrt(x):break
        else:
            for multi in xrange(p+p, x+1, p):
                a[multi] = 0
    a = [x for x in a if x]
    return a
