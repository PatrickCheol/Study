import sys
res=[];val=[];giho={'+':1,'-':1,'*':2,'/':2};giho2=['+','-','*','/']
word=sys.stdin.readline()
if word[-1]=='\n':
   word=word[:-1]
for i in word:
   if i not in giho2 and i!='(' and i!=')':
      res.append(i)
   else:
      if i=='(':
         val.append(i)
      elif i==')':
         while val[-1]!='(':
            res.append(val.pop())
         val=val[0:-1]
      else:
         if val!=[]:
            while True:
               if val!=[] and val[-1] in giho2 and giho[i]<=giho[val[-1]]:
                  res.append(val.pop())
               else:
                  break
         val.append(i)
while val!=[]:
   res.append(val.pop())
print(''.join(res))