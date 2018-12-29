import math
cnt=1
while True:
	a,b,c=[int(x) for x in input().split()]
	if a==0 and b==0 and c==0:
		break
	elif a==-1:
		if pow(b,2)>=pow(c,2):
			print("Triangle #%d\nImpossible." % cnt)
		else:
			a=math.sqrt(pow(c,2)-pow(b,2))
			print("Triangle #%d\na = %.3f" % (cnt,a))
	elif b==-1:
		if pow(a,2)>=pow(c,2):
			print("Triangle #%d\nImpossible." % cnt)
		else:
			b=math.sqrt(pow(c,2)-pow(a,2))
			print("Triangle #%d\nb = %.3f" % (cnt,b))
	else:
		c=math.sqrt(pow(a,2)+pow(b,2))
		print("Triangle #%d\nb = %.3f" % (cnt,c))
	cnt+=1
	print("")