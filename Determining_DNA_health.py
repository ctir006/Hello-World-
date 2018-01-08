def find_lps(lps,pat,m):
	index=1
	len=0
	lps[0]=0
	while index < m:
		if pat[index]==pat[len]:
			len+=1
			lps[index]=len
			index+=1
		elif pat[index]!=pat[len]:
			if len!=0:
				len=lps[len-1]
			else:
				lps[index]=0
				index+=1
def searching(txt,pat,lps,tl,pl):
	count=0
	i=0
	j=0
	while(i<tl):
		if txt[i]==pat[j]:
			i+=1
			j+=1
		if j==pl:
			count+=1
			j=lps[j-1]
		elif i<tl and txt[i]!=pat[j]:
			if j!=0:
				j=lps[j-1]
			else:
				i+=1
	return count
n=int(input())
genes=list(input().split())
values=list(input().split())
ns=int(input())
strands=[]
result=[]
for i in range(ns):
	strands.append(input())
for strand in strands:
	start,end,d=strand.split()
	start=int(start)
	end=int(end)
	t_genes=genes[start:end+1]
	t_values=values[start:end+1]
	res=0
	for i in range(len(t_genes)):
		lps=[]
		for j in range(len(t_genes[i])):
			lps.append(0)
		find_lps(lps,t_genes[i],len(t_genes[i]))
		res+=searching(d,t_genes[i],lps,len(d),len(t_genes[i]))*int(t_values[i])
	result.append(res)
result=sorted(result)
print(result[0],result[-1])