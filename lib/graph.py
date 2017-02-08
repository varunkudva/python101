#!/usr/bin/env python
"""
graph.py: Simple graph module
"""
__author__ = "vkudva"

from collections import defaultdict

class Graph():
    '''
    Directed graph without weights associated.

    Represented as adjacency list with each
    node as a key in dict and a list of edges
    as values
    '''
    def __init__(self, v):
        self.adj = defaultdict(list)
        self.num_vertices = v
        self.num_edges = 0

        # marker to identify nodes visited
        self.visited = [False] * v

        # count of connected vertices
        # to a particular source
        self.count = 0

    def _validate_vertex(self, v):
        if v < 0 or v >= self.num_vertices:
            raise

    def add_edge(self, u, v):
        # u and v are nodes
        self.num_edges += 1
        self.adj[u].append(v)

    def remove_edge(self, u, v):
        self.num_edges -= 1
        self.adj[u].remove(v)

    def bfs(self, source):
        queue = []
        visited = [False] * len(self.adj)

        queue.append(source)
        visited[source] = True

        while queue:
            u = queue.pop(0)
            print u
            for i in self.adj[u]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True

    def dfs_search(self):
        for v in range(self.num_vertices):
            self.visited = [False] * self.num_vertices
            self.count = 0 # initialize connected vertex count
            print "DFS from {}:".format(v),
            self.dfs(v)
            print
            print "Vertices connected {}".format(v, self.count)

    def dfs_search_2(self):
        self.visited = [False] * self.num_vertices
        for u in range(self.num_vertices):
            if not self.visited[u]:
                self.dfs(u)

    def dfs(self, u):
        self.count += 1
        self.visited[u] = True
        print u,
        for v in self.adj[u]:
            if not self.visited[v]:
                self.dfs(v)

    def topo_sort(self):
        pass


if __name__ == '__main__':
    """
    Example Graph
    """
    g = Graph(6)
    g.add_edge(5,0)
    g.add_edge(5,2)
    g.add_edge(2,3)
    g.add_edge(3,1)
    g.add_edge(4,0)
    g.add_edge(4,1)
    # print g.adj
    # g.dfs_search()
    g.dfs_search_2()
    # print g.bfs(5)