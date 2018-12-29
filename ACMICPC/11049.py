def min(a,b):
	return a if a<b else b

def d_list(p_list):
	d=[]
	for i in p_list:
		d.append(i[0])
	d.append(p_list[-1][1])
	return d


num=int(input())
dp=[[0]* (num) for _ in range(num)]
p_list=[[int(x) for x in input().split()] for _ in range(num)]
d=d_list(p_list)

for q in range(num):
	for i in range(num-q):
		j=i+q
		if i==j:
			dp[i][j]=0
			continue
		dp[i][j]=999999
		for k in range(i,j):
			dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+d[i-1]*d[k]*d[j])

print(dp[0][-1])
print(dp)
