from random import randint
def qselect(k,l):
	q=l[randint(0,len(l)-1)]
	l.remove(q)
	left=[i for i in l if i<=q]
	right=[i for i in l if i>q]
	if len(left)==k-1:
		return q
	if len(left)<k-1:
		return qselect(k-len(left)-1,right)
	if len(left)>k-1:
		return qselect(k,left)
list=[0,1,1,1,9,2,8,3,4,7,5,6]
k=int(input())
print(qselect(k,list))