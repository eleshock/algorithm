import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

# map 함수로 1과 0으로 이루어진 문자열을 int형으로 변환 후 list에 담음
miro = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 범위 이탈 확인 함수
def isBoundary(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True

# 너비 우선 탐색
def bfs(x, y):
    # 상하좌우
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()

        # 현재 위치에서 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위를 벗어나면 진행불가
            if not isBoundary(nx, ny):
                continue

            # 벽이면 진행불가
            if miro[nx][ny] == 0:
                continue

            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                q.append((nx, ny))
    # 오른쪽 아래 출구까지의 카운트를 반환
    return miro[n-1][m-1]

print(bfs(0, 0))