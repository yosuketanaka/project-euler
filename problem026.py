imax=0
jmax=0
x=(2**9)*(5**4)
for i in range(1,1000):
    j=1
    if x%i!=0:
        while True:
            if x*(10**j-1)%i!=0:j+=1
            else:break
    if jmax<j:
        jmax=j
        imax=i
print imax
