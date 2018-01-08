str1=input()
str2=input()
d1={}
d2={}
count=0
for i in range(len(str1)):
	d1[str1[i]]=d1.get(str1[i],0)+1
for i in range(len(str2)):
	d2[str2[i]]=d2.get(str2[i],0)+1
for i in d1:
	if i not in d2:
		count+=d1[i]
	else:
		if d1[i]>d2[i]:
			count+=d1[i]-d2[i]
			d2[i]=0
		else:
			count+=d2[i]-d1[i]
			d2[i]=0
for i in d2:
	count+=d2[i]
print(count)