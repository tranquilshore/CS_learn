'''
Kosaraju's algorithm:

1. Fill vertices in stack according to their finishing time while doing DFS
2. Create a reversed DFS graph
3. Now process all vertices in order defined by Stack

'''
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    #a function used for DFS
    def DFSUtil(self,v,visited):
        visited[v] = True
        print v,
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i,visited)
                
    def fillOrder(self,v,visited,stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i,visited,stack)
        stack = stack.append(v)
        
    def getTranspose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g
    
    def scc(self):
        stack = []
        #marking all not visited
        visited = [False]*(self.V)
        #filling vertices to stack acc to finishing time in dfs
        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i,visited,stack)
                
        #creating a reversed graph
        gr = self.getTranspose()
        
        #mark again as not visited
        visited = [False]*(self.V)
        
        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.DFSUtil(i, visited)
                print""
                
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)


g.scc()
        
