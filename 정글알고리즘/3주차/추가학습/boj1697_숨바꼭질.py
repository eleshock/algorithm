from collections import deque
import sys
input = sys.stdin.readline

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        w = q.popleft()
        if w == k:
            return dist[w]
        for nw in (w-1, w+1, w*2):
            if 0 <= nw <= 100000 and not dist[nw]:
                dist[nw] = dist[w] + 1
                q.append(nw)


dist = [0] * 100001
n, k = map(int, input().split())

print(bfs(n))