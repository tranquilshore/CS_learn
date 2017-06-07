def deletemiddle(self):
    if self.head == None or self.head.next == None:
        return self.head
    
    nxt = self.head.next
    nxtnxt = nxt.next
    
    if self.head.x == nxt.x:
        while nxtnxt != None and nxt.x == nxtnxt.x:
            self.head.nxt = nxt.next
            nxt.next = None
            nxt = nxtnxt
            nxtnxt = nxtnxt.next
            
    elif self.head.y == nxt.y:
        while nxtnxt != None and nxt.y == nxtnxt.y:
            self.head.next = nxt.next
            nxt.next = None
            
            nxt = nxtnxt
            nxtnxt = nxtnxt.next
    else:
        return None
    #recur for other segments
    
    tmp = self.head
    self.head = self.head.next
    self.deletemiddle()
    self.head = tmp
    return self.head

'''
time complexity: O(n)
'''