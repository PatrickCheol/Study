com_num,conn_num=[int(input()) for _ in range(2)];visit=[];que=[1];re=0
conn_map=[[] for _ in range(com_num+1)]
for _ in range(conn_num):
	par,chi=[int(x) for x in input().split()]
	conn_map[par].append(chi)
	conn_map[chi].append(par)

while que!=[]:
	value=que[0]
	del que[0]
	if value in visit:
		continue
	visit.append(value)
	for i in conn_map[value]:
		que.append(i)
print(len(visit[1:]))