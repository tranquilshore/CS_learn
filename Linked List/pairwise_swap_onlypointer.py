def pairwiseswap(head):
    if head == None or head.next == None:
        return head
    
    prev = head
    curr = head.next
    
    head = curr
    
    while True:
        nxt = curr.next
        curr.next = prev
        
        if nxt == None or nxt.next == None:
            prev.next = nxt
            break
        
        prev.next = nxt.next
        
        prev = nxt
        curr = prev.next
        