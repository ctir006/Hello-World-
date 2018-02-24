def merge(l,left,lcount,right,rcount,inversions):
	i=j=k=0
	while(i<lcount and j<rcount):
		if(left[i]<right[j]):
			l[k]=left[i]
			k+=1
			i+=1
		else:
			inversions+=lcount-i
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
	return inversions
def msort_help(k,l,n,inversions):
	if n<2:
		return
	mid=int(n/2)
	left=l[0:mid]
	right=l[mid:n]
	msort_help(k,left,mid,inversions)
	msort_help(k,right,n-mid,inversions)
	#print(inversions)
	k[0]+=merge(l,left,mid,right,n-mid,inversions)

def msort(l,n):
	k=[0]
	msort_help(k,l,n,0)
	return k[0]

l=[1,4,2,5,6,7,3,8]
print(msort(l,len(l)))