import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left = 0
right = n-1

target = float('INF')
ans = [0 , 0]
while left < right:
    liquid_sum = liquid[left] + liquid[right]
    if abs(liquid_sum) < target:
        target = abs(liquid_sum)
        ans[0], ans[1] = liquid[left], liquid[right]
    if liquid_sum < 0:
        left += 1
    else:
        right -= 1

print(ans[0], ans[1])