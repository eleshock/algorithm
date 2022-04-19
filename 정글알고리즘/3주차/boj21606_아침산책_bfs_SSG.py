# 너무 어려움

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

# 1은 실내, 0은 실외
A = 'n'+input().strip()
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    '''실외에 맞닿아있는 실내 점을 세주는 함수'''
    cnt = 0 
    visited[v] = True
    for i in graph[v]:
        if A[i] == "1": # 실내면
            cnt += 1

        elif A[i]== "0" and not visited[i]: # 실외면 
            cnt += dfs(i)
    return cnt

visited = [False] * (N + 1)

ans = 0
for i in range(1, N + 1):
    if A[i] == '1': # 시작 지점이 실내 
        for j in graph[i]: 
            if A[j] == '1': # 끝 지점도 실내
                ans += 1 # 그럼 카운트
    else:  
        if not visited[i]: # 시작이 실외면
            temp = dfs(i) # 맞닿아있는 실내 점 개수 찾아라
            ans += temp * (temp - 1)
print(ans)