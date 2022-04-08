import sys

input = sys.stdin.readline

m, n, l = map(int, input().split())

place = list(map(int, input().split()))
place.sort()

animals = [list(map(int, input().split())) for _ in range(n)]

count = 0

for animal in animals:
    start = 0
    end = m - 1
    while start <= end:
        mid = (start + end) // 2
        if abs(place[mid] - animal[0]) + animal[1] <= l:
            count += 1
            break
        elif animal[0] > place[mid]:
            start = mid + 1
        else:
            end = mid - 1

print(count)