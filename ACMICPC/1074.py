n,r,c=[int(x) for x in input().split()];re=0
x=pow(2,n)//2;y=x
while n>0:
	n-=1
	temp=pow(2,n)//2
	skip=pow(4,n)
	if r<x and c<y:
		x-=temp;y-=temp
	elif r<x and y<=c:
		x-=temp;y+=temp;re+=skip
	elif x<=r and c<y:
		x+=temp;y-=temp;re+=skip*2
	else:
		x+=temp;y+=temp;re+=skip*3

print(re)
