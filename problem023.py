sum=[1 for i in range(28124)] 
for j in range(12,28124):
    i = 2
    while True:
        if i**2>j:break
        if j%i==0:sum[j] += (i+j/i)
        if i**2==j:sum[j] -= i
        i += 1
for j in range(28124):
    if sum[j]>j:sum[j]=j
    else:sum[j]=0
sum[1]=0
sum=[x for x in sum if x]
b=[i for i in range(28124)]
for i in sum:
    for j in sum:
        if i+j<28124:
            b[i+j]=0
b=[x for x in b if x]
ysum=0
for x in b:ysum+=x
print ysum
