from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append([home[0], home[1]])
    while q:
        x, y = q.popleft()
        if abs(x-festival[0]) + abs(y-festival[1]) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]
                if abs(nx - x) + abs(ny - y) <= 1000:
                    q.append([nx, ny])
                    visited[i] = 1
    print("sad")
    return


t = int(input())
for _ in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n)]
    festival = list(map(int, input().split()))
    visited = [0 for _ in range(n+1)]
    bfs()
