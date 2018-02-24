inversion_count=0
def merge(l,left,right,lc,rc):
	global inversion_count
	k=i=j=0
	while i<lc and j<rc:
		if left[i]<right[j]:
			l[k]=left[i]
			i+=1
			k+=1
		else:
			inversion_count+=1
			l[k]=right[j]
			j+=1
			k+=1
	while i<lc:
		l[k]=left[i]
		k+=1
		i+=1
	while j<rc:
		l[k]=right[j]
		k+=1
		j+=1
	return inversion_count
def merge_sort(l,n):
	global inversion_count
	if(n>=2):
		mid=int(n/2)
		left=l[0:mid]
		right=l[mid:n]
		merge_sort(left,mid)
		merge_sort(right,n-mid)
		merge(l,left,right,mid,n-mid)
	return inversion_count
l=[int(i)for i in input().split()]
print(merge_sort(l,len(l)))