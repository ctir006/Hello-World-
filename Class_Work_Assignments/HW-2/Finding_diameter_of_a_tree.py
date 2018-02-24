'''def build_tree(l):
	if l==[]:
		return []
	p=l[0]
	left=[i for i in l if i<p]
	right=[i for i in l if i>p]
	return [build_tree(left)]+[p]+[build_tree(right)]
def print_tree(t):
	if t==[]:
		return
	print_tree(t[0])
	print(t[1],end=" ")
	print_tree(t[2])
'''	
def find_diameter(t):
	if t==[]:
		return (0,0)
	ltd,lh=find_diameter(t[0])
	rtd,rh=find_diameter(t[2])
	return max(lh+rh+1,max(ltd,rtd)),max(lh,rh)+1
	
def longest(tree):
	if tree==[]:
		return 0
	else:
		return find_diameter(tree)[0]
	
