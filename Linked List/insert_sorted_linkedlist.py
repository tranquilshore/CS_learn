def sortedInsert(self,newnode):
    #case 1
    if self.head is None:
        newnode.next = self.head
        self.head = newnode
    #case 2
    elif self.head.data>= newnode.data:
        newnode.next = self.head
        self.head = newnode
    #case 3
    else:
        current = self.head
        while current.next is not None and current.next.data < newnode.data:
            current = current.next
            
        newnode.next = current.next
        current.next = newnode