import sys

input = sys.stdin.readline

n, k = map(int, input().split())

s = list(input().rstrip())
m = n - k # n-k 자리수만큼만 출력하기 위함
stk = []
for i in range(n):
    while stk and k:
        if int(stk[-1]) < int(s[i]):
            stk.pop()
            k -= 1
        else:
            break
    stk.append(s[i])

print(''.join(stk[:m]))