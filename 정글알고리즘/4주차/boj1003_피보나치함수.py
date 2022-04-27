# 예제에서 소스를 다 제공해줬다.
import sys
input = sys.stdin.readline

T = int(input())
dp = []
for i in range(41):
    if i == 0:
        dp.append((1, 0))
    elif i == 1:
        dp.append((0, 1))
    else:
        dp.append((dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]))

for _ in range(T):
    n = int(input())
    print(*dp[n])