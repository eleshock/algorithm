import sys

input = sys.stdin.readline

n, c = map(int, input().split())

router = [int(input()) for _ in range(n)]
router.sort()

start = 1
end = max(router) -1
max_distance = 0

def binary_search(router, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = router[0] # 제일 왼쪽에 있는 공유기를 하나 픽하고
        count = 1 # 설치 카운트를 1로 초기화한다.

        for i in range(1, n): # 선택한 첫번째 공유기(인덱스 0 공유기)를 제외하고 인덱스 1~n-1까지 공유기 중에서
            if router[i] >= current + mid: # 0번째 라우터에서 mid 이상 떨어져 있다면
                count += 1 # 공유기를 설치 조건에 부합하므로 설치카운트 1 증가
                current = router[i] # 설치한 공유기로 현재 공유기를 갱신
        
        if count >= c:
            global max_distance
            max_distance = mid
            start = mid + 1
        else:
            end = mid -1

binary_search(router, start, end)
print(max_distance)