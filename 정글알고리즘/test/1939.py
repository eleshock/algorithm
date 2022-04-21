from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    pass

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = map(int, input().split())
