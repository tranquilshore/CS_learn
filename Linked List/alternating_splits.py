def alternating_splits(source):
    adummy = None
    atail = adummy
    
    bdummy = None
    btail = bdummy
    
    current = source
    adummy.next=None
    bdummy.next = None
    
    while current != None:
        push(atail.next, current)
        atail = atail.next
        if current != None:
            push(btail.next, current)
            btail = btail.next
        
    return adummy.next, bdummy.next
