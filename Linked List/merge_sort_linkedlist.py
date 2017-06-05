"merge sort is preferred for sorting a linked list. slow random access performance of a linked list makes quicksort and other algorithms like this to perform poorly"

#sorts by changing next pointers not data
def mergesort(headref):
    head = headref
    a = None
    b = None
    
    if head == None or head.next = None:
        return
    
    #splitting head into a and b sublists
    frontbacksplit(head, a, b)
    
    #recursively sort the subtitles
    mergesort(a)
    mergesort(b)
    
    headref = sortedmerge(a,b)

def frontbacksplit(source, frontref, backref):
    fast = None
    slow = None
    if source == None or source.next == None:
        frontref = source
        backref = None
    else:
        slow = source
        fast = source.next
        #advance fast to two nodes and advance slow one node
        while fast != None:
            fast = fast.next
            if fast != None:
                slow = slow.next
                fast = fast.next
        frontref = source
        backref = slow.next
        slow.next = None

def sortedmerge(a, b):
    result = None
    #base cases
    if a == None:
        return b
    elif b == None:
        return a
    
    if a.data <= b.data:
        result = a
        result.next = sortedmerge(a.next,b)
    else:
        result = b
        result.next = sortedmerge(a,b.next)
        
    return result