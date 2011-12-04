n=range(6)
sum2=0
for x in range(1000000):
    sum=0
    n[0]=x/100000
    n[1]=x/10000-x/100000*10
    n[2]=x/1000-x/10000*10
    n[3]=x/100-x/1000*10
    n[4]=x/10-x/100*10
    n[5]=x-x/10*10
    for i in range(6):
        sum+=n[i]**5
    if sum==x and x!=1:sum2+=x
print sum2
