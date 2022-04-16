import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph, visited = {}, [False]*(n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
    
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

def dfs(v):
    visited[v] = True
    if v in graph:
        for u in graph[v]:
            if not visited[u]:
                dfs(u)
    return True

for i in range(1, n+1):
    if not visited[i]:
        cnt += dfs(i)

print(cnt)