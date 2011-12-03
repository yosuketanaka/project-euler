a = range(2000000)
a[1] = 0
for p in a:
    if not p:continue
    elif p > 1414:break
    else:
        for multi in xrange(p+p, 2000000, p):
            a[multi] = 0

a = [x for x in a if x]
sum = 0
for i in a:sum += i

print sum
