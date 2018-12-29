import queue

dx=[-1,0,1,0];dy=[0,1,0,-1]
def bfs(value):
	re=0
	q=queue.Queue()
	q.put(value)
	while q.qsize():
		v=q.get()
		ar_map[v[0]][v[1]]=2
		if v in visit:
			continue
		re+=1
		visit.append(v)
		for i in range(4):
			dx_x=v[1]+dx[i]
			dy_y=v[0]+dy[i]	
			if dx_x>=0 and dx_x<se and dy_y>=0 and dy_y<ga:
				if ar_map[dy_y][dx_x]==0:
					q.put([dy_y,dx_x])
	sm_re.append(re)

ga,se,num=[int(x) for x in input().split()];sm_re=[];bi_re=0;visit=[];
ar_map=[[0]*se for _ in range(ga)]
for _ in range(num):
	x,y,x1,y1=[int(x) for x in input().split()]
	for i in range(y,y1):
		for j in range(x,x1):
			ar_map[i][j]=1

for i in ar_map:
	print(i)

for i in range(ga):
	for j in range(se):
		if ar_map[i][j]==0:
			bfs([i,j])
			bi_re+=1

print(bi_re)
for i in sorted(sm_re):
	print(i,end=" ")

