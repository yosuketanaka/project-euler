import math
p=[]
for b in range(2,499):
    for a in range(1,498):
        if a<b:
            c=math.sqrt(a**2+b**2)
            if c==int(c):
                if 1000>a+b+c and 500>c:p.append(a+b+int(c))
max=0
maxp=0
for x in p:
    if max<p.count(x):
        max=p.count(x)
        maxp=x
print maxp
    
