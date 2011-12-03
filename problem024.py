def pro(i):
    p=1
    for x in range(1,i+1):p*=x
    return p

a=[i for i in range(10)]
b=999999
c=range(10)
for j in range(10):
    i=0
    while True:
        if b < (i+1)*pro(9-j):
            c[j]=a[i]
            b-=(i)*pro(9-j)
            a.pop(i)
            break
        i += 1
print c
