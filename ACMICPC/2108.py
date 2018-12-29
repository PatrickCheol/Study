import sys
import math
num_list=[];num=int(sys.stdin.readline());sum_num=0;cnt=0
for _ in range(num):
	a=int(sys.stdin.readline())
	sum_num+=a;num_list.append(a)

num_list=sorted(num_list)
num_count=[];tmp=4001;cnt=0;max_count=0;min_re=[];num_count2=[]
for i in num_list:
	if i!=tmp:
		num_count.append(1)
		num_count2.append(i)
		tmp=i
	else:
		num_count[-1]+=1
for i in range(len(num_count)):
	if num_count[i]>max_count:
		min_re=[i]
		max_count=num_count[i]
	elif num_count[i]==max_count:
		min_re.append(i)

print(math.floor(sum_num/num+0.5))
print(num_list[num//2])
print(num_count2[min_re[1]] if len(min_re)>=2 else num_count2[min_re[0]])
print(num_list[-1]-num_list[0])