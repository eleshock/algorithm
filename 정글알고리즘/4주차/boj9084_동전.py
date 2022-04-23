import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    dp = [0 for _ in range(target+1)]
    dp[0] = 1
    for coin in coins:
        for i in range(1, target+1):
                if i - coin >= 0:
                    dp[i] += dp[i-coin]
    print(dp[target])