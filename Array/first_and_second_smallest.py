import sys
#O(n)
def twosmallest(a, n):
    if n < 2:
        return "invalid input"
    
    first = sys.maxint
    second = sys.maxint
    
    for i in range(n):
        #if current elem is smaller than first
        if a[i]<first:
            second = first
            first = a[i]
        elif a[i]<second and a[i]!= first:
            second = a[i]
    if second == sys.maxint:
        print "no second smallest"
    else:
        print first, second
        
a = [12, 13, 1, 10, 34, 1]
n = len(a)
print twosmallest(a,n)