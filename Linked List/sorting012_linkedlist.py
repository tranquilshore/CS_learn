def sortlist(head):
    count = [0,0,0]
    ptr = head
    
    while ptr != None:
        count[ptr.data] += 1
        ptr = ptr.next
    
    i = 0
    ptr = head
    
    while ptr != None:
        if count[i] == 0:
            i += 1
        else:
            ptr.data = i
            count[i] -= 1
            ptr = ptr.next
'''
Time Complexity: O(n) where n is number of nodes in linked list.
Auxiliary Space: O(1)
'''