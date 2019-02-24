cnt=0
for _ in range(int(input())):
	alpa=[0]*26;flag=1
	string=input()
	alpa[ord(string[0])-97]=1
	for i,value in enumerate(string[1:]):
		if alpa[(ord(value)-97)]==0:
			alpa[ord(value)-97]=1
		else:
			if value!=string[i]:
				flag=2
				break
	if flag==1:
		cnt+=1
print(cnt)

