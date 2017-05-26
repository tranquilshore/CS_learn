def recursive(a,b):
    if a == None and b == None:
        return True
    
    if a != None and b != None:
        return a.data == b.data and recursive(a.next,b.next)
    #if we reach here one list is empty
    return False
