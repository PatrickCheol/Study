import sys
cnt_space=[0]*10001
for _ in range(int(input())):
	cnt_space[int(sys.stdin.readline())]+=1
for i in range(10001):
	if cnt_space[i]>0:
		for _ in range(cnt_space[i]):
			print(i)
