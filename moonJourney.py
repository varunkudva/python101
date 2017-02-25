# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

def moon_pair(N):
    visited = [0] * N
    exclude_pair = 0
    total_pairs = (N * (N-1)) / 2
    for i in range(0, N):
        if not visited[i]:
            count = dfs(i, visited)
            exclude_pair += (count * (count-1))/2

    return total_pairs - exclude_pair

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

