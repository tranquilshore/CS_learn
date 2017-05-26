#O(n), constant space
def iterative(self):
    current = self.head
    prev = None
    while current != None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    self.head = prev
    
#O(n) and constant space
#with only two pointers
#using swap technique of XOR
def iterative_two(self):
    prev = None
    current = self.head
    while current is not None:
        nxt,current.next = current.next, prev
        prev,current = current, nxt
    self.head = prev
    
def recursive(self):
    if self.head is None:
        return
    first = self.head
    rest = first.next
    if rest is None:
        return
    
    recursive(rest)
    first.next.next = first
    first.next = None
    self.head = rest
    