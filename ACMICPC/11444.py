import sys
n=int(sys.stdin.readline());i_0=0;i_1=1;res=0
if n==0:
	res=i_0
elif n==1:
	res=i_1
for _ in range(2,n+1):
	res=i_0+i_1
	i_1,i_0=res,i_1
	print(res%1007)
print(res%1000000007)
