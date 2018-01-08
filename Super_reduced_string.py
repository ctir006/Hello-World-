def reduce_string(str,n):
	res=""
	i=1
	while i < n:
		if str[i-1]==str[i]:
			i+=1
		else:
			res+=str[i-1]
		i+=1
	if i-1 < n:
		res+=str[i-1]
	if len(res)<n:
		reduce_string(res,len(res))
	else:
		if len(res)==0:
			print("Empty String")
		else:
			print(res)

str=input()
reduce_string(str,len(str))
