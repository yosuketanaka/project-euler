x = 600851475143
while x >= 4 and x % 2 == 0:x /= 2
d = 3; q = x / d
while q >= d:
    if x % d == 0:x = q
    else:d += 2
    q = x / d

print "%d" % x
