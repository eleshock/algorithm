'''
문제 : N [1, 10000] 섬 , 중량제한, 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램 작성
입력 : N, M [1, 100000] // A,B,[1,N] C[1, 10억] (모든 다리의 방향은 양방향) 
출력 : 답 출력
'''

import heapq
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])                  # 양방향으로 입력 받음
    graph[b].append([a,c])

distance = [0]*(n+1)                        # 거리 테이블 노드 만큼 만든다
X,Y = map(int, input().split())             # X -> Y로 가는 중량의 최댓값


def bfs(b, start):                          # BFS 시작
    
    q = []
    heapq.heappush(q, [b, start])           # 왜 heappush를 써야하는가?
                                            # 1) 최댓값을 구하기 떄문이다
                                            # 그냥 큐를 사용하면 최댓값만 나오지 않고 모든 것이 다돌아야 하기 때문에
                                            # heap을 쓰면 무조건 뽑는 것들이 최댓값이 되기 때문에 바로 break 가능
    while q:
        
        cur_cost, cur_index = heapq.heappop(q)      # cost, index를 받는다.
    
        if cur_index == Y:                      # index가 목표값 Y이면 바로 break
            break                               
        
        if distance[cur_index] > -cur_cost:     # cur_index의 거리 값이, cur_cost값보다 크면 continue
            continue                            # 밑에 과정을 실행할 필요가 없다. 어쨌든 최댓값으로 갈아끼워야하는 것인데
                                                # 최솟값 비교를 하고 최댓값 비교를 하기 떄문에 이미 최댓값이어서 굳이 밑에 작업을 할 필요없음.
        
        for next_index, next_cost in graph[cur_index]:  # index에 next 탐색
            
            if cur_cost == 0:   # 0일 떄, 따로 빼줘야함 왜냐하먼
                # 밑에 식을 보면 결국 cur_cost와 next_cost를 비교해줘야하는데 0은 무조건 작기 때문에 
                # 결국 cur_cost가 가장 작게되고 밑에 if조건에 안걸리게되고 결국 아무것도 처리해주지 못한다.                         
                distance[next_index] = next_cost        
                # heapq에 next index의 distance 값과 next index의 값을 최대힙으로 넣어준다 (마이너스 기준이니까, 거리가 먼저 나와야한다)
                heapq.heappush(q, [-distance[next_index], next_index]) 
                continue    # continue로 바로 for로 넘겨준다.
            
            if -cur_cost > next_cost :  
                    # cur_cost가 next_cost보다 크고
                if distance[next_index] < next_cost:
                    # next_cost가 distance[next_index]보다 크면 
                    distance[next_index] = next_cost
                # next_index의 distance의 값을 next_cost로 갱신한다.
                    heapq.heappush(q, [-distance[next_index], next_index])
                
            else: # cur_cost가 next_cost보다 작고
                if distance[next_index] < -cur_cost:
                    # cur_cost가 distance[next_index]보다 크면 
                    distance[next_index] = -cur_cost
                    # next_index의 distance의 값을 cur_cost로 갱신한다
                    heapq.heappush(q, [-distance[next_index], next_index])
                    # 그 값을 heapq에 넣어준다.
                    
bfs(0, X)               
print(distance[Y])

# https://velog.io/@redcarrot01/ProblemSolving-1939-%EC%A4%91%EB%9F%89%EC%A0%9C%ED%95%9C-BFS-%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89-%ED%81%AC%EB%A3%A8%EC%8A%A4%EC%B9%BC