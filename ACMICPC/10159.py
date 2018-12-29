import sys
def find(num):
	global re_map
	for i in range(num):
		for j in range(num):
			for k in range(num):
				if re_map[j][i]==1 and re_map[i][k]==1:
					re_map[j][k]=1

num=int(sys.stdin.readline())
re_map=[[0]*num for _ in range(num)]
for _ in range(int(sys.stdin.readline())):
	a,b=[int(x) for x in sys.stdin.readline().split()]
	re_map[a-1][b-1]=1
find(num)
for i in range(num):
	cnt=0
	for j in range(num):
		if not re_map[i][j] and not re_map[j][i]:
			cnt+=1
	print(cnt-1)
