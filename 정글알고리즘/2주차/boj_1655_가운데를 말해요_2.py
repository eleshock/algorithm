import heapq
import sys

input = sys.stdin.readline

n = int(input())

left_heap = []
right_heap = []

for i in range(n):
    num = int(input())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

    if len(left_heap) >= 1 and len(right_heap) >= 1 and left_heap[0] * -1 > right_heap[0]:
        a = heapq.heappop(left_heap) * -1
        b = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -b)
        heapq.heappush(right_heap, a)
    print(-left_heap[0])