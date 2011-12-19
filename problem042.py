import euler

a=[n*(n+1)/2 for n in range(100)]
data=euler.readfile("words.txt")
x=0
for j in range(len(data)):
    sum=0
    for i in range(1,len(data[j])-1):
        sum+=ord(data[j][i])-64
    if sum in a:x+=1
print x
