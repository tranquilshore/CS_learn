'''
cycle detection in undirected:

DFS traversal of graph with vertex v which has a neighbour u which is already visited but is not the parent of v.

'''
graph = { 
        0 : [1],
        1 : [0, 2, 3, 5],
        2 : [1],
        3 : [1, 4],
        4 : [3, 5],
        5 : [1, 4]
}

def cycle_exists(graph):
    marked = {u: False for u in graph}
    found_cycle = [False]
    
    for u in graph:
        if not marked[u]:
            dfs_visit(graph, u, found_cycle, u, marked) #u is its own predecessor initially
        if found_cycle[0]:
            break
    return found_cycle[0]

def dfs_visit(graph, u, found_cycle, pred_node, marked):
    if found_cycle[0]:
        return
    marked[u] = True
    for v in graph[u]:
        if marked[v] and v != pred_node:
            found_cycle[0] = True
            return
        if not marked[v]:
            dfs_visit(graph, v, found_cycle, u, marked)
            
print cycle_exists(graph)