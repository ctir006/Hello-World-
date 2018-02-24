import bisect 
def find(l,x,k):
	f=bisect.bisect_left(l,x)
	left,right=f-1,f
	while k>0:
		if right>=len(l) or abs(l[left]-x)<=abs(l[right]-x) and left>=0:
			left-=1
			k-=1
		else:
			right+=1
			k-=1
	return l[left+1:right]
	
print(find([1,2,3,4,4,7], 6.5, 3))
print(find([1,2,3,4,4,7], 5.2, 2))
print(find([1,2,3,4,4,6,6], 5, 3))