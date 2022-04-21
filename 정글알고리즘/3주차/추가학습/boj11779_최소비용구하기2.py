import heapq
import sys
input = sys.stdin.readline
INF = float('INF')

# 함수 정의
def dijkstra(start, end):
    distance = [INF for _ in range(n+1)]
    q = [(0, start, [start])]
    distance[start] = 0
    while q:
        dist, now, path = heapq.heappop(q)
        if now == end:
            return dist, path
        if distance[now] < dist:
            continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0], path + [j[0]]))

# 초기화
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

# 함수 실행 및 답 도출
minCost, path = dijkstra(start, end)
print(minCost)
print(len(path))
print(*path)