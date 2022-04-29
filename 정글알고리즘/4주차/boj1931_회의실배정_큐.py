# O(n) 안에 끝내야 함

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key = lambda x: (x[1], x[0]))

current_start, current_end = meetings[0]
queue = deque(meetings[1:])

result = 1
while queue:
    next_start, next_end = queue.popleft()
    if next_start < current_end:
        continue
    else:
        result+= 1
        current_start, current_end = next_start, next_end

print(result)
