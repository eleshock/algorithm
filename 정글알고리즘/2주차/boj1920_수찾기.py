n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))

def binary_search(start, end, i):
    while True:
        mid = (start + end) // 2
        if start > end:
            if a[mid] == i:
                return 1
            else:
                return 0
        if a[mid] > i:
            end = mid - 1
        else:
            start = mid + 1

for i in b:
    print(binary_search(0, len(a)-1, i))
