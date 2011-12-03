f1=None
try:
    f1 = open("names.txt","r")
    data = f1.read()
except IOError, inst:
    print inst
finally:
    if f1:f1.close()
data=data.split(',')
data.sort()
ssum=0
for j in range(len(data)):
    psum=j+1
    sum=0
    for i in range(1,len(data[j])-1):
        sum+=ord(data[j][i])-64
    psum*=sum
    ssum+=psum
print ssum
