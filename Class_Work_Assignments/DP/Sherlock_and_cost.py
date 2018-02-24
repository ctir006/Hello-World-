def find_cost(input_list):
	for i in input_list:
		n=i[0]
		list=i[1]
		list.sort()
		print(list)
		k=0
		l=len(list)-1
		t=[]
		pos=0
		while k<l:
			t.append(list[l])
			t.append(list[k])
			k+=1
			l-=1
		if k==l:
			t.append(list[k])
		print(t)
		sum=0
		for k in range(1,len(t)):
			sum+=abs(1-t[k-1])
			print(sum,t[k],t[k-1])
		return sum
n=int(input())
input_list=[]
for i in range(n):
	k=int(input())
	l=[int(i) for i in input().split()]
	input_list.append((k,l))
print(find_cost(input_list))