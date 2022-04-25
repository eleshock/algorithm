import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

LIS = [1] * n
for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            LIS[i] = max(LIS[i], LIS[j] + 1)

print(max(LIS))