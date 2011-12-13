import itertools
a=list(itertools.permutations(range(1,10), 4))
y=[]
for i in range(len(a)):
    x=2*(a[i][0]*1000+a[i][1]*100+a[i][2]*10+a[i][3])
    if x>10000:
        b=[x/10000,x/1000-x/10000*10,x/100-x/1000*10,x/10-x/100*10,x-x/10*10]
        if not 0 in b:
            if b[0] in a[i]:pass
            elif b[1] in a[i] or b[1]==b[0]:pass
            elif b[2] in a[i] or b[2]==b[1] or b[2]==b[0]:pass
            elif b[3] in a[i] or b[3]==b[2] or b[3]==b[1] or b[3]==b[0]:pass
            elif b[4] in a[i] or b[4]==b[3] or b[4]==b[2] or b[4]==b[1] or b[4]==b[0]:pass
            else:
                if x in y:pass
                else:
                    y.append(x)
max=0
for p in y:
    if p>max:max=p
print int(str(p/2)+str(p))
