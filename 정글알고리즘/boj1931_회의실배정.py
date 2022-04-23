# O(n)안에 끝내야 함

import sys
input = sys.stdin.readline

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key = lambda x: (x[1], x[0]))

current_start, current_end = meetings[0]
ans = [meetings[0]]
for meeting in meetings[1:]:
    next_start, next_end = meeting
    if next_start < current_end:
        continue
    else:
        ans.append(meeting)
        current_start, current_end = next_start, next_end

print(len(ans))
