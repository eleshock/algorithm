import sys

input = sys.stdin.readline

n, m = map(int, input().split())

trees = list(map(int, input().split()))

max_value = -float('INF')

def binary_search(start, end, trees):
    global max_value
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for tree in trees:
            if tree > mid:
                sum += tree-mid
        if sum >= m:
            max_value = max(max_value, mid)
            start = mid + 1
        else:
            end = mid -1

binary_search(0, max(trees), trees)

print(max_value)