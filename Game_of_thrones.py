str=input()
f=0
d=[]
for i in range(len(str)):
	if str[i] not in d:
		d.append(str[i])
		count=str.count(str[i])
		if count%2==1:
			if f>=2:
				print("NO")
				quit()
			else:
				f+=1
if f==0 or f==1:
	print("YES")
			