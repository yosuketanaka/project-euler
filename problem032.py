import itertools
a=list(itertools.permutations(range(1,10), 5))
sum=0
y=[]
for i in range(len(a)):
    x=a[i][0]*(a[i][1]*1000+a[i][2]*100+a[i][3]*10+a[i][4])
    if 10000>x>1000:
        b=[x/1000,x/100-x/1000*10,x/10-x/100*10,x-x/10*10]
        if not 0 in b:
            if b[0] in a[i]:pass
            elif b[1] in a[i] or b[1]==b[0]:pass
            elif b[2] in a[i] or b[2]==b[1] or b[2]==b[0]:pass
            elif b[3] in a[i] or b[3]==b[2] or b[3]==b[1] or b[3]==b[0]:pass
            else:
                if x in y:pass
                else:
                    y.append(x)
                    sum+=x
    x=(a[i][0]*10+a[i][1])*(a[i][2]*100+a[i][3]*10+a[i][4])
    if 10000>x>1000:
        b=[x/1000,x/100-x/1000*10,x/10-x/100*10,x-x/10*10]
        if not 0 in b:
            if b[0] in a[i]:pass
            elif b[1] in a[i] or b[1]==b[0]:pass
            elif b[2] in a[i] or b[2]==b[1] or b[2]==b[0]:pass
            elif b[3] in a[i] or b[3]==b[2] or b[3]==b[1] or b[3]==b[0]:pass
            else:
                if x in y:pass
                else:
                    y.append(x)
                    sum+=x
print sum 
