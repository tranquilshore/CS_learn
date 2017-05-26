#iterative using dummy node
def iterative_merge(a, b):
    dummy = None
    tail = dummy
    dummy.next = None
    while True:
        if a == None:
            tail.next = b
            break
        elif b == None:
            tail.next = a
            break
        if a.data <= b.data:
            #take node from front of source and move it to front of dest
            movenode(tail.next,a)
        else:
            movenode(tail.next,b)
        tail = tail.next
        
    return dummy.next

def movenode(dest, source):
    newnode = source
    source = newnode.next
    newnode.next = dest
    dest = newnode

#recusive not good for production as it uses stack space
def recursive_merge(a,b):
    result = None
    if a == None:
        return b
    elif b == None:
        return a
    
    if a.data <= b.data:
        result = a
        result.next = recursive_merge(a.next,b)
    else:
        result = b
        result.next = recursive_merge(a,b.next)
    return result
