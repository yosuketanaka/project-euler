c = 0
plist = [i for i in range(100000,1000000) if i/100000==i%10 and i/10000-(i/100000)*10==((i%100)-(i%10))/10 and i/1000-(i/10000)*10==((i%1000)-(i%100))/100]
jlist = [j for j in range(110, 1001, 11)]
for j in jlist:
    for i in plist:
        if i%j==0 and i/j<1000:
            if i>c:c=i

print c
