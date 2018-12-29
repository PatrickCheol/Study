import sys
num=int(sys.stdin.readline());start=1;cnt=1;i=1
while start<=num:
	start=start+cnt
	cnt+=1

start_num=start-(cnt-1)
cnt-=1
tmp=cnt
i=1

for _ in range(num-start_num):
	cnt-=1
	i+=1
	
print("%d/%d" % (i,cnt) if tmp%2==0 else "%d/%d" % (cnt,i))
	


