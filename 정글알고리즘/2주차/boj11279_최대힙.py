import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap_q = []
for _ in range(n):
    comm = int(input())

    if comm == 0:
        if heap_q:
            print(heapq.heappop(heap_q)[1]) #우선순위가 높은 원소의 값을 print / [우선순위, value]
        else:
            print(0)
    else:
        heapq.heappush(heap_q, (-comm, comm))