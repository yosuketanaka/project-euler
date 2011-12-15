def f1(x):
    return x
def f2(x):
    return int(str(x/2+10)[(x-1)%2])
def f3(x):
    return int(str(x/3+100)[(x-1)%3])
def f4(x):
    return int(str(x/4+1000)[(x-1)%4])
def f5(x):
    return int(str(x/5+10000)[(x-1)%5])
def f6(x):
    return int(str(x/6+100000)[(x-1)%6])

print f1(1)*f2(10-9)*f2(100-9)*f3(1000-189)*f4(10000-2889)*f5(100000-38889)*f6(1000000-488889)
