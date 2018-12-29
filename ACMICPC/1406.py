'''
import sys

lst=list(sys.stdin.readline()[:-1])
rst=[]
N=int(sys.stdin.readline())

for _ in range(N):
	cmd=sys.stdin.readline().split()
	if cmd[0] == 'L' and lst:
		rst.append(lst.pop())
	elif cmd[0] == 'D' and rst:
		lst.append(rst.pop())
	elif cmd[0] =='B' and lst:
		lst.pop()
	elif cmd[0] =='P':
		lst.append(cmd[1])

while lst:
  ch = lst.pop()
  rst.append(ch)
output = ''
while rst:
  output += rst.pop()
print(output)
'''
import sys
k=list(sys.stdin.readline()[:-1])
cur=len(k)
for _ in range(int(sys.stdin.readline())):
	cmd=sys.stdin.readline()
	if (cmd[0]=='P'):
		#k.insert(cur,cmd[2])
		k=k[0:cur]+[cmd[2]]+k[cur:]
		cur+=1
	elif (cmd[0] == 'L' and cur>=1):
		cur-=1;
	elif (cmd[0] == 'D' and cur<=len(k)-1):
		cur+=1
	elif (cmd[0] =='B' and cur>=1):
		#k.pop(cur-1)
		k=k[0:cur-1]+k[cur:]
		cur-=1
for x in k:
	print(x,end="")
