def find_sum(n,l,dp):
	for i in range(1,n):
		if l[i]>l[i-1]:
			dp[i]=dp[i]+dp[i-1]
	j=n-2
	while j>=0:
		if l[j]>l[j+1] and dp[j]<=dp[j+1]:
			dp[j]=dp[j+1]+1
		j-=1
	return sum(dp)
n=int(input())
l=[]
for i in range(n):
	l.append(int(input()))
dp=[]
for i in range(n):
	dp.append(1)
print(find_sum(n,l,dp))