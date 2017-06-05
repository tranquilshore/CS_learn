def segregateevenodd1(head):
    end = head
    prev = None
    current = head
    
    while end.next != None:
        end = end.next
        
    new_end = end
    
    #to move all the odd nodes before the first even node and move them after end
    while current.data % 2 != 0 and current != end:
        new_end.next = current
        current = current.next
        new_end.next.next = None
        new_end = new_end.next
    
    #do following for even nodes
    if current.data % 2 == 0:
        head = current
        while current != end:
            if current.data % 2 == 0:
                prev = current
                current = current.next
            else:
                prev.next = current.next
                current.next = None
                new_end.next = current
                new_end = current
                current = prev.next
    else:
        prev = current
    
    if new_end != end and end.data % 2 != 0:
        prev.next = end.next
        end.next = None
        new_end.next = end
    return

def segregateevenodd2():
    evenstart = None
    evenend = None
    oddstart = None
    oddend = None
    currentnode = head
    
    while currentnode != None:
        element = currentnode.data
        if element%2 == 0:
            if evenstart == None:
                evenstart = currentnode
                evenend = evenstart
            else:
                evenend.next = currentnode
                evenend = evenend.next
        else:
            if oddstart == None:
                oddstart = currentnode
                oddend = oddstart
            else:
                oddend.next = currentnode
                oddend = oddend.next
        
        currentnode = currentnode.next
    
    if oddstart == None or evenstart == None:
        return
    
    evenend.next = oddstart
    oddend.next = None
    head = evenstart

'''
time complexity: O(n)
'''