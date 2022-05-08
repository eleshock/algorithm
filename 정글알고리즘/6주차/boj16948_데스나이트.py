from collections import deque
import sys
input = sys.stdin.readline

def bfs(r, c):
    q = deque()
    q.append((r, c))
    graph[r][c] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if (0 <= nr < n) and (0 <= nc < n) and graph[nr][nc] == -1:
                q.append((nr,nc))
                graph[nr][nc] = graph[r][c] + 1

n = int(input())
r1,c1,r2,c2 = list(map(int, input().split()))
moves = [(-2,-1), (-2,1), (0,-2), (0,2), (2,-1), (2,1)]
graph = [[-1] * n for _ in range(n)]

bfs(r1,c1)
print(graph[r2][c2])