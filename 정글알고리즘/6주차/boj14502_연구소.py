from itertools import combinations as c
from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
walls = [] # 벽 가능 좌표
viruses = [] # 바이러스 좌표
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            walls.append((i, j)) # 벽 후보들(현재는 빈칸) 넣기
        if graph[i][j] == 2:
            viruses.append([i, j]) # 최초 바이러스 좌표 넣기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, walls, graph):
    maps = deepcopy(graph)
    safe = 0
    for a, b in walls:
        maps[a][b] = 1 # 벽 3개를 맵에 반영
    queue = deque(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maps[nx][ny] == 0:
                maps[nx][ny] = 2 # 바이러스를 싹 퍼뜨리자
                queue.append((nx, ny))
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                safe += 1
    return safe

survive = 0
for i in c(walls, 3):
    survive = max(survive, bfs(viruses, list(i), graph))
print(survive)