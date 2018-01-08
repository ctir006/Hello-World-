n=int(input())
strings=[]
for i in range(n):
	strings.append(input())
for str in strings:
	rev=""
	f=0
	for i in range(1,len(str)+1):
		rev+=str[-i]
	for i in range(1,len(str)):
		l=ord(str[i-1])-ord(str[i])
		r=ord(rev[i-1])-ord(rev[i])
		if l<0:
			l*=-1
		if r<0:
			r*=-1
		if l!=r:
			f=1
			print("Not Funny")
			break
	if f==0:
		print("Funny")