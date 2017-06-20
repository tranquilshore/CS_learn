class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
        
def buildTree(inorder, preorder, start, end):
    if start > end:
        return None
    node = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1
    
    if start == end:
        return node
    
    inIndex = search(inorder, start, end, node.data)
    
    node.left = buildTree(inorder, preorder, start, inIndex-1)
    node.right = buildTree(inorder, preorder, inIndex+1, end)
    
    return node

def search(arr, start, end, val):
    for i in range(start, end+1):
        if val == arr[i]:
            return i

def printInorder(node):
    if node is None:
        return

    printInorder(node.left)
    print node.data,
    printInorder(node.right)
        
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
inOrder = ['D', 'B' ,'E', 'A', 'F', 'C']

buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder)-1)
printInorder(root)
'''
Time Complexity: O(n^2). Worst case occurs when tree is left skewed. Example Preorder and Inorder traversals for worst case are {A, B, C, D} and {D, C, B, A}
'''