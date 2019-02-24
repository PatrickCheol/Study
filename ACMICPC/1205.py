import sys

num,song,rank=map(int,input().split())
song_rank=1
if num==0:print(1)
elif rank==0:print(-1)
else:
	whole_rank=list(map(int,sys.stdin.readline().split()))
	if song<=whole_rank[-1] and len(whole_rank)>=rank:
		print(-1)
	else:
	
		length=rank if rank<=len(whole_rank) else len(whole_rank)
		for i in range(length):
			if song<whole_rank[i]:
				song_rank+=1
			elif song==whole_rank[i]:
				continue
			else:
				break
		print(song_rank)
