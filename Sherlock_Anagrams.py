tc=int(input())
inp=[]
for i in range(tc):
	inp.append(input())
result=[]
for str in inp:
	l=[]
	d={}
	res=0
	for j in range(1,len(str)):
		for k in range(len(str)-(j-1)):
			l.append("".join(sorted(str[k:k+j])))
	for i in l:
		count=d.get(i,0)+1
		d[i]=count
	k=[(y,x)for x,y in d.items()]
	k=sorted(k,reverse=True)
	for i in k:
		if i[0]==1:
			break
		if i[0]>=2:
			res+=1
	result.append(res)
for i in result:
	print(i)