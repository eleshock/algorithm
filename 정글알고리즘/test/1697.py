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
        for nw in (w-1, w+1, 2*w): # 3가지 선택지
            if 0 <= nw < 100001 and not dist[nw]:
                dist[nw] = dist[w] + 1 
                q.append(nw)

# 0 ~ 100,000까지의 위치별 소요되는 시간을 담는 더미 리스트
dist = [0] * (100001)

n, k = map(int, input().split())

print(bfs(n))