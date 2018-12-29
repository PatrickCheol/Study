n,m=list(map(int,input().split()))
a_map=[[int(x) for x in input().split()] for _ in range(n)]
b_map=[[int(x) for x in input().split()] for _ in range(n)]
for i in range(n):
	for j in range(m):
		print(a_map[i][j]+b_map[i][j],end=" ")
	print("")
