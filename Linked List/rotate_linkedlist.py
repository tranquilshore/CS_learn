def rotate(self, k):
    if k = 0:
        return
    
    current = self.head
    count = 1
    while count <k and current is not None:
        current = current.next
        count += 1
        
    if current is None:
        return
    
    kthnode = current
    while current.next is not None:
        current = current.next
        
    current.next = self.head
    self.head = kthnode.next
    
    kthnode.next = None
    
'''
Time Complexity: O(n) 
'''