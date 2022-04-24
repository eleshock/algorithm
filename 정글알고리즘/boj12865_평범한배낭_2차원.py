import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(1, k+1):
        if w > j: # 현재 물건의 무게가 가방 무게 j보다 무거운 경우
            dp[i][j] = dp[i-1][j]
        else: # 가방 무게와 같거나 가벼운 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[-1][-1])
