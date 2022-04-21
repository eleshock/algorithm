from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0,-1,1,-1,1], [0,0,-1,1,1,1,-1,-1]
ans = []
def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1
    ans.append(count)

print(*ans, sep='\n')