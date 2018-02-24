import heapq
def ksmallest(k,l):
	heap=[]
	for i in l:
		if len(heap)<k:
			heapq.heappush(heap,-1*i)
		else:
			if heap[0]<(-1*i):
				heapq.heappushpop(heap,-1*i)
	return sorted([-1*i for i in heap])

print(ksmallest(3, range(1000000, 0, -1)))