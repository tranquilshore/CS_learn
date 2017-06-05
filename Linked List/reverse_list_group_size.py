def reverse(head, k):
    current = head
    nxt = None
    prev = None
    cnt = 0
    while current != None and cnt < k:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
        cnt += 1
    if nxt != None:
        head.next = reverse(nxt, k)
        
    return prev
'''
time complexity : O(n)
'''