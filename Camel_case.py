str=input()
count=1
for i in range(len(str)):
	if str[i].isupper():
		count+=1
print(count)