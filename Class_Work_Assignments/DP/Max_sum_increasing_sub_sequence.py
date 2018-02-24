def msis_help(l,i,j,sum):
	if j>=len(l):
		return 0
	if l[i]<l[j]:
		s=l[i]+l[j]+msis_help(l,j,j+1,sum)
		if s>sum[0]:
			sum[0]=s
		return sum[0]
	else:
		return msis_help(l,i,j+1,sum)

def msis(l,r):
	for i in range(len(l)):
		msis_help(l,i,i,r)
		print(r[0])
		r[0]=0
		
	
a=[20,3,1,15,16,2,12,13]
r=[0]
msis(a,r)
print(r[0])