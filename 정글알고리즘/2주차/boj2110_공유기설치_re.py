import sys
input = sys.stdin.readline
n, c = map(int, input().split())

router = [int(input()) for _ in range(n)]
router.sort()

start = 1
end = router[-1] - router[0]
ans = 0

while start <= end:
    count = 1
    mid = (start + end) // 2
    now = router[0]
    for i in range(1, n):
        if router[i] - now >= mid:
            count += 1
            now = router[i]
    if count < c:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)