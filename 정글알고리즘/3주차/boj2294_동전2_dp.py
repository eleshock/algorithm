import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

d = [10001] * (k+1)

d[0] = 0
for coin in coins:
    for i in range(coin, k+1):
        d[i] = min(d[i], d[i-coin]+1)
        
if d[k] == 10001:
    print(-1)
else:
    print(d[k])