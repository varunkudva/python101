"""
graph.py: Simple graph module

"""
__author__ = "vkudva"

from collections import defaultdict

CYCLES_DG = "../tests/cycles.txt"  # directed
TOPO_DAG = "../tests/topo.txt"
CYCLES_G = "../tests/cycles_ug.txt"  # undirected


class Graph():
    '''
    Directed graph(Directed Graph) without weights associated.

    Represented as adjacency list with each
    node as a key in dict and a list of edges
    as values
    '''

    def __init__(self, v):
        self.adj = defaultdict(list)
        self.vertices = v
        self.num_edges = 0

        # marker to identify nodes visited
        self.visited = [False] * v

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

    def bfs(self, source):
        """ Breadth First traversal from a single source.
        visited keeps track of nodes already seen on the
        traversal. Can be used to check if a node is
        connected to the source
        """
        queue = []
        self.visited = [False] * len(self.adj)

        # add source vertex to queue
        queue.append(source)
        self.visited[source] = True

        while queue:
            u = queue.pop(0)
            print(u)
            for v in self.adj[u]:
                if visited[v] is False:
                    # mark and append to queue
                    visited[v] = True
                    queue.append(v)

    def dfs_search(self):
        """ DFS from all source to all vertices """
        for v in range(self.vertices):
            self.visited = [False] * self.vertices
            self.count = 0  # initialize connected vertex count
            print("DFS from {}:".format(v), end=' ')
            self.dfs(v)
            print()
            print("Vertices connected {}".format(v, self.count))

    def dfs(self, u):
        """ DFS from source vertex u. Count keeps track of number
        of vertices connected to a given source vertex
        """
        self.count += 1
        self.visited[u] = True
        print(u, end=' ')
        for v in self.adj[u]:
            if not self.visited[v]:
                self.dfs(v)

    def topo_sort_dfs(self, u, tlist):
        """
        Topological sort is basically dfs on the graph and ordering nodes
        based on finish times. Keep adding nodes to a stack in the order
        they finish.
        :param u: start node
        :param tlist: stack of nodes. Top finished last
        :return: tlist
        """
        self.visited[u] = True
        for v in self.adj[u]:
            if not self.visited[v]:
                self.topo_sort_dfs(v, tlist)
        tlist.insert(0, u)

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
        self.visited = [False] * self.vertices
        for u in range(self.vertices):
            if not self.visited[u]:
                self.topo_sort_dfs(u, tlist)
        return tlist

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


if __name__ == '__main__':
    filename = CYCLES_DG
    with open(filename) as fd:
        V = int(fd.readline())
        E = int(fd.readline())
        g = Graph(V)
        for lines in range(E):
            u, v = tuple(map(int, fd.readline().split()))
            g.add_edge(u, v)

        print("DFS from vertex 0:", g.dfs(0))
        g.directed_cycle()
