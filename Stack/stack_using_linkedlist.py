class stacknode:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class stack:
    
    def __init__(self):
        self.root = None
        
    def isempty(self):
        return True if self.root is None else False
    
    def push(self, data):
        newnode = stacknode(data)
        newnode.next = self.root
        self.root = newnode
        
    def pop(self):
        if self.isempty():
            return float("-infy")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped
    
    def peek(self):
        if self.isempty():
            return float("-inf")
        return self.root.data
'''
dynamic but required extra memory
'''