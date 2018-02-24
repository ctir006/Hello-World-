#al - array length
#al - array length
import math
import heapq

def merge(ol,arrays,n,k):
        heap=[]
        res=[]
        pos=0
        for i in range(k):
                if arrays[i]!=[]:
                        heapq.heappush(heap,(arrays[i][0],i,0))
        while len(heap)!=0:
                k=heapq.heappop(heap)
                ol[pos]=k[0]
                pos+=1
                p=k[2]
                ar=k[1]
                if p+1>=len(arrays[ar]):
                        continue
                else:
                        heapq.heappush(heap,(arrays[ar][p+1],ar,p+1))

def kmergesort_help(l,n,k):
        if n<2:
            return
        al=int(math.ceil(n/k))
        arrays=[]
        for i in range(k):
                arrays.append([])
        pos=0
        for i in range(k):
                arrays[i]=l[pos:pos+al]
                pos+=al
        for i in range(k):
                kmergesort_help(arrays[i],len(arrays[i]),k)
        merge(l,arrays,al,k)

def kmergesort(l,k):
        c=len(l)%k
        if c!=0:
                for i in range(k-c):
                        l.append(-1)
        kmergesort_help(l,len(l),k)
        pos=0
        while True:
                if l[pos]!=-1:
                        break
                pos+=1
        return l[pos:]
		
print(kmergesort([4,1,5,2,6,3,7,0], 5)) 