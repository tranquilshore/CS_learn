'''
juggling algorithm:
time complexity: O(n)
space complexity : O(1)
'''
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)


def left_rotate(a, d, n):
    for i in range(gcd(d,n)):
        temp = a[i]
        j = i
        while True:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            a[j] = a[k]
            j = k
        a[j] = temp
        
        
#different and easy approach
def rev_array(a, s, e):
    while s < e:
        temp = a[s]
        a[s] = a[e]
        a[e] = temp
        s += 1
        e -= 1

def l_rotate(a, d, n):
    rev_array(a, 0, d-1)
    rev_array(a, d, n-1)
    rev_array(a, 0, n-1)
        
a = [1, 2, 3, 4, 5, 6, 7]
d = 2
n = 7

l_rotate(a,d,n)
print a