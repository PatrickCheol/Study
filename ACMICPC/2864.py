a,b=(x for x in input().split())
string_a1="";string_a2=""
string_b1="";string_b2=""
for i in a:
	if i=='6':
		string_a1+='5'
	else:
		string_a1+=i

	if i=='5':
		string_a2+='6'
	else:
		string_a2+=i

for i in b:
	if i=='6':
		string_b1+='5'
	else:
		string_b1+=i

	if i=='5':
		string_b2+='6'
	else:
		string_b2+=i
print(int(string_a1)+int(string_b1),int(string_a2)+int(string_b2))
