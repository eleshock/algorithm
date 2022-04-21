from collections import deque
import sys
input = sys.stdin.readline

def bfs(S, X, Y):
    q = deque(sorted(virus))
    time = 0
    while q:
        if time == S:
            break
        for _ in range(len(q)):
            virus_num, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = virus_num
                        q.append((graph[nx][ny], nx, ny))
        time += 1
    return graph[X-1][Y-1]


# 초기 세팅
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j))
S, X, Y = map(int, input().split())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

print(bfs(S, X, Y))