from random import randint
import heapq
def qselect(l,k):
	q=l[0]
	l.remove(q)
	left=[i for i in l if i[0]<q[0]]
	right=[i for i in l if i[0]>=q[0]]
	if len(left)==k-1:
		return q
	if len(left)<k-1:
		return qselect(right,k-len(left)-1)
	if len(left)>k-1:
		return qselect(left,k)
def find(l,x,k):
	d=[]
	r=[]
	res=[]
	for i in range(len(l)):
		d.append((abs(l[i]-x),l[i],i))
	for i in range(1,k+1):
		t=d[:]
		x,y,z=qselect(t,i)
		heapq.heappush(r,(z,y,x))
	for i in range(k):
		res.append(heapq.heappop(r)[1])
	return res
if __name__ == "__main__":
	print(find([4,1,3,2,7,4], 5.2, 2))
	print(find([4,1,3,2,7,4], 6.5, 3))
	print(find([5,3,4,1,6,3], 3.5, 2))
	print(find([1,2,3,4,4,7], 5.2, 2))
	print(find([1,2,3,4,4,7], 6.5, 3))
	print(find([1,2,3,4,4,6,6], 5, 3))
	print(find([1,2,3,4,4,5,6], 4, 5))
