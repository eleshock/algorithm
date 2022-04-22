import sys
input = sys.stdin.readline

n = int(input())

stones = [1, 3]

dp = [1001] * (n+3)
dp[1] = 1
dp[3] = 1
for stone in stones:
    for i in range(stone, n+1):
        if dp[i] == 1:
            dp[i+stone] = 0
        elif dp[i] == 0:
            dp[i+stone] = 1

if dp[n] == 1:
    print('SK')
else:
    print('CY')