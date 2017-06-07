def findmaxsumlist(self, a, b):
    result = None
    pre1 = a
    curr1 = a
    pre2 = b
    curr2 = b
    
    while curr1 != None or curr2 != None:
        sum1 = 0
        sum2 = 0
        
        while curr1 != None and curr2 != None and curr1.data != curr2.data:
            if curr1.data < curr2.data:
                sum1 += curr1.data
                curr1 = curr1.next
            else:
                sum2 += curr2.data
                curr2 = curr2.next
                
        if curr1 == None:
            while curr2 != None:
                sum2 += curr2.data
                curr2 = curr2.next
        if curr2 = None:
            while curr1 != None:
                sum1 += curr1.data
                curr1 = curr1.next
        
        if prev1 == a and prev2 == b:
            result = pre1 if (sum1 > sum2) else pre2
        else:
            if sum1 > sum2:
                pre2.next = pre1.next
            else:
                pre1.next = pre2.next
                
        pre1 = curr1
        pre2 = curr2
        if curr1 != None:
            curr1 = curr1.next
        if curr2 != None:
            curr2 = curr2.next
    
    while result != None:
        print result.data
        result = result.next
        
    print ''