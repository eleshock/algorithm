n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)] # 성권이가 가진 캐릭터들의 레벨을 리스트에 포함
arr.sort()

# 시작점과 끝점을 잡을 때는 극단적으로. k(레벨업물약)을 젤높은 캐릭에 다 몰아주는 경우에서부터 점차 줄여나간다.
start = arr[0]
end = arr[-1] + k

def count(mid, arr): # 레벨 낮은애들 목표레벨까지 채우는데 얼마나 필요한가?
    sum = 0 # 초기화
    for chr in arr: # 성권이가 가진 캐릭터 레벨들 중에서
        if chr < mid: # 목표레벨보다 낮은 캐릭터일 경우
            sum += mid - chr # sum에 필요량을 포함시켜줌
        else: # 목표레벨보다 높은 애들부터는 안 필요하므로 반복문 빠져나옴
            break
    return sum # 누적된 sum을 반환함

while start <= end:
    mid = (start + end) // 2

    if count(mid, arr) <= k:
        target = mid
        start = mid + 1
    else:
        end = mid -1

print(target)