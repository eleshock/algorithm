import sys

input = sys.stdin.readline

t = int(input())
ans = []
for _ in range(t):
    comm = input()
    stk = []
    for bracket in comm:
        if bracket == '(':
            stk.append(bracket)
        elif bracket == ')':
            if not stk:
                ans.append('NO')
                break
            else:
                stk.pop()
    else:
        if not stk:
            ans.append('YES')
        else:
            ans.append('NO')

for i in ans:
    print(ans)