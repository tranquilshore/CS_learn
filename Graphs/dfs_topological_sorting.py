'''
Applications:

1. Build Systems : to build your project on some ide
2. Advanced packaging tool (apt-get)
3. Job scheduling 
4. Pre-requisite problem

Topological sort is not unique

Def: For DAGs (Directed Acyclic Graphs), it's a linear order of vertices s.t. vertex u comes before v for every directed edge(u,v)

Approach: Colour code traversing which checks for cycle as well and return the reverse of list with all black colour nodes.

'''
graph = { 0 : [1, 2],
           1 : [3, 4],
           2 : [],
           3 : [],
           4 : [],
           5 : [6, 7],
           6 : [],
           7 : [] }

def dfs_topsort(graph):
    L = []
    color = { u: 'white' for u in graph}
    found_cycle = [False]
    
    for u in graph:
        if color[u] == 'white':
            dfs_visit(graph, u, color, L, found_cycle)
        if found_cycle[0]:
            break
    if found_cycle[0]:
        L = []
    L.reverse()
    return L

def dfs_visit(graph, u, color, L, found_cycle):
    if found_cycle[0]:
        return
    color[u] = 'grey'
    for v in graph[u]:
        if color[v] == 'grey':
            found_cycle[0] = True
            return
        if color[v] == 'white':
            dfs_visit(graph, v, color, L, found_cycle)
    color[u] = 'black'
    L.append(u)

print dfs_topsort(graph)
