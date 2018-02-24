import heapq
from random import randint

def nbesta(a,b):
	pairs=[]
	res=[]
	temp=[]
	for i in a:
		for j in b:
			pairs.append((i+j,(i,j)))
	pairs.sort()
	for i in range(len(a)):
		pos=len(temp)
		for j in range(1,len(temp)+1):
			if temp[-j][0]==pairs[i][0]:
				if temp[-j][1][1]>pairs[i][1][1]:
					pos=-j
			else:
				break
		if pos==len(temp):
			temp.append(pairs[i])
			res.append(pairs[i][1])
		else:
			temp.insert(pos,pairs[i])
			res.insert(pos,pairs[i][1])
	return res
	
def qselect(pairs,k):
	q=pairs[randint(0,len(pairs)-1)]
	left=[i for i in pairs if i<q]
	right=[i for i in pairs if i>q]
	if len(left)==k-1:
		return q
	if len(left)>k-1:
		return qselect(left,k)
	if len(left)<k-1:
		return qselect(right,k-(len(left)+1))
	
def nbestb(a,b):
	pairs=[]
	res=[]
	temp=[]
	for i in a:
		for j in b:
			pairs.append((i+j,(i,j)))
	for i in range(1,len(a)+1):
		t=qselect(pairs,i)
		pos=len(temp)
		for j in range(1,len(temp)+1):
			if temp[-j][0]==t[0]:
				if temp[-j][1][1]>t[1][1]:
					pos=-j
			else:
				break
		if pos==len(temp):
			temp.append(t)
			res.append(t[1])
		else:
			temp.insert(pos,t)
			res.insert(pos,t[1])
	return res
	
def nbestc(a,b):
	a.sort()
	b.sort()
	heap=[]
	res=[]
	temp=[]
	count=0
	heapq.heappush(heap,(a[0]+b[0],(0,0)))
	while count<len(a):
		k=heapq.heappop(heap)
		r=k[1][0]
		c=k[1][1]		
		pos=len(temp)
		for j in range(1,len(temp)+1):
			if temp[-j][0]==a[r]+b[c]:
				if temp[-j][1][1]>c:
					pos=-j
			else:
				break
		if pos==len(temp):
			temp.append((a[r]+b[c],(a[r],b[c])))
			res.append((a[r],b[c]))
		else:
			temp.insert(pos,(a[r]+b[c],(a[r],b[c])))
			res.insert(pos,(a[r],b[c]))
		count+=1
		if (a[r+1]+b[c],(r+1,c)) not in heap:
			heapq.heappush(heap,(a[r+1]+b[c],(r+1,c)))
		if (a[r]+b[c+1],(r,c+1)) not in heap:
			heapq.heappush(heap,(a[r]+b[c+1],(r,c+1)))
	return res
	
a, b = [4, 1, 5, 3], [2, 6, 3, 4]
print(nbesta(a,b))
print(nbestb(a,b))
print(nbestc(a,b))