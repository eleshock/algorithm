
import sys
input = sys.stdin.readline

n = int(input())
stick_list = [int(input()) for _ in range(n)]

answer = 0
stack = []
for stick in reversed(stick_list):
    if stack:
        if stack[-1] < stick:
            stack.pop()
            stack.append(stick)
            answer += 1
    else:
        stack.append(stick)
        answer += 1

print(answer)