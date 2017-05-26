def sortedintersect(a,b):
    dummy = Node(0)
    tail = dummy
    dummy.next = None
    
    while a != None and b != None:
        if a.data == b.data:
            push(tail.next, a.data)
            tail = tail.next
            a = a.next
            b = b.next
        elif a.data < b.data:
            a = a.next
        else:
            b = b.next
    
    return dummy.next

#time complexity O(m+n)

def recursive_sortedintersect(a,b):
    if a == None or b == None:
        return None
    
    if a.data < b.data:
        return recursive_sortedintersect(a.next,b)
    
    if a.data > b.data:
        return recursive_sortedintersect(a,b.next)
    
    temp = None
    temp.data = a.data
    
    temp.next = recursive_sortedintersect(a.next, b.next)
    return temp