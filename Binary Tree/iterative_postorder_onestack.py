class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def peek(stack):
    if len(stack)>0:
        return stack[-1]
    return None

def postorder(root):
    if root is None:
        return
    current = root
    s = []
    while current is not None or len(s) > 0:
        if current is not None:
            s.append(current)
            current = current.left
        else:
            temp = peek(s).right
            if temp is None:
                temp = s.pop()
                print temp.data,
                while len(s)>0 and temp == peek(s).right:
                    temp = s.pop()
                    print temp.data,
            else:
                current = temp
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)

postorder(root)
