graph={ 
        'A':['E','B','D'],
        'B':['A','D','C'],
        'C':['B'],
        'D':['A','B'],
        'E':['A']
      }

def dfs(graph,s):
    visited = []
    stack = [s]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack = stack + graph[node]
    return visited

print dfs(graph, 'A')



