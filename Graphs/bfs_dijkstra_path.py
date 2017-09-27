from collections import defaultdict
from heapq import *

edges = [
    ("A", "B", 9),
    ("A", "C", 5),
    ("A", "E", 2),
    ("B", "A", 9),
    ("B", "D", 2),
    ("B", "F", 2),
    ("D", "C", 6),
    ("D", "B", 2),
    ("C", "A", 5),
    ("C", "D", 6),
    ("E", "A", 2),
    ("E", "F", 3),
    ("F", "E", 3),
    ("F", "B", 2)
]

def dijkstra(edges, s, d):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0, s, ())], set()
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == d:
                return (cost,path)
            for c,v2 in g.get(v1,()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))
    return float("inf")

print dijkstra(edges, 'A', 'C')
