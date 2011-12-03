c=2*3*5*7*11*13*17*19
for i in range(1,21):
    if c % i != 0:c*=i/(c%i)

print c