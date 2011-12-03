for i in range(1,333):
    for j in range(1,1000):
        if (1000-i)*(1000-j) == 500000:
            c, x = 1, 1
            c = 1000-i-j
            x = c*i*j

print x