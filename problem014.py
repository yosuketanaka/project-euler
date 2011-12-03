chain=0
for x in range(1,1000000):
    c = 0
    j = x
    while True:
        if j == 1:break
        if j % 2 == 0:j/=2
        else: j = 3*j+1
        c += 1
    if c > chain:
        chain=c
        print x