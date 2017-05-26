def removeduplicates(self):
    current = self.head
    if current == None:
        return
    while current.next != None:
        if current.data == current.next.data:
            next_next = current.next.next
            current.next = next_next
        else:
            current = current.next
'''
time complexity: O(n)
'''