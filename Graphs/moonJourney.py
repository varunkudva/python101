"""
The member states of the UN are planning to send people to the Moon. But there is a problem. In line
with their principles of global unity, they want to pair astronauts of different countries.
There are trained astronauts numbered from to . But those in charge of the mission did not
receive information about the citizenship of each astronaut. The only information they have is that some
particular pairs of astronauts belong to the same country.

Your task is to compute in how many ways they can pick a pair of astronauts belonging to different
countries. Assume that you are provided enough pairs to let you identify the groups of astronauts even
though you might not know their country directly. For instance, if are astronauts from the same
country; it is sufficient to mention that and are pairs of astronauts from the same country
without providing information about a third pair .
"""
from collections import defaultdict

def moon_pair(N):
    visited = [0] * N
    exclude_pair = 0
    total_pairs = (N * (N-1)) / 2
    for i in range(0, N):
        if not visited[i]:
            count = bfs(i, visited)
            exclude_pair += (count * (count-1))/2

    return total_pairs - exclude_pair

def bfs(i, visited):
   queue = []
   queue.append(i)
   count = 0
   while queue:
       i = queue.pop(0)
       visited[i] = 1
       count += 1
       for j in adj[i]:
           if not visited[j]:
               queue.append(j)
   return count

def dfs(i, visited, count=0):
    visited[i] = 1
    count += 1
    for j in adj[i]:
        if not visited[j]:
            count=dfs(j, visited,count)
    return count

N, l = map(int, raw_input().split())
adj = defaultdict(list)
for i in xrange(l):
    a, b = map(int, raw_input().split())
    # Store a and b in an appropriate data structure
    adj[a].append(b)
    adj[b].append(a)


result = 0
# Compute the final result using the inputs from above
result = moon_pair(N)
print result

