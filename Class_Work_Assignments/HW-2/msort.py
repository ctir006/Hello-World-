def merge(l,left,lcount,right,rcount):
	i=j=k=0
	while(i<lcount and j<rcount):
		if(left[i]<=right[j]):
			l[k]=left[i]
			k+=1
			i+=1
		else:
			l[k]=right[j]
			k+=1
			j+=1
	while(i<lcount):
		l[k]=left[i]
		k+=1
		i+=1
	while(j<rcount):
		l[k]=right[j]
		k+=1
		j+=1
	print(l)
def msort(l,n):
	if n<2:
		return
	mid=int(n/2)
	left=l[0:mid]
	right=l[mid:n]
	msort(left,mid)
	msort(right,n-mid)
	merge(l,left,mid,right,n-mid)
	
l=[1,4,2,5,6,7,3,8]
msort(l,len(l))
print(l)