num=1
den=1
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if (9*a+b)*c==10*a*b and a!=b:
                num*=a
                den*=c
print den/num

