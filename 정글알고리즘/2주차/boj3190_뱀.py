from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

k = int(input())
field = [[0]* n for _ in range(n)]
for _ in range(k):                              # 사과를 field에 1로 표시해주자
    r, c = map(int, input().split())
    field[r-1][c-1] = 1                         # 0, 0을 기준점으로 하기 때문에 1씩 빼준다

l = int(input())
change = dict()
for _ in range(l):
    x, c = input().split()
    change[int(x)] = c

# 방향 정리(북동남서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d = 1 # 오른쪽(동쪽) 이동으로 시작
x, y = 0, 0

count = 0

snake = deque([[0, 0]]) # 뱀의 처음 위치를 데크에 추가하고 시작

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

def turn_right():
    global d
    d += 1
    if d == 4:
        d = 0

def boundary_check(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

while True:
    count += 1
    nx = x + dx[d]
    ny = y + dy[d]

    if count in change.keys():              # change의 key 중 count가 있으면
        if change[count] == 'D':            # change의 value가 D인지 L인지 확인해서
            turn_right()                    # 방향을 전환한다
        else:
            turn_left()

    if boundary_check(nx, ny):              # 범위체크를 한 번 하고
        if [nx, ny] in snake:               # 몸에 부딪히면 break
            break

        if field[nx][ny] == 1:              # 방문한 곳에 사과가 있으면 길이 1 증가
            snake.append([nx, ny])
            field[nx][ny] = 0               # 먹은 사과는 없애주자
        else:                               # 사과가 없으면 꼬리를 자르자
            snake.append([nx, ny])
            snake.popleft()
            
        x, y = nx, ny

    else:                                   # 범위 밖이면 break                             
        break

print(count)