graph = {
    0:[1,2],
    1:[0,2],
    2:[1,0]
}

def isbipartite(graph,s):
    color = [-1]*len(graph)
    color[s] = 1
    
    queue = []
    queue.append(s)
    
    while queue:
        s = queue.pop(0)
        
        #return false if self-loop is there
        for i in graph[s]:
            if i == s:
                return False
            
        for i in graph[s]:
            if color[i] == -1:
                color[i] = 1 - color[s]
                queue.append(i)
            elif color[i] == color[s]:
                return False
    return True

print "yes" if isbipartite(graph,0) else "No"