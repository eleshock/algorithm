import sys
input = sys.stdin.readline

n = int(input())

sugars = [3, 5]

dp = [5001] * (n+5)
dp[3] = 1
dp[5] = 1
for sugar in sugars:
    for i in range(sugar+1, n+1):
        dp[i] = min(dp[i], dp[i-sugar] + 1)

if dp[n] == 5001:
    print(-1)
else:
    print(dp[n])