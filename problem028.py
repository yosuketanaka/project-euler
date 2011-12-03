a=[2*n for n in range(1,501)]
y=1
sum=1
for x in a:
    sum+=y+x+y+2*x+y+3*x+y+4*x
    y+=4*x
print sum
