"""
graph.py: Simple directed graph module
Ref: Algorithms by Robert Sedgewick
https://algs4.cs.princeton.edu/41graph/

undirected graph templates. identical for

"""
from collections import defaultdict
import heapq

CYCLES_DG = "../tests/cycles.txt"  # directed
TOPO_DAG = "../tests/topo.txt"
CYCLES_G = "../tests/cycles_ug.txt"  # undirected


class Graph():
    '''
    Undirected graph without weights associated.

    Represented as adjacency list with each
    node as a key in dict and a list of edges
    as values
    '''
    def __init__(self, v):
        self.adj = defaultdict(list)
        self.vertices = v
        self.num_edges = 0

        # different markers for each node in the graph
        self.visited = set()
        self.parent = {}
        self.color = {}     # color of a node in bipartite case
        self.level = {}     # used to keep track of level of node
        self.disc = {}      # discovery time of a node
        self.finish = {}     # finish time of a node

        # count of connected vertices
        # to a particular source
        self.count = 0

    def _validate_vertex(self, v):
        if v < 0 or v >= self.vertices:
            raise

    def add_edge(self, u, v):
        # u and v are nodes
        self.num_edges += 1
        self.adj[u].append(v)
        # self.adj[v].append(u)

    def remove_edge(self, u, v):
        self.num_edges -= 1
        self.adj[u].remove(v)
        self.adj[v].remove(u)

    def bfs(self, src):
        """ Breadth First traversal from a single source.
        visited keeps track of nodes already seen on the
        traversal. Can be used to check if a node is
        connected to the source

        parent: To identify parent of a vertex in traversal to construct path
        level: level of a vertex in bfs traversal to calculate distance from source
        """
        queue = []
        visited = set()
        parent = dict()
        level = dict()

        # add source vertex to queue
        queue.append(src)
        visited.add(src)
        parent[src] = None
        level[src] = 0

        while queue:
            src = queue.pop(0)
            for neigh in self.adj[src]:
                if neigh not in visited:
                    """
                    this is different from dfs, in dfs we add node to visited
                    when we enter the node. here we it when discovering itself
                    as there can be multiple edges to the node from previous level
                    """
                    visited.add(neigh)
                    parent[neigh] = src
                    level[neigh] = level[src] + 1
                    queue.append(neigh)

    def bipartite(self):
        pass


    def dfs_search(self):
        """ DFS from all source to all vertices """
        components = 0 # no. of components in the graph
        visited = set()
        count = dict()
        parent = dict()
        discovered = dict() # discovery time
        finished = dict() # finish time
        timestamp = [0] # global time counter

        def dfs(self, src):
            """ DFS from source vertex. Count keeps track of number
            of vertices connected to a given source vertex
            """
            nonlocal timestamp
            timestamp = timestamp + 1
            visited.add(src)
            discovered[src] = timestamp
            for neigh in self.adj[src]:
                if neigh not in self.visited:
                    parent[neigh] = src
                    dfs(neigh)
                elif neigh not in finished:
                    # neigh is still on stack. So a cycle exists
                    pass

            timestamp += 1
            finished[src] = timestamp


        # outer vertices loop
        for src in range(self.vertices):
            self.count = 0
            if src not in visited:
                # new component
                components += 1
                dfs(src)



    def dfs_paths(self, src):
        # do a dfs to reach all the vertices connected
        # and record the paths
        self.dfs(src)
        # visited will say if theres a path from src to
        # vertex v
        def print_paths(src, dst):
            while parent[dst] != src:
                stack.append(dst)
                dst = parent[dst]
            stack.append[src]
            return stack

        for v in self.vertices:
            path = []
            if self.visited[v]:
                path = print_paths(src, v)
            return path



    def topo_sort(self):
        """
        Topological sort is a sorting of vertices in a DAG
        such that if there is an edge from u -> v, then u
        appears before v in the sorted order.

        A modified dfs of the graph where the vertices are stored
        in a stack instead of printing them accomplishes them
        Do a dfs through all the vertices and add the vertices to
        the front of a stack based on finishing times.
        """
        tlist = []
        visited = set()
        def topo_sort_dfs(self, node):
            """
            Topological sort is basically dfs on the graph and ordering nodes
            based on finish times. Keep adding nodes to a stack in the order
            they finish.
            :param u: start node
            :param tlist: stack of nodes. Top finished last
            :return: tlist
            """
            visited.add(node)
            for neigh in self.adj[u]:
                if neigh not in visited:
                    topo_sort_dfs(neigh)

            # all neighbors of node visited
            tlist.insert(0, node)

        for vertex in range(self.vertices):
            if not self.visited[vertex]:
                topo_sort_dfs(vertex, tlist)

        return tlist

    def isBipartite(self, graph):
        """
        bipartite checks if the vertices in the graph can be split into
        2 sets such that edges connect only vertices from one set to
        another set
        we do a dfs and color every neighbor with a flipped color than
        nodes color. If at any point we run into a neighbor which is
        already colored with same color as current node, we return false
        two coloring and bipartite
        color =[]
        """
        color = dict()
        visited = set()

        def dfs(node):
            visited.add(node)
            for neigh in adj[node]:
                if not visited[neigh]:
                    color[neigh] = 1 - color[node]
                    dfs(neigh)
                elif color[neigh] == color[node]:
                    self.is_bipartite = False

        for node in range(len(graph)):
            if not visited[node]:
                dfs(node)

        return self.is_bipartite

    def find_bridges(self):
        """
        based on https://cp-algorithms.com/graph/bridge-searching.html
        :return:
        """
        visited = set()
        disc = dict()
        low = [float('inf')] * self.vertices
        timestamp = 0
        def bridge_find(node, parent):
            nonlocal  timestamp
            timestamp += 1
            disc[node] = low[node] = timestamp
            visited.add(node)
            for neigh in self.adj[node]:
                if neigh == parent:
                    continue
                if node in visited:
                    # backedge
                    low[node] = min(low[node], disc[neigh])
                else:
                    # tree edge
                    if bridge_find(neigh):
                        return True

                    low[node] = min(low[neigh], low[node])
                    if low[neigh] > disc[node]:
                        # found bridge edge
                        res = (node, neigh)
                        return True

        res = [] # contains the edge
        for node in range(self.vertices):
            if node not in visited:
                if bridge_find(node, None):
                    return res

    def dfs_cycle(self, v):
        """
        modified dfs to check for cycles in Digraph
        """
        self.visited[v] = True
        self.on_stack[v] = 1
        for w in self.adj[v]:
            if self.cycle:
                return
            if self.on_stack[w]:
                # cycle
                x = v
                self.cycle.insert(0, w)
                while x != w:
                    # save cycle in stack
                    self.cycle.insert(0, x)
                    x = self.path_to[x]
                self.cycle.insert(0, w)
            elif not self.visited[w]:
                self.path_to[w] = v
                self.dfs_cycle(w)

        self.on_stack[v] = 0

    def directed_cycle(self):
        """
        Directed cycle checks if there is a back edge from a node to any
        node in the recursive stack.
        on_stack: keeps track of all the nodes visited on a given recursive
        call from source vertex.
        path_to: keeps track of previous vertex connecting to this vertex and
        can be used to backtrack back to the source vertex from a given vertex.
        cycle[]: is a stack maintaining the cycle found
        :return:
        """
        self.on_stack = [0] * self.vertices
        self.path_to = [0] * self.vertices
        self.visited = [False] * self.vertices
        self.cycle = []
        for u in range(self.vertices):
            if not self.visited[u]:
                self.dfs_cycle(u)

            if self.cycle:
                print("Cycle: {}".format(",".join(map(str, self.cycle))))
                return True

        print("No cycle found!!")

    def dijkstra_lazy(self, src):
        """
        This algo uses a min pq to get the edge with lowest weight and add it
        to the path. PQ stores the (dist[src], node) pairs.
        During the process of relaxing all its neighbors, the d[neigh] needs
        to be reduced, which in turn requires access to the heap node and a reduce
        key. To reduce complexity, we do a lazy insert of the pair again with new
        distance. source: https://cp-algorithms.com/graph/dijkstra_sparse.html

        Time complexity:
        In min index version: (1) find_min from pq takes logV and (2) relaxing an edge takes logV
        (1) runs for all V and (2) for all E => O(VlogV + ElogV) => O(ElogV)
        Since we have duplicate nodes in the heap with different d[u] max nodes in heap == E
        so the complexity for (1) and (2) changes to O(ElogE + ElogE) => O(ElogE)
        """
        # d: distance of vertices from src
        d = [float('inf')] * self.vertices
        parent = [None] * self.vertices
        d[src] = 0
        parent[src] = src
        pq = [(d[src],src)] # minheap

        while pq:
            # pop min node
            node_dist, node = heapq.heappop(pq)

            if node_dist != d[node]:
                # this is a old pair, delete
                # this is a lazy way to check if the node is ineligible
                continue

            # for all neighbors of node, relax neigh
            for neigh, weight in self.adj[node]:
                # relax distance of v
                if d[neigh] > d[node] + weight:
                    d[neigh] = d[node] + weight
                    parent[neigh] = node
                    # insert back into pq
                    heapq.heappush((d[neigh], neigh)
