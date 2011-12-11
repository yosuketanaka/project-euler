import math
a = range(1000001)
a[1] = 0
for p in a:
    if not p:continue
    elif p > 1000:break
    else:
        for multi in xrange(p+p, 1000001, p):
            a[multi] = 0

a = [x for x in a if x]
b=[]
for p in a:
    if p<10:b.append(p)
    else:
        if ('2' or '4' or '6' or '8' or '0') in str(p):pass
        elif p>200000:pass
        else:
            y=int(math.log10(p))
            i=0
            while True:
                p=p/10+p%10*(10**y)
                if p in a:
                    if i==y:
                        b.append(p)
                        break
                    else:
                        i+=1
                else:break
c=0
for p in b:
    if p>100000:c+=1
print len(b)+c*5
