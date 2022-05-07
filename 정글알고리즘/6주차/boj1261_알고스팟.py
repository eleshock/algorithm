from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

miro = []
for i in range(n):
    miro.append(list(map(int, input().strip())))

dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if miro[nx][ny] == 0:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
print(bfs())