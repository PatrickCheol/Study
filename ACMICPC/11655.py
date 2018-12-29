big_alph=[];small_alph=[]
for i in range(65,91):
	a=chr(i+13) if i+13<91 else chr((i+13)%91+65)
	big_alph.append(a)
for i in range(97,123):
	a=chr(i+13) if i+13<123 else chr((i+13)%123+97)
	small_alph.append(a)
string=input()
for i in string:
	if ord(i)>=65 and ord(i)<91:
		print(big_alph[ord(i)-65],end="")
	elif ord(i)>=97 and ord(i)<123:
		print(small_alph[ord(i)-97],end="")
	else:
		print(i,end="")



