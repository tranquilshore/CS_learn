from heapq import heappush, heappop
'''
Dijkstra’s Algorithm modified by heap, for a binary heap, the time complexity gets to be O((E+V)log(V))

'''
def dijkstra(graph, source):
    A = [None]*len(graph)
    queue = [(0,source)]# 0 is path len, source is vertex
    while queue:
        pathlen, v = heappop(queue)
        #if v is unvisited
        if A[v] is None:
            A[v] = pathlen
            for w, edgelen in graph[v].items():
                if A[w] is None:
                    heappush(queue, (pathlen+edgelen, w))
    
    return [-1 if x is None else x for x in A]

graph = {
  0: { 1:9, 2:5, 4:2 },
  1: { 0:9, 3:2, 5:2 },
  2: { 0:5, 3:6},
  3: { 1:2, 2:6 },
  4: { 0:2, 5:3 }, 
  5: { 1:2, 4:3}
}
source = 0

print dijkstra(graph, source)
