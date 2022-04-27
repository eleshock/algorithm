import sys
input= sys.stdin.readline

n = int(input())

# 아래 dp 초기값 넣을 때 s가 2까지는 있다고 가정하므로, n이 1이더라도 s[2]까지는 0으로라도 만들어지게 초기화를 해야함
s = [0 for _ in range(n+2)]
for i in range(n):
    s[i] = int(input())

dp = [0 for _ in range(n+2)]
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1]+ s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i-3] + s[i-1]+ s[i], dp[i-2] + s[i])
    # dp[i-1] + s[i]로 하게 되면 i-1을 밟을 당시 이미 연속으로 2번 밟은 경우를 구분해낼 수 없고, dp[i-3]까지의 누적분에 두 계단을 오르는 것으로 마지막 계단을 밟을 수 있는 case를 구분해낼 수 있다.

print(dp[n-1])

# 근데 배열을 문제에서 주어진 전체크기+1 등으로 만들어주나 필요한 만큼만 할당해주나 메모리, 시간 측면에서는 유의미한 차이가 없습니다!