from sys import *

setrecursionlimit(10 ** 6)

def dfs(li,height):
	x=li[0];y=li[1]
	visit[x][y]=1
	for i in range(4):
		dx_x=x+dx[i]
		dy_y=y+dy[i]
		if dx_x>=0 and dx_x <length and dy_y>=0 and dy_y<length and visit[dx_x][dy_y]!=1 and rain_map[dx_x][dy_y]>height:
			dfs([dx_x,dy_y],height)

length=int(input())
dx=[1,-1,0,0];dy=[0,0,1,-1];ans=0
rain_map=[[int(x) for x in input().split()] for _ in range(length)]

max_height=max(max(rain_map))

for i in range(max_height):
	visit=[[0]*length for _ in range(length)];cnt=0
	for p in range(length):
		for q in range(length):
			if rain_map[p][q]>i and visit[p][q]!=1:
				cnt+=1
				dfs([p,q],i)

	if cnt>ans:
		ans=cnt
	if cnt==0:
		break
print(ans)
