#node class
class Node:    
    #function to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

#linked list class
class LinkedList:
    def __init__(self):
        self.head = None
    
    #function to print the linked list
    def printlist(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next
    #function to add a node at the front of the list, O(1) time complexity
    def push(self, push_data):
        push_node = Node(push_data)
        push_node.next = self.head
        self.head = push_node
    
    def insertafter(self, prev_node, new_data):
        if prev_node is None:
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    #time complexity is O(n)
    def append(self, append_data):
        append_node = Node(append_data)
        if self.head is None:
            self.head = append_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = append_node
        
    #deletion with a given key
    def deleteNodeK(self,key):
        temp = self.head
        
        #if head node holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        #searching for the key to be deleted and keeping the note of previous element
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        #if key is not present
        if temp == None:
            return
        
        prev.next = temp.next
        temp = None
        
    #deletion with a given position
    def deleteNodeP(self,position):
        if self.head == None:
            return 
        #store head node
        temp = self.head
        #if head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        #finding previous node of the node to be deleted
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
        #position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return
        
        next = temp.next.next
        temp.next = None
        temp.next = next
    
    #length of the linked list
    def getLength_iterative(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    def getLength_recursive(self, node):
        if not node:
            return 0
        else:
            return 1 + self.getLength_recursive(node.next)
        
    def getCount(self):
        return self.getCount(self.head)
    
    def search_iterative(self,key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    
    def search_recursive(self,key,node):
        if not node:
            return False
        if node.data == key:
            return true
        
        return search_recursive(node.next, key)
    
    def swapnodes(self,x,y):
        if x == y:
            return
        prevx = None
        currx = self.head
        while currx != None and currx.data !=y:
            prevx = currx
            currx = currx.next
            
        prevy = None
        curry = self.head
        while curry != None and curry.data != y:
            prevy = curry
            curry = curry.next
            
        if currx == None or curry == None:
            return
        
        
        #important
        if prevx != None:
            prevx.next = curry
        else:
            self.head = curry
        
        if prevy != None:
            prevy.next = currx
        else:
            self.head = currx
            
        temp = currx.next
        currx.next = curry.next
        curry.next = temp
    
        
#linked list with 3 nodes

if __name__ == '__main__':
    llist = LinkedList()
    
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    llist.head.next = second
    second.next = third
    
    llist.printlist()
    
