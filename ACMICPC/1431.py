def comp(a):
	re=0
	for i in a:
		if i>='0' and i<='9':
			re+=int(i)
	return re
num=int(input())
value_list=[input() for _ in range(num)]
value_list=sorted(value_list,key=lambda x:(len(x),comp(x),x))
print('\n'.join(value_list))