'''
Serialization is to store tree in a file so that it can be later restored. The structure of tree must be maintained. Deserialization is reading tree back from file.

If given binary tree is:
1. For Binary Search Tree, we can store it by either storing preorder or postorder traversal.
2. For a complete Binary Tree, level order traversal is sufficient to store the tree.
3. For Full Binary Tree,  We can simply store preorder traversal and store a bit with every node to indicate whether the node is an internal node or a leaf node.

For general binary tree:
We can do Preorder traversal and keep a marker for NULL pointers. This will save the space of keeping two diffenrent traversals

eg.

Input:
         20
       /    
      8     
     / \
    4  12 
      /  \
     10  14
Output: 20 8 4 -1 -1 12 10 -1 -1 14 -1 -1 -1 
'''
#here i have used # instead of -1 for null pointers
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def serialize(root):
    def doit(node):
        if node:
            vals.append(str(node.data))
            doit(node.left)
            doit(node.right)
        else:
            vals.append("#")
    vals = []
    doit(root)
    return ' '.join(vals)

def deserialize(data):
    def doit():
        val = next(vals)
        if val == "#":
            return None
        node = Node(int(val))
        node.left = doit()
        node.right = doit()
        return node
    vals = iter(data.split())
    return doit()

root = Node(10)
root.left = Node(10)
root.right = Node(19)
root.left.left = Node(-5)
root.right.left = Node(17)
root.right.right = Node(21)

data = serialize(root)
node = deserialize(data)
print node.left.left.data


#deserialize(root1,f1)


