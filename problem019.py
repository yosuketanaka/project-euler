x,y=1,0
for i in range(1,1213):
    if x%7==0 and i>12:y+=1
    if i==2:x+=28%7
    elif i%48==2: x += 29%7
    elif i%12==2: x += 28%7
    elif i%12==4 or i%12==6 or i%12==9 or i%12==11:x += 30%7
    else: x += 31%7
print y