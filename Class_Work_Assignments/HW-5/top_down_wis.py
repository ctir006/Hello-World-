def max_wis_help(l,n,dp): 
	if dp[n+2][0]>=0:
		return dp[n+2][0]
	if n<0:
		dp[n+2]=(0,0)
		return dp[n+2][0]
	m=l[n]+max_wis_help(l,n-2,dp)
	k=max_wis_help(l,n-1,dp)
	if m>k:
		dp[n+2]=(max(m,k),1)
	else:
		dp[n+2]=(max(m,k),0)
	return dp[n+2][0]

def max_wis(list):
	dp=[]
	for i in range(len(list)+2):
		dp.append((-1,-1))
	r=max_wis_help(list,len(list)-1,dp)
	res=[]
	n=len(list)
	l=n+1
	k=dp[n+1][0]
	while k>0:
		if dp[l][1]==0:
			l-=1
		else:
			res.append(list[l-2])
			k-=list[l-2]
			l-=2
	res=res[::-1]
	return r,res
print(max_wis([7,8,5]))
print(max_wis([7,8,5]))
print(max_wis([-1,8,10]))
print(max_wis([]))
print(max_wis([-1,-5,-4]))
print(max_wis([5,6,3,8,2,1,9,4]))