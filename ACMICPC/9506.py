for _ in range(int(input())):
	sum=0
	a,b=[int(x) for x in input().split()]
	candy=[int(x) for x in input().split()]
	for i in candy:
		sum+=i//b
	print(sum)


