def skipmdeleten(head, m, n):
    curr = head
    t = None
    while curr:
        if curr != None:
            for count in range(1,m):
                curr = curr.next
                
        if curr == None:
            return
        
        t = curr.next
        if t != None:
            for count in range(1,n+1):
                t = t.next
        curr.next = t
    curr = t
    
'''
Time Complexity: O(n)
'''