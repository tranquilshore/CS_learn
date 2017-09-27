graph= { 
        0 : [1],
        1 : [2],
        2 : [3],
        3 : [4],
        4 : [1] 
        }

def cycle_exist(graph):
    color = {u:'white' for u in graph}
    found_cycle = [False]
    
    for u in graph:
        if color[u] == 'white':
            dfs_visit(graph, u, color, found_cycle)
        if found_cycle[0]:
            break
    return found_cycle[0]

def dfs_visit(graph, u, color, found_cycle):
    if found_cycle[0]:
        return
    color[u] = 'grey'
    for v in graph[u]:
        if color[v] == 'grey':
            found_cycle[0] = True
            return
        if color[v] == 'white':
            dfs_visit(graph, v, color, found_cycle)
    color[u] = 'black'
    
print cycle_exist(graph)
