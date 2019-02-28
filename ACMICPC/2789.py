alph=[0]*26
for i in 'CAMBRIDGE':
	alph[ord(i)-65]=1
matter=input()
for i in matter:
	if alph[ord(i)-65]==1:
		continue
	print(i,end="")
