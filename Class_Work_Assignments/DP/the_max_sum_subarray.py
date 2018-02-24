import math
def max_sum_subarray(a):
        max_so_far=0
        cur_sum=0
        index=None
        for i in range(len(a)):
                cur_sum+=a[i]
                if cur_sum>max_so_far:
                        max_so_far=cur_sum
                        index=i
        return max_so_far

n=int(input())
res=[]
for i in range(n):
    k=int(input())
    l=[int(j) for j in input().split()]
    s=0
    for j in l:
        if j>0:
            s+=j
    if s==0:
        s=float('inf')
        for j in l:
            if j>s:
                s=j
    res.append((max_sum_subarray(l),s))
for i in res:
	print(i)