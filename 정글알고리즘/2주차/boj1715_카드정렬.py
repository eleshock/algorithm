import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap_q = []
for _ in range(n):
    num = int(input())
    heapq.heappush(heap_q, num)

if len(heap_q) == 1:
    print(0)
else:
    sum = 0
    while len(heap_q) > 1:
        card_1 = heapq.heappop(heap_q)
        card_2 = heapq.heappop(heap_q)
        sum += card_1 + card_2
        heapq.heappush(heap_q, card_1 + card_2)
    print(sum)