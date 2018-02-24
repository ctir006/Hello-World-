import random
def qselect (ose , a):
    #print(a)
    if a == []:
        return
    else:
        re = random.choice(a)
        #print(re)
        pivot = [re]
        a.remove(re)
        #print (pivot)
        left = [x for x in a[0:] if x <= pivot[0] ]
        #print (left)
        right = [x for x in a[0:] if x > pivot[0] ]
        #print(left,right,end=" ")
        #print (right)
        #print (left,pivot,right)
        ll = len(left)
        rl = len(right)

        #print (pp)
        if(ll == ose-1):
            return re
        if (ll < ose-1):
            return qselect((ose-(ll+1)),right)
        if (ll > ose-1):
            return qselect(ose,left)

hihih = qselect(3,[3,3,3,3,8,2,7,5,6,4])
print (hihih)
