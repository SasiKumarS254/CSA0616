import itertools
def tsp(dist):
    return min((sum(dist[p[i]][p[i+1]] for i in range(len(p)-1)) + dist[p[-1]][p[0]], p) 
               for p in itertools.permutations(range(len(dist))))

dist = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
print(tsp(dist))
