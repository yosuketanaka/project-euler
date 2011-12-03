result = []
a, b = 1, 1
while True:
    result.append(a)
    a, b = b, a+b
    if a > 10**999:break
print len(result)+1
