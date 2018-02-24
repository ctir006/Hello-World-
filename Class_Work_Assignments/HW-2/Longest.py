def sort(l):
	if l==[]:
		return []
	p=l[0]
	left=[i for i in l if i<p]
	right=[i for i in l if i>p]
	return [sort(left)]+[p]+[sort(right)]

def longest(t,diameter):
	if t==[]:
		return (0,diameter)
	ltd,diameter=longest(t[0],diameter)
	rtd,diameter=longest(t[2],diameter)
	return 1+max(ltd,rtd),max(diameter,ltd+rtd)

def longest_helper(tree,diameter):
	if tree[0]==[] and tree[2]==[]:
		return 0
	else:
		x,y=longest(tree,1)
		return y
		
l=[1,4,2,5,6,7,3,8]
tree=sort(l)
print(tree)
print(tree)
print(longest_helper(tree,0))