"""
Graph Module for programs
"""
from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def remove_edge(self, u, v):
        self.graph[u].remove(v)

    def bfs(self, source):
        queue = []
        visited = [0] * len(self.graph)

        queue.append(source)
        while queue:
            u = queue.pop(0)
            if visited[u] == 1:
                continue
            else:
                visited[u] = 1
                print u
                queue.extend(self.graph[u])





if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print g.graph
    print g.bfs(0)