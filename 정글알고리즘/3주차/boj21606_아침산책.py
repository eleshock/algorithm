'''
1. 실외 노드를 기준으로 인접해있는 실내 노드 개수를 count
2. 실외 노드를 중간에 놓고 실내 점 n개가 붙어있을 때 갈 수 있는 경로의 수는 n<출발점 선택> * 1<거쳐가는 실외> * (n-1)<출발점을 제외하고 선태할 수 있는 도착점 수> = n*(n-1)
3. 실외 노드끼리 연결되는 경우는 1) 실외끼리 인접 노드로 연결될 때 2) 중간에 실내 노드를 끼고 연결될 때. 이를 분리해서 생각
'''

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(v, cnt): # v: 정점 번호, cnt: 실외와 연결된 실내 노드 카운트
    visited[v] = True
    for i in graph[v]: 
        if location[i] == 1: # 실내이면
            cnt += 1 # 실내 개수 카운트 + 1
        elif not visited[i] and location[i] == 0: # 방문한 적 없고 실외이면
            cnt = dfs(i, cnt) # 해당 실외 노드에 대해 dfs 수행. 이 함수를 실행하면서 누적된 cnt 값을 갖고 재귀한 최종 cnt를 return한다
    return cnt

ans = 0
n = int(input())
location = [0] + list(map(int, input().rstrip())) # 노드의 인덱스를 1부터 시작하기 위한 보정작업

graph = [[] for _ in range(n+1)]

for _ in range(n-1): # 간선정보 받기
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    if location[a] == 1 and location[b] == 1: # 둘 다 실내이면
        ans += 2 # 서로 방문하는 케이스가 2가지이니 정답에 추가

sum = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i] and location[i] == 0: # 실외인 애들 기준으로
        x = dfs(i, 0) # 현재 cnt = 0
        sum += x*(x-1) # 실외인 노드를 기준으로 인접 노드 애들 개수 세는게 총 n*(n-1)이니 실외 노드 걸릴 때마다 이걸 전부 세기

print(sum + ans)