def best_help(i,w,w_i,v_i,dp):
	if dp[i][w][0]!=-1:
		return dp[i][w][0]
	if i==-1 or w==0:
		return 0
	elif w_i[i]>w:
		dp[i][w][0]=best_help(i-1,w,w_i,v_i,dp)
		dp[i][w][1]=i-1
		dp[i][w][2]=w
		return dp[i][w][0]
	else:
		l=v_i[i]+best_help(i,w-w_i[i],w_i,v_i,dp)
		m=best_help(i-1,w,w_i,v_i,dp)
		if l>m:
			dp[i][w][0]=l
			dp[i][w][1]=i
			dp[i][w][2]=w-w_i[i]
			dp[i][w][3].append(v_i[i])
		else:
			dp[i][w][0]=m
			dp[i][w][1]=i-1
			dp[i][w][2]=w
		return dp[i][w][0]

def best(c,l):
	w,h=c,len(l)
	dp=[[[-1,-1,-1,[]] for i in range(w+1)]for y in range(h)]
	w=[]
	v=[]
	for i in l:
		w.append(i[0])
		v.append(i[1])
	k=best_help(len(l)-1,c,w,v,dp)
	i=len(l)-1
	j=c
	res={}
	r=[]
	while True:
		if dp[i][j][3]!=[]:
			c=res.get(dp[i][j][3][0],0)+1
			res[dp[i][j][3][0]]=c
		i,j=dp[i][j][1],dp[i][j][2]
		if dp[i][j][1]==-1 and dp[i][j][2]==-1:
			break
	#print("\t",v)
	t=k
	for i in range(len(v)):
		if v[i] in res:
			r.append(res[v[i]])
			t=t-(res[v[i]]*v[i])
			#print(t)
			if t<=0:
				i+=1
				while i<len(v):
					r.append(0)
					i+=1
				break
			#print(r,t)
		else:
			r.append(0)
	return k,r
		
print(best(3, [(2, 4), (3, 5)]))	#5	
print(best(3,[(1,5),(1,5)]))		#15
print(best(3, [(1, 2), (1, 5)]))	#15
print(best(3, [(1, 2), (2, 5)]))	#7
print(best(58, [(5, 9), (9, 18), (6, 12)]))	#114
print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))	#109
