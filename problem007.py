a = range(150000)
a[1] = 0
for p in a:
    if not p:continue
    elif p > 387:break
    else:
        for multi in xrange(p+p, 150000, p):
            a[multi] = 0

a = [x for x in a if x]

print a[10000]