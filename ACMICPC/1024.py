def getSum(a,b):
	return int((b*(b+1))/2-(a*(a-1))/2)
m,n=[int(x) for x in input().split()]
na=m//n;i=n-1
while 1:
	print(getSum(na,na+i))
	if getSum(na,na+i)==m:
		for j in range(i):
			print(na+i,end=" ")
		break
	elif getSum(na,na+i)>m:
		print(-1)
		break
	elif i>99:
		print(-1)
		break
	else:
		i+=1

