from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs(x, y, count):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        visited[x][y] = count
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = count

count = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            count += 1
            bfs(i, j, count)

ans = [0] * (count)
for i in range(1, count+1):
    for j in range(n):
        for k in range(n):
            if visited[j][k] == i:
                ans[i-1] += 1

print(count)
print(*ans, sep='\n')