def print_all_permutation(str,start,end):
	if start==end:
		print("".join(str))
	else:
		for index in range(start,end):
			str[start],str[index]=str[index],str[start]
			print_all_permutation(str,start+1,end)
			str[start],str[index]=str[index],str[start]

inp=list(input())
print_all_permutation(inp,0,len(inp))

