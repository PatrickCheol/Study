m,n=list(map(int,input().split()));dx=[-1,0,1,0];dy=[0,1,0,-1];cnt=0;que=[]
to_map=[[int(x) for x in input().split()] for _ in range(n)]
for i,i_list in enumerate(to_map):
	for j,j_list in enumerate(i_list):
		if j_list==1:
			que.append([i,j])

while que!=[]:
	now=que[0]
	del que[0]
	x=now[0];y=now[1]
	cnt=cnt if cnt>to_map[x][y] else to_map[x][y]
	for i in range(4):
		dx_x=x+dx[i];dy_y=y+dy[i]
		if dx_x<n and dx_x>=0 and dy_y<m and dy_y>=0:
			if to_map[dx_x][dy_y]==0:
				que.append([dx_x,dy_y])
				to_map[dx_x][dy_y]=to_map[x][y]+1

for i,i_list in enumerate(to_map):
	for j,j_list in enumerate(i_list):
		if j_list==0:
			cnt=0

print(cnt-1)