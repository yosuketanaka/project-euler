result = []
a, b = 1, 2
while a < 4000000:
    result.append(a)
    a, b = b, a+b

sum = 0
for i in result:
    if i % 2 == 0:
        sum += i

print sum