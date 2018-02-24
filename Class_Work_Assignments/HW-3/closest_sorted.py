import bisect
def find(arr,x,k):
        i = bisect.bisect_left(arr, x)
        left, right = i-1, i
        while k:
            if right >= len(arr) or \
               (left >= 0 and abs(arr[left]-x) <= abs(arr[right]-x)):
                left -= 1
            else:
                right += 1
            k -= 1
        return arr[left+1:right]
print(find([1,2,3,4,4,7], 6.5, 3))
print(find([1,2,3,4,4,7], 5.2, 2))
print(find([1,2,3,4,4,6,6], 5, 3))