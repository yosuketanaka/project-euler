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
    x=p
    y=int(math.log10(p))
    if p<10:pass
    elif ('4' or '6' or '8' or '0') in str(p):pass
    elif p%10==9:pass
    else:
        i=0
        while True:
            x=x/10
            if x in a:
                i+=1
                if i==y:
                    b.append(p)
                    break
            else:break
c=[]
for p in b:
    y=int(math.log10(p))
    while True:
        if p%(10**y) in a:
            y-=1
            if y==0:
                c.append(p)
                break
        else:break
sum=0
for p in c:
    sum+=p
print sum
