import heapq

def prim_mst(graph):
    mst, visited, pq = 0, [False] * len(graph), [(0, 0)]
    while pq:
        cost, u = heapq.heappop(pq)
        if visited[u]: continue
        visited[u], mst = True, mst + cost
        for v, w in graph[u]: 
            if not visited[v]: heapq.heappush(pq, (w, v))
    return mst

# Example usage
graph = {0: [(1, 2), (3, 6)], 1: [(0, 2), (2, 3), (3, 8)], 2: [(1, 3), (3, 5)], 3: [(0, 6), (1, 8), (2, 5)]}
print(prim_mst(graph))
