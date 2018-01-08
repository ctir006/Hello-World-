n=int(input())
str=input()
k=int(input())
k=k%26
res=""
for i in range(len(str)):
	ascii=ord(str[i])
	if ascii >=65 and ascii <=90:
		r=ascii+k
		if r > 90:
			res+=chr(64+(r-90))
		else:
			res+=chr(r)
	elif ascii>=97 and ascii<=122:
		r=ascii+k
		if r > 122:
			res+=chr(96+(r-122))
		else:
			res+=chr(r)
	else:
		res+=str[i]
print(res)