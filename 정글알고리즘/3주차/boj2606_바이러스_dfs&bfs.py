N = int(input())
T = int(input())
graph = dict()
for _ in range(T):
    key, value = map(int, input().split())
    if key in graph:
        graph[key].append(value)
    else:
        graph[key] = [value]
    if value in graph:
        graph[value].append(key)
    else:
        graph[value] = [key]

# dfs
visited = [1]
def dfs(key):
    for line in graph[key]:
        if line in visited:
            continue
        visited.append(line)
        dfs(line)
dfs(1)
print(len(visited)-1)

# bfs
from collections import deque
def bfs(graph, start):
    visit = []
    queue = deque([])
    queue.append(start)

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit
print(len(bfs(graph, 1)) -1)