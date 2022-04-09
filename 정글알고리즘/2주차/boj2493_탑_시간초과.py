import sys

input = sys.stdin.readline

n = int(input())

s = list(map(int, input().split()))

stack = []

ans = []

for i in range(n):
    if not stack:
        stack.append(s[i])
        ans.append(0)
    
    else:
        if stack[-1] < s[i]:
            if max(stack) < s[i]:
                ans.append(0)
            else:
                ans.append(max(stack))
            stack.append(s[i])
        else:
            ans.append(stack[-1])
            stack.append(s[i])

for i in ans:
    if i == 0:
        print(0, end = ' ')
    else:
        print(s.index(i)+1, end = ' ')
