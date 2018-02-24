def check_subsum(i,l,s,d):
	if (i,s) in d:
		return d[(i,s)]
	if s==0:
		return True
	elif i==0 and s!=0:
		return False
	elif l[i]>s:
		d[(i,s)]=check_subsum(i-1,l,s,d)
		return d[(i,s)]
	else:
		d[(i,s)]=check_subsum(i-1,l,s-l[i],d) or check_subsum(i-1,l,s,d)
		return d[(i,s)]
		
l=[3, 34, 5, 12, 5, 2]
d={}
print(check_subsum(len(l)-1,l,6,d))