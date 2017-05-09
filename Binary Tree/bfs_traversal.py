class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
  
'''
time complexiy is O(n^2)
'''
def height(node):
    if node is None:
        return 0
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1
        
def printgivenlevel(root, level):
    if root is None:
        return
    if level == 1:
        print root.data,
    elif level > 1:
        printgivenlevel(root.left, level-1)
        printgivenlevel(root.right, level-1)
        
def printlevelorder(root):
    h = height(root)
    for i in range(1,h+1):
        printgivenlevel(root,i)
        
        
'''
Using queue
time complexity is O(n)
'''

def printlevelorder_queue(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while 1:
        n = len(queue)
        if n == 0:
            break
        while n>0:
            print queue[0].data,
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)
            n -= 1
        print "\n"
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print "Level order traversal of binary tree is -"
printlevelorder_queue(root)




        