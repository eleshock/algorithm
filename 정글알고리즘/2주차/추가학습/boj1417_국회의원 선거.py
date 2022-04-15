import heapq
import sys
input = sys.stdin.readline

n = int(input())

dasom, *candidates = [int(input()) for _ in range(n)]
tmp = dasom
# 지지자 수가 가장 많은 사람을 계속 체크해서 그 사람의 표를 뺏어오자!
heap = []
for hoobo in candidates:
    heapq.heappush(heap, -hoobo)
if heap:
    while True:
        if -1 * heap[0] < tmp:
            break

        else:
            a = -1 * heapq.heappop(heap)
            heapq.heappush(heap, -(a-1))
            tmp += 1    

print(tmp - dasom)