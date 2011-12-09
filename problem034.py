f = lambda x: x and x * f(x - 1) or 1
for a in range(1,10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    if 10000*a+b*1000+c*100+d*10+e==f(a)+f(b)+f(c)+f(d)+f(e):
                        print 10000*a+1000*b+100*c+10*d+e+145
