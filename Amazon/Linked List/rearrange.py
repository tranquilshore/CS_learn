class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)


def lastnode(head):
    curr = head
    prev = None
    while curr.next != None:
        prev = curr
        curr = curr.next
    return curr,prev

def rearrange(head):
    curr = head
    prev = None
    while curr.next != None:
        last,prev = lastnode(curr)
        print last,prev
        if prev == None:
            return curr
        last.next = curr.next
        curr.next = last 
        prev.next = None
        curr = curr.next.next

def printlist(head):
    curr = head
    while curr != None:
        print curr.data,
        curr = curr.next

rearrange(head)
#last,prev = lastnode(head.next.next)
#print last.data, prev.data 
printlist(head)

