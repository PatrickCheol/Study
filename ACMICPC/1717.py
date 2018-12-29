import sys

def find(x):
	global set_list
	if x!=set_list[x]:
		set_list[x]=find(set_list[x])
	return set_list[x]

def unite(a, b):
    root1 = find(a)
    root2 = find(b)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            set_list[root2] = root1
        else:
            set_list[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1
num,b=list(map(int,sys.stdin.readline().split()))
set_list=[int(x) for x in range(num+1)]
rank = [0 for i in range(num+1)]
for _ in range(b):
	ch,fir,sed=[int(x) for x in sys.stdin.readline().split()]
	if not ch:
		unite(fir,sed)
	else:
		if find(fir)==find(sed):
			print("YES")
		else:
			print("NO")
