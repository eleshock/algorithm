import sys

input = sys.stdin.readline

n = int(input())

ans = []

for _ in range(n):
    stack = []
    a = input()
    for i in a:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop() 
            else:
                ans.append('NO')
                break
    else:
        if not stack:
            ans.append('YES')
        else:
            ans.append('NO')

for i in ans:
    print(i)