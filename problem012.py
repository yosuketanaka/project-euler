a=[n*(n+1)/2 for n in range(1,15000)]
b = range(100)
b[1] = 0
for p in b:
    if not p:continue
    elif p > 10:break
    else:
        for multi in xrange(p+p, 100, p):b[multi] = 0

b = [x for x in b if x]
for j in a:
     x = j
     i = 0
     c = [1 for y in b]
     while True:
        if x%b[i]==0:
            x /= b[i]
            c[i] += 1
        else: i += 1
        if x==1: break
        if b[i] == 97: break
    pro=1
    for z in c:pro*=z
    if pro > 500:print pro
    if pro > 500:print j

