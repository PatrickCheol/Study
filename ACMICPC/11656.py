a=input();re=[]
for i in range(len(a)):
	re.append(a[i:])
re=sorted(re)
print("\n".join(re))