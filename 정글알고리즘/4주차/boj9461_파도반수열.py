import sys
input = sys.stdin.readline

dp = [1,1,1,2,2]

T = int(input())
for i in range(5, 100):
    dp.append(dp[i-1] + dp[i-5])

for _ in range(T):
    n = int(input())
    print(dp[n-1])