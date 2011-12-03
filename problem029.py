a=[x for x in range(2,101)]
y=0
n=2
while n<7:
    for x in range(2,101):
        if n*x in a: y+=1
        else: a.append(n*x)
    if n==2: b=y
    if n==4: c=y
    n+=1
print 99*99-4*b-c-y

