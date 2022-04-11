import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
shot_point = list(map(int, input().split()))
animals = [list(map(int, input().split())) for _ in range(n)]
shot_point.sort()

count = 0
for animal in animals:
    start = 0
    end = m - 1
    while start <= end:
        mid = (start + end) // 2
        if abs(shot_point[mid] - animal[0]) + animal[1] <= l:
            count += 1
            break
        if animal[0] > shot_point[mid]:
            start = mid + 1
        else:
            end = mid - 1

print(count)