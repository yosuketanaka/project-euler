qlist = [i for i in range (1000) if i % 3 == 0 or i % 5 == 0]

sum = 0

for i in qlist:
    sum += i

print sum