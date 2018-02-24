def change(money,a,n,dp):
	if dp[money][n]!=-1:
		return dp[money][n]
	if money==0:
		return 1
	elif n<0 or money<0:
		return 0
	else:
		k=0
		if money>=a[n]:
			k=change(money-a[n],a,n,dp)
		l=change(money,a,n-1,dp)
		dp[money][n]=l+k
	return dp[money][n]
money,n=[int(i)for i in input().split()]
l=[int(i)for i in input().split()]
dp=[]
for i in range(money+1):
	k=[]
	for j in range(n+1):
		k.append(-1)
	dp.append(k)
print(change(money,l,n-1,dp))
