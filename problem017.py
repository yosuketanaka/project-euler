a='onetwothreefourfivesixseveneightnine'
b='teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen'
c='twentythirtyfortyfiftysixtyseventyeightyninety'
d='hundred'
e='and'
f='onethousand'
print 900*len(d)+100*len(a)+(999-99-9)*len(e)+(len(a)+len(b)+len(c)*10+8*len(a))*10+len(f)

