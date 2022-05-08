import sys
input = sys.stdin.readline

a, b = map(int, input().split())
ans = float('INF')
def dfs(x, n):
    global ans
    if x == b:
        ans = min(ans, n)
        return
    elif x < b:
        dfs(x*2, n+1)
        dfs(int(str(x)+'1'), n+1)
    else:
        return

dfs(a, 0)

if ans == float('INF'):
    print(-1)
else:
    print(ans+1)