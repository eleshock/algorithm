import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    dp = [0] * 10001
    for coin in coins:
        dp[coin] = 1
    for i in range(coins[0], target+1):
        for coin in coins:
            dp[i] = dp[i-coin] + 1