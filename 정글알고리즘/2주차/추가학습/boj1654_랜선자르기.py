import sys

input = sys.stdin.readline

n, k = map(int, input().split())

lans = [int(input()) for _ in range(n)]

start = 0
end = max(lans)
res = 0
while start <= end:
    sum = 0
    mid = (start + end) // 2
    if mid == 0:
        mid = 1
    for lan in lans:
        sum += lan // mid
    
    if sum >= k:
        res= max(res, mid)
        start = mid + 1
    else:
        end = mid - 1

print(res)