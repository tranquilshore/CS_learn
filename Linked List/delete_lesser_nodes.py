def dellessernodes(head):
    reverselist(head)
    _dellessernodes(head)
    reverse(head)
    
def _dellessernodes(head):
    current = head
    maxnode = head
    temp = None
    
    while current != None and current.next != None:
        if current.next.data < maxnode.data:
            temp = current.next
            current.next = temp.next
        else:
            current = current.next
            maxnode = current
'''
time complexity: O(n)
'''