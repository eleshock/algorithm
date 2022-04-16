import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 도시 수, 도로 수, 거리정보, 출발도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    # a노드에서 b노드로 가는 비용을 모두 1로 설정
    graph[a].append((b, 1))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 우선순위 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않으면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for j in graph[now]:
            cost = dist + j[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(x)

answer = []
for i in range(1, n+1):
    if distance[i] == k:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)