def test(temp):
	for i in range(1,len(temp)):
		if(temp[i][0]=='0'):
			return False
		if int(temp[i-1]) != int(temp[i])-1:
			return False
	return True
	
n=int(input())
strings=[]
for i in range(n):
	strings.append(input())
for str in strings:
	f=0
	if len(str)%2==0:
		for i in range(1,len(str)):
			temp=[]
			for j in range(0,len(str),i):
				temp.append(str[j:j+i])
			if(test(temp)):
				f=1
				print("YES",temp[0])
				break
	else:
		for i in range(1,len(str)):
			temp=[]
			j=0
			while j<len(str):
				if j==0 and i!=1:
					temp.append(str[j:j+i-1])
					j+=i-1
				else:
					temp.append(str[j:j+i])
					j+=i
			if(test(temp)):
				f=1
				print("YES",temp[0])
				break
	if(f==0):
		print("NO")
		