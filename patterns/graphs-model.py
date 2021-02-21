"""
This document is for revising graphs
1. Undirected, directed
2. DFS, BFS on graphs
3. Path to a node
4. using parent, level, color of nodes
5. using timestamps
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Write your code here.
        # this is basically directed graph problem where we see there is no cycle
        # or the graph is DAG.
        # by ik tutorial, we just check if there is a link to ancestor or not
        # this is done by if we see neighbor in departure or not. if its not in departure
        # then its ancestor. ancestors depart later then children.
        # for reference watch omkars video.
        # the problems gives: course and dependency
        # its probably easier to do this direct graph problem by doing
        # dependency -> course
        # so we set the edge list as such.
        adj_map = defaultdict(list)
        for dst, src in prerequisites:
            adj_map[src].append(dst)
        visited = set()
        arrival = {}
        departure = {}
        result = []
        timestamp = 0
        # dfs will return True if there is cycle else False
        def dfs(node):
            nonlocal timestamp
            visited.add(node)
            arrival[node] = timestamp
            timestamp += 1
            for neighbor in adj_map[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor not in departure:
                    # parent so cycle
                    return True
            departure[node] = timestamp
            timestamp += 1
            result.append(node)
            # no cycle
            return False
        for v in range(numCourses):
            if v not in visited:
                if dfs(v):
                    return []
        # reverse as the first course will be added last to list
        return result[::-1]

    class Solution:
        def validTree(self, n: int, edges: List[List[int]]) -> bool:
            adj_map = defaultdict(list)
            for src, dst in edges:
                adj_map[src].append(dst)
                adj_map[dst].append(src)
            q = []
            visited = set()
            components = 0
            parent = {}

            # bfs way
            def bfs(source):
                q = [source]
                visited.add(source)
                parent[source] = -1
                while q:
                    node = q.pop(0)
                    for neighbor in adj_map[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            parent[neighbor] = node
                            q.append(neighbor)
                        elif neighbor != parent[node]:
                            return True
                return False

            # dfs wway
            def dfs(node):
                visited.add(node)
                for neighbor in adj_map[node]:
                    if neighbor not in visited:
                        parent[neighbor] = node
                        if dfs(neighbor):
                            return True
                    elif neighbor != parent[node]:
                        return True
                return False

            # This is the key. you cannot run over adj_list
            for vertex in range(n):
                if vertex not in visited:
                    components += 1
                    if components > 1:
                        return False
                    # if bfs(vertex):
                    #    return False
                    if dfs(vertex):
                        return False
                    # dfs(vertex)
            return True

