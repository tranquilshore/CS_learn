def movetofront(self):
    last = self.head
    while last.next != None:
        seclast = last
        last = last.next
        
    seclast.next = None
    last.next = self.head
    self.head = last
    
#time complexity O(n)
