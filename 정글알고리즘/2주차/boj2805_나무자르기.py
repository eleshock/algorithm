n, m = map(int, input().split())

tree = list(map(int, input().split()))

h = -float('inf')

def binary_search(start, end):
    global h
    while True:
        mid = (start + end) //2
        sum = 0
        if start > end:
            return h
        
        for i in range(n):
            if tree[i] > mid:
                sum += tree[i]-mid
        if sum >= m:
            h = max(h, mid)
            start = mid + 1
        else:
            end = mid - 1

print(binary_search(0, max(tree)))