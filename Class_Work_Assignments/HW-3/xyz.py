def find(l):
	l.sort()
	res=[]
	for k in range(len(l)):
		k=l[k]
		i=0
		j=len(l)-1
		while i<j:
			if k!=l[i]+l[j]:
				if l[i]+l[j]>k:
					j-=1
				else:
					i+=1
			else:
				res.append((k,l[i],l[j]))
				i+=1
				j-=1
	return res
if __name__=='__main__':
	l=[1, 4, 2, 3, 5]
	print(find(l))