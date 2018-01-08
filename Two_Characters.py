def delete(temp,c,n):
	for i in range(temp.count(c)):
		temp.remove(c)
		
def make_t(str,l,p):
	max=0
	for i in range(len(p)):
		temp=[i for i in str]
		for j in l:
			if j not in p[i]:
				delete(temp,j,len(temp))
		res="".join(temp)
		f=0
		for i in range(1,len(res)):
			if res[i-1]==res[i]:
				f=1
				break
		if f==0:
			if len(res)>max:
				max=len(res)
	print(max)
	
inp=int(input())
str=list(input())
l=[]
p=[]
for i in range(inp):
	if str[i] not in l:
		l.append(str[i])
for i in range(len(l)):
	for j in range(i+1,len(l)):
		if (l[i],l[j]) not in p:
			p.append((l[i],l[j]))
make_t(str,l,p)
