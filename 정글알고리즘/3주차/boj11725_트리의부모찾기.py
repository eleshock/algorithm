import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

# 루트노드가 1이므로 1로 부모를 모두 초기화
parent = [1 for _ in range(n+1)]

def dfs(v):
    visited[v] = True # 방문처리
    for i in graph[v]: # v와 연결된 노드들 중에
        if not visited[i]: # 아직 방문하지 않은 i가 있다면
            parent[i] = v # i의 부모노드가 v라고 할 수 있다
            dfs(i) # i의 자식노드를 찾기 위해 dfs 수행
    return

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

# 2번 노드부터 출력하라고 했으므로
for i in range(2, len(parent)):
    print(parent[i])