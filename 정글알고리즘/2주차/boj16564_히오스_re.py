import sys

input = sys.stdin.readline

n, k = map(int, input().split())

levels = [int(input()) for _ in range(n)]

# 정렬하는 것 보다는 min과 max로 필요한 값을 뽑아내는게 빠르다!
start = min(levels)
end = max(levels) + k

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for level in levels:
        if level < mid:
            sum += mid - level
    if sum <= k:
        target = mid
        start = mid + 1
    else:
        end = mid - 1

print(target)