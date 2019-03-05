num_list=[0]*10
num=int(input())
for i in range(1,num+1):
	for j in str(i):
		num_list[int(j)]+=1
for i in num_list:
	print(i,end=" ")