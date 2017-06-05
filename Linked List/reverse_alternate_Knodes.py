def kaltreverse(head, k):
    current = head
    nxt = None
    prev = None
    cnt = 0
    
    while current != None and cnt<k:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
        cnt += 1
        
    if head!= None:
        head.next = current
    #skipping k nodes
    cnt = 0
    while cnt < k-1 and current != None:
        current = current.next
        cnt += 1
    
    if current != None:
        current.next = kaltreverse(current.next, k)
        
    return prev

'''
time complexity : O(n)
'''