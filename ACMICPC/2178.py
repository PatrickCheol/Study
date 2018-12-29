import sys

n,m=[int(x) for x in sys.stdin.readline().split()];dx=[-1,0,1,0];dy=[0,1,0,-1];que=[[0,0,1]];visit=[]
miro_map=[input() for _ in range(n)]
result_map=[[0]*m for _ in range(n)]
for i,value in enumerate(miro_map):
	for j,value2 in enumerate(value):
		result_map[i][j]=int(value2)


while que!=[]:
	x=que[0][0];y=que[0][1];cnt=que[0][2]
	del que[0]
	if [x,y] in visit:
		continue
	if x==n-1 and y==m-1:
		print(cnt)

	visit.append([x,y])
	for i in range(4):
		dx_x=x+dx[i]
		dy_y=y+dy[i]
		if dx_x>=0 and dx_x<n and dy_y<m and dy_y>=0 and result_map[dx_x][dy_y]==1:
			que.append([dx_x,dy_y,cnt+1])
