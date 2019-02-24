dx=[-2,-2,-1,-1,1,1,2,2];dy=[1,-1,2,-2,2,-2,1,-1]
for _ in range(int(input())):
	ches_map=[[0]*300 for _ in range(300)];cnt=0
	map_length=int(input())
	start=[int(x) for x in input().split()]
	end=[int(x) for x in input().split()]
	Queue=[[start,end,cnt]]
	while Queue!=[]:
		a=Queue.pop(0)
		start=a[0]
		end=a[1]
		cnt=a[2]
		if start==end:
			print(cnt)
			break
		x=start[0];y=start[1]
		for i in range(8):
			dx_x=x+dx[i]
			dy_y=y+dy[i]
			if dx_x>=0 and dx_x<map_length and dy_y>=0 and dy_y<map_length:
				if ches_map[dx_x][dy_y]!=1:
					ches_map[dx_x][dy_y]=1
					Queue.append([[dx_x,dy_y],end,cnt+1])