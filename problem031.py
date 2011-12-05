i=0
for a in range(2):
    for b in range(3-a):
        for c in range(5-4*a-2*b):
            for d in range(11-10*a-5*b-2*c):
                for e in range(21-20*a-10*b-5*c-2*d):
                    for f in range(41-40*a-20*b-10*c-4*d-2*e):
                        for g in range(101-100*a-50*b-25*c-10*d-5*e-2*f):
                            if 200-(a*200+b*100+c*50+d*20+e*10+f*5+g*2)>=0:i+=1
print i
