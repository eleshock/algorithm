import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

stk = [a[-1]]
ans = [-1] * n

for i in range(n-2, -1, -1):
    while stk:
        if stk[-1] > a[i]:
            ans[i] = stk[-1]
            break
        else:
            stk.pop()
    stk.append(a[i])

print(* ans)