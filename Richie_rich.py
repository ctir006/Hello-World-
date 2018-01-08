n,k=input().split(" ")
n=int(n)
k=int(k)
a=list(input())
pos=[0 for i in range(n)]
ccount=0
for i in range(1,int(n/2)+1):
	if a[i-1]!=a[-i]:
		ccount+=1
if(ccount>k):
	print("-1")
	quit()

ccount=0	
for i in range(1,int(n/2)+1):
	if a[i-1]!=a[-i]:
		if(int(a[i-1])>int(a[-i])):
			a[-i]=a[i-1]
			pos[-i]=1
			ccount+=1
		else:
			a[i-1]=a[-i]
			pos[i-1]=1
			ccount+=1
if(ccount==0):
	i=1
	while(ccount<k and i<(int(n/2)+1)):
		if a[i-1]!='9':
			a[i-1]='9'
			ccount+=1
		if a[-i]!='9':
			a[-i]='9'
			ccount+=1
		i+=1
	if(n%2!=0):
		if(ccount<k):
			a[int(n/2)]='9'
elif(ccount<k):
	i=0
	while(ccount<=k and i<(int(n/2)+1)):
		if(pos[i]==1):
			a[i]='9'
			a[-(i+1)]='9'
			ccount+=1
		else:
			a[i]='9'
			a[-(i+1)]='9'
			ccount+=2
		i+=1
print("".join(a))