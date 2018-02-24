from random import randint
def _search(l,e):
	if l==[]:
		return []
	if l[1]==e:
		return l
	if l[1]>e:
		return _search(l[0],e)
	if l[1]<e:
		return _search(l[2],e)
	return []	
def search(l,e):
	if l==[]:
		return None
	if l[1]==e:	
		return True
	if search(l[0],e)== True:
		return True
	if search(l[2],e)== True:
		return True
	return False
def insert(l,e):
	if l==[]:
		l.append([])
		l.append(e)
		l.append([])
		return True
	elif l[1]>e:
		insert(l[0],e)
	elif l[1]<e:
		insert(l[2],e)
	else:
		return False
def sorted_helper(l,s1):
	if l==[]:
		return
	else:
		sorted_helper(l[0],s1)
		s1.append(l[1])
		sorted_helper(l[2],s1)
	return s1
def sorted(l):
	s1=[]
	return sorted_helper(l,s1)
	
def sort(a):
	if a==[]:
		return []
	else:
		p=a[randint(0,len(a)-1)]
		left=[i for i in a if i<p]
		right=[i for i in a if i>p]
		return [sort(left)]+[p]+[sort(right)]
l=[4,2,6,3,5,7,1,9]
list=sort(l)
print(list)
k=float(input())
print(_search(list,k))
insert(list,6.5)
print(sorted(list))