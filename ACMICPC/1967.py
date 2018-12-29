import sys
sys.setrecursionlimit(15000)
def dfs(start,visit,dist):
	global res;global idx
	'''
	if dist>res:
		res=dist
		idx=start
	'''
	visit.append(start)
	print(start,dist)
	for i in node_map[start]:
		if i[0] not in visit:
			dfs(i[0],visit,dist+i[1])

	

num=int(input());idx=0;res=0
node_map=[[] for _ in range(num+1)]
print(node_map)
for i in range(num-1):
	parent,child,weight=[int(x) for x in input().split()]
	node_map[parent].append([child,weight])
	node_map[child].append([parent,weight])

print(node_map)
dfs(1,[],0)
dfs(idx,[],0)
print(res)



private static int dfs(int i, int max) {
        visit[i] = true;
        System.out.println("max " + max + " / " + "node "+ i);
        for (int[] j : tree.get(i).val)
            if (!visit[j[0]]) {
                max = dfs(j[0], max + j[1]);
            } else {
                a.add(max);
//                max -= j[1];
            }
        return max;
    }


    private static void dfs(int i, int max) {
        visit[i] = true;
        for (int[] j : tree.get(i).val) {
            int temp = max;
            if (!visit[j[0]]) {
                dfs(j[0], max + j[1]);
            } else if (tree.get(i).val.size() == 1) {
                result.add(max);
            }
            max = temp;
        }
    }