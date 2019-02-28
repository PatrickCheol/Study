import sys
num_map=[0]*20000000
n=int(input())
n_num=[int(x) for x in input().split()]
for a in n_num:
	if a<0:
		a=(a*-1)+10000000
	num_map[a]+=1
m=int(input())
m_num=[int(x) for x in input().split()]
for a in m_num:
	if a<0:
		a=(a*-1)+10000000
	print(1 if num_map[a]==1 else 0,end=" ")