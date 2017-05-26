def floyd_cycle_detection(self):
    slow = self.head
    fast = self.head
    
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

'''
time complexity: O(n)
space complexity: O(1)
'''
