import math

#list prime numbers below x
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

#read 'x' file which is splited by ','
def readfile(x):
    f1=None
    try:
        f1 = open(x,"r")
        data = f1.read()
    except IOError, inst:
        print inst
    finally:
        if f1:f1.close()
    data=data.split(',')
    return data

