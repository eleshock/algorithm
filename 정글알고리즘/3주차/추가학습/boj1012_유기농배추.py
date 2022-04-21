from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs(x, y):
    q = deque([])
    q.append((x, y))
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    
    count = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1
    
    print(count)