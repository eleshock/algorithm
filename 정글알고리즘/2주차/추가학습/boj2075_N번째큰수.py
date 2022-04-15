import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    nums = list(map(int, input().split()))
    
    # 힙이 비어있을 땐 우선 push를 해준다. 이 때 힙에 n개의 원소가 담긴다
    if not heap:
        for num in nums:
            heapq.heappush(heap, num)
    # 힙이 비어있지 않을 때는
    else:
        for num in nums:
            # 최소힙의 특성을 이용하여 작은 수는 빼고 큰 수들은 계속 넣어준다
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
# 최종적으로 힙에는 가장 큰 5개의 원소가 담기며, 최소힙의 특성에 따라 제일 앞에는 5번째로 큰 수가 오게 된다.
print(heap[0])