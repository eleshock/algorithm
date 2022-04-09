import sys

input = sys.stdin.readline

n = int(input())

ans = []

for _ in range(n):
    a = input()
    sum = 0
    # for-else 사용, for문 종료 시점까지 break로 빠져나가지 않았을 때만 else문 동작
    for i in range(len(a)):
        if a[i] == '(':
            sum += 1
        elif a[i] == ')':
            sum -= 1
        if sum < 0:
            ans.append('NO')
            break
    else:
        if sum == 0:
            ans.append('YES')
        else:
            ans.append('NO')

for j in ans:
    print(j)