graph = {
    0:[1,2],
    1:[0,2],
    2:[0,1,3],
    3:[2,3]
}

def bfs(graph,s):
    visited = [False]*(len(graph))
    queue = []
    
    queue.append(s)
    visited[s] = True
    
    while queue:
        s = queue.pop(0)
        print s,
        
        for i in graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

bfs(graph,2)
'''

Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph.

'''