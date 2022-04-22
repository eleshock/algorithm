import sys
from collections import deque

def bfs(d, e, mm):              # BFS 시작
    q = deque()                 # 큐를 만든다
    visited = [0]*(n+1)         # visited를 만든다
    q.append(d)                 # 시작값(d)을 넣어준다.
    visited[d] = 1              # 방문처리를 해준다.

    while q:                    
        v = q.popleft()         # 큐의 제일 앞에 있는 원소(먼저들어간 원소)를 하나씩 pop해준다.
        if v == e:              # 큐에서 꺼낸 값이 e가 되면(즉, 아래 if 조건에서 d->e까지 가는 경로에 있는 모든 다리의 적재하중이 mm을 넘으면)      
            return True         # True를 반환한다
        for i in graph[v]:      # 큐에서 꺼낸 원소(섬)과 인접한 섬들의 (노드번호, 적재하중)을 하나씩 확인
            if visited[i[0]]==0 and i[1] >= mm: # 아직 방문하지 않은 섬이고 적재하중이 mm(mid)보다 크다면
                visited[i[0]] =1                # 방문 처리를 해주고
                q.append(i[0])                  # 섬의 노드번호를 큐에 append 해준다.
    return False                                # while문을 도는 동안 큐에 담긴 원소들 중 e가 없었다면 섬에 도달하지 못한다는 의미이므로 False 반환(mid값을 내려야 함)

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[]for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

d, e = map(int, input().split())
left, right = 1, int(1e9)           # 문제에서 주어진 적재하중(C)의 최소/최대 값을 이진 탐색의 left, right 범위로 지정해준다.

while left <= right:                # 이진 탐색 시작
    
    mid = (left + right)//2         # mid 값을 구해준다. 

    if bfs(d, e, mid):              # mid 값을 넣고 BFS 를 시작한다.
        answer = mid                # if를 만족하면 우선 answer 후보이므로 mid에 answer를 넣어준다
        left = mid + 1              # 더 맞는 값을 갖기 위해서 mid값을 조금 더 올려본다
    else:
        right = mid -1              # 조건에 부합하지 않는다는 것(False)이므로 right값을 내리면서 mid 값을 내려본다
        
print(answer)

'''
6 12
1 2 7
1 3 8
1 4 7
1 6 9
2 3 7
3 4 7
3 5 7
4 5 7
4 6 7
3 6 7
1 3 11
5 6 12
6 3
9
7
'''