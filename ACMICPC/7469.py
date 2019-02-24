##Fail

import sys
n,m=map(int,input().split())
array=list(map(int,sys.stdin.readline().split()))
for _ in range(m):
	a,b,c=map(int,sys.stdin.readline().split())
	print(sorted(array[a-1:b])[c-1])