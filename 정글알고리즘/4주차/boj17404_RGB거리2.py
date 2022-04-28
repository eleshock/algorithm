import sys
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
result = float('INF')

for firstHouse in range(3):
    dp = [[0] * 3 for _ in range(n)]
    for i in range(3):
        if i == firstHouse:
            dp[0][i] = info[0][i]
            continue
        dp[0][i] = result
    
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + info[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + info[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + info[i][2]
    for i in range(3):
        if i == firstHouse:
            continue
        result = min(result, dp[-1][i])

print(result)