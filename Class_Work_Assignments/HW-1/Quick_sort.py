"""l=[5,3,1,9,6,8,7,4,0]

def partition(l,begin,end):
	p=l[end]
	i=begin-1
	for j in range(begin,end):
		if l[j]<p:
			i+=1
			if i!=j:
				l[i],l[j]=l[j],l[i]
		else:
			continue
	i=i+1	
	l[i],l[end]=l[end],l[i]
	print(l)
	return i
	
def quick_sort(l,begin,end):
	if begin<end:
		q=partition(l,begin,end)
		quick_sort(l,begin,q-1)
		quick_sort(l,q+1,end)

quick_sort(l,0,8)"""

def partition(l,begin,end):
	i=begin-1
	j=begin
	p=l[end]
	while j<end:
		if l[j]<p:
			i+=1
			if i!=j:
				l[i],l[j]=l[j],l[i]
		j+=1
	i+=1
	l[i],l[end]=l[end],l[i]
	print(i)
	print(l)
	return i
def quick_sort(l,begin,end):
	if(begin<end):
		q=partition(l,begin,end-1)
		quick_sort(l,begin,q-1)
		quick_sort(l,q+1,end)
	
n=int(input())
l=[int(i)for i in input().split()]
quick_sort(l,0,n)
print(l)