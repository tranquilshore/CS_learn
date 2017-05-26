def delalt(self):
    if self.head == None:
        return
    
    prev = self.head
    node = self.head.next
    
    while prev != None and node != None:
        prev.next = node.next
        #automatically free memory
        prev = prev.next
        if prev != None:
            node = prev.next

def recursive_delalt(self):
    if self.head == None:
        return
    node = head.next
    
    if node == None:
        return
    
    head.next = node.next
    #automatically free memory
    recursive_delalt(head.next)
    
#timecomplexity O(n)
