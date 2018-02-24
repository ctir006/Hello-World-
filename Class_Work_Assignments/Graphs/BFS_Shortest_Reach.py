def shortest_reach(adj,res,a,c):
	#print(adj)
	#print(res)
	while len(a)!=0:
		s=a.pop(0)
		for i in adj[s]:
			if res[i]!=-1:
				continue
			a.append(i)
			res[i]=c
		c+=1
		#print(res)
	return res
	
q=int(input())
for k in range(q):
	n,m=[int(i)for i in input().split()]
	adj={}
	res=[]
	for i in range(n+1):
		res.append(-1)
	for i in range(1,n+1):
		adj[i]=[]
	for i in range(m):
		u,v=[int(j)for j in input().split()]
		if u not in adj[v]:
			adj[v].append(u)
		if v not in adj[u]:
			adj[u].append(v)
	s=int(input())
	a=[]
	a.append(s)
	c=1
	for i in shortest_reach(adj,res,a,1)[1:]:
		if c==s:
			c+=1
			continue
		if i!=-1:
			print(i*6,end=' ')
		else:
			print(i,end=' ')
		c+=1
	print()