def merge(self, q):
    p_curr = self.head
    q_curr = q.head
    
    while p_curr != None and q_curr != None:
        p_next = p_curr.next
        q_next = q_curr.next
        
        q_curr.next = p_next
        p_curr.next = q_curr
        
        p_curr = p_next
        q_curr = q_next
        
    q.head = q_curr