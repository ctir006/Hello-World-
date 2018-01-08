str=input()
inp=int(input())
weights=[]
for i in range(inp):
	weights.append(input())
u_string=[]
d={}
for i in range(1,len(str)):
	for j in range(len(str)+1-i):
		t=str[j:j+i]
		if t.count(t[0])==len(t):
			if t not in u_string:
				u_string.append(t)
for i in u_string:
	wei=(ord(i[0])-96)*len(i)
	d[i]=wei
values=d.values()
for i in weights:
	if int(i) in values:
		print("Yes")
	else:
		print("No")
	