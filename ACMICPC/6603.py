
k=0
tmp=['0']*20
def dfs(start,cnt):
	if cnt==6:
		print(" ".join(tmp[0:6]))
	for i in range(start,k):
		tmp[cnt]=a[i]
		dfs(i+1,cnt+1)

while 1:
	a=input()
	if a[0]=='0':
		break
	else:
		k=int(a[0])
		a=a[1:].split()
		dfs(0,0)
		print()
	

'''

from itertools import combinations
while True:
    a = input().split()
    if a.pop(0) == '0': break
    for a in combinations(a, 6):
    	print(" ".join(a))
    print()
'''
