#assumes that the list b is sorted in ascending order and c is sorted in descending order.

def triplet_sum(heada, headb, headc, num):
    a = heada
    while a != None:
        b = headb
        c = headc
        
        while b != None and c != None:
            sum_ = a.data + b.data + c.data
            if sum_ == num:
                return True
            elif sum_ < num:
                b = b.next
            else:
                x = c.next
    a = a.next
'''
time complexity :O(nlogn) + O(nlogn) + O(n*n) = O(n*n)
'''