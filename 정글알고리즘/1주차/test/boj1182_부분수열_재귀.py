N, S = map(int, input().split())
A = tuple(map(int, input().split()))

ans = [0]
def solve(i=0, s=0):
    if i == N:
        if s == S:
            ans[0] += 1
        return
    solve(i+1, s+A[i])
    solve(i+1, s) # s+A[i]값 확인 및 모든 경우의 수 
solve()
print(ans[0]) if S else print(ans[0]-1)