a = range(1000)
a[1] = 0
for p in a:
    if not p:continue
    elif p > 31:break
    else:
        for multi in xrange(p+p, 1000, p):
            a[multi] = 0

a = [x for x in a if x]
n=0
while True:
    if n**2-79*n+1601 in a:break
    else: n+=1
y=n**2-79*n+1601
x=-79+2*n
print x*y
