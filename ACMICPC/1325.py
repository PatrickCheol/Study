import sys
sys.setrecursionlimit(15000)
visit=[0]*10000
dp=[0]*10000
def dfs(i,j):
	if visit[i]==j:
		return 0
	res=0
	res+=1
	visit[i]=j
	for i in truth_map[i]:
		res += dfs(i,j)
	return res


num,truth_info=[int(x) for x in input().split()]
truth_map=[[]*(num+1) for _ in range(num+1)]
for i in range(truth_info):
	a,b=[int(x) for x in sys.stdin.readline().split()]
	truth_map[b].append(a)

for i in range(1,num+1):
	dp[i]=dfs(i,i)

hei=max(dp[1:num+1])
for i in range(1,num+1):
	if dp[i]==hei:
		print(i,end=" ")


