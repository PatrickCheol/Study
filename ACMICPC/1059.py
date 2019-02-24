num=int(input())
l_set=sorted([int(x) for x in input().split()])
add=int(input())
least=1;large=0;cnt=0
for i,value in enumerate(l_set):
	if add<=value:
		large=value
		break
	least=value+1

for i in range(least,large):
	for j in range(i+1,large):
		if i<=add and add<=j:
			cnt+=1
print(cnt)