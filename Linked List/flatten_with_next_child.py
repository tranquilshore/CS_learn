def flattenlist(head):
    if head == None:
        return
    
    tmp = None
    tail = head
    
    while tail.next != None:
        tail = tail.next
        
    curr = head
    while curr != tail:
        if curr.child:
            tail.next = curr.child
            
            tmp = curr.child
            while tmp.next:
                tmp = tmp.next
            tail = tmp
        curr = curr.next
'''
time complexity : O(n)
'''