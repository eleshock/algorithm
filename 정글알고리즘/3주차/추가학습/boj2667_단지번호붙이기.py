from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
apt = []

for i in range(n):
    apt.append(list(map(int, input().rstrip())))
	
visit = [[0] * n for _ in range(n)]				# 1 방문 흔적을 남길 리스트
dx = [-1, 0, 1 ,0]						# 2 다음 x,y 좌표를 위한 리스트
dy = dx[::-1]			

def bfs(x, y, idx):
    q = deque([[x,y]])						# 6 기본적인 bfs의 형태. queue 를 이용해 조건에 충족하는 경우가 없을 때까지 순회한다.
    visit[x][y] = 1				
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]				# 7 상하좌우 탐색 준비
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:			# 8 인덱스를 벗어날 경우 제외
                if apt[nx][ny] == 1 and visit[nx][ny] == 0: 	# 9 아파트단지이거나 방문한 이력이 없을 경우
                    q.append([nx,ny])				# 10 다음 순회를 위해 queue에 추가
                    visit[nx][ny] = 1				# 11 방문처리
                    apt_list[idx] += 1				# 12 해당 아파트 단지 가구수 추가
apt_list={}
idx = 0
for i in range(n):						# 3 이차원 배열의 모든 경우의 수를 훑어나가기 시작.
    for j in range(n):
        if apt[i][j] != 0 and visit[i][j] == 0:			# 4 문제의 조건을 충족할 경우 bfs 시작
            apt_list[idx] = 1					# 5 bfs 의 각 대상(아파트 단지)을 발견했을 경우 초기값으로 1을 넣어주고 bfs를 실행.
            bfs(i,j,idx)
            idx+=1						# 13 다음 아파트 단지의 인덱스 설정

apt_list=sorted(apt_list.values())
print(len(apt_list))
for i in apt_list:
    print(i)