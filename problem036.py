a=[1,3,5,7,9]
b=[11,33,55,77,99]
for j in a:
    for i in range(10):
        b.append(int(str(j)+str(i)+str(j)))
        b.append(int(str(j)+str(i)+str(i)+str(j)))
for i in range(10):
    for j in range(10):
        for k in a:
            b.append(int(str(k)+str(j)+str(i)+str(j)+str(k)))
            b.append(int(str(k)+str(j)+str(i)+str(i)+str(j)+str(k)))
sum=0
for x in b:
    i=format(x,'b')
    j=0
    while True:
        if i[j]==i[len(i)-1-j]:
            j+=1
            if len(i)/2==j:
                sum+=x
                break
        else:break
print sum+1+3+5+7+9
