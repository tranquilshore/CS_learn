def detectandremoveloop(self):
    slow = fast = self.head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            self.removeloop(slow)
            return 1
    return 0

def removeloop(self, loop_node):
    ptr1 = self.head
    while True:
        ptr2 = loop_node
        while ptr2.next != loop_node and ptr2.next != ptr1:
            ptr2 = ptr2.next
        if ptr2.next == ptr1:
            break
        ptr1 = ptr1.next
    ptr2.next = None
    

#better solution
def detectandremoveloop(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        if slow == fast:
            break
        slow = slow.next
        fast = fast.next.next
    if slow == fast:
        slow = head
        while slow != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None
'''
Distance traveled by fast pointer = 2 * (Distance traveled 
                                         by slow pointer)

(m + n*x + k) = 2*(m + n*y + k)

Note that before meeting the point shown above, fast
was moving at twice speed.

x -->  Number of complete cyclic rounds made by 
       fast pointer before they meet first time

y -->  Number of complete cyclic rounds made by 
       slow pointer before they meet first time

From above equation, we can conclude below

    m + k = (x-2y)*n

Which means m+k is a multiple of n. 
So if we start moving both pointers again at same speed such that one pointer (say slow) begins from head node of linked list and other pointer (say fast) begins from meeting point. When slow pointer reaches beginning of linked list (has made m steps). Fast pointer would have made also moved m steps as they are now moving same pace. Since m+k is a multiple of n and fast starts from k, they would meet at the beginning. Can they meet before also? No because slow pointer enters the cycle first time after m steps.


'''