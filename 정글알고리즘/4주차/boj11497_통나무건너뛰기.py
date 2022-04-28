from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    q = deque(nums)
    log = deque()
    while q:
        log.append(q.pop())
        if not q:
            break
        log.appendleft(q.pop())
    log.append(log[0])
    level = -float('INF')
    for i in range(N):
        if abs(log[i+1]-log[i]) > level:
            level = abs(log[i+1]-log[i])
    print(level)

'''
다소 무식하지만 오름차순 정렬 후 제일 큰 수부터 pop을 하면서 가운데부터 앞뒤로 하나씩 붙여나간다. 이후에 제일 첫번째 원소를 끝에 한번 더 붙여줌으로써 리스트를 완성
'''