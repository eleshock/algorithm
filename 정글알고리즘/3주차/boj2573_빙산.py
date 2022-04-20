from collections import deque
from sys import stdin
input = stdin.readline

def check(x, y): # 바다와 맞닿은 면의 수를 세는 함수
    cnt = 0
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if glacier[nx][ny] == 0:
            cnt += 1
    return cnt

def bfs(x, y):
    visited[x][y] = True
    q = deque([[x, y]])
    while q:
        x, y = q.popleft()
        cnt = check(x, y) # 바다와 맞닿은 면의 수
        re[x][y] = (0 if glacier[x][y] - cnt < 0 else glacier[x][y] - cnt) # 녹은 빙산 정보 업데이트
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and glacier[nx][ny] != 0:
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return

N, M = map(int, input().split())
glacier = [list(map(int, input().split())) for _ in range(N)] # 빙산 정보
# glacier = [[0, 0, 0, 0, 0, 0, 0], [0, 2, 4, 5, 3, 0, 0], [0, 3, 0, 2, 5, 2, 0], [0, 7, 6, 2, 4, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 4방향
answer = 0 # 분리될 때까지 걸리는 시간 초기화


while True:
    tmp = 0 # 덩어리 수 
    re = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and glacier[i][j] > 0: # 아직 방문 x & 다 녹지 않은 곳
                bfs(i, j) # 한 덩어리로 연결되어 있는 애들 모두 탐색
                tmp += 1
                
    glacier = re

    if tmp == 0:
        print(0)
        break
    if tmp >= 2:
        print(answer)
        break
    answer += 1