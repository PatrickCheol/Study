import sys
n=int(input())
m=[sys.stdin.readline() for _ in range(n)]
num_list=[];string=''
for i in m:
	for j,value in enumerate(i):
		if value>='0' and value<='9':
			string+=value
		else:
			if string=='':
				continue
			else:
				num_list.append(int(string))
				string=''
	if string!='':
		num_list.append(int(string))
for i in sorted(num_list):
	print(i)
