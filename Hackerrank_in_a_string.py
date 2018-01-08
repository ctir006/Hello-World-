n=int(input())
strings=[]
s="hackerrank"
for i in range(n):
	strings.append(input())
for str in strings:
	pos=0
	f=0
	for i in range(len(str)):
		if str[i]==s[pos]:
			pos+=1
		if pos==10:
			f=1
			print("YES")
			break
	if f==0:
		print("NO")