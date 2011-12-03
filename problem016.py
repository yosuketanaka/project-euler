pro=1
for x in [2 for i in range(1,1001)]:pro*=x
a=str(pro)
sum=0
i=0
while True:
    sum+=int(a[i])
    if i==len(a)-1:break
    i += 1

print sum