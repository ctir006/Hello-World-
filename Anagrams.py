inp=int(input())
input_strings=[]
for i in range(inp):
	input_strings.append(input())
res=[]
for str in input_strings:
	if len(str)%2==1:
		res.append(-1)
		continue
	else:
		count=0
		str1="".join(sorted(str[:int(len(str)/2)]))
		str2="".join(sorted(str[int(len(str)/2):]))
		d={}
		v=[]
		for i in range(len(str1)):
			if str1[i] not in d:
				d[str1[i]]=str1.count(str1[i])
		for i in range(len(str2)):
			if str2[i] not in v:
				v.append(str2[i])
				if str2[i] not in d:
					d[str2[i]]=str2.count(str2[i])
					count+=d[str2[i]]
				else:
					s2_count=str2.count(str2[i])
					s1_count=d[str2[i]]
					if(s1_count<s2_count):
						count+=s2_count-s1_count

		res.append(count)
for i in res:
	print(i)