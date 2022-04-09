import sys

input = sys.stdin.readline

n = int(input())

s = list(map(int, input().split()))

stack = [0]                         # 제일 앞에 있는 탑은 무조건 레이저가 닿지 않으므로 인덱스 0을 추가한 상태로 시작

ans = [0] * n                       # 탑의 인덱스 값을 모두 0으로 초기화 후, 레이저가 도달하는 탑이 있을 경우에만 인덱스를 변경

for i in range(1, n):               # 두번째 탑부터 시작
    while stack:                    # 스택이 비어있지 않다면
        if s[stack[-1]] >= s[i]:    # 가장 최근에 추가된 탑의 높이가 확인하려는 탑의 높이보다 크거나 같으면
            ans[i] = stack[-1] + 1  # 레이저가 도달하므로 ans를 갱신시켜줌(인덱스 보정 + 1)
            break                   # ans가 갱신되면 while문을 빠져나옴
        else:                       # 가장 최근에 추가된 탑의 높이가 확인하려는 탑의 높이보다 작으면
            stack.pop()             # 자기보다 높은 탑을 만날 때까지 계속 pop (pop 하다가 스택이 비어버리면 while 문 탈출)
    stack.append(i)                 # pop으로 인해 스택이 다 비어버렸거나 ans가 갱신되어 while문을 빠져나온 경우 stack에 탑의 인덱스추가
            
print(*ans)                         # 리스트에 담긴 원소들을 한칸씩 띄어 출력