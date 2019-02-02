import sys

num_list=sorted([int(sys.stdin.readline()) for _ in range(int(input()))])
max=1;cnt=1;ans=num_list[0]
for i,value in enumerate(num_list[1:]):
	if value==num_list[i]:
		cnt+=1
	else:
		cnt=1
	if cnt>max:
		max=cnt
		ans=value
print(ans)

