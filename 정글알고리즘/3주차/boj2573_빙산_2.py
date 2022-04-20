from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

year = 0
check = False
queue = deque()

def bfs(x, y):
    queue.append((x,y))                
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True # 처음 것 방문처리 해줘야함    
        for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m:
                   
                
                    if data[nx][ny] != 0 and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        queue.append((nx,ny))
                        
                    elif data[nx][ny] == 0:
                        count[x][y] += 1
                    
    return "승원이섬"


while True:
    visited = [[False]*m for _ in range(n)]     
    count = [[0]*m for _ in range(n)]         
    result = []
   
    for i in range(n):
        for j in range(m):
            if data[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i,j))

    for i in range(n):
        for j in range(m):
            data[i][j] -= count[i][j]
            if data[i][j] < 0:
                data[i][j] = 0
    print(result)
    if len(result) == 0:           
       break                           
    if len(result) >= 2:
        check = True
        break
    year += 1
    print(count)
            
if check:
    print(year)
else:
    print(0)

