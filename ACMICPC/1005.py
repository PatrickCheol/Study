class node:
	def __init__(self,num,data,):
		self.data=data
		self.num=num
		self.left=None
		self.right=None
node_list=[]
for _ in range(int(input())):
	house,rule=[int(x) for x in input().split()]
	house_time=[int(x) for x in input().split()]
	for i in range(house):
		node_list.append(node(i,house_time[i]))
	for _ in range(house):
		start,end=[int(x) for x in input().split()]
		node_list[start-1].