from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
INF = float('INF')

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))
    return distance[end]

ans1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
ans2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)
ans = min(ans1, ans2)

if ans >= INF:
    print(-1)
else:
    print(ans)
