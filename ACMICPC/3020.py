import sys
width,height=map(int,input().split())
bottom=[0]*height;min=99999;cnt=1
up=[0]*height;result=[0]*height

for i in range(1,width+1):
	a=int(sys.stdin.readline())
	if i%2==1:
		bottom[a-1]+=1
	else:
		up[a-1]+=1
for i in range(height-2,-1,-1):
	bottom[i]=bottom[i]+bottom[i+1]
for i in range(height-2,-1,-1):
	up[i]=up[i]+up[i+1]

for i in range(height):
	result[i]=bottom[i]+up[-i-1]
	if result[i]<=min:
		if result[i]<min:
			min=result[i]
			cnt=1
		else:
			cnt+=1
print(min,cnt)

