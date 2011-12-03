sum=[1 for i in range(10001)] 
xsum=0
for j in range(3,10001):
    i = 2
    while True:
        if j%i==0:sum[j] += (i+j/i)
        if i**2==j:sum[j] -= i
        if i**2>j:break
        i += 1
for j in range(1,10001):
    if sum[j]<10000:
        if sum[sum[j]]==j and sum[j]!=j:xsum+=j
print xsum