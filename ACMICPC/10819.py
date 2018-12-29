a=int(input());b=sorted([int(x) for x in input().split()]);c=sorted(b,reverse=True);sum=0
for i in range(0,len(b)//2):
	sum+=abs(b[i]-c[i])
	sum+=abs(c[i]-b[i+1])
print(sum,b,c)
