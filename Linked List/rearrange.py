def rearrange(head):
    slow = head
    fast = slow.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    head1 = head
    head2 = slow.next
    slow.next = None
    
    reverselist(head2)
    
    head = None
    curr = head
    
    while head1 or head2:
        if head1 :
            curr.next = head1
            curr = curr.next
            head1 = head1.next
            
        if head2:
            curr.next = head2
            curr = curr.next
            head2 = head2.next
    
    head = head.next
    
'''
Time Complexity of this solution is O(n).
'''