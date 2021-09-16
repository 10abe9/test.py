from math import sqrt
a = 4 #int(input))
b = 8 #int(input))
c = 1 #int(input))
x1=0
x2=0
Dis=0
x1 = -b + sqrt(b**2-4*a*c)
x2 = -b - sqrt(b**2-4*a*c)
Dis = b**2-4*a*c
if Dis == 0:
	 print ("net korney")
else:

	if x1==x2: 
		print (x1)
	else: 
		print (x1,x2)

