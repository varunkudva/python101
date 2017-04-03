"""
Problem:


Algorithmic Pattern:
<BruteForce, Greedy, HashTable, DP, Divide and Conquer, Binary, Backtracking>

Approach/Solution:

Caveats:

Notes:

Compexity:
 Time: O(n)
 Space: O(n)

Source:
<URL>
"""
from lib.graph import Graph

def find_diameter(graph, u):
    queue, visited = [], []
    bfs_len = 0

    visited.append(u)
    queue.append(u)
    queue.append(-1)
    while queue:
       u = queue.pop(0)

       if u == -1 and queue:
           # marker node for levels
           queue.append(-1)
           bfs_len += 1
       else:
           for v in graph.adj[u]:
               if v not in visited:
                   visited.append(v)
                   queue.append(v)

    return bfs_len, visited

if __name__ == '__main__':

    filename = "../tests/DiameterGraph.txt"
    with open(filename) as fd:
        V = int(fd.readline())
        E = int(fd.readline())

        g = Graph(V)
        for lines in range(E):
            u, v = tuple(map(int, fd.readline().split()))
            g.add_edge(u, v)

        maxd = 0
        for u in g.adj.iterkeys():
            d, vertices = find_diameter(g, u)
            maxd = max(d, maxd)

        print "Max diameter {} vertices {}".format(maxd, vertices)




