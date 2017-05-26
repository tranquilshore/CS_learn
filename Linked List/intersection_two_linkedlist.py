def getcount(self):
    current = self.head
    count = 0
    while current is not None:
        count += 1
        current = current.next
    return count

def getintersectionnode(d, head1, head2):
    c1 = getcount(head1)
    c2 = getcount(head2)
    if c1 > c2:
        d = c1 - c2
        return _getintersectionnode(d, head1, head2)
    else:
        d = c2 - c1
        return _getintersectionnode(d, head2, head1)

def _intersectionnode(d, head1, head2):
    current1 = head1
    current2 = head2
    
    for i in range(d):
        if current1 == None:
            return -1
        current1 = current1.next
        
    while current1 != None and current2 != None:
        if current1 == current2:
            return current1.data
        current1 = current1.next
        current2 = current2.next
    return -1

'''
time complexity: O(m+n)
space complexity: O(1)
'''