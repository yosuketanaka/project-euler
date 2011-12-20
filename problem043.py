import itertools
a=list(itertools.permutations(range(10)))
sum=0
for i in range(len(a)):
    if a[i][0]!=0:
        if(a[i][1]*100+a[i][2]*10+a[i][3])%2==0:
            if (a[i][2]*100+a[i][3]*10+a[i][4])%3==0:
                if (a[i][3]*100+a[i][4]*10+a[i][5])%5==0:
                    if (a[i][4]*100+a[i][5]*10+a[i][6])%7==0:
                        if (a[i][5]*100+a[i][6]*10+a[i][7])%11==0:
                            if (a[i][6]*100+a[i][7]*10+a[i][8])%13==0:
                                if (a[i][7]*100+a[i][8]*10+a[i][9])%17==0:
                                    for j in range(10):
                                        sum+=a[i][j]*(10**(9-j))                                    
print sum
