def addtwolists(self, first, second):
    prev = None
    temp = None
    carry = 0
    
    while first is not None or second is not None:
        fdata = 0 if first is None else first.data
        sdata = 0 if second is None else second.data
        
        sum_ = carry + fdata + sdata
        
        #updating carry
        carry = 1 if sum_ >= 10 else 0
        #updating sum
        sum_ = sum_ if sum_ < 10 else sum_%10
        
        #creating the resulting list
        temp = Node(sum_)
        if self.head is None:
            self.head = temp
        else:
            prev.next = temp
        
        #set prev for next iteration
        prev = temp
        
        if first is not None:
            first = first.next
        if second is not None:
            second = second.next
    
    if carry > 0:
        temp.next = Node(carry)
        
'''
Time Complexity: O(m + n)
'''

# not allowed to modify the list. also, not allowed to use explicit extra space. using recursion
def addlist(head1, head2, result):
    cur = None
    
    if head1 == None:
        result = head2
        return
    elif head2 == None:
        return
    
    size1 = getsize(head1)
    size2 = getsize(head2)
    
    carry = 0
    if size1 == size2:
        result = addsamesize(head1, head2, carry)
    else:
        diff = abs(size1 - size2)
    
        if size1 < size2:
            swappointers(head1, head2)
    
        #move diff no. of nodes in first list
        cur = head1
        for diff in range(diff,0,-1):
            cur = cur.next
    
        #addition of same size list
        result = addsamesize(cur, head2, carry)
        #addition of remaining first list and carry
        addcarrytoremaining(head1, cur, carry, result)
    
    if carry:
        push(result, carry)
        
def addsamesize(head1, head2, carry):
    if head1 == None:
        return None
    
    result = None
    #Recursively add remaining nodes and get the carry
    result.next = addsamesize(head1.next, head2.next, carry)
    sum_ = head1.data + head2.data + carry
    carry = sum_/10
    sum_ = sum_%10
    
    result.data = sum_
    return result

# This function is called after the smaller list is added to the bigger lists's sublist of same size.  Once the right sublist is added, the carry must be added toe left side of larger list to get the final result.
  
def addcarrytoremaining(head1, cur, carry, result):
    if head1 != cur:
        addcarrytoremaining(head1.next, cur, carry, result)
        sum_ = head1.data + carry
        carry = sum_/10
        sum_ = sum_/10
        
        push(result, sum_)


