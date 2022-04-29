import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0 for _ in range(m+1)]
    dp[0] = 1
    for coin in coins:
        for i in range(1, m+1):
                if i - coin >= 0:
                    dp[i] += dp[i-coin]
    print(dp[m])


''' 
굳이 오름차순일 필요는 없다. 어처피 경우의 수를 더해주는 것이기 때문
dp[0] = 1을 해주는 이유:
dp[i-coin]에서 i-coin이 0이되는 경우가 무조건 생긴다
ex) 2원으로 2원을 만드는 경우는 dp[i-coin] = dp[0] = 1로 처리해줘야 함
'''