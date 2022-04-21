# my solution

from collections import deque
import sys
input = sys.stdin.readline
INF = float('INF')

def bfs(start, end):
    q = deque()
    q.append(start)
    visited[start] = 0
    while q:
        w = q.popleft()
        if w == end:
            return visited[w]
        for i in graph[w]:
            if visited[i] == INF:
                visited[i] = visited[w]+ 1
                q.append(i)
    return -1

n = int(input())
start, end = map(int, input().split())
m = int(input())
visited = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(start, end))