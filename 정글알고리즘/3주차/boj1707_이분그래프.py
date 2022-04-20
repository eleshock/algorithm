import sys
from collections import deque


def bfs(start, c):
    queue = deque([(start, c)])
    visited[start] = c
    while queue:
        v, c = queue.popleft()
        for nv in graph[v]:
            if visited[nv] == 0:
                visited[nv] = -c
                queue.append((nv, -c))
            elif visited[nv] == visited[v]:
                return False
    return True

ans = []
K = int(sys.stdin.readline())
for k in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for e in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    result = 'YES'
    for i in range(1, V + 1):
        if visited[i] == 0:
            if not bfs(i, 1):
                result = 'NO'
                break
    ans.append(result)

print(*ans, sep='\n')