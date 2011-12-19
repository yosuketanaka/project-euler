import euler
p=euler.prime(10000000)
a=[]
for x in p:
    if '1' in str(x):
        if '2' in str(x):
            if '3' in str(x):
                if '4' in str(x):
                    if '5' in str(x):
                        if '6' in str(x):
                            if '7' in str(x):a.append(x)
print a[-1]
