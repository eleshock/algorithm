# 통과 / 소요시간 40분
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
flag = [[False] * n for _ in range(n)]
flag[0][0] = True
for i in range(n):
    for j in range(n):
        val = board[i][j]
        
        if val == 0:
            print(dp[-1][-1])
            exit()
        if flag[i][j]:
            if i + val < n:
                dp[i+val][j] += dp[i][j]
                flag[i+val][j] = True
            if j + val < n:
                dp[i][j+val] += dp[i][j]
                flag[i][j+val] = True