from collections import deque
import sys
input = sys.stdin.readline

result = 0
def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        for w in graph[v]:
            if not visited[w]:
                if status[w-1] == 0:
                    visited[w] = True
                    q.append(w)
                else:
                    global result
                    result += 1
    return

N = int(sys.stdin.readline())
status = list(map(int, input().rstrip()))
graph = [[] for _ in range(N + 1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    if status[i-1] == 1:
        visited = [False] * (N+1)
        bfs(i)

print(result)