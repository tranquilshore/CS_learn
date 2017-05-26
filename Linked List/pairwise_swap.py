def iterative_pairwiseswap(self):
    temp = self.head
    while temp != None and temp.next != None:
        temp.data, temp.next.data = temp.next.data, temp.data
        temp = temp.next.next

def recursive_pairwiseswap(self):
    if self.head != None and self.head.next != None:
        self.head.data, self.head.next.data = self.head.next.data, self.head.data
        
        recursive_pairwiseswap(self.head.next.next)
        
