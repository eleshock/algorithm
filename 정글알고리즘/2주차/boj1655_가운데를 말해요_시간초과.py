import heapq
import copy
import sys

input = sys.stdin.readline

n = int(input())

heap_q1 = []
heap_sort = []
for _ in range(n):
    num1 = int(input())
    heapq.heappush(heap_q1, (num1, num1))
    heap_q2 = copy.deepcopy(heap_q1)
    while heap_q2:
        heap_sort.append(heapq.heappop(heap_q2))
    print(heap_sort[(len(heap_sort)-1)//2][1])
    heap_sort = []
