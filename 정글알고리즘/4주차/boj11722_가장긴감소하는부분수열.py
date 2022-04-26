import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
LDS = [1] * n
for i in range(n-1, 0, -1):
    for j in range(i,-1,-1):
        if nums[j] > nums[i]:
            LDS[j] = max(LDS[j], LDS[i] + 1)

print(max(LDS))