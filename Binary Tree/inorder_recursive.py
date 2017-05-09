def inorder(root):
    current = root
    s = []
    done = 0
    
    while not done:
        if current is not None:
            s.append(current)
            current = current.left
            
        else:
            if len(s)>0:
                current = s.pop()
                print current.data,
                current = current.right
            else:
                done = 1