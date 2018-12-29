def reco_num(x):
   p_list=[]
   p=2
   if x==1:
      p_list.append(1)
      return p_list
   while x!=1:
      if not x%p:
         x=x//p
         p_list.append(p)
         p=2
      else:
         p+=1
   return p_list

for i in range(int(input())):
   li2=reco_num(int(input()))
   li=sorted(list(set(li2)))
   for i in range(len(li)):
      print(li[i],li2.count(li[i]))
      