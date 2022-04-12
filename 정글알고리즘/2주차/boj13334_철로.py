import heapq
import sys
input = sys.stdin.readline

n = int(input())
road_info = [list(map(int, input().split())) for _ in range(n)]
d = int(input())

roads = []
for road in road_info:
    h, o = road
    if abs(h - o) <= d:
        road = sorted(road)
        roads.append(road)
roads.sort(key = lambda x:x[1])

ans = 0
heap = []
for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        while heap[0][0] < road[1] - d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    ans = max(ans, len(heap))

print(ans)