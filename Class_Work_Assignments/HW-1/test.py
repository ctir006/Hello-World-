def count(n):
	for i in range(n):
		yield i
l=count(10)
for i in l:
	print(i)